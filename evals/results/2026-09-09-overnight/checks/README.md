# Local checks and recovered environment failures

These are development-tool and distribution checks, not planning-quality
measurements. They ran on macOS arm64; no new CI or release was triggered.

## Node 22 nested npm failure

The first complete run used:

```sh
npx --yes --package=node@22 --call 'node --version && npm test'
```

Node was 22.23.2 and npm was 11.19.0. Seventy of 71 tests passed. The package
consumption test failed before invoking BANDIT because the outer `npx --call`
exported `npm_config_call` to the inner `npm exec`, which also supplied
positional command arguments. The installed npm implementation rejects that
combination with `EUSAGE` (`lib/commands/exec.js`, line 77).

A separate audit reproduced and isolated the failure without editing any
product or test code:

| Control | Observed result | Original output |
| --- | --- | --- |
| Node 22, inherited outer call option | Package test fails with EUSAGE | [Failure](node22-package-failure.txt) |
| Node 22, only `npm_config_call` removed | Package test passes | [Clean environment](node22-package-clean-call.txt) |
| Node 26, call option injected | Same package test fails with EUSAGE | [Injected control](node26-package-injected-call.txt) |

The [selected environment fields](node22-nested-npm-environment.txt) record the
inherited option without dumping unrelated host environment variables. These
four logs are copied byte-for-byte from the audit's temporary files; they keep
local temporary paths. No customer documents or credentials were supplied.

The full suite subsequently passed **71/71** with:

```sh
npx --yes --package=node@22 --call 'node --version && env -u npm_config_call npm test'
```

This is a local minimum-supported-major check, not evidence of Windows/Linux
compatibility. The invocation failure is retained, not counted as a BANDIT
installer defect or concealed by weakening a test.

## Python and skill metadata

Python validation and **79/79** unit tests passed using Python 3.11.16 at
`/Users/DEVELOPER/.local/bin/python3.11`. Four new runner tests use mocked task
execution to check staged inputs, original bytes, failed-run records and
invalid paths. They are not four additional planning evaluations. The system
`python3` remains the unsupported 3.9.6 and was not upgraded.

The official skill-creator metadata validator initially failed for each skill
because the development interpreter lacked `yaml`. A probe also found no `uv`
on PATH. Creating a temporary Python 3.11 environment and installing
`PyYAML==6.0.2` there allowed all five validations to pass. This did not add a
project, package, lifecycle or end-user dependency. The npm installation path
remains dependency-free and independent of Python.

Resource synchronization and the Node validator passed for all five skills
and 34 files. Structural validity does not establish planning effectiveness.

## Task-local recovery

The post-change first-stage specification task attempted `python` for a word
count and received command-not-found, then successfully used `python3`.
Both attempts remain in that task's `events.jsonl` (lines 18 and 20). The task
completed with only its allowed PRD changed. Its final artifact, not an
intermediate counting command, determines the recorded word count.
