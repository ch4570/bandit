import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bandit_eval_run_local", ROOT / "evals/run_local.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class EvalIntegrityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="bandit eval tests ")
        self.addCleanup(temporary.cleanup)
        self.area = Path(temporary.name).resolve()
        self.root = self.area / "repository"
        self.case = "06-existing-spec-rewrite"
        self.inputs = {
            "request.md": b"Synthetic fixture: rewrite docs/PRD.md using the observations.\n",
            "observations.md": b"Synthetic observation: three users could not find the action.\n",
            "docs/PRD.md": b"# Original synthetic PRD\nPreserve this historical evidence.\n",
        }
        for relative, data in self.inputs.items():
            target = self.root / "evals/cases" / self.case / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        for name in ("bandit", "bandit-specify"):
            target = self.root / "skills" / name / "SKILL.md"
            target.parent.mkdir(parents=True)
            target.write_text("Synthetic instructions: preserve the evidence.\n")
        root_patch = patch.object(runner, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.runs = 0

    def execute(self, change=None, *, arm="baseline", edit_artifact=None, process_exit_code=0, error=None, **settings):
        self.runs += 1
        output = self.area / f"results-{self.runs}"
        run = output / f"{self.case}--{arm}"

        def fake_process(command, *, input, text, stdout, stderr, timeout):
            workspace = Path(command[command.index("-C") + 1])
            if isinstance(error, OSError):
                raise error
            stdout.write('{"type":"synthetic-event"}\n')
            stderr.write("synthetic process diagnostic\n")
            if change:
                change(workspace)
            if error:
                raise error
            Path(command[command.index("-o") + 1]).write_text("Unscored synthetic answer.\n")
            return subprocess.CompletedProcess(command, process_exit_code)

        with patch.object(runner.subprocess, "check_output", return_value="codex synthetic-test-version\n"), patch.object(runner.subprocess, "run", side_effect=fake_process), contextlib.redirect_stdout(io.StringIO()):
            code = runner.run_case(self.case, arm, output, None, edit_artifact, **settings)
        return code, json.loads((run / "metadata.json").read_text()), run

    def assert_run_retained(self, metadata, run, *, process_started=True):
        original = run / "original-input"
        self.assertTrue(original.is_dir())
        self.assertEqual({path.relative_to(original).as_posix(): path.read_bytes()
                          for path in original.rglob("*") if path.is_file()}, self.inputs)
        self.assertTrue((run / "prompt.txt").is_file())
        self.assertTrue((run / "events.jsonl").is_file())
        self.assertTrue((run / "stderr.txt").is_file())
        if process_started:
            self.assertIn('"synthetic-event"', (run / "events.jsonl").read_text())
            self.assertIn("synthetic process diagnostic", (run / "stderr.txt").read_text())
        self.assertEqual(metadata["quality_status"], "not_evaluated")

    def test_forbidden_input_edit_fails_integrity_even_when_process_succeeds(self):
        code, metadata, run = self.execute(lambda workspace: (workspace / "input/observations.md").write_text("rewritten evidence"))
        self.assertNotEqual(code, 0)
        self.assertEqual(metadata["process_exit_code"], 0)
        self.assertEqual(metadata["integrity_status"], "failed")
        self.assertIn({"path": "input/observations.md", "change": "modified"}, metadata["violations"])
        self.assert_run_retained(metadata, run)

    def test_unchanged_baseline_passes_integrity_without_a_quality_verdict(self):
        code, metadata, run = self.execute()
        self.assertEqual(code, 0)
        self.assertEqual(metadata["process_exit_code"], 0)
        self.assertEqual(metadata["integrity_status"], "passed")
        self.assertEqual(metadata["violations"], [])
        self.assert_run_retained(metadata, run)

    def test_explicit_execution_settings_are_recorded_without_inventing_observed_identity(self):
        code, metadata, run = self.execute(model="synthetic-model", reasoning_effort="low",
                                           timeout_seconds=17, max_output_words=350,
                                           condition="candidate", replicate=2, attempt=3)
        self.assertEqual(code, 0)
        self.assertEqual(metadata["condition"], "candidate")
        self.assertEqual((metadata["replicate"], metadata["attempt"]), (2, 3))
        self.assertEqual(metadata["execution_settings"]["model"], "synthetic-model")
        self.assertEqual(metadata["execution_settings"]["reasoning_effort"], "low")
        self.assertEqual(metadata["execution_settings"]["timeout_seconds"], 17)
        self.assertIn("synthetic-model", metadata["command"])
        self.assertIn('model_reasoning_effort="low"', metadata["command"])
        self.assertIn('web_search="disabled"', metadata["command"])
        self.assertIn("350 words", (run / "prompt.txt").read_text())
        self.assertIsNone(metadata["telemetry"]["observed_model"])
        self.assertEqual(metadata["telemetry"]["usage_status"], "unavailable")

    def test_timeout_retains_partial_evidence_without_claiming_a_billing_cap(self):
        timeout = subprocess.TimeoutExpired("synthetic codex", 1)
        code, metadata, run = self.execute(error=timeout, timeout_seconds=1)
        self.assertEqual(code, 124)
        self.assertIsNone(metadata["process_exit_code"])
        self.assertIn("descendant cleanup is unverified", metadata["execution_error"])
        self.assertEqual(metadata["telemetry"]["usage_status"], "unavailable")
        self.assert_run_retained(metadata, run)

    def test_invalid_run_limits_fail_before_model_execution_or_run_creation(self):
        for settings in ({"timeout_seconds": 0}, {"timeout_seconds": float("nan")},
                         {"timeout_seconds": float("inf")}, {"max_output_words": -1},
                         {"replicate": 0}, {"attempt": -1}, {"model": ""}):
            with self.subTest(settings=settings), patch.object(runner.subprocess, "run") as launch:
                output = self.area / "invalid-run"
                with self.assertRaises(ValueError):
                    runner.run_case(self.case, "baseline", output, None, **settings)
                launch.assert_not_called()
                self.assertFalse(output.exists())

    def test_a_frozen_skill_directory_is_copied_and_hashed_for_the_selected_condition(self):
        frozen = self.area / "frozen-skills"
        entrypoint = frozen / "bandit-specify" / "SKILL.md"
        entrypoint.parent.mkdir(parents=True)
        entrypoint.write_bytes(b"Frozen synthetic instructions.\n")
        code, metadata, run = self.execute(arm="bandit-specify", skills_dir=frozen, condition="current")
        self.assertEqual(code, 0)
        self.assertEqual((run / "workspace/.agents/skills/bandit-specify/SKILL.md").read_bytes(), entrypoint.read_bytes())
        self.assertEqual(metadata["instruction_sha256"]["bandit-specify/SKILL.md"],
                         hashlib.sha256(entrypoint.read_bytes()).hexdigest())

    def test_only_the_allowed_existing_prd_may_be_rewritten(self):
        revised = b"# Revised synthetic PRD\nA clearer action.\n"
        code, metadata, run = self.execute(lambda workspace: (workspace / "input/docs/PRD.md").write_bytes(revised),
                                           edit_artifact="input/docs/PRD.md")
        self.assertEqual(code, 0)
        self.assertEqual(metadata["integrity_status"], "passed")
        self.assertEqual(metadata["violations"], [])
        self.assertEqual((run / "workspace/input/docs/PRD.md").read_bytes(), revised)
        self.assert_run_retained(metadata, run)

    def test_forbidden_input_additions_and_deletions_are_reported(self):
        for change in ("created", "deleted"):
            with self.subTest(change=change):
                relative = "input/new-evidence.md" if change == "created" else "input/observations.md"

                def mutate(workspace):
                    target = workspace / relative
                    if change == "created":
                        target.write_text("invented evidence")
                    else:
                        target.unlink()

                code, metadata, run = self.execute(mutate)
                self.assertNotEqual(code, 0)
                self.assertEqual(metadata["integrity_status"], "failed")
                self.assertIn({"path": relative, "change": change}, metadata["violations"])
                self.assert_run_retained(metadata, run)

    def test_general_and_specialist_instructions_are_immutable(self):
        for arm, relative in (("bandit", "instructions/bandit/SKILL.md"),
                              ("bandit-specify", ".agents/skills/bandit-specify/SKILL.md")):
            with self.subTest(arm=arm):
                code, metadata, run = self.execute(lambda workspace: (workspace / relative).write_text("weaker instructions"), arm=arm)
                self.assertNotEqual(code, 0)
                self.assertEqual(metadata["integrity_status"], "failed")
                self.assertIn({"path": relative, "change": "modified"}, metadata["violations"])
                self.assert_run_retained(metadata, run)

    @unittest.skipIf(os.name == "nt", "Windows chmod does not expose POSIX permission bits")
    def test_permission_changes_are_violations_even_for_the_editable_prd(self):
        cases = (("baseline", "input/observations.md", None),
                 ("bandit", "instructions/bandit", None),
                 ("baseline", "input/docs/PRD.md", "input/docs/PRD.md"))
        for arm, relative, editable in cases:
            with self.subTest(relative=relative):
                def mutate(workspace):
                    target = workspace / relative
                    target.chmod(stat.S_IMODE(target.stat().st_mode) ^ stat.S_IWGRP)

                code, metadata, run = self.execute(mutate, arm=arm, edit_artifact=editable)
                self.assertNotEqual(code, 0)
                self.assertEqual(metadata["integrity_status"], "failed")
                self.assertIn({"path": relative, "change": "modified"}, metadata["violations"])
                self.assert_run_retained(metadata, run)

    def test_new_files_and_empty_directories_outside_input_are_violations(self):
        for relative in ("agent-notes.md", "empty-agent-output"):
            with self.subTest(relative=relative):
                def mutate(workspace):
                    target = workspace / relative
                    if relative.endswith(".md"):
                        target.write_text("unauthorized agent output")
                    else:
                        target.mkdir()

                code, metadata, run = self.execute(mutate)
                self.assertNotEqual(code, 0)
                self.assertEqual(metadata["integrity_status"], "failed")
                self.assertIn({"path": relative, "change": "created"}, metadata["violations"])
                self.assert_run_retained(metadata, run)

    def test_edit_permission_does_not_allow_deleting_or_replacing_the_prd(self):
        external = self.area / "external-prd.md"
        external.write_bytes(b"External synthetic content.\n")
        for replacement in ("deleted", "directory", "symlink"):
            with self.subTest(replacement=replacement):
                def mutate(workspace):
                    target = workspace / "input/docs/PRD.md"
                    target.unlink()
                    if replacement == "directory":
                        target.mkdir()
                    elif replacement == "symlink":
                        target.symlink_to(external)

                code, metadata, run = self.execute(mutate, edit_artifact="input/docs/PRD.md")
                self.assertNotEqual(code, 0)
                self.assertEqual(metadata["integrity_status"], "failed")
                change = "deleted" if replacement == "deleted" else "type_changed"
                self.assertIn({"path": "input/docs/PRD.md", "change": change}, metadata["violations"])
                self.assertEqual(external.read_bytes(), b"External synthetic content.\n")
                self.assert_run_retained(metadata, run)

    def test_new_external_symlink_outside_input_is_a_violation(self):
        external = self.area / "external-document.md"
        external.write_bytes(b"External synthetic document.\n")
        original_link = []

        def create_link(workspace):
            link = workspace / "agent-link"
            link.symlink_to(external)
            original_link.append(link.readlink())

        code, metadata, run = self.execute(create_link)
        self.assertNotEqual(code, 0)
        self.assertEqual(metadata["integrity_status"], "failed")
        self.assertIn({"path": "agent-link", "change": "created"}, metadata["violations"])
        self.assertEqual((run / "workspace/agent-link").readlink(), original_link[0])
        self.assertEqual(external.read_bytes(), b"External synthetic document.\n")
        self.assert_run_retained(metadata, run)

    def test_nonzero_process_exit_retains_raw_status_and_integrity_evidence(self):
        code, metadata, run = self.execute(lambda workspace: (workspace / "input/observations.md").unlink(), process_exit_code=17)
        self.assertNotEqual(code, 0)
        self.assertEqual(metadata["process_exit_code"], 17)
        self.assertEqual(metadata["integrity_status"], "failed")
        self.assertIn({"path": "input/observations.md", "change": "deleted"}, metadata["violations"])
        self.assert_run_retained(metadata, run)

    def test_launch_error_retains_metadata_inputs_and_log_files(self):
        code, metadata, run = self.execute(error=OSError("synthetic launch failure"))
        self.assertNotEqual(code, 0)
        self.assertIsNone(metadata["process_exit_code"])
        self.assertIn("synthetic launch failure", json.dumps(metadata) + (run / "stderr.txt").read_text())
        self.assert_run_retained(metadata, run, process_started=False)

    def test_keyboard_interrupt_retains_partial_logs_and_detects_mutation(self):
        code, metadata, run = self.execute(lambda workspace: (workspace / "input/observations.md").write_text("partial unauthorized edit"),
                                           error=KeyboardInterrupt())
        self.assertNotEqual(code, 0)
        self.assertIsNone(metadata["process_exit_code"])
        self.assertEqual(metadata["integrity_status"], "failed")
        self.assertIn({"path": "input/observations.md", "change": "modified"}, metadata["violations"])
        self.assert_run_retained(metadata, run)

    def test_snapshot_failure_never_produces_an_integrity_pass(self):
        original_snapshot = runner.workspace_snapshot
        for fail_at in (1, 2):
            with self.subTest(fail_at=fail_at):
                calls = 0

                def unavailable_snapshot(directory):
                    nonlocal calls
                    calls += 1
                    result = original_snapshot(directory)
                    if calls == fail_at:
                        result["errors"].append({"path": "input/observations.md", "error": "synthetic snapshot read failure"})
                    return result

                with patch.object(runner, "workspace_snapshot", side_effect=unavailable_snapshot):
                    code, metadata, run = self.execute()
                self.assertNotEqual(code, 0)
                self.assertEqual(metadata["integrity_status"], "unavailable")
                self.assertIn("synthetic snapshot read failure", json.dumps(metadata))
                self.assert_run_retained(metadata, run, process_started=metadata["process_exit_code"] is not None)

    def test_workspace_snapshot_records_files_directories_and_links_without_traversal(self):
        workspace = self.area / "snapshot-workspace"
        workspace.mkdir()
        (workspace / "empty").mkdir()
        content = b"Raw synthetic file.\x00\xff\r\n"
        (workspace / "document.bin").write_bytes(content)
        external = self.area / "external-tree"
        external.mkdir()
        outside = external / "outside.txt"
        outside.write_text("Do not read this external content.")
        # Inspecting a link must work even when its external target is unreadable.
        outside.chmod(0)
        self.addCleanup(outside.chmod, 0o600)
        (workspace / "file-link").symlink_to(external / "outside.txt")
        (workspace / "directory-link").symlink_to(external, target_is_directory=True)
        (workspace / "dangling-link").symlink_to(self.area / "absent-target")
        link_targets = {name: os.readlink(workspace / name)
                        for name in ("file-link", "directory-link", "dangling-link")}
        result = runner.workspace_snapshot(workspace)
        self.assertEqual(result["errors"], [])
        expected = {
            "empty": {"kind": "directory"},
            "document.bin": {"kind": "file", "sha256": hashlib.sha256(content).hexdigest()},
            **{name: {"kind": "symlink", "target": target} for name, target in link_targets.items()},
        }
        self.assertEqual(set(result["entries"]), set(expected))
        for relative, fields in expected.items():
            entry = result["entries"][relative]
            self.assertEqual({key: entry[key] for key in fields}, fields)
            self.assertEqual(entry["mode"], stat.S_IMODE((workspace / relative).lstat().st_mode))

    @unittest.skipIf(os.name == "nt", "This symlink replacement fixture requires POSIX link privileges")
    def test_portable_snapshot_rejects_a_file_swapped_to_a_symlink_at_open(self):
        workspace = self.area / "racing-workspace"
        workspace.mkdir()
        target = workspace / "document.md"
        target.write_text("Original synthetic input.")
        external = self.area / "external-race-target.md"
        external.write_bytes(b"External bytes must not enter the snapshot.")
        original_open = runner.os.open
        swapped = False

        def swap_before_open(path, flags, *args, **kwargs):
            nonlocal swapped
            if Path(path) == target and not swapped:
                swapped = True
                target.unlink()
                target.symlink_to(external)
            return original_open(path, flags, *args, **kwargs)

        # Exercise the portable identity guard even on hosts with O_NOFOLLOW.
        with patch.object(runner.os, "supports_dir_fd", set()), patch.object(runner.os, "O_NOFOLLOW", 0, create=True), patch.object(runner.os, "open", side_effect=swap_before_open):
            result = runner.workspace_snapshot(workspace)
        self.assertTrue(swapped)
        self.assertTrue(any(error["path"] == "document.md" for error in result["errors"]))
        self.assertNotIn("document.md", result["entries"])
        self.assertEqual(target.readlink(), external)
        self.assertEqual(external.read_bytes(), b"External bytes must not enter the snapshot.")
