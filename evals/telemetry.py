"""Read Codex exec JSONL accounting without altering the raw event log.

Only top-level CLI turn.completed cumulative session snapshots are supported.
Input includes cached input; output includes reasoning. Counts represent the
whole session, not per-turn deltas or the incremental cost of a resumed run.
The pinned rust-v0.153.4 emitter copies the last total token usage:
https://github.com/openai/codex/blob/3d2ee51ca2d5db578f328aa75e20aa22c0197c9a/codex-rs/exec/src/event_processor_with_jsonl_output.rs
"""
from __future__ import annotations

from datetime import date
import json
import math
from pathlib import Path
from urllib.parse import urlsplit


REQUIRED_TOKENS = ("input_tokens", "cached_input_tokens", "output_tokens")
OPTIONAL_TOKENS = ("cache_write_input_tokens", "reasoning_output_tokens")
LIFECYCLE_EVENTS = {"thread.started", "turn.started", "turn.completed", "turn.failed"}


def _usage(value: object) -> dict:
    if not isinstance(value, dict):
        raise ValueError("Missing or malformed turn usage")
    result = {}
    for field in (*REQUIRED_TOKENS, *OPTIONAL_TOKENS):
        count = value.get(field)
        if field in OPTIONAL_TOKENS and count is None:
            result[field] = None
        elif type(count) is not int or count < 0:
            raise ValueError(f"{field} must be a nonnegative integer")
        else:
            result[field] = count
    if result["cached_input_tokens"] > result["input_tokens"]:
        raise ValueError("cached_input_tokens exceeds inclusive input_tokens")
    reasoning = result["reasoning_output_tokens"]
    if reasoning is not None and reasoning > result["output_tokens"]:
        raise ValueError("reasoning_output_tokens exceeds inclusive output_tokens")
    result["total_tokens"] = result["input_tokens"] + result["output_tokens"]
    return result


def _invalid_constant(value: str) -> None:
    raise ValueError(f"Invalid JSON constant: {value}")


def summarize_events(path: Path) -> dict:
    """Return the final cumulative snapshot from a complete, valid CLI stream.

    A single valid thread.started header must precede the turns. Missing or
    repeated headers and duplicate terminals make usage unavailable.
    partial_usage is the last validated snapshot when the stream is incomplete
    or invalid; snapshots are never added. Optional fields omitted from the
    final snapshot remain unknown. Known counters must not decrease, even
    across a snapshot that omitted an optional counter. Model/effort are
    observations only when actual lifecycle events supply top-level fields.
    """
    errors = []
    last_usage = None
    known_counts = {}
    cache_writes_observed = False
    models, efforts, unknown_types = set(), set(), set()
    active_turn = False
    started = completed = failed = duplicates = 0
    terminal_seen = False
    thread_headers = 0
    thread_ready = False
    try:
        with path.open(encoding="utf-8") as stream:
            for number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                try:
                    event = json.loads(line, parse_constant=_invalid_constant)
                    if not isinstance(event, dict):
                        raise ValueError("Event must be a JSON object")
                except (ValueError, RecursionError) as exc:
                    errors.append(f"Line {number}: invalid JSON event: {exc}")
                    continue
                kind = event.get("type")
                if event.get("method") == "thread/tokenUsage/updated" or kind == "thread/tokenUsage/updated":
                    errors.append(f"Line {number}: unsupported app-server cumulative token usage event")
                    continue
                if isinstance(kind, str) and kind in LIFECYCLE_EVENTS:
                    for field, observed in (("model", models), ("reasoning_effort", efforts)):
                        value = event.get(field)
                        if isinstance(value, str) and value.strip():
                            observed.add(value)
                if kind == "thread.started":
                    thread_headers += 1
                    if thread_headers > 1:
                        errors.append(f"Line {number}: repeated thread.started header")
                    thread_id = event.get("thread_id")
                    if not isinstance(thread_id, str) or not thread_id.strip():
                        errors.append(f"Line {number}: thread.started requires a nonempty thread_id")
                    else:
                        thread_ready = True
                elif kind == "turn.started":
                    if not thread_ready:
                        errors.append(f"Line {number}: turn started before a valid thread.started header")
                    if active_turn:
                        errors.append(f"Line {number}: new turn started before previous turn ended")
                    active_turn = True
                    terminal_seen = False
                    started += 1
                elif kind in ("turn.completed", "turn.failed"):
                    if not active_turn:
                        if terminal_seen:
                            duplicates += 1
                        errors.append(f"Line {number}: terminal event without a new turn.started")
                        continue
                    active_turn = False
                    terminal_seen = True
                    if kind == "turn.failed":
                        failed += 1
                        errors.append(f"Line {number}: turn failed; complete usage is unknown")
                    else:
                        completed += 1
                        try:
                            snapshot = _usage(event.get("usage"))
                            reported = {field: value for field, value in snapshot.items() if value is not None}
                            decreased = [field for field, value in reported.items()
                                         if field in known_counts and value < known_counts[field]]
                            if decreased:
                                raise ValueError("Cumulative usage counter decreased: " + ", ".join(decreased))
                            last_usage = snapshot
                            known_counts.update(reported)
                            cache_writes_observed |= bool(snapshot["cache_write_input_tokens"])
                        except ValueError as exc:
                            errors.append(f"Line {number}: {exc}")
                elif kind == "error":
                    errors.append(f"Line {number}: CLI error; complete usage is unknown")
                elif kind not in ("item.started", "item.updated", "item.completed"):
                    unknown_types.add(kind if isinstance(kind, str) else "<missing-or-invalid-type>")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read event log: {exc}")
    if thread_headers == 0:
        errors.append("Missing thread.started header; prior run history is unknown")
    if active_turn:
        errors.append("Event stream ended before the active turn completed")
    if last_usage is None:
        errors.append("No complete valid CLI turn usage was observed")
    available = not errors and last_usage is not None
    return {"schema": "bandit.telemetry/v1", "usage_scope": "top-level-cli-events",
            "usage_semantics": "cumulative-session-snapshot",
            "usage_status": "available" if available else "unavailable",
            "usage": last_usage if available else None, "partial_usage": last_usage if not available else None,
            "errors": errors, "turns_started": started, "turns_completed": completed,
            "turns_failed": failed, "duplicate_terminal_events": duplicates,
            "nonzero_cache_write_tokens_observed": cache_writes_observed,
            "observed_model": next(iter(models)) if len(models) == 1 else None,
            "observed_reasoning_effort": next(iter(efforts)) if len(efforts) == 1 else None,
            "observed_models": sorted(models), "observed_reasoning_efforts": sorted(efforts),
            "unknown_event_types": sorted(unknown_types)}


