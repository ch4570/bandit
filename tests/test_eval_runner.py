"""Runner isolation and evidence preservation, not planning-quality tests."""
from _support import DistributionTest
from evals import run_local
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import subprocess
from unittest.mock import patch


class EvalRunnerTests(DistributionTest):
    def setUp(self):
        super().setUp()
        self.raw = self.area / "sequence/stage-1"
        (self.raw / "docs").mkdir(parents=True)
        (self.raw / "request.md").write_text("Rewrite input/docs/PRD.md.\n")
        (self.raw / "docs/PRD.md").write_text("Original adopted plan.\n")
        later = self.raw.parent / "stage-2"
        later.mkdir()
        (later / "request.md").write_text("A later direction not supplied yet.\n")
        self.output = self.area / "runs"

    def invoke(self, behavior, *, edit=None, web_search="disabled", version_error=None, model=None):
        with patch.object(run_local, "ROOT", self.source), \
             patch.object(run_local.subprocess, "check_output", return_value="codex-test\n", side_effect=version_error), \
             patch.object(run_local.subprocess, "run", side_effect=behavior), \
             redirect_stdout(io.StringIO()):
            return run_local.run_case("staged-task", "bandit-specify", self.output, None,
                                      edit, True, self.raw, web_search,
                                      **({"model": model} if model is not None else {}))

    def test_model_default_keeps_host_selection_and_existing_permissions(self):
        def task(command, **kwargs):
            workspace = Path(command[command.index("-C") + 1])
            self.assertEqual(command, [
                "codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
                "-c", 'web_search="disabled"', "--sandbox", "read-only", "--color", "never",
                "--json", "-C", str(workspace), "-o", str(workspace.parent / "output.md"), "-",
            ])
            self.assertIn("Do not browse or contact anyone", kwargs["input"])
            return subprocess.CompletedProcess(command, 0)

        self.assertEqual(self.invoke(task), 0)
        metadata = json.loads((self.output / "staged-task--bandit-specify/metadata.json").read_text())
        self.assertIsNone(metadata["model_override"])
        self.assertEqual(metadata["config"], "--ignore-user-config; host model defaults; explicit web_search")

    def test_model_override_is_forwarded_without_changing_web_or_sandbox_scope(self):
        for index, (model, web_search) in enumerate([
            ("synthetic-model", "disabled"), ("vendor/model:vNext+canary", "live"),
        ]):
            self.output = self.area / f"model-{index}"

            def task(command, **kwargs):
                self.assertEqual(command[-3:], ["--model", model, "-"])
                self.assertEqual(command.count("--model"), 1)
                self.assertEqual(command[command.index("-c") + 1], f'web_search="{web_search}"')
                self.assertEqual(command[command.index("--sandbox") + 1], "read-only")
                self.assertIn("--ignore-user-config", command)
                self.assertIn("--ephemeral", command)
                self.assertIn("Do not change files", kwargs["input"])
                metadata = json.loads((self.output / "staged-task--bandit-specify/metadata.json").read_text())
                self.assertEqual(metadata["model_override"], model)
                self.assertNotIn("host model defaults", metadata["config"])
                self.assertEqual(metadata["runner_status"], "running")
                return subprocess.CompletedProcess(command, 0)

            with self.subTest(model=model, web_search=web_search):
                self.assertEqual(self.invoke(task, model=model, web_search=web_search), 0)
                metadata = json.loads((self.output / "staged-task--bandit-specify/metadata.json").read_text())
                self.assertEqual(metadata["model_override"], model)
                self.assertEqual(metadata["config"], "--ignore-user-config; explicit model override; explicit web_search")
                self.assertEqual(metadata["web_search"], web_search)
                self.assertEqual(metadata["input_sha256"], metadata["input_after_sha256"])

    def test_model_invalid_identifiers_are_rejected_before_staging_or_subprocess(self):
        invalid = ["", " ", " synthetic", "synthetic ", "two models", "synthetic\tmodel",
                   "synthetic\nmodel", "synthetic\u00a0model", "-synthetic", "--model=other",
                   "synthetic\x00model", "synthetic\x1fmodel", "synthetic\x7fmodel",
                   "synthetic\x80model", "synthetic\x9fmodel", 0, True, b"synthetic-model"]
        for index, model in enumerate(invalid):
            output = self.area / f"invalid-model-{index}"
            with self.subTest(model=model), patch.object(run_local, "ROOT", self.source), \
                 patch.object(run_local.subprocess, "check_output") as probe, \
                 patch.object(run_local.subprocess, "run") as task, \
                 patch.object(run_local.shutil, "copytree") as copy:
                with self.assertRaises(ValueError):
                    run_local.run_case("staged-task", "bandit-specify", output, None,
                                       standalone=True, fixture_dir=self.raw, model=model)
                self.assertFalse(output.exists())
                probe.assert_not_called()
                task.assert_not_called()
                copy.assert_not_called()

    def test_model_override_is_retained_after_nonzero_task_exit(self):
        def task(command, **kwargs):
            kwargs["stdout"].write('{"type":"turn.failed"}\n')
            return subprocess.CompletedProcess(command, 9)

        self.assertEqual(self.invoke(task, model="synthetic-model"), 9)
        run = self.output / "staged-task--bandit-specify"
        metadata = json.loads((run / "metadata.json").read_text())
        self.assertEqual(metadata["model_override"], "synthetic-model")
        self.assertNotIn("host model defaults", metadata["config"])
        self.assertEqual(metadata["runner_status"], "exited")
        self.assertEqual(metadata["exit_code"], 9)
        self.assertTrue(metadata["finished_at_utc"].endswith("+00:00"))
        self.assertEqual(run_local.snapshot(run / "original-input"), metadata["input_sha256"])
        self.assertEqual(run_local.snapshot(run / "workspace/input"), metadata["input_after_sha256"])

    def test_model_override_is_retained_after_launch_failures(self):
        failures = [
            ("task_launch", FileNotFoundError("simulated task launch failure")),
            ("version_probe", FileNotFoundError("simulated missing codex executable")),
            ("version_probe", subprocess.CalledProcessError(7, ["codex", "--version"])),
        ]
        for index, (phase, failure) in enumerate(failures):
            self.output = self.area / f"model-launch-failure-{index}"

            def task(*args, **kwargs):
                if phase != "task_launch":
                    self.fail("Task must not launch after a failed version probe")
                raise failure

            with self.subTest(phase=phase, error=type(failure).__name__):
                with self.assertRaises(type(failure)):
                    self.invoke(task, model="synthetic-model",
                                version_error=failure if phase == "version_probe" else None)
                run = self.output / "staged-task--bandit-specify"
                metadata = json.loads((run / "metadata.json").read_text())
                self.assertEqual(metadata["model_override"], "synthetic-model")
                self.assertEqual(metadata["command"][-3:], ["--model", "synthetic-model", "-"])
                self.assertNotIn("host model defaults", metadata["config"])
                self.assertEqual(metadata["runner_status"], "launch_failed")
                self.assertIsNone(metadata["exit_code"])
                self.assertEqual(metadata["runner_error"]["phase"], phase)
                self.assertTrue(metadata["finished_at_utc"].endswith("+00:00"))
                self.assertEqual(run_local.snapshot(run / "original-input"), metadata["input_sha256"])
                self.assertEqual(run_local.snapshot(run / "workspace/input"), metadata["input_after_sha256"])

    def test_model_cli_argument_is_forwarded_after_web_search(self):
        argv = ["run_local.py", "--case", "staged-task", "--arm", "bandit-specify",
                "--output-dir", str(self.output), "--fixture-dir", str(self.raw), "--standalone",
                "--web-search", "live", "--model", "synthetic-model"]
        with patch("sys.argv", argv), patch.object(run_local, "run_case", return_value=9) as invoke, \
             redirect_stderr(io.StringIO()):
            self.assertEqual(run_local.main(), 9)
        invoke.assert_called_once_with("staged-task", "bandit-specify", self.output, None,
                                       None, True, self.raw, "live", "synthetic-model")
        self.assertFalse(self.output.exists())

    def test_model_cli_default_remains_unset(self):
        argv = ["run_local.py", "--case", "staged-task", "--arm", "bandit-specify",
                "--output-dir", str(self.output), "--fixture-dir", str(self.raw)]
        with patch("sys.argv", argv), patch.object(run_local, "run_case", return_value=0) as invoke:
            self.assertEqual(run_local.main(), 0)
        invoke.assert_called_once_with("staged-task", "bandit-specify", self.output, None,
                                       None, False, self.raw, "disabled", None)
        self.assertFalse(self.output.exists())

    def test_stage_contains_only_current_inputs_and_selected_skill(self):
        def task(command, **kwargs):
            self.assertEqual(command[command.index("-c") + 1], 'web_search="disabled"')
            workspace = Path(command[command.index("-C") + 1])
            self.assertEqual(set(run_local.snapshot(workspace / "input")), {"request.md", "docs/PRD.md"})
            self.assertEqual([p.name for p in (workspace / ".agents/skills").iterdir()], ["bandit-specify"])
            self.assertFalse((workspace / "stage-2").exists())
            (workspace / "input/docs/PRD.md").write_text("Rewritten plan.\n")
            return subprocess.CompletedProcess(command, 0)

        self.assertEqual(self.invoke(task, edit="input/docs/PRD.md"), 0)
        run = self.output / "staged-task--bandit-specify"
        self.assertEqual((run / "original-input/docs/PRD.md").read_text(), "Original adopted plan.\n")
        self.assertEqual((run / "workspace/input/docs/PRD.md").read_text(), "Rewritten plan.\n")
        self.assertEqual((self.raw / "docs/PRD.md").read_text(), "Original adopted plan.\n")
        metadata = json.loads((run / "metadata.json").read_text())
        self.assertNotEqual(metadata["input_sha256"]["docs/PRD.md"], metadata["input_after_sha256"]["docs/PRD.md"])
        self.assertTrue(metadata["custom_fixture"])
        self.assertEqual(metadata["web_search"], "disabled")

    def test_failed_task_retains_original_inputs_instructions_and_after_hashes(self):
        def task(command, **kwargs):
            workspace = Path(command[command.index("-C") + 1])
            self.assertNotIn("exit_code", json.loads((workspace.parent / "metadata.json").read_text()))
            (workspace / "input/docs/PRD.md").write_text("Unexpected task edit.\n")
            (workspace / ".agents/skills/bandit-specify/SKILL.md").write_text("Unexpected instruction edit.\n")
            kwargs["stdout"].write('{"type":"turn.failed"}\n')
            return subprocess.CompletedProcess(command, 1)

        self.assertEqual(self.invoke(task), 1)
        run = self.output / "staged-task--bandit-specify"
        metadata = json.loads((run / "metadata.json").read_text())
        self.assertEqual(metadata["exit_code"], 1)
        self.assertEqual(run_local.snapshot(run / "original-input"), metadata["input_sha256"])
        self.assertEqual(run_local.snapshot(run / "original-instructions"), metadata["instruction_sha256"])
        self.assertEqual(run_local.snapshot(run / "workspace/input"), metadata["input_after_sha256"])
        self.assertNotEqual(metadata["instruction_sha256"], metadata["instruction_after_sha256"])

    def test_launch_failures_are_terminal_without_a_task_exit_code(self):
        failures = [
            ("task_launch", FileNotFoundError("simulated task launch failure")),
            ("version_probe", FileNotFoundError("simulated missing codex executable")),
            ("version_probe", subprocess.CalledProcessError(7, ["codex", "--version"])),
        ]
        for index, (phase, failure) in enumerate(failures):
            self.output = self.area / f"failed-launch-{index}"

            def task(*args, **kwargs):
                if phase != "task_launch":
                    self.fail("Task must not launch after a failed version probe")
                raise failure

            with self.subTest(phase=phase, error=type(failure).__name__):
                with self.assertRaises(type(failure)):
                    self.invoke(task, web_search="live", version_error=failure if phase == "version_probe" else None)
                run = self.output / "staged-task--bandit-specify"
                metadata = json.loads((run / "metadata.json").read_text())
                self.assertEqual(metadata["runner_status"], "launch_failed")
                self.assertIsNone(metadata["exit_code"])
                self.assertEqual(metadata["runner_error"], {
                    "phase": phase, "type": type(failure).__name__, "message": str(failure),
                })
                self.assertEqual(metadata["codex_version"], "codex-test" if phase == "task_launch" else None)
                self.assertTrue(metadata["started_at_utc"].endswith("+00:00"))
                self.assertTrue(metadata["finished_at_utc"].endswith("+00:00"))
                self.assertGreaterEqual(metadata["finished_at_utc"], metadata["started_at_utc"])
                self.assertGreaterEqual(metadata["elapsed_seconds"], 0)
                self.assertEqual(metadata["web_search"], "live")
                self.assertEqual(run_local.snapshot(run / "original-input"), metadata["input_sha256"])
                self.assertEqual(run_local.snapshot(run / "workspace/input"), metadata["input_after_sha256"])
                self.assertEqual(run_local.snapshot(run / "original-instructions"), metadata["instruction_sha256"])
                self.assertEqual(run_local.snapshot(run / "workspace/.agents/skills"), metadata["instruction_after_sha256"])
                self.assertEqual((self.raw / "docs/PRD.md").read_text(), "Original adopted plan.\n")
                self.assertEqual((run / "events.jsonl").read_text(), "")
                self.assertEqual((run / "stderr.txt").read_text(), "")
                self.assertFalse((run / "output.md").exists())

    def test_instruction_source_overlap_is_rejected_before_any_staging(self):
        case = "01-multiple-decisions"
        built_in = self.source / "evals/cases" / case
        built_in.mkdir(parents=True)
        (built_in / "request.md").write_text("A synthetic request.\n")
        upstream = self.area / "upstream"
        upstream.mkdir()
        modes = [
            ("bandit-specify", True, self.source / "skills/bandit-specify", "standalone"),
            ("bandit-specify", False, self.source / "skills", "siblings"),
            ("bandit", False, self.source / "skills/bandit", "general"),
            ("upstream", False, upstream, "upstream"),
        ]
        for arm, standalone, source, label in modes:
            output = source / ("runs-" + label)
            before = run_local.snapshot(source)
            with self.subTest(mode=label), patch.object(run_local, "ROOT", self.source), \
                 patch.object(run_local.subprocess, "check_output", side_effect=[run_local.UPSTREAM_COMMIT, ""]), \
                 patch.object(run_local.shutil, "copytree", side_effect=AssertionError("Must reject before copying")), \
                 patch.object(run_local.subprocess, "run", side_effect=AssertionError("Task must not launch")):
                with self.assertRaisesRegex(ValueError, "overlap"):
                    run_local.run_case(case, arm, output, upstream, standalone=standalone)
                self.assertFalse(output.exists())
                self.assertEqual(run_local.snapshot(source), before)

    def test_linked_instruction_source_overlap_is_rejected_before_staging(self):
        alias = self.area / "skill-alias"
        self.link(alias, self.source / "skills/bandit-specify", directory=True)
        self.output = alias / "runs"
        with patch.object(run_local.shutil, "copytree", side_effect=AssertionError("Must reject before copying")):
            with self.assertRaisesRegex(ValueError, "overlap"):
                self.invoke(lambda *args, **kwargs: self.fail("Task must not launch"))
        self.assertFalse(self.output.exists())

    def test_standalone_output_may_use_an_unselected_sibling_directory(self):
        self.output = self.source / "skills/bandit-review/runs"
        self.assertEqual(self.invoke(lambda command, **kwargs: subprocess.CompletedProcess(command, 0)), 0)

    def test_nested_instruction_link_cannot_reenter_the_output_directory(self):
        self.output.mkdir()
        linked_output = self.source / "skills/bandit-specify/linked-output"
        self.link(linked_output, self.output, directory=True)
        with patch.object(run_local.shutil, "copytree", side_effect=AssertionError("Must reject before copying")):
            with self.assertRaisesRegex(ValueError, "symlinks"):
                self.invoke(lambda *args, **kwargs: self.fail("Task must not launch"))
        self.assertEqual(list(self.output.iterdir()), [])
        self.assertTrue(linked_output.is_symlink())

    def test_upstream_ignored_links_are_not_copied_or_treated_as_resources(self):
        case = "01-multiple-decisions"
        fixture = self.source / "evals/cases" / case
        fixture.mkdir(parents=True)
        (fixture / "request.md").write_text("A synthetic request.\n")
        upstream = self.area / "upstream"
        upstream.mkdir()
        self.link(upstream / ".git", self.area / "absent-git-dir", directory=True)
        self.link(upstream / "__pycache__", self.area / "absent-cache-dir", directory=True)
        for name in run_local.ROUTES[case]:
            target = upstream / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("Synthetic upstream instructions.\n")

        def task(command, **kwargs):
            workspace = Path(command[command.index("-C") + 1])
            self.assertEqual(set(run_local.snapshot(workspace / "instructions/upstream")), set(run_local.ROUTES[case]))
            return subprocess.CompletedProcess(command, 0)

        with patch.object(run_local, "ROOT", self.source), \
             patch.object(run_local.subprocess, "check_output", side_effect=[run_local.UPSTREAM_COMMIT, "", "codex-test\n"]), \
             patch.object(run_local.subprocess, "run", side_effect=task), redirect_stdout(io.StringIO()):
            self.assertEqual(run_local.run_case(case, "upstream", self.output, upstream), 0)

    def test_invalid_targets_and_overlapping_output_leave_no_run_directory(self):
        for edit in ["input/missing.md", "../outside.md", "input/../../outside.md", "."]:
            with self.subTest(edit=edit), self.assertRaises(ValueError):
                self.invoke(lambda *args, **kwargs: self.fail("Task must not launch"), edit=edit)
            self.assertFalse(self.output.exists())
        with self.assertRaisesRegex(ValueError, "overlap"):
            run_local.run_case("stage", "baseline", self.raw / "runs", None, fixture_dir=self.raw)
        self.assertFalse((self.raw / "runs").exists())
        with self.assertRaisesRegex(ValueError, "Case names"):
            run_local.run_case("../escape", "baseline", self.output, None, fixture_dir=self.raw)
        self.assertFalse(self.output.exists())

    def test_fixture_symlink_cannot_import_other_stage_or_external_material(self):
        self.link(self.raw / "future.md", self.raw.parent / "stage-2/request.md")
        with self.assertRaisesRegex(ValueError, "symlinks"):
            self.invoke(lambda *args, **kwargs: self.fail("Task must not launch"))
        self.assertFalse(self.output.exists())

    def test_web_search_is_explicit_and_does_not_expand_write_permissions(self):
        for mode in ("disabled", "live"):
            self.output = self.area / ("runs-" + mode)

            def task(command, **kwargs):
                self.assertEqual(command[command.index("-c") + 1], f'web_search="{mode}"')
                self.assertEqual(command[command.index("--sandbox") + 1], "read-only")
                self.assertIn("--ignore-user-config", command)
                self.assertIn("--ephemeral", command)
                self.assertIn("Do not change files", kwargs["input"])
                if mode == "live":
                    self.assertIn("Public web search and reading are allowed only", kwargs["input"])
                    self.assertIn("Do not sign in, submit forms, contact anyone", kwargs["input"])
                    self.assertNotIn("Do not browse", kwargs["input"])
                else:
                    self.assertIn("Do not browse or contact anyone", kwargs["input"])
                return subprocess.CompletedProcess(command, 0)

            with self.subTest(mode=mode):
                self.assertEqual(self.invoke(task, web_search=mode), 0)
                metadata = json.loads((self.output / "staged-task--bandit-specify/metadata.json").read_text())
                self.assertEqual(metadata["web_search"], mode)
                self.assertTrue(metadata["started_at_utc"].endswith("+00:00"))
                self.assertGreaterEqual(metadata["finished_at_utc"], metadata["started_at_utc"])
                self.assertEqual(metadata["input_sha256"], metadata["input_after_sha256"])

    def test_unknown_web_search_mode_is_rejected_before_staging(self):
        with self.assertRaisesRegex(ValueError, "Web search"):
            self.invoke(lambda *args, **kwargs: self.fail("Task must not launch"), web_search="cached")
        self.assertFalse(self.output.exists())
