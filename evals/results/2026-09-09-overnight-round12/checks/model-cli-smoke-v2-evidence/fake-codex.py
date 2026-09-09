#!/Users/DEVELOPER/.local/bin/python3.11
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
