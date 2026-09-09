# Runner regression receipt

Synthetic, mocked engineering checks run on 2026-09-09 local time with Python
3.11.16 and Node 26.8.1. No task model, browsing, publication, or product-skill
change was involved. These checks are not planning-quality evidence.

Regression tests were added and run against the pre-fix runner and archiver
before implementation. The same commands were then rerun after the fixes:

```sh
python3.11 -m unittest discover -s tests -p test_eval_runner.py -v
node --test tests-node/eval-archive.test.mjs
```

| Focused suite | Before implementation | After implementation |
| --- | --- | --- |
| Python runner, initial regressions | 10 test methods; 5 failed subtests and 3 erroring subtests; exit 1 | 10/10 passed; exit 0 |
| Python runner, nested-link follow-up | 11 passed, 1 failed; exit 1 | 12/12 passed; exit 0 |
| Node archiver | 10 passed, 2 failed; exit 1 | 12/12 passed; exit 0 |

## Launch failure

Before: a mocked task-launch `FileNotFoundError` left metadata without terminal
state, finish time, elapsed time, or after hashes. A missing executable or
nonzero exit during `codex --version` left no metadata file. New assertions
failed with `KeyError: 'runner_status'` for the task launch and
`FileNotFoundError` for the two version-probe cases. The existing archiver
rejected explicit launch-failure metadata because it required a child exit code.

After: those three cases preserve original inputs/instructions, current hashes,
UTC start/finish times, elapsed time, and the error's phase, type, and message.
Metadata records `runner_status: "launch_failed"` and `exit_code: null`; no
task exit, output, or event is invented. Exceptions still reach the CLI's error
handler. Successful version probes record their version; unavailable/failed
probes leave it null. The raw fixture is unchanged and the failed run is retained.

The archiver accepts this explicit terminal state as `launch-failed`, with
`source_exit_code: null`. New negative cases reject missing or contradictory
error/status/exit/timestamp fields before archive creation. Existing checks for
missing after hashes, hash mismatches, unfinished runs, nonzero task exits, and
zero-exit incomplete responses remain in place.

## Instruction-source overlap

Before: output beneath a selected standalone specialist, all-skill source,
general skill, upstream checkout, or symlink alias reached staging. Five bounded
mock assertions failed with `Must reject before copying`. The copy stub aborted
at the first copy; the tests did not execute a recursive copy into its own source.

After: the resolved selected instruction source and run path are checked for
containment in either direction before any run directory is created. The checked
source is also used for the copy. All five cases reject without changing source
bytes or launching a task. Standalone runs may still write beneath an unselected
sibling, and staged fixtures still expose only the supplied stage.

Independent review then confirmed a nested-link bypass: a resource directory
link could point at an external output parent, which `copytree` would follow
back into the run. Another test was added before closing this path; the 12-test
Python suite failed only that bounded copy assertion. After the follow-up fix,
all 12 tests pass. Selected instruction sources now require real resources, not
nested symlinks; source-root aliases remain resolved normally. Upstream entries
named `.git` or `__pycache__` remain excluded, including linked entries, as a
separate passing regression verifies.

These are preflight checks, not a lock against concurrent filesystem changes.
Interruption, disk failure during evidence finalization, and general retry or
timeout handling are outside this bounded fix; incomplete evidence remains
nonterminal rather than being promoted to a completed task.
