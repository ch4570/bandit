"""Capture selected mock-only engineering tests; never launch a real model task."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

checks = Path(__file__).resolve().parent
root = checks.parents[3]
names = ("evals/run_local.py", "tests/test_eval_runner.py")
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
before = {name: digest(root / name) for name in names}
assert before[names[0]] != digest(checks / "run-local-before.py")
assert before[names[1]] == "763e45ebcf89ea628b8904d6f2efcd3163d085f02f57ecf61def25f5d8e568d5"
assert sys.version_info[:2] == (3, 11)
command = [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests",
           "-p", "test_eval_runner.py", "-k", "model", "-v"]
started = datetime.now(timezone.utc).isoformat()
result = subprocess.run(command, cwd=root, stdin=subprocess.DEVNULL,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
receipt = {"command": command, "cwd": str(root), "stdin": "closed", "shell": False,
           "started_at_utc": started, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
           "python_version": sys.version, "exit_code": result.returncode,
           "hashes_before": before, "hashes_after": {name: digest(root / name) for name in names},
           "stdout": "model-tests-after.stdout.txt", "stderr": "model-tests-after.stderr.txt",
           "scope": "Selected unittest methods only; all Codex child/version calls mocked; no native TASK or PM-quality measurement."}
for stream in ("stdout", "stderr"):
    with (checks / receipt[stream]).open("x", encoding="utf-8") as output:
        output.write(getattr(result, stream))
with (checks / "model-tests-after.json").open("x", encoding="utf-8") as output:
    output.write(json.dumps(receipt, indent=2) + "\n")
assert receipt["hashes_after"] == before
assert result.returncode == 0, "The frozen model tests must pass after implementation."
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
raise SystemExit(result.returncode)
