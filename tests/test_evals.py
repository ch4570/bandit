import contextlib
from datetime import datetime, timezone
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

    def execute(self, change=None, *, arm="baseline", edit_artifact=None, process_exit_code=0, error=None,
                stdout_events=None, **settings):
        self.runs += 1
        output = self.area / f"results-{self.runs}"
        run = output / f"{self.case}--{arm}"

        def fake_process(command, *, input, text, stdout, stderr, timeout):
            workspace = Path(command[command.index("-C") + 1])
            if isinstance(error, OSError):
                raise error
            stdout.write('{"type":"synthetic-event"}\n')
            for event in stdout_events or []:
                stdout.write(json.dumps(event) + "\n")
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

    def test_local_cases_reject_unconfigured_upstream_before_launch(self):
        output = self.area / "unsupported-upstream"
        with patch.object(runner.subprocess, "check_output") as probe, patch.object(runner.subprocess, "run") as launch:
            for case in runner.LOCAL_CASES:
                with self.subTest(case=case), self.assertRaisesRegex(ValueError, "No pinned upstream route"):
                    runner.run_case(case, "upstream", output, self.area / "upstream")
            probe.assert_not_called()
            launch.assert_not_called()
        self.assertFalse(output.exists())

    def test_live_research_requires_explicit_opt_in_and_keeps_offline_cases_offline(self):
        output = self.area / "web-mode-mismatch"
        with patch.object(runner.subprocess, "run") as launch:
            for case, allow_web in ((runner.LIVE_CASES[0], False), (self.case, True)):
                with self.subTest(case=case), self.assertRaisesRegex(ValueError, "require --allow-web"):
                    runner.run_case(case, "baseline", output, None, allow_web=allow_web)
            launch.assert_not_called()
        self.assertFalse(output.exists())

    def test_live_research_records_web_setting_and_preserves_inputs(self):
        original_case = self.case
        self.case = runner.LIVE_CASES[0]
        (self.root / "evals/cases" / original_case).rename(self.root / "evals/cases" / self.case)
        code, metadata, run = self.execute(arm="bandit", allow_web=True)
        self.assertEqual(code, 0)
        self.assertEqual(metadata["integrity_status"], "passed")
        self.assertEqual(metadata["execution_settings"]["web_search"], "live")
        self.assertIn('web_search="live"', metadata["command"])
        prompt = (run / "prompt.txt").read_text()
        self.assertIn("using live web search", prompt)
        self.assertNotIn("Do not browse", prompt)
        self.assertEqual(metadata["input_sha256"], metadata["input_after_sha256"])

    def test_unchanged_baseline_passes_integrity_without_a_quality_verdict(self):
        code, metadata, run = self.execute()
        self.assertEqual(code, 0)
        self.assertEqual(metadata["process_exit_code"], 0)
        self.assertEqual(metadata["integrity_status"], "passed")
        self.assertEqual(metadata["violations"], [])
        self.assert_run_retained(metadata, run)

    def test_session_capture_default_remains_ephemeral_and_discloses_cli_coverage(self):
        with patch.object(runner, "collect_session_tools") as collect:
            code, metadata, run = self.execute()
        collect.assert_not_called()
        self.assertEqual(code, 0)
        self.assertIn("--ephemeral", metadata["command"])
        self.assertEqual(metadata["session_tools"]["status"], "not_requested")
        self.assertFalse(metadata["session_tools"]["requested"])
        self.assertIn("not a complete tool trace", metadata["session_tools"]["cli_event_coverage"])
        self.assertFalse((run / "session-tools.jsonl").exists())

    @unittest.skipUnless(hasattr(os, "O_NOFOLLOW") and hasattr(os, "O_DIRECTORY")
                         and os.open in os.supports_dir_fd and os.scandir in os.supports_fd,
                         "Safe descriptor-relative session traversal is unavailable on this host")
    def test_opt_in_capture_uses_persisted_exact_session_and_preserves_separate_verdicts(self):
        thread = "01a089b5-ad9f-7803-8a4c-bdccf12cb79c"
        home = self.area / "synthetic-codex-home"

        def persist_session(workspace):
            source = home / "sessions/2026/09/10" / f"rollout-synthetic-{thread}.jsonl"
            source.parent.mkdir(parents=True)
            rows = [
                {"type": "session_meta", "payload": {"id": thread, "cwd": str(workspace), "source": "exec",
                                                        "timestamp": datetime.now(timezone.utc).isoformat()}},
                {"type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn-1"}},
                {"type": "response_item", "payload": {"type": "custom_tool_call", "call_id": "call-1", "name": "exec", "input": "text(1+1);"}},
                {"type": "response_item", "payload": {"type": "custom_tool_call_output", "call_id": "call-1", "output": "2"}},
                {"type": "event_msg", "payload": {"type": "task_complete", "turn_id": "turn-1"}},
            ]
            source.write_text("".join(json.dumps(row) + "\n" for row in rows))

        with patch.dict(os.environ, {"CODEX_HOME": str(home)}):
            code, metadata, run = self.execute(persist_session, capture_session_tools=True,
                                               stdout_events=[{"type": "thread.started", "thread_id": thread}])
        self.assertEqual(code, 0)
        self.assertNotIn("--ephemeral", metadata["command"])
        self.assertTrue(metadata["execution_settings"]["capture_session_tools"])
        self.assertEqual(metadata["session_tools"]["status"], "captured")
        self.assertEqual(metadata["session_tools"]["record_count"], 2)
        self.assertEqual(metadata["session_tools"]["export_sha256"], hashlib.sha256((run / "session-tools.jsonl").read_bytes()).hexdigest())
        self.assertEqual(metadata["session_tools"]["capture_module_sha256"], hashlib.sha256((ROOT / "evals/session_tools.py").read_bytes()).hexdigest())
        self.assertEqual(metadata["process_exit_code"], 0)
        self.assertEqual(metadata["integrity_status"], "passed")
        self.assert_run_retained(metadata, run)

    def test_requested_capture_failure_retains_outputs_and_fails_independently(self):
        for process_exit_code in (0, 17):
            with self.subTest(process_exit_code=process_exit_code):
                code, metadata, run = self.execute(capture_session_tools=True, process_exit_code=process_exit_code)
                self.assertEqual(code, process_exit_code or 2)
                self.assertEqual(metadata["process_exit_code"], process_exit_code)
                self.assertEqual(metadata["integrity_status"], "passed")
                self.assertEqual(metadata["session_tools"]["status"], "unavailable")
                self.assertIn("Missing stdout", metadata["session_tools"]["errors"][0])
                self.assertTrue((run / "output.md").is_file())
                self.assertTrue((run / "session-tools.jsonl").is_file())
                self.assert_run_retained(metadata, run)

    def test_unsupported_capture_fails_runner_without_opening_host_sources_or_losing_outputs(self):
        thread = "01a089b5-ad9f-7803-8a4c-bdccf12cb79c"
        home = self.area / "synthetic-codex-home"
        source = home / "sessions" / f"rollout-synthetic-{thread}.jsonl"
        source.parent.mkdir(parents=True)
        source.write_bytes(b"Synthetic private session must not be read.\n")
        with patch.dict(os.environ, {"CODEX_HOME": str(home)}), \
                patch.object(runner.os, "supports_dir_fd", set()), \
                patch("evals.session_tools._directory") as host_directory:
            code, metadata, run = self.execute(capture_session_tools=True,
                                               stdout_events=[{"type": "thread.started", "thread_id": thread}])
        host_directory.assert_not_called()
        self.assertEqual(code, 2)
        self.assertEqual(metadata["process_exit_code"], 0)
        self.assertEqual(metadata["integrity_status"], "passed")
        self.assertEqual(metadata["session_tools"]["status"], "unavailable")
        self.assertIn("Safe session traversal is unavailable", metadata["session_tools"]["errors"][0])
        self.assertIsNone(metadata["session_tools"]["source_sha256"])
        self.assertEqual(metadata["session_tools"]["record_count"], 0)
        self.assertEqual((run / "session-tools.jsonl").read_bytes(), b"")
        self.assertEqual((run / "output.md").read_text(), "Unscored synthetic answer.\n")
        self.assertEqual(source.read_bytes(), b"Synthetic private session must not be read.\n")
        self.assert_run_retained(metadata, run)

    def test_cli_capture_flag_reaches_runner(self):
        arguments = ["run_local.py", "--case", self.case, "--arm", "baseline", "--output-dir", str(self.area),
                     "--capture-session-tools"]
        with patch.object(runner.sys, "argv", arguments), patch.object(runner, "run_case", return_value=0) as run:
            self.assertEqual(runner.main(), 0)
        self.assertTrue(run.call_args.kwargs["capture_session_tools"])

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

    def test_missing_selected_skill_fails_before_model_execution_or_run_creation(self):
        for arm in ("bandit", "bandit-research", "bandit-scope", "bandit-specify", "bandit-review"):
            for kind in ("empty", "individual-folder", "wrong-sibling", "directory-entrypoint"):
                with self.subTest(arm=arm, kind=kind):
                    frozen = self.area / f"{arm}-{kind}"
                    frozen.mkdir()
                    if kind == "individual-folder":
                        (frozen / "SKILL.md").write_text("Synthetic individual skill folder.\n")
                    elif kind == "wrong-sibling":
                        (frozen / "other-skill").mkdir()
                        (frozen / "other-skill/SKILL.md").write_text("Synthetic unrelated skill.\n")
                    elif kind == "directory-entrypoint":
                        (frozen / arm / "SKILL.md").mkdir(parents=True)
                    output = self.area / f"results-{arm}-{kind}"
                    with patch.object(runner.subprocess, "check_output", return_value="codex synthetic-test-version\n"), \
                            patch.object(runner.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)) as launch, \
                            contextlib.redirect_stdout(io.StringIO()):
                        with self.assertRaisesRegex(ValueError, "SKILL.md"):
                            runner.run_case(self.case, arm, output, None, skills_dir=frozen)
                    launch.assert_not_called()
                    self.assertFalse(output.exists())

    def test_baseline_does_not_require_a_skill_bundle(self):
        code, metadata, _ = self.execute(skills_dir=self.area / "absent-skills")
        self.assertEqual(code, 0)
        self.assertEqual(metadata["instruction_sha256"], {})

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

    def assert_workspace_root_mode_change_rejected(self, traversal):
        def mutate(workspace):
            workspace.chmod(stat.S_IMODE(workspace.stat().st_mode) ^ stat.S_IWOTH)

        code, metadata, run = self.execute(mutate, arm="bandit")
        self.assertNotEqual(code, 0)
        self.assertEqual(metadata["process_exit_code"], 0)
        self.assertEqual(metadata["integrity_status"], "failed")
        self.assertEqual(metadata["violations"], [{"path": ".", "change": "modified"}])
        before, after = metadata["workspace_before"], metadata["workspace_after"]
        for snapshot in (before, after):
            self.assertEqual(snapshot["traversal"], traversal)
            self.assertEqual(snapshot["entries"]["."]["kind"], "directory")
        self.assertEqual(before["entries"]["."]["mode"] ^ stat.S_IWOTH, after["entries"]["."]["mode"])
        self.assertEqual(metadata["input_sha256"], {name: hashlib.sha256(data).hexdigest()
                                                   for name, data in self.inputs.items()})
        self.assertEqual(metadata["input_sha256"], metadata["input_after_sha256"])
        self.assertEqual(set(metadata["instruction_sha256"]), {"bandit/SKILL.md"})
        self.assertEqual(metadata["instruction_sha256"], metadata["instruction_after_sha256"])
        self.assert_run_retained(metadata, run)

    @unittest.skipIf(os.name == "nt", "Windows chmod does not expose POSIX permission bits")
    @unittest.skipUnless(os.open in os.supports_dir_fd and os.scandir in os.supports_fd,
                         "Descriptor-relative traversal is unavailable")
    def test_descriptor_snapshot_detects_workspace_root_permission_changes(self):
        self.assert_workspace_root_mode_change_rejected("descriptor-relative")

    @unittest.skipIf(os.name == "nt", "Windows chmod does not expose POSIX permission bits")
    def test_portable_snapshot_detects_workspace_root_permission_changes(self):
        with patch.object(runner.os, "supports_dir_fd", set()):
            self.assert_workspace_root_mode_change_rejected("portable-quiescent")

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
            ".": {"kind": "directory"},
            "empty": {"kind": "directory"},
            "document.bin": {"kind": "file", "sha256": hashlib.sha256(content).hexdigest()},
            **{name: {"kind": "symlink", "target": target} for name, target in link_targets.items()},
        }
        self.assertEqual(set(result["entries"]), set(expected))
        for relative, fields in expected.items():
            entry = result["entries"][relative]
            self.assertEqual({key: entry[key] for key in fields}, fields)
            self.assertEqual(entry["mode"], stat.S_IMODE((workspace / relative).lstat().st_mode))

    @unittest.skipIf(os.name == "nt", "This root symlink fixture requires POSIX link privileges")
    def test_missing_or_nondirectory_workspace_root_never_passes_integrity(self):
        external = self.area / "external-root-target"
        external.mkdir()
        (external / "outside.txt").write_text("Do not traverse this external tree.")
        for kind in ("file", "symlink", "missing"):
            workspace = self.area / f"workspace-root-{kind}"
            if kind == "file":
                workspace.write_text("The workspace directory was replaced.")
            elif kind == "symlink":
                workspace.symlink_to(external, target_is_directory=True)
            for supports_dir_fd in (os.supports_dir_fd, set()):
                with self.subTest(kind=kind, portable=not supports_dir_fd):
                    with patch.object(runner.os, "supports_dir_fd", supports_dir_fd):
                        snapshot = runner.workspace_snapshot(workspace)
                    self.assertTrue(snapshot["errors"])
                    self.assertEqual({error["path"] for error in snapshot["errors"]}, {"."})
                    self.assertEqual(runner.integrity_result(snapshot, snapshot, None)["integrity_status"], "unavailable")
                    self.assertEqual(set(snapshot["entries"]), set() if kind == "missing" else {"."})
                    if kind != "missing":
                        self.assertEqual(snapshot["entries"]["."]["kind"], kind)
                        self.assertIn({"path": ".", "error": "Workspace root is no longer a directory"}, snapshot["errors"])
                    if kind == "symlink":
                        self.assertEqual(snapshot["entries"]["."]["target"], str(external))

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
