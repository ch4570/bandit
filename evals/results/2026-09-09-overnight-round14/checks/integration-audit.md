# Final-candidate offline npx integration

The first attempt passed all six planned fixtures on **Node 22.23.2 / npm
11.19.0, macOS arm64**. There were 19 terminal command records: 17 exit 0 and
two expected customization refusals exit 2. Every command has empty stderr,
null signal and null launch error. No unexpected failure, harness correction,
retry, product edit, full-suite run or package build was part of this task.

## Exact artifacts and invocation

The [before-run freeze](before-run.json) was written before the harness. It
records both archive hashes and 45 relevant source-file hashes. All 43 current
candidate package members matched their source files before execution; all
45 frozen source files and both archives remained unchanged afterward.

| Local archive | SHA-256 |
| --- | --- |
| `dist/overnight-round13/ch4570-bandit-0.4.0.tgz` | `7f8592028d1b2f350dd304526e57a550c4b133a0f93d5b971d2a133d67bb5f84` |
| `dist/overnight-round9/public-sources/public-0.3.0.tgz` | `b1cba7db515776d86d1d2e06b627e30df7c5a6ecaa9e52a7330e43726b1e8b29` |

The old archive is the previously retained public-release download identified
in [round 9's source receipt](../../2026-09-09-overnight-round9/attempt2/sources.json).
It was not downloaded again. Both manifests were inspected before npx:
expected package/bin identity, no runtime dependencies, and no checked
installation/preparation lifecycle hooks.

The [one-off harness](offline-npx-flow.mjs) uses the explicit local-package
form documented in CONTRIBUTING, adding offline mode:

```text
npx --yes --offline --cache=/fresh/scratch/cache --package=/absolute/local.tgz -- bandit ...
```

The command environment is constructed explicitly, with empty user/global npm
configuration files, two fresh scratch caches, scratch temporary storage and
only Node/npm/npx/sh on PATH. HOME and CODEX_HOME are not supplied or repointed;
no credentials are passed. Stdin is closed. The runtime check confirms Git,
Python and Python 3 are absent from that PATH. `--offline` and
`npm_config_offline=true` apply to every npx invocation. No web/API tool or
download call was made.

## Observed project results

Counts include every project file and directory, including the project root:

| Fixture | Files / directories | Observed result |
| --- | ---: | --- |
| Default, Korean/space-containing path | 40 / 21 | JSON preview unchanged; installation succeeds; repeat reports unchanged |
| Custom `pm-craft` core | 40 / 20 | JSON install and post-install preview, plus normal text repeat: no false legacy warning |
| Custom `PM-Craft` core | 40 / 20 | Same successful checks; lowercase lookup resolves to the same device/inode on this filesystem |
| `core-planner` beside genuine `pm-craft` | 41 / 21 | Preview/install retain the warning; legacy sentinel tree remains unchanged |
| Clean authentic 0.3 migration | 42 / 23 | Preview unchanged; migration reports both retired skills; repeat unchanged |
| Customized retired skill | 44 / 25 | Preview and installation both refuse with exit 2; complete tree remains unchanged |

Every successful candidate installation has 34 archive-matching skill payloads
and five markers exactly equal to `{format: 1, name, version: "0.4.0", files}`,
where `files` contains only that skill's managed payload hashes. Custom core
markers still name `bandit`. Project notes are preserved. Complete path/type
sets exclude unexpected locks, staging files, package configuration, lockfiles
and project `node_modules`.

Clean migration removes all old managed files and markers in both retired
skills, not merely their entrypoints. The unrelated retired note/empty
directory and active-skill note remain; `bandit-update` disappears entirely.
For the conflict fixture, authentic old payloads and all six markers were
checked before one explicit synthetic append to `bandit-update/SKILL.md`.
Both [preview refusal](attempt1/logs/18-conflict-plan.json) and
[installation refusal](attempt1/logs/19-conflict-install.json) preserve all
69 recorded paths, including the project root, byte hashes, types, modes,
device/inode, nanosecond mtime and ctime. No partial upgrade appears.

## Retention and independent readback

Scratch originals remain at `/TEMP/bandit-round14-lSJnNY` (31,360 KiB
allocated at inspection). All **44 mirrored evidence files**—19 command logs,
23 snapshots, sources and result—were compared byte-for-byte with their scratch
originals. The [source record](attempt1/sources.json) and
[result](attempt1/result.json) identify the paths and exact inventory counts.
Separate readback corroborated current project snapshots, complete installed
payload/marker/path sets, and both complete cache-package trees: 43 candidate
files/23 directories and 46 old files/27 directories, including package roots.
The single compressed content blob in each cache also matches its archive hash.

| Evidence | SHA-256 |
| --- | --- |
| Before-run freeze | `3597b863c473d39e3f80b395a6999f9f8f17d451190506eaaec58c56e47feccf` |
| Harness | `1e2a5e332a4b5a76173f530857de1645fe8f522bbe953a49a961ea346ee1bb97` |
| Sources | `c9836809e6f6f869df2f4a182a8ab05cdedda4a26206755d222f1e92ac082797` |
| Result | `6169e65786485f50cc8446bef9adc2e45cd059b624b310efb042cda16221268f` |

The binaries remain in ignored `dist/` and scratch caches; they are not copied
into this source-evidence attempt directory. No evidence or scratch was deleted.
Free space was monitored at each child boundary; the minimum recorded there
was 350,126,080 bytes. Later volume fluctuations are not attributed solely to
this task.

These are offline local-tarball checks, not a new public-release download,
publication, Windows/Linux result, native skill-discovery check, or PM-quality
measurement. Explicit npm offline/config/PATH settings are not a syscall or
network-sandbox audit. Inventory comparisons do not cover atime, xattrs or
arbitrary concurrent host changes. Other final gates and final packaging are
separate evidence.
