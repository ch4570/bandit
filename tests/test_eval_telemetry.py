"""Offline synthetic Codex CLI streams; no account or model calls."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bandit_eval_telemetry", ROOT / "evals/telemetry.py")
telemetry = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(telemetry)


def usage(**overrides):
    return {"input_tokens": 100, "cached_input_tokens": 40, "output_tokens": 20, **overrides}


def completed(**overrides):
    return {"type": "turn.completed", "usage": usage(**overrides)}


def thread_started(**overrides):
    return {"type": "thread.started", "thread_id": "synthetic-thread", **overrides}


class SyntheticStreamCase(unittest.TestCase):
    def summarize(self, *events):
        with tempfile.TemporaryDirectory(prefix="bandit telemetry ") as directory:
            path = Path(directory) / "events.jsonl"
            raw = "\n".join(event if isinstance(event, str) else json.dumps(event) for event in events) + "\n"
            path.write_text(raw, encoding="utf-8")
            result = telemetry.summarize_events(path)
            self.assertEqual(path.read_text(encoding="utf-8"), raw, "The parser must preserve raw logs")
            return result


class TelemetryTests(SyntheticStreamCase):
    def test_documented_cli_usage_is_inclusive_and_route_is_not_assumed(self):
        result = self.summarize(thread_started(),
                                {"type": "turn.started"}, completed(reasoning_output_tokens=5))
        self.assertEqual(result["schema"], "bandit.telemetry/v1")
        self.assertEqual(result["usage_scope"], "top-level-cli-events")
        self.assertEqual(result["usage_semantics"], "cumulative-session-snapshot")
        self.assertEqual(result["usage_status"], "available")
        self.assertEqual(result["usage"], {**usage(), "total_tokens": 120,
                                           "reasoning_output_tokens": 5, "cache_write_input_tokens": None})
        self.assertEqual(result["turns_completed"], 1)
        self.assertIsNone(result["observed_model"])
        self.assertIsNone(result["observed_reasoning_effort"])
        self.assertEqual(result["errors"], [])

    def test_identical_snapshots_from_distinct_turns_are_not_doubled(self):
        result = self.summarize(thread_started(), {"type": "turn.started"}, completed(reasoning_output_tokens=5),
                                {"type": "turn.started"}, completed(reasoning_output_tokens=5))
        self.assertEqual(result["usage_status"], "available")
        self.assertEqual(result["turns_completed"], 2)
        self.assertEqual(result["usage"]["input_tokens"], 100)
        self.assertEqual(result["usage"]["cached_input_tokens"], 40)
        self.assertEqual(result["usage"]["output_tokens"], 20)
        self.assertEqual(result["usage"]["total_tokens"], 120)
        self.assertEqual(result["usage"]["reasoning_output_tokens"], 5)

    def test_last_cumulative_snapshot_replaces_earlier_usage(self):
        result = self.summarize(thread_started(), {"type": "turn.started"}, completed(reasoning_output_tokens=5),
                                {"type": "turn.started"}, completed(input_tokens=160, cached_input_tokens=60,
                                  output_tokens=35, reasoning_output_tokens=10))
        self.assertEqual(result["usage_status"], "available")
        self.assertEqual(result["turns_completed"], 2)
        self.assertEqual(result["usage"], {"input_tokens": 160, "cached_input_tokens": 60,
                         "output_tokens": 35, "reasoning_output_tokens": 10,
                         "cache_write_input_tokens": None, "total_tokens": 195})

    def test_decreasing_cumulative_counters_leave_last_valid_snapshot_partial(self):
        initial = {"input_tokens": 100, "cached_input_tokens": 40, "output_tokens": 20,
                   "reasoning_output_tokens": 5, "cache_write_input_tokens": 2}
        for field in initial:
            with self.subTest(field=field):
                decreasing = {**initial, field: initial[field] - 1}
                result = self.summarize(thread_started(), {"type": "turn.started"}, completed(**initial),
                                        {"type": "turn.started"}, completed(**decreasing))
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertIsNone(result["usage"])
                self.assertEqual(result["partial_usage"], {**initial, "total_tokens": 120})
                self.assertTrue(any(field in error and "decreased" in error for error in result["errors"]))

    def test_missing_intermediate_breakdown_does_not_hide_counter_decrease(self):
        result = self.summarize(thread_started(), {"type": "turn.started"}, completed(reasoning_output_tokens=5),
                                {"type": "turn.started"}, completed(input_tokens=160),
                                {"type": "turn.started"}, completed(input_tokens=180, reasoning_output_tokens=4))
        self.assertEqual(result["usage_status"], "unavailable")
        self.assertEqual(result["partial_usage"]["input_tokens"], 160)
        self.assertIsNone(result["partial_usage"]["reasoning_output_tokens"])

    def test_optional_breakdown_comes_only_from_the_final_snapshot(self):
        result = self.summarize(thread_started(), {"type": "turn.started"}, completed(reasoning_output_tokens=5,
                                                                        cache_write_input_tokens=0),
                                {"type": "turn.started"}, completed())
        self.assertEqual(result["usage_status"], "available")
        self.assertIsNone(result["usage"]["reasoning_output_tokens"])
        self.assertIsNone(result["usage"]["cache_write_input_tokens"])

        result = self.summarize(thread_started(), {"type": "turn.started"}, completed(),
                                {"type": "turn.started"}, completed(reasoning_output_tokens=5,
                                                                     cache_write_input_tokens=0))
        self.assertEqual(result["usage_status"], "available")
        self.assertEqual(result["usage"]["reasoning_output_tokens"], 5)
        self.assertEqual(result["usage"]["cache_write_input_tokens"], 0)

    def test_duplicate_or_conflicting_terminal_cannot_verify_complete_accounting(self):
        for duplicate in (completed(), completed(input_tokens=150), {"type": "turn.failed"}):
            with self.subTest(duplicate=duplicate):
                result = self.summarize(thread_started(), {"type": "turn.started"}, completed(), duplicate)
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertIsNone(result["usage"])
                self.assertEqual(result["partial_usage"]["total_tokens"], 120)
                self.assertEqual(result["turns_completed"], 1)
                self.assertTrue(result["errors"])

    def test_missing_or_malformed_usage_is_unavailable(self):
        bad_values = [None, [], {}, {"input_tokens": 100}, usage(input_tokens=-1),
                      usage(input_tokens=True), usage(output_tokens=1.5),
                      usage(cached_input_tokens=101), usage(cached_input_tokens="40"),
                      usage(reasoning_output_tokens=-1), usage(reasoning_output_tokens=21),
                      usage(cache_write_input_tokens=True)]
        for value in bad_values:
            with self.subTest(value=value):
                result = self.summarize(thread_started(), {"type": "turn.started"}, {"type": "turn.completed", "usage": value})
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertIsNone(result["usage"])
                self.assertTrue(result["errors"])

    def test_missing_optional_values_remain_unknown_and_zero_is_valid(self):
        result = self.summarize(thread_started(), {"type": "turn.started"}, completed(input_tokens=0,
                                 cached_input_tokens=0, output_tokens=0, reasoning_output_tokens=None))
        self.assertEqual(result["usage_status"], "available")
        self.assertEqual(result["usage"]["total_tokens"], 0)
        self.assertIsNone(result["usage"]["reasoning_output_tokens"])

    def test_incomplete_or_failed_final_turn_preserves_only_last_valid_snapshot(self):
        endings = [({"type": "turn.started"},),
                   ({"type": "turn.started"}, {"type": "turn.failed", "error": {"message": "synthetic failure"}}),
                   ({"type": "error", "message": "synthetic failure"},),
                   ({"type": "turn.started"}, {"type": "turn.completed"}),
                   ("{broken",)]
        for ending in endings:
            with self.subTest(ending=ending):
                result = self.summarize(thread_started(), {"type": "turn.started"}, completed(),
                                        {"type": "turn.started"}, completed(input_tokens=160), *ending)
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertIsNone(result["usage"])
                self.assertEqual(result["partial_usage"]["input_tokens"], 160)
                self.assertEqual(result["partial_usage"]["total_tokens"], 180)

    def test_empty_truncated_and_invalid_streams_do_not_become_zero_usage(self):
        for events in ((), ("[]",), ("null",), ("{broken",), ("{\"type\":NaN}",),
                       ({"type": "thread.started"},), ({"type": "turn.started"},),
                       (completed(),), ({"type": "turn.failed"},)):
            with self.subTest(events=events):
                result = self.summarize(*events)
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertIsNone(result["usage"])
                self.assertTrue(result["errors"])

    def test_overlapping_starts_leave_usage_unavailable(self):
        result = self.summarize(thread_started(), {"type": "turn.started"}, {"type": "turn.started"}, completed())
        self.assertEqual(result["usage_status"], "unavailable")

    def test_missing_thread_header_preserves_only_partial_usage(self):
        result = self.summarize({"type": "turn.started"}, completed())
        self.assertEqual(result["usage_status"], "unavailable")
        self.assertIsNone(result["usage"])
        self.assertEqual(result["partial_usage"]["total_tokens"], 120)
        self.assertTrue(any("thread.started" in error for error in result["errors"]))

    def test_malformed_thread_header_preserves_only_partial_usage(self):
        headers = [{"type": "thread.started"}, *[thread_started(thread_id=value)
                   for value in (None, "", "  ", True, 12, [], {})]]
        for header in headers:
            with self.subTest(header=header):
                result = self.summarize(header, {"type": "turn.started"}, completed())
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertIsNone(result["usage"])
                self.assertEqual(result["partial_usage"]["total_tokens"], 120)
                self.assertTrue(any("thread_id" in error for error in result["errors"]))

    def test_repeated_thread_header_is_unavailable_even_for_the_same_thread(self):
        for repeated in (thread_started(), thread_started(thread_id="another-synthetic-thread")):
            for events in ((thread_started(), repeated, {"type": "turn.started"}, completed()),
                           (thread_started(), {"type": "turn.started"}, completed(), repeated)):
                with self.subTest(events=events):
                    result = self.summarize(*events)
                    self.assertEqual(result["usage_status"], "unavailable")
                    self.assertIsNone(result["usage"])
                    self.assertEqual(result["partial_usage"]["total_tokens"], 120)
                    self.assertTrue(any("repeated thread.started" in error for error in result["errors"]))

    def test_late_thread_header_does_not_repair_truncated_history(self):
        for events in (({"type": "turn.started"}, thread_started(), completed()),
                       ({"type": "turn.started"}, completed(), thread_started())):
            with self.subTest(events=events):
                result = self.summarize(*events)
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertIsNone(result["usage"])
                self.assertEqual(result["partial_usage"]["total_tokens"], 120)

    def test_missing_file_and_invalid_encoding_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.jsonl"
            self.assertEqual(telemetry.summarize_events(path)["usage_status"], "unavailable")
            path.write_bytes(b"\xff\n")
            self.assertEqual(telemetry.summarize_events(path)["usage_status"], "unavailable")

    def test_cumulative_app_server_events_are_not_accepted_as_cli_snapshots(self):
        event = {"method": "thread/tokenUsage/updated", "params": {"tokenUsage": {"total": usage()}}}
        for stream in ((event,), (event, event), (thread_started(), {"type": "turn.started"}, completed(), event)):
            with self.subTest(stream=stream):
                result = self.summarize(*stream)
                self.assertEqual(result["usage_status"], "unavailable")
                self.assertTrue(any("cumulative" in error.lower() for error in result["errors"]))

    def test_unknown_events_and_tool_prose_never_supply_usage_or_route(self):
        result = self.summarize(thread_started(), {"type": "future.event", "model": "false-route", "usage": usage()},
                                {"type": "turn.started"},
                                {"type": "item.completed", "item": {"type": "command_execution",
                                 "aggregated_output": "model: false-route; reasoning_effort: high", "model": "false-route"}},
                                completed())
        self.assertEqual(result["usage_status"], "available")
        self.assertEqual(result["usage"]["total_tokens"], 120)
        self.assertIsNone(result["observed_model"])
        self.assertIsNone(result["observed_reasoning_effort"])

    def test_only_runtime_lifecycle_fields_are_route_observations(self):
        result = self.summarize(thread_started(model="synthetic-model"),
                                {"type": "turn.started", "reasoning_effort": "high"}, completed())
        self.assertEqual(result["observed_model"], "synthetic-model")
        self.assertEqual(result["observed_reasoning_effort"], "high")

    def test_changing_model_is_not_collapsed_to_one_observation(self):
        result = self.summarize(thread_started(), {"type": "turn.started", "model": "synthetic-one"}, completed(),
                                {"type": "turn.started", "model": "synthetic-two"}, completed())
        self.assertEqual(result["usage_status"], "available")
        self.assertIsNone(result["observed_model"])
        self.assertEqual(result["observed_models"], ["synthetic-one", "synthetic-two"])


class CostTests(SyntheticStreamCase):
    def setUp(self):
        self.observed = self.summarize(thread_started(), {"type": "turn.started", "model": "synthetic-model"}, completed())
        self.pricing = {"model": "synthetic-model", "currency": "USD", "effective_date": "2026-09-09",
                        "source_url": "https://example.invalid/synthetic-pricing",
                        "input_per_million": 2, "cached_input_per_million": 0.5, "output_per_million": 8}

    def estimate(self, *, observed=None, pricing=None, model="synthetic-model"):
        return telemetry.estimate_cost(self.observed if observed is None else observed,
                                       self.pricing if pricing is None else pricing, model)

    def test_inclusive_input_cache_and_output_formula(self):
        result = self.estimate()
        self.assertEqual(result["status"], "available")
        self.assertAlmostEqual(result["amount"], 0.0003)
        self.assertEqual(result["currency"], "USD")
        self.assertEqual(result["reasons"], [])

    def test_reasoning_is_not_charged_twice(self):
        observed = self.summarize(thread_started(), {"type": "turn.started"}, completed(reasoning_output_tokens=10))
        self.assertAlmostEqual(self.estimate(observed=observed)["amount"], 0.0003)
        self.assertIsNone(observed["observed_model"], "Pricing a caller model must not invent observed identity")

    def test_bad_or_missing_pricing_provenance_and_rates_are_unavailable(self):
        changes = [{"model": "different-model"}, {"currency": ""}, {"effective_date": "20260909"},
                   {"effective_date": "2026-02-30"}, {"source_url": "no source"},
                   {"source_url": "file:///private/pricing"}, {"input_per_million": -1},
                   {"cached_input_per_million": True}, {"output_per_million": float("inf")},
                   {"output_per_million": float("nan")}, {"output_per_million": "8"}]
        for change in changes:
            with self.subTest(change=change):
                result = self.estimate(pricing={**self.pricing, **change})
                self.assertEqual(result["status"], "unavailable")
                self.assertIsNone(result["amount"])
                self.assertTrue(result["reasons"])
        for field in self.pricing:
            with self.subTest(missing=field):
                self.assertEqual(self.estimate(pricing={key: value for key, value in self.pricing.items()
                                                       if key != field})["status"], "unavailable")

    def test_unknown_model_or_observed_mismatch_is_unavailable(self):
        for model in (None, "", "different-model"):
            with self.subTest(model=model):
                self.assertEqual(self.estimate(model=model)["status"], "unavailable")
        observed = {**self.observed, "observed_model": "different-model"}
        self.assertEqual(self.estimate(observed=observed)["status"], "unavailable")
        observed = {**self.observed, "observed_model": None, "observed_models": ["one", "two"]}
        self.assertEqual(self.estimate(observed=observed)["status"], "unavailable")

    def test_unavailable_usage_or_unsupported_scope_cannot_be_priced(self):
        for change in ({"usage_status": "unavailable"}, {"usage": None},
                       {"schema": "unknown"}, {"usage_scope": "cumulative"},
                       {"usage_semantics": None}, {"usage_semantics": "per-turn-deltas"},
                       {"usage": usage(cached_input_tokens=101)}):
            with self.subTest(change=change):
                self.assertEqual(self.estimate(observed={**self.observed, **change})["status"], "unavailable")

    def test_nonzero_cache_writes_have_unsupported_billing_semantics(self):
        observed = self.summarize(thread_started(), {"type": "turn.started"}, completed(cache_write_input_tokens=1))
        self.assertEqual(self.estimate(observed=observed)["status"], "unavailable")
        observed = self.summarize(thread_started(), {"type": "turn.started"}, completed(cache_write_input_tokens=0))
        self.assertEqual(self.estimate(observed=observed)["status"], "available")

    def test_missing_cache_write_breakdown_cannot_hide_known_cache_writes(self):
        observed = self.summarize(thread_started(), {"type": "turn.started"}, completed(cache_write_input_tokens=1),
                                  {"type": "turn.started"}, completed())
        self.assertIsNone(observed["usage"]["cache_write_input_tokens"])
        self.assertTrue(observed["nonzero_cache_write_tokens_observed"])
        self.assertEqual(self.estimate(observed=observed)["status"], "unavailable")

    def test_malformed_telemetry_inputs_return_reasons_without_crashing(self):
        for observed in ([], {**self.observed, "observed_models": None},
                         {**self.observed, "observed_models": "synthetic-model"}):
            with self.subTest(observed=observed):
                self.assertEqual(self.estimate(observed=observed)["status"], "unavailable")
        self.assertEqual(self.estimate(pricing=[])["status"], "unavailable")

    def test_overflow_does_not_emit_nonfinite_cost(self):
        observed = {**self.observed, "usage": usage(input_tokens=10 ** 310)}
        self.assertEqual(self.estimate(observed=observed)["status"], "unavailable")

    def test_zero_rates_and_zero_usage_are_valid(self):
        self.assertEqual(self.estimate(pricing={**self.pricing, "input_per_million": 0,
                          "cached_input_per_million": 0, "output_per_million": 0})["amount"], 0)
        observed = self.summarize(thread_started(), {"type": "turn.started"}, completed(input_tokens=0,
                                  cached_input_tokens=0, output_tokens=0))
        self.assertEqual(self.estimate(observed=observed)["amount"], 0)


if __name__ == "__main__":
    unittest.main()
