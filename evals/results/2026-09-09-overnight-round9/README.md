# Overnight development, round 9 — 2026-09-09

Fresh installation checks exercise the public GitHub command and the current
local candidate on Node 22.23.2/npm 11.19.0 in four synthetic macOS projects.
They add no planning TASKs: the cumulative overnight count stays **44**.
The five skills, installers, runner and public onboarding commands are unchanged.
The development guide now shows an explicit local-package check and warns
against identifying same-version candidate bytes by a version label alone.

## What actually ran

The public invocation is copied from [INSTALL.md](../../../INSTALL.md):

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz
```

Each project is newly created under a retained scratch directory, not a real
project or personal skill folder. The child environment has only Node/npm/npx/sh
on PATH, no Git or Python, closed stdin, empty npm configuration files and
initially empty package-identity caches. HOME and CODEX_HOME are not overridden.
Downloaded package manifests are checked for dependencies and lifecycle hooks
before execution; hooks are not disabled to hide side effects. No user project
package configuration, API key, cloned repository or Python runtime is supplied.

The [corrected run](attempt2/result.json) passes all four fixture checks:

| Fixture | Observed result |
| --- | --- |
| Published 0.4.0 in a Unicode/space-containing project path | Exact positional URL command installs five skills; repeat reports unchanged and preserves bytes/modes/inodes/mtimes. |
| Unreleased round-8 candidate | Explicit `--package` preview changes no project files; installation matches the candidate's 34 skill files and five markers; repeat is unchanged. |
| Authentic published 0.3.0, clean managed files | Preview is read-only; candidate upgrade retires old decide/update managed files and markers, preserves active/retired notes and an unrelated empty directory, and leaves five current skills. |
| Authentic 0.3.0 with a customized retired managed file | Candidate exits 2 with a JSON error; the entire project inventory is unchanged and no new scope folder appears. |

All fixtures preserve the original project note and create no project
`package.json`, lockfile or `node_modules`. The retired update directory, which
has no unrelated contents, disappears after the clean migration. The decide
directory retains its note and unrelated empty directory without an old
entrypoint or ownership marker. Only synthetic managed files were removed;
their original bytes remain recoverable from the retained 0.3 archive.

This is not the first public installation proof. The
[earlier public receipt](../2026-09-08-bandit-scope-specify/public-install.json)
already records the released path on Node 26.8.1. This round rechecks Node 22
and the distinct current candidate; it does not retroactively replace that record.

## The failed first harness is preserved

The [first execution](attempt1/failure.json) stops at its candidate preview.
The public install and repeat had succeeded, but a plain positional absolute
`.tgz` path was treated as an executable by npm 11.19.0 and exited 126. The
candidate installer did not run, and that project remained unchanged.
This was a test-command mistake, not an observed installer defect.

The [correction record](harness-correction.md) keeps the original source,
assertions, receipt and failure intact. A second harness changes only local
candidate argv to `npx --yes --package=/absolute/candidate.tgz -- bandit ...`,
the explicit package/command form described by the
[npm npx documentation](https://docs.npmjs.com/cli/v11/commands/npx/).
It runs from a new scratch root with fresh caches. Neither assertion weakening,
a permission change nor a product fix makes the original command pass.

## Package identity and independent audit

Published and candidate packages both identify as 0.4.0. The
[source record](attempt2/sources.json) distinguishes the actual archive bytes:

| Package | SHA-256 |
| --- | --- |
| Published 0.4.0 | `af5e83e5c45ab15956f1d7463ed9194ef1362f2ea68c6db9a7a967c915a3735f` |
| Round-8 candidate | `a2fb5d29889010c2c0c8d0da3783be052667d6c295ffac72039ac99045655252` |
| Published 0.3.0 bootstrap | `b1cba7db515776d86d1d2e06b627e30df7c5a6ecaa9e52a7330e43726b1e8b29` |

The [independent audit](integration-audit.md) compares exact file and directory
sets as well as hashes, not merely the harness's expected-file subset checks.
It verifies all 43/43/46 cached package files against downloaded/candidate
archives, exact active marker maps, removal of every retired managed payload,
and unchanged full preview/repeat/conflict inventories. It does not execute or
retry installs. The [first](before-run.json) and [second](v2-before-run.json)
pre-run receipts identify their immutable harnesses and candidate.

All retained command records and snapshots are copied byte-for-byte, as listed
in [archive provenance](archive-provenance.json). Original projects/caches stay
in their scratch roots; downloaded public binaries are also retained separately
under ignored `dist/overnight-round9/public-sources/`. They are not embedded in
this text evidence or the source ZIP. Hashes provide local consistency, not a
trusted execution attestation. No complete syscall or npm debug-log capture is
claimed. A browser-only GitHub API metadata request was blocked and not retried;
no API response is used as evidence. The exact release-archive tests were already
planned independently of that request.

## Engineering and limits

[Full checks](checks/README.md) remain separate from integration assertions and
planning grades. All 34 skill files and 1,030 previous result files remain
[byte-identical](checks/preservation.json) to the frozen round-8 ZIP; all 93
historical PM Craft files also match HEAD. Earlier failures/partials are not
rescored. No new CI, commit, release or npm registry publication occurs.

This is a bounded local macOS/Node-22 check, not Windows/Linux coverage, host
named-skill discovery, concurrency or crash-durability proof, planning-quality
measurement, or customer validation. No general reliability claim follows from
four successful fixture scenarios. The one-off harnesses are retained evidence,
not a new product runtime or an added end-user dependency.
