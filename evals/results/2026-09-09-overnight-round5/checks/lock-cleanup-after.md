# Lock-cleanup correction — after-fix receipt

Local macOS engineering checks recorded on 2026-09-09. The separate
[before-fix receipt](lock-cleanup-regressions.md) remains byte-identical at
SHA-256 `e051d2a8bc04a9a834d23e3f41062c88c78971041a8fc49476b52afec260a94e`.
No planning task, user/host skill mutation, customer outreach, or publication was
part of these regression checks.

The before receipt's statement about editing only tests and the receipt refers
to that regression-author subtask, not the whole worktree. Onboarding edits and
evaluation authoring proceeded in parallel; installer implementation bytes
remained unchanged until the failing-before checks finished.

## Bounded change

Both installers now capture lock identity with `fstat` on the descriptor
returned by exclusive creation, before closing that descriptor. They retain
the immediate-close behavior and existing lock names/format; no new lock token,
persistent-descriptor scheme, or stale-lock force deletion was introduced.

Cleanup first rechecks the path's ancestry and uses `lstat` to inspect the
current object without following a final-component link. It releases only a
regular file whose device, inode, mode, size, modification time and change time
match the acquired lock. Node uses BigInt identity/nanosecond fields; Python
uses integer identity and `*_ns` fields. Matching empty contents alone is not
ownership proof. Access time is not part of the comparison.

Each lock is handled independently. Missing, replaced, modified or unsafe paths
are preserved or skipped; a cleanup exception does not mask the primary error
or prevent attempts to release the remaining unchanged, safely reachable locks.
The new logic is at `lib/installer.mjs:263` and `install.py:283`, with identity
capture at Node line 296 and Python line 315. Existing file-update, retirement,
marker and rollback semantics were not expanded by this correction.

## Terminal suite results

The main agent reported the following completed console results. The reviewer
independently checked the source/test digests below and performed the additional
diagnostics in the next section; it did not poll or restart those test runs.

| Check | Runtime | Result | Exit |
| --- | --- | --- | ---: |
| Copied before-code installer replay | Node 22.23.2 | 48 tests: 45 pass, the same 3 regressions fail; no skips | 1 |
| Focused after-code installer suite | Node 22.23.2 | 48/48 pass | 0 |
| Focused after-code installer suite | Python 3.11.16 | 51/51 pass | 0 |
| Full `npm test` | Node 22.23.2 | 76/76 pass; no skips | 0 |
| Full Python test suite | Python 3.11.16 | 90/90 pass; no skips | 0 |

The supplementary before-code replay uses the same Node runtime version as
the after runs, rather than relying only on the original Node 26 reproduction:

```sh
npx --yes --package=node@22 --call 'env -u npm_config_call node --test /TEMP/bandit-round5-WDXmd0/before-source/tests-node/install.test.mjs'
```

That copied test imports the retained original installer at
`before-source/lib/installer.mjs`. Both copied files independently hash-match
the frozen before-code/test digests. The inherited `npm_config_call` setting is
removed for the nested command, consistent with the previously recorded npm
environment issue.

The fixed regressions verify preservation of all seven unrelated lock files
behind a changed parent, preservation of a different-inode empty replacement,
and cleanup of the other six locks when the first-released lock is missing.
Ordinary installation still removes its unchanged locks; existing successful
bundle tests assert that only the five skill directories remain afterward.

## Four additional disposable diagnostics

A separate reviewer ran two cases against each current installer, using Node
26.8.1 and Python 3.11.16. All four completed successfully:

| Mutation after lock acquisition | Node result | Python result |
| --- | --- | --- |
| Write text into the existing lock without changing its inode | Exact text and same inode retained; other six locks released; installation returns `installed` | Same result |
| Move the acquired lock aside and replace its path with a directory containing a note | Directory/note retained; other six locks released; installation returns `installed` | Same result |

Each diagnostic used only a disposable synthetic source/project and restored
its injection hook afterward. It verified actual remaining paths and content,
not merely a successful return or expected exception. No frozen test or before
receipt was edited to obtain these results.

## Independently verified digests

| Artifact | SHA-256 |
| --- | --- |
| Node before source, including the copied replay source | `948c57ee73cd0f37c484162c2f057e0ba1862a28988698320d301cad0f3e6b89` |
| Python retained before source | `c960efd88aced5c99d1ef6f66b0feace8640706a8b7044853998663fda5ca7c2` |
| Current `lib/installer.mjs` | `698eb379641ac63a799dba1f8a2281bbe4728a4eb847e991d158a465ef171db7` |
| Current `install.py` | `406b2dd565d47883f4dcea14d10e74ff3429e6ffd3082042b4d8b905d75899b1` |
| Frozen Node tests, also matching the replay copy | `d68ead52d0c4f4af4f762d0af0a240f45807ab214673da90c32c1de5eae3f1f8` |
| Frozen Python tests | `02e5ae5c264813cc89fd9496be9d301efb4ef928a20a49297fc6d1088bf90533` |

## Limits

These are local macOS checks, not a new CI run or proof of Windows/Linux
behavior. They establish the specific preservation and cleanup results above,
not absolute concurrency safety or planning quality. The final path/identity
check and `unlink` are still separate filesystem operations: arbitrary mutation
in that last interval is not eliminated. Changed or unverifiable lock objects
may intentionally remain for manual inspection; no promise is made to recover
every lock after arbitrary I/O failures or process interruption. The correction
does not broaden authorization to overwrite user work or force-remove locks.