def estimate_cost(telemetry: dict, pricing: dict | None, model: str | None) -> dict:
    """Estimate supplied model pricing, without asserting backend model identity.

    Rates are caller-supplied currency units per million tokens. An explicitly
    supplied model may price a stream whose route was not observed; callers
    requiring an observed route must pass telemetry['observed_model'].
    """
    reasons = []
    if not isinstance(telemetry, dict):
        telemetry = {}
    if (telemetry.get("schema") != "bandit.telemetry/v1"
            or telemetry.get("usage_scope") != "top-level-cli-events"
            or telemetry.get("usage_semantics") != "cumulative-session-snapshot"):
        reasons.append("Unsupported telemetry accounting contract")
    if telemetry.get("usage_status") != "available":
        reasons.append("Complete token usage is unavailable")
    try:
        counts = _usage(telemetry.get("usage"))
    except ValueError as exc:
        counts = None
        reasons.append(str(exc))
    if (counts and counts["cache_write_input_tokens"]
            or telemetry.get("nonzero_cache_write_tokens_observed")):
        reasons.append("Nonzero cache-write tokens have unsupported billing semantics")
    if not isinstance(model, str) or not model.strip():
        reasons.append("An explicit pricing model is required")
    observed_model = telemetry.get("observed_model")
    if observed_model is not None and observed_model != model:
        reasons.append("Pricing model does not match the observed runtime model")
    observed_models = telemetry.get("observed_models", [])
    if not isinstance(observed_models, list):
        reasons.append("Malformed runtime model observations")
    elif len(observed_models) > 1:
        reasons.append("Multiple runtime models cannot use one pricing model")
    if not isinstance(pricing, dict):
        pricing = {}
    if pricing.get("model") != model or not pricing.get("model"):
        reasons.append("Pricing table model must explicitly match the selected model")
    currency = pricing.get("currency")
    if not isinstance(currency, str) or not currency.strip():
        reasons.append("Pricing currency is required")
    effective_date = pricing.get("effective_date")
    try:
        if not isinstance(effective_date, str) or date.fromisoformat(effective_date).isoformat() != effective_date:
            raise ValueError("Expected ISO date")
    except ValueError:
        reasons.append("Pricing effective_date must be a valid YYYY-MM-DD date")
    try:
        source_url = urlsplit(pricing.get("source_url") or "")
        valid_source = source_url.scheme in ("http", "https") and bool(source_url.hostname)
    except (ValueError, TypeError, AttributeError):
        valid_source = False
    if not valid_source:
        reasons.append("Pricing source_url must be an explicit HTTP(S) URL")
    for field in ("input_per_million", "cached_input_per_million", "output_per_million"):
        rate = pricing.get(field)
        try:
            valid = type(rate) in (int, float) and math.isfinite(rate) and rate >= 0
        except OverflowError:
            valid = False
        if not valid:
            reasons.append(f"Pricing {field} must be a finite nonnegative number")
    amount = None
    if not reasons:
        try:
            amount = ((counts["input_tokens"] - counts["cached_input_tokens"]) * pricing["input_per_million"]
                      + counts["cached_input_tokens"] * pricing["cached_input_per_million"]
                      + counts["output_tokens"] * pricing["output_per_million"]) / 1_000_000
            if not math.isfinite(amount):
                raise OverflowError("Nonfinite estimate")
        except OverflowError:
            amount = None
            reasons.append("Cost estimate exceeds finite numeric range")
    return {"status": "unavailable" if reasons else "available", "amount": amount,
            "currency": currency if isinstance(currency, str) and currency.strip() else None,
            "reasons": reasons}
