"""Dependency-free comparison checks using synthetic, never model-generated runs."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from evals.compare import summarize_comparison


ROOT = Path(__file__).resolve().parents[1]


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


class EvalComparisonTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="bandit synthetic comparison ")
        self.addCleanup(temporary.cleanup)
        self.area = Path(temporary.name).resolve()
        self.manifest = {"schema": "bandit.comparison/v1", "conditions": ["baseline", "bandit"], "runs": []}
        self.pricing = {"model": "synthetic-model", "currency": "USD", "effective_date": "2026-09-01",
                        "source_url": "https://example.com/synthetic-pricing", "input_per_million": 2,
                        "cached_input_per_million": 1, "output_per_million": 4}
        self.settings = {"model": "synthetic-model", "reasoning_effort": "high", "timeout_seconds": 60,
                         "max_output_words": 1000, "web_search": "disabled", "multi_agent": False}

    def add_run(self, condition, *, case="synthetic-case", replicate=1, attempt=1, status="passed", arm=None,
                exit_code=0, integrity="passed", edited=False, events=None, metadata_changes=None):
        run_id = f"{condition}-{case}-{replicate}-{attempt}"
        directory = self.area / run_id
        directory.mkdir()
        output = "Synthetic evaluation output.\n"
        (directory / "output.md").write_bytes(output.encode("utf-8"))
        if events is None:
            events = [{"type": "thread.started", "thread_id": run_id, "model": "synthetic-model", "reasoning_effort": "high"},
                      {"type": "turn.started"},
                      {"type": "turn.completed", "usage": {"input_tokens": 100, "cached_input_tokens": 40,
                                                             "output_tokens": 20}}]
        (directory / "events.jsonl").write_text("".join(json.dumps(event) + "\n" for event in events))
        arm = arm or ("baseline" if condition == "baseline" else "bandit")
        invocation = f"${arm}" if arm.startswith("bandit-") else None
        metadata = {"case": case, "arm": arm, "invocation": invocation,
                    "condition": condition, "replicate": replicate, "attempt": attempt,
                    "execution_settings": dict(self.settings), "codex_version": "codex synthetic-test-version",
                    "runner_sha256": digest("Synthetic frozen runner source"),
                    "input_sha256": {"request.md": digest("Synthetic task input")},
                    "instruction_sha256": {} if arm == "baseline" else {f"{arm}/SKILL.md": digest("Synthetic instructions")},
                    "editable_artifact": None, "input_after_sha256": {"request.md": digest("Synthetic task input")},
                    "exit_code": exit_code, "process_exit_code": exit_code, "integrity_status": integrity,
                    "elapsed_seconds": 10}
        quality = {"status": status, "evidence": "Synthetic rubric review, all required checks recorded.",
                   "output_sha256": digest(output)}
        if edited:
            artifact = directory / "workspace/input/docs/PRD.md"
            artifact.parent.mkdir(parents=True)
            artifact.write_bytes(b"Synthetic revised PRD\n")
            metadata["editable_artifact"] = "input/docs/PRD.md"
            metadata["input_after_sha256"]["docs/PRD.md"] = digest("Synthetic revised PRD\n")
            quality["artifact_sha256"] = metadata["input_after_sha256"]["docs/PRD.md"]
        metadata.update(metadata_changes or {})
        (directory / "metadata.json").write_text(json.dumps(metadata))
        entry = {"id": run_id, "directory": run_id, "condition": condition, "case": case,
                 "replicate": replicate, "attempt": attempt, "quality": quality}
        self.manifest["runs"].append(entry)
        return entry, directory

    def pair(self, **kwargs):
        return self.add_run("baseline", **kwargs), self.add_run("bandit", **kwargs)

    def summarize(self, pricing=True):
        return summarize_comparison(self.manifest, self.area, self.pricing if pricing else None)

    def change_metadata(self, directory, **changes):
        path = directory / "metadata.json"
        metadata = json.loads(path.read_text())
        metadata.update(changes)
        path.write_text(json.dumps(metadata))

    def test_matched_runs_report_descriptive_usage_quality_and_cache_correct_cost(self):
        self.pair()
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])
        self.assertEqual(result["usage_scope"], "top-level-cli-events")
        for condition in result["conditions"].values():
            self.assertEqual(condition["successful_tasks"], 1)
            self.assertEqual(condition["usage"]["input_tokens"], 100)
            self.assertEqual(condition["usage"]["cached_input_tokens"], 40)
            self.assertEqual(condition["usage"]["total_tokens"], 120)
            self.assertAlmostEqual(condition["cost"], 0.00024)
            self.assertAlmostEqual(condition["cost_per_successful_task"], 0.00024)
            self.assertEqual(condition["elapsed_seconds_per_successful_task"], 10)

    def test_failed_attempts_and_retries_stay_in_the_numerator(self):
        self.pair(status="failed", exit_code=1)
        self.pair(attempt=2)
        self.pair(attempt=3)
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])
        for condition in result["conditions"].values():
            self.assertEqual(condition["run_count"], 3)
            self.assertEqual(condition["retry_count"], 2)
            self.assertEqual(condition["successful_attempts"], 2)
            self.assertEqual(condition["successful_tasks"], 1)
            self.assertEqual(condition["failed_attempts"], 1)
            self.assertEqual(condition["usage"]["total_tokens"], 360)
            self.assertAlmostEqual(condition["cost_per_successful_task"], 0.00072)
            self.assertEqual(condition["elapsed_seconds_per_successful_task"], 30)

    def test_success_denominator_counts_distinct_case_replicate_tasks(self):
        self.pair()
        self.pair(replicate=2)
        self.pair(case="another-synthetic-case")
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])
        for condition in result["conditions"].values():
            self.assertEqual(condition["successful_tasks"], 3)
            self.assertAlmostEqual(condition["cost_per_successful_task"], 0.00024)

    def test_zero_successes_leave_cost_per_success_null(self):
        self.pair(status="failed")
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])
        self.assertIsNone(result["conditions"]["baseline"]["cost_per_successful_task"])
        self.assertIsNone(result["conditions"]["baseline"]["elapsed_seconds_per_successful_task"])
        self.assertAlmostEqual(result["conditions"]["baseline"]["cost"], 0.00024)

    def test_process_and_integrity_failures_cannot_be_quality_successes(self):
        self.add_run("baseline", exit_code=9)
        self.add_run("bandit", integrity="failed")
        result = self.summarize()
        for condition in result["conditions"].values():
            self.assertEqual(condition["successful_tasks"], 0)
            self.assertEqual(condition["failed_attempts"], 1)

    def test_missing_grade_or_evidence_remains_unavailable(self):
        (first, _), (second, _) = self.pair()
        first.pop("quality")
        second["quality"].pop("evidence")
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        for condition in result["conditions"].values():
            self.assertEqual(condition["successful_tasks"], 0)
            self.assertEqual(condition["unavailable_attempts"], 1)
            self.assertEqual(condition["quality_unavailable_runs"], 1)
            self.assertIsNone(condition["cost_per_successful_task"])

    def test_stale_output_grade_is_unavailable(self):
        (_, directory), _ = self.pair()
        (directory / "output.md").write_text("Output changed after grading\n")
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertIn("output_sha256", " ".join(result["reasons"]))
        self.assertEqual(result["conditions"]["baseline"]["successful_tasks"], 0)

    def test_edited_artifact_requires_matching_content_and_recorded_hash(self):
        (_, directory), (other, _) = self.pair(edited=True)
        self.assertEqual(self.summarize()["status"], "complete")
        (directory / "workspace/input/docs/PRD.md").write_text("Changed after grading\n")
        other["quality"].pop("artifact_sha256")
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertTrue(all(run["quality_status"] == "unavailable" for run in result["runs"]))

    def test_edited_artifact_grade_also_checks_input_after_hash(self):
        (_, directory), _ = self.pair(edited=True)
        self.change_metadata(directory, input_after_sha256={"docs/PRD.md": digest("Wrong recorded digest")})
        self.assertIn("recorded hash", " ".join(self.summarize()["reasons"]))

    def test_missing_artifact_mode_cannot_turn_rewrites_into_answer_only_successes(self):
        for entry, directory in self.pair(edited=True):
            path = directory / "metadata.json"
            metadata = json.loads(path.read_text())
            metadata.pop("editable_artifact")
            path.write_text(json.dumps(metadata))
            entry["quality"].pop("artifact_sha256")
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(sum("editable_artifact unavailable" in reason for reason in result["reasons"]), 2)
        for condition in result["conditions"].values():
            self.assertEqual(condition["successful_tasks"], 0)
            self.assertEqual(condition["quality_unavailable_runs"], 1)
            self.assertEqual(condition["unavailable_attempts"], 1)
            self.assertIsNone(condition["cost_per_successful_task"])
            self.assertEqual(condition["usage"]["total_tokens"], 120)

    def test_explicit_null_artifact_mode_allows_answer_only_quality(self):
        self.pair()
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])
        self.assertTrue(all(run["quality_status"] == "passed" for run in result["runs"]))

    def test_malformed_artifact_mode_never_counts_as_quality_success(self):
        runs = self.pair()
        for artifact in ("", " ", False, 0, [], {}, "input/", "input/missing.md"):
            with self.subTest(artifact=artifact):
                for _, directory in runs:
                    self.change_metadata(directory, editable_artifact=artifact)
                result = self.summarize()
                self.assertEqual(result["status"], "incomplete")
                for condition in result["conditions"].values():
                    self.assertEqual(condition["successful_tasks"], 0)
                    self.assertEqual(condition["quality_unavailable_runs"], 1)

    def test_specialist_route_cannot_change_within_condition_case_with_identical_bundle(self):
        bundle = {f"{skill}/SKILL.md": digest(f"Synthetic {skill} instructions")
                  for skill in ("bandit", "bandit-research", "bandit-scope", "bandit-specify", "bandit-review")}
        self.add_run("baseline")
        self.add_run("bandit", arm="bandit-specify", metadata_changes={"instruction_sha256": bundle})
        self.add_run("baseline", replicate=2)
        _, directory = self.add_run("bandit", arm="bandit-scope", replicate=2,
                                    metadata_changes={"instruction_sha256": bundle})
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        for field in ("arm", "invocation"):
            self.assertIn(f"{field} differs within condition/case", " ".join(result["reasons"]))
        self.change_metadata(directory, arm="bandit-specify", invocation="$bandit-specify")
        self.assertEqual(self.summarize()["status"], "complete")
        self.add_run("bandit", arm="bandit-review", attempt=2,
                     metadata_changes={"instruction_sha256": bundle})
        self.assertIn("arm differs within condition/case", " ".join(self.summarize()["reasons"]))

    def test_routes_can_differ_between_cases_and_intentional_conditions(self):
        self.manifest["conditions"] = ["baseline", "current", "candidate", "upstream"]
        for replicate in (1, 2):
            for case, current, candidate in (("scope-case", "bandit-scope", "bandit"),
                                              ("specify-case", "bandit-specify", "bandit-review")):
                for condition, arm in (("baseline", "baseline"), ("current", current),
                                       ("candidate", candidate), ("upstream", "upstream")):
                    self.add_run(condition, case=case, replicate=replicate, arm=arm)
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])

    def test_missing_arm_or_invocation_cannot_make_a_complete_comparison(self):
        runs = self.pair()
        originals = [(directory, (directory / "metadata.json").read_text()) for _, directory in runs]
        for field in ("arm", "invocation"):
            with self.subTest(field=field):
                for directory, original in originals:
                    metadata = json.loads(original)
                    metadata.pop(field)
                    (directory / "metadata.json").write_text(json.dumps(metadata))
                result = self.summarize()
                self.assertEqual(result["status"], "incomplete")
                self.assertEqual(sum(f"{field} unavailable" in reason for reason in result["reasons"]), 2)

    def test_malformed_or_mismatched_routes_cannot_make_a_complete_comparison(self):
        runs = self.pair()
        routes = [(arm, None) for arm in (None, "", " ", [], {}, "unknown", 1)]
        routes += [("baseline", invocation) for invocation in ("", "$baseline", "$bandit-scope", [], 1)]
        routes += [("bandit-scope", invocation) for invocation in (None, "", "$bandit-specify", [], 1)]
        for arm, invocation in routes:
            with self.subTest(arm=arm, invocation=invocation):
                for _, directory in runs:
                    self.change_metadata(directory, arm=arm, invocation=invocation)
                result = self.summarize()
                self.assertEqual(result["status"], "incomplete")
                self.assertTrue(any("arm unavailable" in reason or "invocation" in reason
                                    for reason in result["reasons"]))

    def test_missing_usage_is_not_zero_and_retains_observed_condition_totals(self):
        self.pair()
        self.add_run("baseline", replicate=2, events=[])
        self.add_run("bandit", replicate=2)
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        condition = result["conditions"]["baseline"]
        self.assertEqual(condition["usage_status"], "unavailable")
        self.assertIsNone(condition["usage"])
        self.assertIsNone(condition["cost"])
        self.assertEqual(condition["observed_usage"]["total_tokens"], 120)
        self.assertAlmostEqual(condition["observed_costs"]["USD"], 0.00024)
        self.assertEqual(condition["usage_unavailable_runs"], 1)

    def test_missing_runtime_identity_is_not_inferred_from_requested_settings(self):
        events = [{"type": "thread.started", "thread_id": "synthetic-no-route"}, {"type": "turn.started"},
                  {"type": "turn.completed", "usage": {"input_tokens": 100, "cached_input_tokens": 40, "output_tokens": 20}}]
        self.pair(events=events)
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertIn("observed_model unavailable", " ".join(result["reasons"]))
        self.assertIn("observed_reasoning_effort unavailable", " ".join(result["reasons"]))
        self.assertEqual(result["conditions"]["baseline"]["usage"]["total_tokens"], 120)
        self.assertIsNone(result["conditions"]["baseline"]["cost"])

    def test_raw_events_override_cached_metadata_telemetry(self):
        self.pair(metadata_changes={"telemetry": {"usage_status": "available", "usage": {"total_tokens": 0}}})
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])
        self.assertEqual(result["conditions"]["baseline"]["usage"]["total_tokens"], 120)

    def test_final_cumulative_snapshot_is_counted_once_per_fresh_run(self):
        events = [{"type": "thread.started", "thread_id": "synthetic-cumulative-session", "model": "synthetic-model", "reasoning_effort": "high"},
                  {"type": "turn.started"},
                  {"type": "turn.completed", "usage": {"input_tokens": 100, "cached_input_tokens": 40, "output_tokens": 20}},
                  {"type": "turn.started"},
                  {"type": "turn.completed", "usage": {"input_tokens": 200, "cached_input_tokens": 80, "output_tokens": 40}}]
        self.pair(events=events)
        self.pair(replicate=2, events=events)
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])
        for run in result["runs"]:
            self.assertEqual(run["telemetry"]["usage_semantics"], "cumulative-session-snapshot")
            self.assertEqual(run["telemetry"]["usage"]["total_tokens"], 240)
        for condition in result["conditions"].values():
            self.assertEqual(condition["usage"]["input_tokens"], 400)
            self.assertEqual(condition["usage"]["total_tokens"], 480)
            self.assertAlmostEqual(condition["cost"], 0.00096)

    def test_settings_fixture_cli_and_instruction_mismatches_are_explicit(self):
        (_, directory), _ = self.pair()
        original = (directory / "metadata.json").read_text()
        differences = {"execution_settings": {**self.settings, "max_output_words": 2000},
                       "codex_version": "codex synthetic-other-version",
                       "input_sha256": {"request.md": digest("Different fixture")}}
        for field, value in differences.items():
            with self.subTest(field=field):
                (directory / "metadata.json").write_text(original)
                self.change_metadata(directory, **{field: value})
                result = self.summarize()
                self.assertEqual(result["status"], "incomplete")
                self.assertIn(f"{field} differs", " ".join(result["reasons"]))
        (directory / "metadata.json").write_text(original)
        self.pair(replicate=2)
        self.change_metadata(directory, instruction_sha256={"SKILL.md": digest("Changed instructions")})
        self.assertIn("instruction_sha256 differs", " ".join(self.summarize()["reasons"]))

    def test_missing_settings_and_elapsed_data_remain_unknown(self):
        self.pair(metadata_changes={"execution_settings": None, "elapsed_seconds": None})
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertIsNone(result["conditions"]["baseline"]["elapsed_seconds"])
        self.assertIsNone(result["conditions"]["baseline"]["observed_elapsed_seconds"])

    def test_selected_instruction_entrypoint_is_required_for_skill_arms(self):
        self.add_run("baseline")
        _, directory = self.add_run("bandit")
        for arm in ("bandit", "bandit-research", "bandit-scope", "bandit-specify", "bandit-review"):
            invocation = f"${arm}" if arm != "bandit" else None
            for inventory in ({}, {"SKILL.md": digest("Wrong-level entrypoint")},
                              {"other-skill/SKILL.md": digest("Wrong skill")},
                              {f"{arm}/references/guide.md": digest("Missing entrypoint")}):
                with self.subTest(arm=arm, inventory=inventory):
                    self.change_metadata(directory, arm=arm, invocation=invocation, instruction_sha256=inventory)
                    result = self.summarize()
                    self.assertEqual(result["status"], "incomplete")
                    self.assertTrue(any("instruction_sha256" in reason for reason in result["reasons"]))
            self.change_metadata(directory, instruction_sha256={f"{arm}/SKILL.md": digest("Selected entrypoint")})
            result = self.summarize()
            self.assertEqual(result["status"], "complete", result["reasons"])

    def test_upstream_needs_nonempty_instructions_while_baseline_allows_empty(self):
        self.add_run("baseline")
        _, directory = self.add_run("bandit", arm="upstream", metadata_changes={"instruction_sha256": {}})
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertIn("instruction_sha256 unavailable or invalid", " ".join(result["reasons"]))
        self.assertEqual(result["runs"][0]["reasons"], [])
        self.change_metadata(directory, instruction_sha256={"upstream/skills/create-prd/SKILL.md": digest("Upstream skill")})
        result = self.summarize()
        self.assertEqual(result["status"], "complete", result["reasons"])

    def test_multi_agent_usage_is_never_assumed_to_cover_children(self):
        self.pair(metadata_changes={"execution_settings": {**self.settings, "multi_agent": True}})
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["usage_scope"], "top-level-cli-events")
        self.assertIn("multi-agent must be disabled", " ".join(result["reasons"]))

    def test_missing_condition_case_or_replicate_cell_is_incomplete(self):
        self.pair()
        self.add_run("baseline", replicate=2)
        self.add_run("baseline", case="only-baseline")
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(sum("missing matched task cell" in reason for reason in result["reasons"]), 2)

    def test_missing_retry_indices_are_incomplete_without_losing_supplied_costs(self):
        self.pair(attempt=2)
        self.add_run("baseline", attempt=5)
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        reasons = " ".join(result["reasons"])
        self.assertIn("missing attempt 1", reasons)
        self.assertIn("missing attempt 3..4", reasons)
        self.assertAlmostEqual(result["conditions"]["baseline"]["cost"], 0.00048)
        self.assertEqual(result["conditions"]["baseline"]["run_count"], 2)

    def test_unbound_runtime_setting_and_changed_runner_are_incomplete(self):
        (_, directory), _ = self.pair()
        self.change_metadata(directory, execution_settings={**self.settings, "reasoning_effort": "low"},
                             runner_sha256=digest("Different runner source"))
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        reasons = " ".join(result["reasons"])
        self.assertIn("observed_reasoning_effort does not match requested", reasons)
        self.assertIn("runner_sha256 differs", reasons)

    def test_missing_runner_hashes_cannot_make_a_complete_comparison(self):
        for _, directory in self.pair():
            path = directory / "metadata.json"
            metadata = json.loads(path.read_text())
            metadata.pop("runner_sha256")
            path.write_text(json.dumps(metadata))
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(sum("runner_sha256 unavailable or invalid" in reason for reason in result["reasons"]), 2)
        self.assertEqual(result["conditions"]["baseline"]["usage"]["total_tokens"], 120)

    def test_identically_malformed_runner_hashes_still_make_comparison_incomplete(self):
        runs = self.pair()
        for value in (None, "", "a" * 63, "g" * 64, 123, []):
            with self.subTest(value=value):
                for _, directory in runs:
                    self.change_metadata(directory, runner_sha256=value)
                result = self.summarize()
                self.assertEqual(result["status"], "incomplete")
                self.assertEqual(sum("runner_sha256 unavailable or invalid" in reason for reason in result["reasons"]), 2)

    def test_duplicate_usage_events_cannot_be_double_counted_as_complete(self):
        events = [{"type": "thread.started", "thread_id": "synthetic-duplicate-terminal", "model": "synthetic-model", "reasoning_effort": "high"},
                  {"type": "turn.started"},
                  {"type": "turn.completed", "usage": {"input_tokens": 100, "cached_input_tokens": 40, "output_tokens": 20}}]
        events.append(copy.deepcopy(events[-1]))
        self.pair(events=events)
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertIsNone(result["conditions"]["baseline"]["usage"])
        self.assertIsNone(result["conditions"]["baseline"]["cost"])

    def test_missing_directory_and_corrupt_metadata_preserve_the_other_runs(self):
        (_, directory), _ = self.pair()
        (directory / "metadata.json").write_text("{invalid JSON")
        missing = copy.deepcopy(self.manifest["runs"][0])
        missing.update(id="missing-run", directory="missing-run", replicate=2)
        self.manifest["runs"].append(missing)
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["conditions"]["bandit"]["successful_tasks"], 1)
        self.assertEqual(result["run_count"], 3)

    def test_duplicate_resolved_directory_is_not_double_charged(self):
        (entry, directory), _ = self.pair()
        duplicate = copy.deepcopy(entry)
        duplicate["directory"] = str(directory)
        self.manifest["runs"].append(duplicate)
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["manifest_run_count"], 3)
        self.assertEqual(result["run_count"], 2)
        self.assertEqual(result["conditions"]["baseline"]["usage"]["total_tokens"], 120)
        for text in ("duplicate id", "duplicate condition/case/replicate/attempt", "duplicate run directory"):
            self.assertIn(text, " ".join(result["reasons"]))

    def test_duplicate_ids_on_distinct_attempts_remain_incomplete_with_all_costs(self):
        (first, _), _ = self.pair()
        second, _ = self.add_run("baseline", attempt=2)
        second["id"] = first["id"]
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["conditions"]["baseline"]["run_count"], 2)
        self.assertAlmostEqual(result["conditions"]["baseline"]["cost"], 0.00048)

    def test_no_pricing_leaves_tokens_comparable_and_currency_cost_unavailable(self):
        self.pair()
        result = self.summarize(pricing=False)
        self.assertEqual(result["status"], "complete", result["reasons"])
        self.assertEqual(result["conditions"]["baseline"]["cost_status"], "unavailable")
        self.assertIsNone(result["conditions"]["baseline"]["cost_per_successful_task"])

    def test_wrong_model_pricing_does_not_produce_a_cost(self):
        self.pair()
        self.pricing["model"] = "different-model"
        result = self.summarize()
        self.assertIsNone(result["conditions"]["baseline"]["cost"])

    def test_manifest_shape_validation_rejects_ambiguous_identifiers(self):
        self.pair()
        invalid = [None, {}, {**self.manifest, "conditions": ["baseline", "baseline"]},
                   {**self.manifest, "runs": None}]
        for field, value in (("directory", ""), ("directory", "bad\0path"), ("condition", "other"),
                             ("replicate", True), ("attempt", 0), ("id", "")):
            malformed = copy.deepcopy(self.manifest)
            malformed["runs"][0][field] = value
            invalid.append(malformed)
        for manifest in invalid:
            with self.subTest(manifest=manifest), self.assertRaises(ValueError):
                summarize_comparison(manifest, self.area)

    def test_empty_manifest_cannot_be_a_complete_comparison(self):
        result = self.summarize()
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["conditions"]["baseline"]["usage_status"], "unavailable")
        self.assertIsNone(result["conditions"]["baseline"]["cost"])

    def test_artifact_paths_cannot_escape_input_or_the_run_directory(self):
        (_, directory), _ = self.pair()
        for artifact in ("../outside", "/tmp/outside", "input/../../outside", "input\\outside"):
            with self.subTest(artifact=artifact):
                self.change_metadata(directory, editable_artifact=artifact)
                result = self.summarize()
                self.assertEqual(result["conditions"]["baseline"]["successful_tasks"], 0)
                self.assertIn("quality binding unavailable", " ".join(result["reasons"]))

    def test_output_symlink_cannot_bind_a_grade_to_external_content(self):
        (entry, directory), _ = self.pair()
        external = self.area / "external.md"
        external.write_text("External content")
        (directory / "output.md").unlink()
        (directory / "output.md").symlink_to(external)
        entry["quality"]["output_sha256"] = digest("External content")
        result = self.summarize()
        self.assertEqual(result["conditions"]["baseline"]["successful_tasks"], 0)
        self.assertIn("escapes run directory", " ".join(result["reasons"]))

    def test_cli_anchors_runs_to_manifest_and_preserves_history_and_existing_output(self):
        self.pair()
        manifest_path = self.area / "comparison.json"
        manifest_path.write_text(json.dumps(self.manifest))
        before = {str(path): path.read_bytes() for path in self.area.rglob("*") if path.is_file()}
        output = self.area / "new-summary.json"
        command = [sys.executable, str(ROOT / "evals/compare.py"), str(manifest_path), "--output", str(output)]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        result = json.loads(output.read_text())
        self.assertEqual(result["status"], "complete", result["reasons"])
        output_bytes = output.read_bytes()
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(second.returncode, 2)
        self.assertEqual(output.read_bytes(), output_bytes)
        for name, original in before.items():
            self.assertEqual(Path(name).read_bytes(), original)

    def test_cli_rejects_even_new_outputs_inside_historical_runs(self):
        (_, directory), _ = self.pair()
        manifest_path = self.area / "comparison.json"
        manifest_path.write_text(json.dumps(self.manifest))
        output = directory / "new-summary.json"
        result = subprocess.run([sys.executable, str(ROOT / "evals/compare.py"), str(manifest_path), "--output", str(output)],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("outside every run directory", result.stderr)
        self.assertFalse(output.exists())

    def test_nonfinite_metadata_is_unavailable_without_losing_the_valid_companion(self):
        (_, directory), _ = self.pair()
        metadata_path = directory / "metadata.json"
        original = metadata_path.read_text()
        manifest_path = self.area / "comparison.json"
        manifest_path.write_text(json.dumps(self.manifest))
        for token in ("NaN", "Infinity", "-Infinity", "1e9999", "-1e9999"):
            with self.subTest(token=token):
                metadata_path.write_text(original.replace('"timeout_seconds": 60', f'"timeout_seconds": {token}'))
                raw = metadata_path.read_bytes()
                output = self.area / f"nonfinite-{token}.json"
                command = [sys.executable, str(ROOT / "evals/compare.py"), str(manifest_path), "--output", str(output)]
                completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(completed.returncode, 0, completed.stderr)
                result = json.loads(output.read_text())
                self.assertEqual(result["status"], "incomplete")
                self.assertIn("metadata unavailable", " ".join(result["reasons"]))
                self.assertEqual(result["conditions"]["baseline"]["successful_tasks"], 0)
                self.assertEqual(result["conditions"]["baseline"]["quality_unavailable_runs"], 1)
                self.assertEqual(result["conditions"]["bandit"]["successful_tasks"], 1)
                self.assertEqual(result["conditions"]["bandit"]["usage"]["total_tokens"], 120)
                json.dumps(result, allow_nan=False)
                self.assertEqual(metadata_path.read_bytes(), raw)

    def test_nonfinite_manifest_or_pricing_does_not_reserve_the_output_path(self):
        self.pair()
        manifest_path = self.area / "comparison.json"
        pricing_path = self.area / "pricing.json"
        for source in ("manifest", "pricing"):
            for token in ("NaN", "Infinity", "-Infinity", "1e9999", "-1e9999"):
                with self.subTest(source=source, token=token):
                    manifest_path.write_text(json.dumps(self.manifest))
                    pricing_path.write_text(json.dumps(self.pricing))
                    target = manifest_path if source == "manifest" else pricing_path
                    content = target.read_text()
                    target.write_text(content[:-1] + f', "invalid_extra": {token}' + "}")
                    output = self.area / f"{source}-{token}.json"
                    command = [sys.executable, str(ROOT / "evals/compare.py"), str(manifest_path),
                               "--pricing", str(pricing_path), "--output", str(output)]
                    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
                    self.assertEqual(completed.returncode, 2, completed.stderr)
                    self.assertFalse(output.exists())

    def test_serialization_failure_does_not_reserve_the_output_path(self):
        self.pair(metadata_changes={"elapsed_seconds": 1e308})
        self.pair(replicate=2, metadata_changes={"elapsed_seconds": 1e308})
        manifest_path = self.area / "comparison.json"
        manifest_path.write_text(json.dumps(self.manifest))
        output = self.area / "unserializable-summary.json"
        command = [sys.executable, str(ROOT / "evals/compare.py"), str(manifest_path), "--output", str(output)]
        completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 2)
        self.assertIn("JSON compliant", completed.stderr)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
