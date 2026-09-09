# Round 9 — independent integration evidence audit

Read-only inspection confirms the completed public install/repeat in attempt 1
and all four intended fixtures in attempt 2. The first attempt's local-candidate
invocation failure remains a failure; it is not an installer rejection or a
passing candidate preview. No install, retry, fault injection, or product test
was executed during this audit. The only authored audit artifact is this file.

These are local macOS distribution observations on Node 22.23.2/npm 11.19.0,
not planning TASKs, first-ever public installation proof, a public release, or
evidence about planning quality. Earlier public-install evidence remains under
its original conditions.

## Frozen plan, invocation correction, and retained evidence

The original [harness](checks/npx-flow.mjs) still hashes to
`8e1a7533c2680febef603853f49b2f348c8b3e3145daa4ed56b236dbf40f4486`;
the [original receipt](before-run.json) still hashes to
`42271ba8f99876b6dde37fafd276d3758ae9a65e142b3541b0b895b13427def0`.
Its recorded installer, package, INSTALL and package-test source hashes also
match the current files inspected during this audit.

The [v2 source](checks/npx-flow-v2.mjs) differs only in two explanatory header
comments and the candidate argument helper: local archives use
`npx --yes --package=/absolute/candidate.tgz -- bandit ...`. Public-release
and old-bootstrap URLs remain positional; expected outcomes and assertions
are unchanged. V2 hashes to
`f3a966b532b9fb39ca0ef214a27dd2b80067623e06e9cf9b7d4eb07b7f3c26e1`,
matching [v2-before-run.json](v2-before-run.json), whose hash is
`bc97782ba1c9878f14314970aacee0a9ce7e23c9325f22d1f996152e2cd003c9`.
The [correction record](harness-correction.md) preserves the command mistake;
the earlier planning recommendation of a positional local archive was not
supported by its observed behavior in this npm environment.

The source-evidence copies were compared byte-for-byte to their separate scratch
directories, with exact retained file sets:

| Attempt | Scratch directory | Retained files |
| --- | --- | --- |
| 1 | `/TEMP/bandit-round9-pm62vi` | 10: four command logs, four snapshots, sources and failure |
| 2 | `/TEMP/bandit-round9-wwXdSO` | 27: twelve command logs, thirteen snapshots, sources and result |

No normalization or loss of logged stdout/stderr was found in those copies.
Attempt 1's [failure](attempt1/failure.json) hashes to
`3907f27004b2e38b9dfd8db8ceceffe75c215cdea2273285e2e299e1e7cb3056`;
attempt 2's [result](attempt2/result.json) hashes to
`b8b217620f01c938db05f089213b1268036efa0cd08978f583b46bc2c6bc453a`.

## Package identity and actual npm caches

The [source record](attempt2/sources.json) matches independently read archive
bytes and every recorded package-member hash. The same source record is retained
unchanged in both attempts.

| Source | Version | Package files / skill payloads | Tarball SHA-256 |
| --- | --- | ---: | --- |
| Public pinned release | 0.4.0 | 43 / 34 | `af5e83e5c45ab15956f1d7463ed9194ef1362f2ea68c6db9a7a967c915a3735f` |
| Local round-8 candidate | 0.4.0 | 43 / 34 | `a2fb5d29889010c2c0c8d0da3783be052667d6c295ffac72039ac99045655252` |
| Public old bootstrap | 0.3.0 | 46 / 37 | `b1cba7db515776d86d1d2e06b627e30df7c5a6ecaa9e52a7330e43726b1e8b29` |

The public 0.4.0 hash also matches the existing historical release receipt.
Public and candidate version strings are identical, but their package bytes
are distinct; no conclusion relies on version alone.

Each v2 `_npx/.../node_modules/@ch4570/bandit` package has exactly its archive's
file set and bytes, plus exactly the required containing directories: no extra
package files, empty directories or linked members. Counts are 43/43/46 files
and 22/22/26 directories for public/candidate/old respectively, excluding each
package root itself. Attempt 1's public cache likewise matches all 43 public
files with no extra regular files or linked members. Successful JSON reports
point to these audited cache source roots and the intended scratch projects.

All three inspected manifests have the expected package/bin identity, no runtime
dependencies, and none of the installation/preparation lifecycle hooks checked
by the harness. They were inspected before the install commands; hooks were
not disabled to conceal package behavior.

Downloaded public binaries remain in the scratch directories, with identical
copies verified under ignored `dist/overnight-round9/public-sources/`. The
candidate remains the unchanged round-8 tarball. These binary archives are
**not included in the source-evidence attempt directories**: those records retain
URLs, member inventories and hashes, not self-contained binary downloads.

## Attempt 1 — completed public work and failed candidate launch

The [public command](attempt1/logs/02-public-install.json) is the exact documented
`npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz`
form, executed from the synthetic Korean/space-containing project path.
It exits 0 and installs the five intended skills. The actual tree contains
exactly 34 archive-matching payloads, five correct ownership markers and the
preserved project note: 40 files and 20 directories.

