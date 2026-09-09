#!/usr/bin/env python3
"""One-off local verification receipt; no release packaging command is run."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess


OUTPUT = Path(__file__).resolve().parent
ROOT = OUTPUT.parents[3]
NODE = "/Users/DEVELOPER/.npm/_npx/52027bd8fc0022aa/node_modules/node/bin/node"
NPM = "/opt/homebrew/lib/node_modules/npm/bin/npm-cli.js"
PYTHON = "/Users/DEVELOPER/.local/bin/python3.11"
VALIDATOR_PYTHON = "/TEMP/bandit-round2-jumhQp/validator-venv/bin/python"
VALIDATOR = "/Users/DEVELOPER/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
SKILLS = ("bandit", "bandit-research", "bandit-scope", "bandit-specify", "bandit-review")
COMMANDS = [
    ("node-version", [NODE, "--version"]),
    ("npm-version", [NODE, NPM, "--version"]),
    ("python-version", [PYTHON, "--version"]),
    ("validator-python-version", [VALIDATOR_PYTHON, "--version"]),
    ("sync", [NODE, "scripts/sync-skills.mjs", "--check"]),
    ("node-validate", [NODE, NPM, "run", "validate"]),
    ("node-tests", [NODE, NPM, "test"]),
    ("python-validate", [PYTHON, "scripts/validate.py"]),
    ("python-tests", [PYTHON, "-m", "unittest", "discover", "-s", "tests", "-v"]),
    *[(f"metadata-{name}", [VALIDATOR_PYTHON, VALIDATOR, f"skills/{name}"]) for name in SKILLS],
]
ENV = os.environ.copy()
ENV.pop("npm_config_call", None)
ENV["PATH"] = str(Path(NODE).parent) + os.pathsep + ENV.get("PATH", "")
ENV["PYTHONDONTWRITEBYTECODE"] = "1"
ENV["npm_config_update_notifier"] = "false"
ENV["npm_config_offline"] = "true"


def now():
    return datetime.now(timezone.utc).isoformat()


def product_hashes():
    paths = [p for p in (ROOT / "skills").rglob("*") if p.is_file()]
    paths += [ROOT / p for p in ("lib/installer.mjs", "bin/bandit.mjs", "install.py")]
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def run(item):
    label, command = item
    print(f"START {label}", flush=True)
    record = {"label": label, "command": command, "cwd": str(ROOT), "started_at_utc": now()}
    try:
        completed = subprocess.run(command, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        record.update(exit_code=completed.returncode, launch_error=None)
        stdout, stderr = completed.stdout, completed.stderr
    except OSError as error:
        record.update(exit_code=None, launch_error=str(error))
        stdout, stderr = b"", b""
    record["finished_at_utc"] = now()
    print(f"END {label}: {record['exit_code']}", flush=True)
    return record, stdout, stderr


targets = [OUTPUT / "results.json"]
targets += [OUTPUT / f"{label}.{stream}.txt" for label, _ in COMMANDS for stream in ("stdout", "stderr")]
if any(p.exists() for p in targets):
    raise SystemExit("Refusing to overwrite an existing verification receipt.")
before = product_hashes()
# Buffer command output until all checks finish, avoiding live log changes while
# archive-related unit tests inspect the source tree. Those tests use temp files;
# this harness never creates a final npm package or source ZIP.
with ThreadPoolExecutor(max_workers=3) as pool:
    completed_runs = list(pool.map(run, COMMANDS))
after = product_hashes()
records = []
for record, stdout, stderr in completed_runs:
    for stream, data in (("stdout", stdout), ("stderr", stderr)):
        name = f"{record['label']}.{stream}.txt"
        with (OUTPUT / name).open("xb") as destination:
            destination.write(data)
        record[f"{stream}_file"] = name
        record[f"{stream}_sha256"] = hashlib.sha256(data).hexdigest()
    records.append(record)
passed = all(r["exit_code"] == 0 and r["launch_error"] is None for r in records) and before == after
receipt = {
    "status": "pass" if passed else "failed",
    "finished_at_utc": now(),
    "environment": {"npm_config_call_removed": True, "node_bin_prepended_to_path": str(Path(NODE).parent),
                    "stdin": "closed", "python_bytecode_writes_disabled": True, "npm_offline": True},
    "commands": records,
    "product_before_sha256": before,
    "product_after_sha256": after,
    "product_bytes_unchanged": before == after,
    "limitations": "Local structural/unit/package-test evidence, not planning behavior, network integration, host discovery, or final release packaging.",
}
with (OUTPUT / "results.json").open("x") as destination:
    json.dump(receipt, destination, indent=2)
    destination.write("\n")
print(receipt["status"].upper(), flush=True)
raise SystemExit(0 if passed else 1)
