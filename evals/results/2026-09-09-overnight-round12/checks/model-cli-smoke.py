#!/usr/bin/env python3
"""Local fake-executable integration checks; never invokes a model or backend.

Author this harness before the runner change; execute only after the main task
signals readiness. All scenarios are sequential and use one tiny raw fixture.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


OUTPUT = Path(__file__).resolve().parent
ROOT = OUTPUT.parents[3]
PYTHON = Path("/Users/DEVELOPER/.local/bin/python3.11")
NODE = Path("/Users/DEVELOPER/.npm/_npx/52027bd8fc0022aa/node_modules/node/bin/node")
MODEL = "synthetic-model.integration"  # Test string, not an available model.
FAKE_VERSION = "fake-codex model-cli-smoke 0 (no backend)"
REQUEST = b"Synthetic fake-executable integration fixture. No product-planning task or backend call is requested.\n"
PREFIX = "model-cli-smoke"

FAKE_SOURCE = r'''
"""FAKE CODEX: deterministic local argv plumbing, no auth/network/model use."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys

def now():
    return datetime.now(timezone.utc).isoformat()

started = now()
args = sys.argv[1:]
label = os.environ["FAKE_SMOKE_LABEL"]
mode = "version" if args == ["--version"] else "exec" if args[:1] == ["exec"] else "unexpected"
identity = "fake-" + label + "-" + mode
capture = Path(os.environ["FAKE_SMOKE_CAPTURE_DIR"]) / identity
capture.mkdir()
stdin = sys.stdin.buffer.read()
exit_code = 0
stderr = b""
if mode == "version":
    stdout = b"fake-codex model-cli-smoke 0 (no backend)\n"
elif mode == "exec":
    exit_code = int(os.environ["FAKE_SMOKE_EXIT"])
    events = [{"type": "thread.started", "thread_id": "fake-thread-" + label},
              {"type": "turn.started"}]
    if exit_code:
        stderr = b"SYNTHETIC FAKE CHILD FAILURE; no backend was invoked.\n"
        events.append({"type": "turn.failed", "error": {"message": "Synthetic fake child exit"}})
    else:
        text = "SYNTHETIC FAKE OUTPUT; no model or backend was invoked.\n"
        Path(args[args.index("-o") + 1]).write_text(text, encoding="utf-8")
        events += [{"type": "item.completed", "item": {"id": "fake-output", "type": "agent_message", "text": text}},
                   {"type": "turn.completed", "usage": {"input_tokens": 0, "output_tokens": 0}}]
    stdout = ("\n".join(json.dumps(event) for event in events) + "\n").encode()
else:
    exit_code = 97
    stdout = b""
    stderr = b"Unexpected invocation of the synthetic fake executable.\n"
for name, data in (("stdin.txt", stdin), ("stdout.txt", stdout), ("stderr.txt", stderr)):
    (capture / name).write_bytes(data)