The [repeat](attempt1/logs/03-public-repeat.json) exits 0 and reports
`unchanged`, 34 unchanged payload files, no changes and `marker_change: false`.
The installed snapshot, repeat-before snapshot, repeat-after snapshot and actual
current project inventory agree, including recorded inode/mode/mtime values.

The [candidate preview command](attempt1/logs/04-candidate-preview.json) exits
126 with empty stdout and `/bin/sh` reporting permission denied on the archive
pathname. The logs and absence of a candidate cache package are consistent with
an archive-path execution attempt, not a BANDIT installer run. The candidate
project still exactly matches its before snapshot and contains no `.agents`.
There are no migration projects or success result in this attempt. No permissions
were changed or installer assertions relaxed to make that command pass.

## Attempt 2 — exact installed inventories and preservation

The [runtime record](attempt2/logs/01-runtime.json) shows Node 22.23.2 and npm
11.19.0. Twelve child-command records are terminal: eleven exit 0 and the
expected customization refusal exits 2. All have closed stdin and null
signal/launch-error fields; no timeout recovery is claimed.

The auditor checked complete actual file **and directory** sets, not only that
expected payload files exist. Counts exclude the project root itself:

| Fixture | Files / directories | Observed content and result |
| --- | ---: | --- |
| [Public install](attempt2/logs/02-public-install.json) and [repeat](attempt2/logs/03-public-repeat.json) | 40 / 20 | 34 public payloads, five markers, project note; repeat unchanged |
| [Candidate install](attempt2/logs/05-candidate-install.json) and [repeat](attempt2/logs/06-candidate-repeat.json) | 40 / 20 | 34 candidate payloads, five markers, project note; repeat unchanged |
| [Clean migration](attempt2/logs/09-migration-install.json) and [repeat](attempt2/logs/10-migration-repeat.json) | 42 / 22 | Candidate tree plus two explicit notes and the retained unrelated empty directory; updated, then unchanged |
| [Customized retirement refusal](attempt2/logs/12-migration-conflict.json) | 44 / 24 | Six old skills, 37 old payload paths, six old markers and project note; only the preexisting appended customization differs from old payload bytes |

Every current active marker equals `{format: 1, name, version: "0.4.0", files}`,
where `files` is exactly that skill's relative-path/SHA-256 payload map. All
payload bytes match the correct archive, including binary assets. The markers
do not claim themselves or added notes as managed files. No extra locks, staging
files, project package configuration, lockfile or `node_modules` appears.

The [candidate preview snapshots](attempt2/snapshots/candidate-preview-before.json)
and their after counterpart are identical. The
[migration preview snapshots](attempt2/snapshots/migration-preview-before.json)
and their after counterpart are also identical. Each repeat's before/after
inventory agrees with the current scratch tree, including bytes, modes, inodes
and nanosecond mtimes.

Authentic 0.3 bootstrap is recorded in
[the clean install](attempt2/logs/07-old-clean-install.json) and
[the customized install](attempt2/logs/11-old-customized-install.json), both
using the public pinned URL. All 37 old payload hashes in the clean migration's
before snapshot match the downloaded old archive. Its six marker hashes match
the still-preserved marker bytes in the customized fixture; those parsed markers
have version 0.3.0 and exactly the old archive's ownership maps.

After clean migration, **every** formerly managed file under `bandit-decide`
and `bandit-update` is absent, not just their entrypoints. Both ownership markers
are gone. `bandit-update` is removed; `bandit-decide` contains only its explicit
`local-note.md` and `unrelated-empty/`. The active research note and project
note retain their exact bytes. Five current skill folders have candidate data.

The conflict fixture appends a documented synthetic customization to the old
`bandit-update/SKILL.md` before invoking the candidate. The refusal names that
retired skill, and the complete [before](attempt2/snapshots/conflict-before.json),
[after](attempt2/snapshots/conflict-after.json) and current inventories agree
for all 68 recorded descendant paths, including content hashes, sizes, types,
modes, inodes and mtimes. The customized bytes and all six old markers remain;
`bandit-scope` is absent. This is ordinary preexisting-conflict handling, not
concurrent fault injection.

## Scope limits

The child environment is explicitly constructed with scratch caches, empty
user/global npm config files, scratch temporary storage and a four-tool PATH.
The checked bin links supply Node, npm, npx and sh; the runtime probe finds no
Git, `python` or `python3` on that PATH. HOME and CODEX_HOME are not overridden,
no global/personal destination is requested, and stdin is closed. These facts
do not amount to a syscall audit of all host accesses or proof that arbitrary
absolute-path executables could never be reached.

Snapshot equality covers all recorded descendants, not the project root's own
stat record, atime, ctime or unrecorded host state. Exact inventory checks apply
to the project trees and installed cache-package directories, not npm's separate
cache/log bookkeeping. A successful normal install does not establish arbitrary
concurrency safety, Windows/Linux behavior, host named-skill discovery, or
future network availability. No API metadata request, planning TASK, product
code change or publication is part of this audit.
