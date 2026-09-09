# Staged-source regressions: before correction

Recorded at 2026-09-08T17:27:05.506Z before editing either implementation.

Two synthetic ordinary-file changes are injected after the second payload is
staged: an in-place content edit, and a different file with identical contents
at the staging pathname. Both updates currently promote the changed source,
so the expected preservation at its staging pathname fails in both languages.
These are local fault-injection tests, not reported customer incidents.

- Node 22 command: `npx --yes --package=node@22 --call 'env -u npm_config_call node --test tests-node/install.test.mjs tests-node/staging.test.mjs'`.
  Exit 1: existing 48 tests pass; both new tests fail, with no skips.
- Python 3.11.16 command: `/Users/DEVELOPER/.local/bin/python3.11 -m unittest discover -s tests -p test_staging.py -v`.
  Exit 1: both new tests fail, with no skips.
- The full terminal output is retained in [Node](before-node.txt) and
  [Python](before-python.txt); [source and test hashes](before-sha256.txt)
  pin this comparison. The implementation hashes match round 5's final source.
- Four existing Node post-write hooks now accept pathname or descriptor writes.
  Their injection boundaries and assertions are unchanged, and all 48 existing
  tests pass against the unchanged implementation before the correction.

The two staging test files were written before the implementation fix and will
remain unchanged for the after-state run. Complete destination snapshots assert
rollback of the earlier managed-file write and preservation of the old marker,
in addition to preserving the changed staged file and its identity.

A separate agent diagnostic was stopped by the tool's safety filter and produced
no usable finding. It is not retried or used as evidence here. These two local
staged-source tests were independently underway before that stop; the blocked
diagnostic is not part of this comparison.

Temporary pre-fix implementation and skill snapshots are retained under
`/TEMP/bandit-round6-9Y1jS3/`. Timestamps are local unsigned receipts,
not independent time attestations. No skill instructions have changed.

