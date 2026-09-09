#!/usr/bin/env python3
"""Compare explicitly listed evaluation runs without changing their evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re

if __package__:
    from .telemetry import estimate_cost, summarize_events
else:
    from telemetry import estimate_cost, summarize_events


SCHEMA = "bandit.comparison/v1"
USAGE_FIELDS = ("input_tokens", "cached_input_tokens", "output_tokens", "total_tokens",
                "cache_write_input_tokens", "reasoning_output_tokens")
SETTINGS_FIELDS = ("model", "reasoning_effort", "timeout_seconds", "max_output_words",
                   "web_search", "multi_agent")


def _text(value) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\0" not in value


def _number(value) -> bool:
    try:
        return type(value) in (int, float) and math.isfinite(value) and value >= 0
    except OverflowError:
        return False


def _digest(value) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _hashes(value, *, empty=False) -> bool:
    return (isinstance(value, dict) and (bool(value) or empty)
            and all(_text(key) and _digest(digest) for key, digest in value.items()))


def _evidence_path(directory: Path, relative: str) -> Path:
    path = (directory / relative).resolve()
    if not path.is_relative_to(directory) or path == directory:
        raise ValueError(f"Evidence path escapes run directory: {relative}")
    return path


def _sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def _manifest_runs(manifest: dict, base_dir: Path) -> tuple[list[str], list[tuple[dict, Path]]]:
    if not isinstance(manifest, dict) or manifest.get("schema") != SCHEMA:
        raise ValueError(f"Manifest schema must be {SCHEMA}")
    conditions = manifest.get("conditions")
    if (not isinstance(conditions, list) or len(conditions) < 2
            or not all(_text(value) for value in conditions) or len(set(conditions)) != len(conditions)):
        raise ValueError("Manifest conditions must name at least two distinct conditions")
    if not isinstance(manifest.get("runs"), list):
        raise ValueError("Manifest runs must be a list")
    runs = []
    for entry in manifest["runs"]:
        if not isinstance(entry, dict) or not all(_text(entry.get(key)) for key in ("id", "directory", "case")):
            raise ValueError("Each run needs nonempty id, directory, and case strings")
        if entry.get("condition") not in conditions:
            raise ValueError(f"Run {entry['id']}: undeclared condition")
        if any(type(entry.get(key)) is not int or entry[key] < 1 for key in ("replicate", "attempt")):
            raise ValueError(f"Run {entry['id']}: replicate and attempt must be positive integers")
        directory = Path(entry["directory"])
        directory = (directory if directory.is_absolute() else base_dir / directory).resolve()
        runs.append((entry, directory))
    return conditions, runs


def _quality(entry: dict, metadata: dict, directory: Path, reasons: list[str]) -> str:
    grade = entry.get("quality")
    if not isinstance(grade, dict) or grade.get("status") not in ("passed", "failed"):
        reasons.append("quality grade unavailable")
        return "unavailable"
    if not _text(grade.get("evidence")):
        reasons.append("quality evidence unavailable")
        return "unavailable"
    try:
        if not _digest(grade.get("output_sha256")) or _sha256(_evidence_path(directory, "output.md")) != grade["output_sha256"]:
            reasons.append("quality output_sha256 does not match output.md")
            return "unavailable"
        artifact = metadata.get("editable_artifact")
        if artifact is not None:
            if (not _text(artifact) or "\\" in artifact or Path(artifact).is_absolute()
                    or ".." in Path(artifact).parts or not artifact.startswith("input/")):
                raise ValueError("editable_artifact must be a relative path under input/")
            digest = _sha256(_evidence_path(directory, "workspace/" + artifact))
            after = metadata.get("input_after_sha256")
            if (not _digest(grade.get("artifact_sha256")) or digest != grade["artifact_sha256"]
                    or not isinstance(after, dict) or after.get(artifact[len("input/"):]) != digest):
                reasons.append("quality artifact_sha256 does not match the edited artifact and recorded hash")
                return "unavailable"
    except (OSError, ValueError) as exc:
        reasons.append(f"quality binding unavailable: {exc}")
        return "unavailable"
    return grade["status"]


def _read_run(entry: dict, directory: Path, pricing: dict | None) -> tuple[dict, dict]:
    reasons = []
    metadata = {}
    try:
        metadata = json.loads(_evidence_path(directory, "metadata.json").read_text(encoding="utf-8"))
        if not isinstance(metadata, dict):
            raise ValueError("metadata must be an object")
    except (OSError, ValueError) as exc:
        reasons.append(f"metadata unavailable: {exc}")
        metadata = {}
    for key in ("case", "condition", "replicate", "attempt"):
        actual = metadata.get(key, metadata.get("arm") if key == "condition" else 1 if key in ("replicate", "attempt") else None)
        if actual != entry[key]:
            reasons.append(f"manifest {key} does not match metadata")
    settings = metadata.get("execution_settings")
    if not isinstance(settings, dict):
        reasons.append("execution_settings unavailable")
        settings = {}
    elif (any(key not in settings for key in SETTINGS_FIELDS)
          or not all(_text(settings.get(key)) for key in ("model", "reasoning_effort"))
          or not _number(settings.get("timeout_seconds")) or settings.get("timeout_seconds", 0) <= 0
          or type(settings.get("max_output_words")) is not int or settings.get("max_output_words", 0) <= 0
          or settings.get("web_search") != "disabled" or settings.get("multi_agent") is not False):
        reasons.append("execution_settings incomplete or unsupported (web search and multi-agent must be disabled)")
    if not _text(metadata.get("codex_version")):
        reasons.append("codex_version unavailable")
    if not _digest(metadata.get("runner_sha256")):
        reasons.append("runner_sha256 unavailable or invalid")
    if not _hashes(metadata.get("input_sha256")):
        reasons.append("input_sha256 unavailable or invalid")
    if not _hashes(metadata.get("instruction_sha256"), empty=True):
        reasons.append("instruction_sha256 unavailable or invalid")
    for key in ("exit_code", "process_exit_code"):
        if type(metadata.get(key)) is not int:
            reasons.append(f"{key} unavailable")
    if metadata.get("integrity_status") not in ("passed", "failed"):
        reasons.append("integrity_status unavailable")
    elapsed = metadata.get("elapsed_seconds")
    if not _number(elapsed):
        reasons.append("elapsed_seconds unavailable")
        elapsed = None
    try:
        telemetry = summarize_events(_evidence_path(directory, "events.jsonl"))
    except (OSError, ValueError) as exc:
        telemetry = {"schema": "bandit.telemetry/v1", "usage_status": "unavailable", "usage": None,
                     "errors": [str(exc)], "turns_completed": 0, "observed_model": None,
                     "observed_reasoning_effort": None, "usage_scope": "top-level-cli-events"}
    if telemetry["usage_status"] != "available":
        reasons.append("complete usage unavailable: " + "; ".join(str(error) for error in telemetry.get("errors", [])))
    for observed, requested in (("observed_model", "model"), ("observed_reasoning_effort", "reasoning_effort")):
        if not _text(telemetry.get(observed)):
            reasons.append(f"{observed} unavailable in raw events")
        elif _text(settings.get(requested)) and telemetry[observed] != settings[requested]:
            reasons.append(f"{observed} does not match requested {requested}")
    if telemetry.get("usage_scope") != "top-level-cli-events":
        reasons.append("usage_scope unsupported")
    if pricing is None:
        cost = {"status": "unavailable", "amount": None, "currency": None, "reasons": ["No pricing supplied"]}
    elif not _text(telemetry.get("observed_model")):
        cost = {"status": "unavailable", "amount": None, "currency": None, "reasons": ["Observed model unavailable"]}
    else:
        cost = estimate_cost(telemetry, pricing, telemetry["observed_model"])
    quality = _quality(entry, metadata, directory, reasons)
    process_ok = all(type(metadata.get(key)) is int and metadata[key] == 0 for key in ("exit_code", "process_exit_code"))
    successful = process_ok and metadata.get("integrity_status") == "passed" and quality == "passed"
    failed = (any(type(metadata.get(key)) is int and metadata[key] != 0 for key in ("exit_code", "process_exit_code"))
              or metadata.get("integrity_status") == "failed" or quality == "failed")
    result = {key: entry[key] for key in ("id", "condition", "case", "replicate", "attempt")}
    result.update(directory=str(directory), quality_status=quality, quality=entry.get("quality"),
                  successful=successful, failed=failed, elapsed_seconds=elapsed,
                  process_exit_code=metadata.get("process_exit_code"), exit_code=metadata.get("exit_code"),
                  integrity_status=metadata.get("integrity_status"), execution_settings=settings,
                  codex_version=metadata.get("codex_version"), runner_sha256=metadata.get("runner_sha256"),
                  telemetry=telemetry, cost=cost, reasons=reasons)
    return result, metadata


def _condition_summary(runs: list[dict]) -> dict:
    available = [run for run in runs if run["telemetry"]["usage_status"] == "available"]
    observed_usage = {}
    for field in USAGE_FIELDS:
        values = [run["telemetry"]["usage"].get(field) for run in available]
        observed_usage[field] = sum(values) if values and all(type(value) is int for value in values) else None
    successes = {(run["case"], run["replicate"]) for run in runs if run["successful"]}
    tasks = {(run["case"], run["replicate"]) for run in runs}
    priced = [run for run in runs if run["cost"]["status"] == "available"]
    currencies = {run["cost"]["currency"] for run in priced}
    cost_available = bool(runs) and len(priced) == len(runs) and len(currencies) == 1
    cost = sum(run["cost"]["amount"] for run in priced) if cost_available else None
    observed_costs = {currency: sum(run["cost"]["amount"] for run in priced if run["cost"]["currency"] == currency)
                      for currency in sorted(currencies)}
    elapsed = [run["elapsed_seconds"] for run in runs if run["elapsed_seconds"] is not None]
    total_elapsed = sum(elapsed) if runs and len(elapsed) == len(runs) else None
    usage_available = bool(runs) and len(available) == len(runs)
    return {"run_count": len(runs), "task_count": len(tasks), "retry_count": len(runs) - len(tasks),
            "successful_tasks": len(successes), "successful_attempts": sum(run["successful"] for run in runs),
            "failed_attempts": sum(run["failed"] for run in runs),
            "unavailable_attempts": sum(not run["successful"] and not run["failed"] for run in runs),
            "quality_unavailable_runs": sum(run["quality_status"] == "unavailable" for run in runs),
            "usage_scope": "top-level-cli-events", "usage_status": "available" if usage_available else "unavailable",
            "usage": observed_usage if usage_available else None, "observed_usage": observed_usage,
            "usage_available_runs": len(available), "usage_unavailable_runs": len(runs) - len(available),
            "elapsed_seconds": total_elapsed, "observed_elapsed_seconds": sum(elapsed) if elapsed else None,
            "cost_status": "available" if cost_available else "unavailable", "cost": cost,
            "currency": next(iter(currencies)) if cost_available else None,
            "observed_costs": observed_costs, "cost_available_runs": len(priced),
            "cost_per_successful_task": cost / len(successes) if cost is not None and successes else None,
            "elapsed_seconds_per_successful_task": total_elapsed / len(successes) if total_elapsed is not None and successes else None}


def summarize_comparison(manifest: dict, base_dir: Path, pricing: dict | None = None) -> dict:
    """Return descriptive totals and explicit gaps for a manifest of matched tasks.

    A success needs a grade bound to the output, zero runner/process exit codes,
    and passed integrity. All unique run directories contribute to attempt totals.
    Missing evidence is not a zero or a pass. Prices are optional and never inferred.
    """
    conditions, entries = _manifest_runs(manifest, Path(base_dir).resolve())
    reasons, runs = [], []
    seen_ids, seen_directories, seen_cells = set(), set(), set()
    per_case, per_instruction, attempts = {}, {}, {}
    cells = {condition: set() for condition in conditions}
    for entry, directory in entries:
        run_id = entry["id"]
        cell = (entry["condition"], entry["case"], entry["replicate"], entry["attempt"])
        for value, seen, label in ((run_id, seen_ids, "id"), (cell, seen_cells, "condition/case/replicate/attempt")):
            if value in seen:
                reasons.append(f"{run_id}: duplicate {label}")
            seen.add(value)
        if directory in seen_directories:
            reasons.append(f"{run_id}: duplicate run directory (counted only once): {directory}")
            continue
        seen_directories.add(directory)
        run, metadata = _read_run(entry, directory, pricing)
        runs.append(run)
        reasons.extend(f"{run_id}: {reason}" for reason in run["reasons"])
        cells[entry["condition"]].add((entry["case"], entry["replicate"]))
        attempts.setdefault(cell[:3], set()).add(entry["attempt"])
        fields = {key: metadata.get(key) for key in ("input_sha256", "codex_version", "editable_artifact", "runner_sha256")}
        fields["execution_settings"] = run["execution_settings"]
        fields["observed_model"] = run["telemetry"].get("observed_model")
        fields["observed_reasoning_effort"] = run["telemetry"].get("observed_reasoning_effort")
        previous = per_case.setdefault(entry["case"], fields)
        for key, value in fields.items():
            if value != previous[key]:
                reasons.append(f"{run_id}: {key} differs within case {entry['case']}")
        key = (entry["condition"], entry["case"])
        instruction = metadata.get("instruction_sha256")
        if instruction != per_instruction.setdefault(key, instruction):
            reasons.append(f"{run_id}: instruction_sha256 differs within condition/case")
    for (condition, case, replicate), indices in attempts.items():
        previous = 0
        for current in sorted(indices):
            if current > previous + 1:
                missing = str(previous + 1) if current == previous + 2 else f"{previous + 1}..{current - 1}"
                reasons.append(f"{condition}: missing attempt {missing} for {case}/replicate-{replicate}")
            previous = current
    all_cells = set().union(*cells.values())
    if not all_cells:
        reasons.append("No task cells supplied")
    for condition in conditions:
        for case, replicate in sorted(all_cells - cells[condition]):
            reasons.append(f"{condition}: missing matched task cell {case}/replicate-{replicate}")
    reasons = list(dict.fromkeys(reasons))
    summaries = {condition: _condition_summary([run for run in runs if run["condition"] == condition])
                 for condition in conditions}
    return {"schema": "bandit.comparison-result/v1", "status": "incomplete" if reasons else "complete",
            "reasons": reasons, "manifest_run_count": len(entries), "run_count": len(runs),
            "usage_scope": "top-level-cli-events", "pricing": pricing,
            "conditions": summaries, "runs": runs}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="New JSON file outside every run directory")
    parser.add_argument("--pricing", type=Path, help="Explicit model rates, currency, effective date, and source URL")
    args = parser.parse_args()
    try:
        manifest_path = args.manifest.resolve()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        pricing = json.loads(args.pricing.read_text(encoding="utf-8")) if args.pricing else None
        _, entries = _manifest_runs(manifest, manifest_path.parent)
        output = args.output.resolve()
        if any(output.is_relative_to(directory) for _, directory in entries):
            raise ValueError("Output must be outside every run directory to preserve historical evidence")
        result = summarize_comparison(manifest, manifest_path.parent, pricing)
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(json.dumps(result, indent=2, allow_nan=False) + "\n")
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, f"bandit comparison: {exc}\n")
    print(json.dumps({"output": str(output), "status": result["status"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