(capture / "invocation.json").write_text(json.dumps({
    "kind": "synthetic fake executable, not a native Codex invocation",
    "id": identity, "mode": mode, "label": label, "argv": args,
    "cwd": os.getcwd(), "started_at_utc": started, "finished_at_utc": now(),
    "exit_code": exit_code,
}, indent=2) + "\n", encoding="utf-8")
sys.stdout.buffer.write(stdout)
sys.stderr.buffer.write(stderr)
raise SystemExit(exit_code)
'''


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(folder):
    return {p.relative_to(folder).as_posix(): sha(p.read_bytes())
            for p in sorted(folder.rglob("*")) if p.is_file()}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--temporary-parent", type=Path,
                        default=Path("/TEMP/bandit-round12-4a9iyv"))
    args = parser.parse_args()
    if sys.version_info[:2] != (3, 11) or Path(sys.executable).resolve() != PYTHON.resolve():
        raise SystemExit("Run this smoke with the specified local Python 3.11 interpreter.")
    for executable in (PYTHON, NODE):
        if not executable.is_file() or not os.access(executable, os.X_OK):
            raise SystemExit(f"Required existing executable is unavailable: {executable}")
    parent = args.temporary_parent.resolve(strict=True)
    if not parent.is_dir():
        raise SystemExit("Temporary parent must already be a directory.")
    result_path = OUTPUT / f"{PREFIX}-results.json"
    report_path = OUTPUT / f"{PREFIX}-report.md"
    evidence = OUTPUT / f"{PREFIX}-evidence"
    if any(p.exists() for p in (result_path, report_path, evidence)):
        raise SystemExit("Refusing to overwrite existing smoke evidence.")

    started = now()
    source_paths = (ROOT / "evals/run_local.py", ROOT / "evals/archive_run.mjs", Path(__file__).resolve())
    source_before = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in source_paths}
    temporary = Path(tempfile.mkdtemp(prefix="fake-model-cli-", dir=parent)).resolve()
    evidence.mkdir()
    commands_dir = evidence / "commands"
    captures = evidence / "fake-invocations"
    commands_dir.mkdir()
    captures.mkdir()
    fake_bin = temporary / "bin"
    fixture = temporary / "raw"
    fake_bin.mkdir()
    fixture.mkdir()
    (fixture / "request.md").write_bytes(REQUEST)
    (evidence / "request.md").write_bytes(REQUEST)
    fake = fake_bin / "codex"
    fake.write_text(f"#!{PYTHON}\n" + FAKE_SOURCE.lstrip(), encoding="utf-8")
    fake.chmod(0o700)
    (evidence / "fake-codex.py").write_bytes(fake.read_bytes())
    # Deliberately do not inherit auth tokens, host config variables or real
    # Codex directories. The sole executable named codex on PATH is our fake.
    environment = {
        "PATH": os.pathsep.join((str(fake_bin), str(PYTHON.parent), str(NODE.parent))),
        "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1",
        "FAKE_SMOKE_CAPTURE_DIR": str(captures),
    }
    commands, checks, cases = [], [], []

    def check(label, condition, detail=None):
        checks.append({"check": label, "passed": bool(condition), "detail": detail})

    def command(label, argv, env):
        record = {"label": label, "argv": [str(x) for x in argv], "cwd": str(ROOT), "started_at_utc": now()}
        try:
            result = subprocess.run(record["argv"], cwd=ROOT, env=env, stdin=subprocess.DEVNULL,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30, check=False)
            stdout, stderr = result.stdout, result.stderr
            record.update(exit_code=result.returncode, launch_error=None)
        except (OSError, subprocess.TimeoutExpired) as error:
            stdout, stderr = getattr(error, "stdout", None) or b"", getattr(error, "stderr", None) or b""
            record.update(exit_code=None, launch_error=f"{type(error).__name__}: {error}")
        record["finished_at_utc"] = now()
        for stream, data in (("stdout", stdout), ("stderr", stderr)):
            path = commands_dir / f"{label}.{stream}.txt"
            path.write_bytes(data)
            record[stream] = {"path": path.relative_to(OUTPUT).as_posix(), "sha256": sha(data), "bytes": len(data)}
        commands.append(record)
        return record

    def inspect_case(label, requested, expected_exit):
        env = dict(environment, FAKE_SMOKE_LABEL=label, FAKE_SMOKE_EXIT=str(expected_exit))
        case_name = "fake-model-" + label
        output_parent = temporary / "runs" / label
        run = output_parent / f"{case_name}--baseline"
        archive = evidence / "archives" / label
        argv = [PYTHON, ROOT / "evals/run_local.py", "--case", case_name, "--arm", "baseline",
                "--fixture-dir", fixture, "--web-search", "disabled", "--output-dir", output_parent]
        if requested is not None:
            argv += ["--model", requested]
        result = command("runner-" + label, argv, env)
        check(label + ": runner returns fake child exit", result["exit_code"] == expected_exit)
        # Preserve partial artifacts too if an implementation error prevents the
        # remaining assertions. Tiny baseline fixtures avoid skill-tree copies.
        if run.exists():
            shutil.copytree(run, evidence / "originals" / label)
        metadata = load(run / "metadata.json")
        version_capture = load(captures / ("fake-" + label + "-version") / "invocation.json")
        exec_capture = load(captures / ("fake-" + label + "-exec") / "invocation.json")
        captured_argv = exec_capture["argv"]
        expected_prompt = (run / "prompt.txt").read_bytes()
        check(label + ": captured argv equals metadata command", metadata["command"] == ["codex", *captured_argv])
        check(label + ": prompt bytes preserved", (captures / ("fake-" + label + "-exec") / "stdin.txt").read_bytes() == expected_prompt)
        check(label + ": fake version and one exec", metadata["codex_version"] == FAKE_VERSION and version_capture["argv"] == ["--version"])
        check(label + ": explicit request or default metadata", metadata["model_override"] == requested)
        check(label + ": literal model argv", captured_argv.count("--model") == (0 if requested is None else 1)
              and (requested is None or captured_argv[captured_argv.index("--model") + 1] == requested))
        config = metadata["config"].lower()
        check(label + ": config distinguishes request from backend verification",
              "host model defaults" in config if requested is None else
              "requested" in config and "host model defaults" not in config
              and any(phrase in config for phrase in ("not verified", "unverified", "not independently verified")),
              metadata["config"])
        check(label + ": unchanged sandbox and web flags",
              all(flag in captured_argv for flag in ("--ignore-user-config", "--ephemeral", "--skip-git-repo-check", "--json"))
              and captured_argv[captured_argv.index("--sandbox") + 1] == "read-only"
              and captured_argv[captured_argv.index("-c") + 1] == 'web_search="disabled"'
              and metadata["web_search"] == "disabled" and metadata["editable_artifact"] is None)
        check(label + ": raw-only unchanged baseline workspace",
              metadata["input_sha256"] == metadata["input_after_sha256"] == {"request.md": sha(REQUEST)}
              and metadata["instruction_sha256"] == metadata["instruction_after_sha256"] == {}
              and snapshot(run / "workspace") == {"input/request.md": sha(REQUEST)})
        check(label + ": exited metadata keeps nonzero distinct from launch failure",
              metadata["runner_status"] == "exited" and metadata["exit_code"] == expected_exit)
        archive_result = command("archive-" + label, [NODE, ROOT / "evals/archive_run.mjs", run, archive], environment)
        check(label + ": archive CLI succeeds", archive_result["exit_code"] == 0)
        retained = load(archive / "metadata.json")
        provenance = load(archive / "archive-provenance.json")
        check(label + ": archive retains exact requested model", retained["model_override"] == requested
              and retained["config"] == metadata["config"])
        normalized = (run / "metadata.json").read_bytes().replace(str(run).encode(), b"<temporary-run-root>")
        check(label + ": exact metadata path normalization", (archive / "metadata.json").read_bytes() == normalized)
        mapping_errors = []
        for name, mapping in provenance["files"].items():
            original = (run / mapping["source"]).read_bytes()
            copied = (archive / name).read_bytes()
            expected = original.replace(str(run).encode(), b"<temporary-run-root>") if mapping["temporary_path_normalized"] else original
            if sha(original) != mapping["original_sha256"] or sha(copied) != mapping["archived_sha256"] or copied != expected:
                mapping_errors.append(name)
        check(label + ": all archive hashes and transformations", not mapping_errors, mapping_errors)
        check(label + ": archive preserves completed versus failed child",
              provenance["run_status"] == ("completed" if expected_exit == 0 else "failed")
              and provenance["source_exit_code"] == expected_exit
              and provenance["terminal_event"] == ("turn.completed" if expected_exit == 0 else "turn.failed"))
        cases.append({"label": label, "requested_model": requested, "expected_fake_child_exit": expected_exit,
                      "original_run": str(run), "archive": archive.relative_to(OUTPUT).as_posix(),
                      "fake_thread_id": "fake-thread-" + label, "archive_mapping_count": len(provenance["files"]),
                      "original_metadata_sha256": sha((run / "metadata.json").read_bytes()),
                      "archived_metadata_sha256": sha((archive / "metadata.json").read_bytes())})

    for label, requested, expected_exit in (("explicit", MODEL, 0), ("default", None, 0), ("child-failure", MODEL, 23)):
        try:
            inspect_case(label, requested, expected_exit)
        except Exception as error:
            check(label + ": complete inspection", False, f"{type(error).__name__}: {error}")

    before_invalid = sorted(p.name for p in captures.iterdir())
    invalid_output = temporary / "invalid-output"
    invalid_case = "fake-model-empty"
    invalid = command("runner-invalid-empty", [PYTHON, ROOT / "evals/run_local.py", "--case", invalid_case,
                      "--arm", "baseline", "--fixture-dir", fixture, "--output-dir", invalid_output, "--model", ""],
                      dict(environment, FAKE_SMOKE_LABEL="invalid-empty", FAKE_SMOKE_EXIT="0"))
    check("invalid empty: CLI exits 2", invalid["exit_code"] == 2)
    check("invalid empty: no fake child or version probe", sorted(p.name for p in captures.iterdir()) == before_invalid)
    check("invalid empty: no output/run directory", not invalid_output.exists())
    invocations = [load(p / "invocation.json") for p in sorted(captures.iterdir()) if (p / "invocation.json").is_file()]
    check("six distinct fake invocations: three version probes plus three execs",
          len(invocations) == 6 and len({i["id"] for i in invocations}) == 6
          and sum(i["mode"] == "version" for i in invocations) == 3
          and sum(i["mode"] == "exec" for i in invocations) == 3)
    check("all expected fake invocation identities, no fallback exec",
          {i["id"] for i in invocations} == {"fake-" + label + "-" + mode
           for label in ("explicit", "default", "child-failure") for mode in ("version", "exec")})
    source_after = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in source_paths}
    check("runner, archiver and harness unchanged during smoke", source_before == source_after)
    check("synthetic fixture unchanged", snapshot(fixture) == {"request.md": sha(REQUEST)})
    passed = all(item["passed"] for item in checks)
    receipt = {
        "kind": "fake-executable engineering integration smoke; zero real Codex/model/TASK executions",
        "status": "pass" if passed else "failed", "started_at_utc": started, "finished_at_utc": now(),
        "temporary_root_retained": str(temporary), "python": str(PYTHON), "python_version": sys.version,
        "node": str(NODE), "controlled_path": environment["PATH"],
        "environment": "Minimal allowlist; no inherited auth/config variables; fake codex is the only codex on PATH.",
        "requested_model_test_string": MODEL, "model_identity_verified": False,
        "fake_version_string": FAKE_VERSION, "fake_executable_sha256": sha(fake.read_bytes()),
        "fake_invocation_count": len(invocations), "fake_invocations": invocations,
        "commands": commands, "cases": cases, "checks": checks,
        "source_before_sha256": source_before, "source_after_sha256": source_after,
        "evidence_file_sha256": snapshot(evidence),
        "limitations": ["Synthetic fake events and fake thread IDs do not prove native TASK behavior or backend/model identity.",
                        "Tests exercise literal CLI forwarding, metadata, isolation flags, failure propagation and archival only.",
                        "Unsigned local receipts; no network, auth, planning-quality assessment or full engineering gates."]}
    result_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    report = ["# Fake model-option CLI smoke", "", receipt["kind"] + ".", "",
              f"Status: **{receipt['status']}**. {sum(c['passed'] for c in checks)}/{len(checks)} recorded checks satisfied.",
              f"Fake invocations: {len(invocations)}; these are not native Codex runs or planning TASKs.", "",
              "| Check | Result |", "| --- | --- |"]
    report += [f"| {c['check']} | {'pass' if c['passed'] else 'FAIL'} |" for c in checks]
    report += ["", f"[Complete results]({result_path.name}) retain exact argv, UTC timestamps, child exits,",
               "captured prompt/stream hashes, all fake invocation identities, source hashes, and evidence hashes.",
               f"Results SHA-256: `{sha(result_path.read_bytes())}`.", "",
               f"The literal `{MODEL}` is a synthetic test string, not an available or verified model.",
               "Explicit and default success, explicit child exit 23, and empty-option preflight are exercised sequentially.",
               "All fake calls remain local. A requested model value is not evidence that any backend selected it.",
               "The real runner and archive CLIs are used, but all supplied CLI events/output come from the fake.",
               "Raw originals, archives and capture streams are retained under this check's evidence directory.",
               "The temporary root is retained; this harness deletes nothing. No full suites or release packaging run.", ""]
    report_path.write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "results": str(result_path), "fake_invocations": len(invocations),
                      "checks": len(checks), "failed": [c for c in checks if not c["passed"]]}))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
