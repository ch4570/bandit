# Lock-cleanup regression receipt — before fix

Recorded on 2026-09-09 local time using disposable synthetic fixtures on macOS,
Node 26.8.1 and Python 3.11.16. No model task, user/host skill change, external
service action, or publication was performed. Only installer tests and this
receipt were edited before these checks; product implementation was unchanged.
Synthetic temporary directories were removed after each check.

## Observed defect

`lib/installer.mjs:331` and `install.py:355` unconditionally unlink the saved
lock pathname during final cleanup. They do not recheck ancestry or verify
that the current filesystem object is the lock this installation created.
One cleanup error also stops release of subsequent locks.

The same unconditional cleanup is present in HEAD (`f4a376e`), at Node line 315
and Python line 328. This is an unhandled ownership/cleanup defect, not a
regression introduced by the earlier exact-byte update/rollback changes.

Three preservation-focused tests were added per installer before fixing code:

1. **Changed parent.** After all seven active/retired locks are acquired, move
   their parent and replace it with a prepared directory symlink pointing to
   another synthetic directory. That directory contains seven pre-existing
   same-named locks with distinct recorded text. Normal destination checks
   correctly raise `Symlink or junction is not allowed`, but final cleanup
   follows the changed parent and deletes all seven unrelated files. The
   installer's own locks remain in the moved parent. The test compares the
   complete unrelated before/after byte snapshot, not only the exception.
2. **Replaced lock.** Move `.bandit-update.bandit.lock` aside and create a new
   empty regular file at its old pathname. The original and replacement have
   different observed inodes but identical empty contents. Cleanup deletes the
   replacement. The test requires that exact replacement inode to survive and
   checks that other unchanged owned locks are released. Node uses BigInt
   inode values; preservation cannot be justified by matching empty bytes alone.
3. **Removed lock.** Remove `.bandit-update.bandit.lock` after acquisition.
   Because it is released first, its missing-file error stops the loop and
   leaves six unaffected owned locks behind, despite all five active ownership
   markers having committed. The test requires no remaining owned locks; it
   does not pass merely because an exception was thrown.

Node injects after the first real temporary staging write and before the
installer's existing destination recheck. Python injects at entry to the first
`atomic_write`, before its existing path check. Both hooks execute only inside
the fixture and are restored afterward. These are not injections in the tiny
final-check-to-rename/unlink gap. A separate Python diagnostic also replaced
the first-released lock with a directory containing a note: its note survived,
but cleanup stopped and stranded the other six locks. No additional test or
broader object-replacement framework was added for that equivalent cleanup case.

## Failing-before results

```sh
node --test tests-node/install.test.mjs
python3.11 -m unittest discover -s tests -p test_install.py -v
```

| Suite | Observed result | Exit |
| --- | --- | ---: |
| Node installer | 48 tests: 45 pass, the 3 new regressions fail; no skips | 1 |
| Python installer | 51 tests: 48 pass, the 3 new regressions fail; no skips | 1 |

The corresponding failure messages in both suites are:

```text
Cleanup must preserve every unrelated lock byte
  actual: empty snapshot; expected: seven recorded lock files
Another owner's replacement lock must survive
  actual: file absent
A removed lock must not strand unaffected owned locks
  actual: six remaining lock files; expected: none
  cleanup error: ENOENT / FileNotFoundError for .bandit-update.bandit.lock
```

Ordinary successful cleanup remains checked: the existing Node no-argument
installation test requires exactly the five skill directories afterward. The
existing Python bundle/idempotence test now makes the same explicit assertion.
Both pass before the fix, as do the existing migration, marker, lock-contention,
cross-skill rollback and concurrent-edit tests. These are engineering checks,
not planning-quality evidence or a blanket concurrency-safety claim.

## Frozen before-state digests

| File | SHA-256 |
| --- | --- |
| `lib/installer.mjs` | `948c57ee73cd0f37c484162c2f057e0ba1862a28988698320d301cad0f3e6b89` |
| `install.py` | `c960efd88aced5c99d1ef6f66b0feace8640706a8b7044853998663fda5ca7c2` |
| `tests-node/install.test.mjs` | `d68ead52d0c4f4af4f762d0af0a240f45807ab214673da90c32c1de5eae3f1f8` |
| `tests/test_install.py` | `02e5ae5c264813cc89fd9496be9d301efb4ef928a20a49297fc6d1088bf90533` |

Product bytes also match the independently retained before-code snapshots.
`git diff --check` passes. No after-fix outcome is claimed in this receipt;
append subsequent implementation and verification evidence separately.
