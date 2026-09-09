# Custom core destination warning: before and after

The retained [before-fix receipt](legacy-note-before.md) demonstrates a misleading Node CLI warning: an allowed custom general-skill destination named `pm-craft` was reported as a separate installation that BANDIT had left untouched and that the user could remove. Installation itself succeeded. The same issue appeared for `PM-Craft` on the local case-insensitive filesystem.

## Narrow change

The [exact source diff](legacy-note-source-change.txt) changes only the legacy-warning condition and its comment/block, relative to the retained [before source](installer-before.mjs). The `.txt` copy has the original `.patch` bytes and is included by the source-ZIP builder; the original diff remains untouched locally. The note now requires the legacy path and reported general-skill destination to have different canonical spellings. Here `canonical` is the existing Unicode/case-normalization helper, not a filesystem identity lookup. This matches the existing `checkPath` rule that rejects differently spelled canonical aliases as ambiguous before installation succeeds.

No ownership marker, payload-writing, migration, lock, rollback, or Python behavior was changed for this fix. The genuine separate-PM-Craft note remains available. One new regression test was added before the product fix; the existing genuine-sibling positive control remained unchanged.

## Retained observations

| Check | Before | After |
| --- | --- | --- |
| Direct CLI, fresh scratch: 12 commands | All exit 0; false warning on each custom core's install/repeat/post-preview/text repeat | All exit 0; no custom-core warning at any stage |
| Exact `pm-craft` and mixed-case `PM-Craft` JSON preview before install | No files created | No files created |
| Installed marker and repeat/preview inventories | Core marker names `bandit`; inventories unchanged | Core marker names `bandit`; inventories unchanged |
| Genuine `core-planner` plus separate `pm-craft` sentinel | Warning retained; sentinel unchanged | Warning retained; sentinel unchanged |
| Identical targeted Node test command | 2 selected: 1 pass, 1 fail; exit 1 | 2 selected: 2 pass, 0 fail; exit 0 |

Both targeted runs had 0 skipped/cancelled/TODO tests. The full suite is separate evidence and is not included in these counts.

The before and after direct runs used Node **v22.23.2**, macOS arm64, the absolute local Node executable, the repository CLI, explicit fresh scratch destinations, closed stdin, and no shell. They performed no network access, personal skill installation, fault injection, or scratch cleanup. Before-fix files were preserved; after-fix streams use separate `after-*` names.

Evidence:

- Direct CLI: [before harness](legacy-note-before.mjs), [before raw results and stream references](legacy-note-before-results.json); [after harness with explicit no-warning assertions](legacy-note-after.mjs), [after raw results and stream references](legacy-note-after-results.json).
- Frozen targeted test: [before command/status/hashes](legacy-note-targeted-before-results.json), [failure stdout](legacy-note-targeted-before.stdout.txt); [after command/status/hashes](legacy-note-targeted-after-results.json), [passing stdout](legacy-note-targeted-after.stdout.txt), [after stderr](legacy-note-targeted-after.stderr.txt), [after harness](legacy-note-targeted-after.mjs).
- After scratch: `/TEMP/SYSTEM/bandit-round11-legacy-after-YX8PKM`.

## Hashes and limits

| Artifact | SHA-256 |
| --- | --- |
| Installer before | `6c2555e1c09d3efa416ae63ab7870143271bfed7f035f91287d01580ff2456ec` |
| Installer after | `9fc6f906b9dc563a66d55662fe4bdb6b0be37b7108e996d1a443cd6ace39bfd6` |
| Test file, unchanged across both targeted runs | `4a2259d68f57107f270efec164304115f226f98a127cc006878d2220cf2f4a46` |
| After direct CLI results | `ecd0eecd369960a2c713c36115a1431fdd9e9cbd136e89af5cf8655f7e89a285` |
| After targeted receipt | `f9f10cccf33295827a1d5953b9d3a6901102d718748abf5d20d0a2203072b100` |

The retained before receipt, before direct results, and failing stdout still match their originally recorded hashes. Both test receipts record identical source/test hashes at their respective start and finish; the test file stayed frozen between failure and success.

This is local installer-warning regression evidence, not a PM skill-quality result or evidence of broad installer correctness. It does not demonstrate Windows behavior, hostile-race safety, npx/package execution, or release readiness. Existing transaction limitations are unchanged. No further fault diagnostic, full suite, package build, or publication was performed for this bounded check.
