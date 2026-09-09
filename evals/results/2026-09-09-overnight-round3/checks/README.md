# Round 3 engineering checks

These check evaluation support and distribution, not planning quality. The
eleven model task results are reported separately in the parent directory.

## Reproduced runner defects

The [before/after regression record](eval-runner-regressions.md) preserves
failing mock checks before correction. The runner now distinguishes a probe
or launch failure from a child process's returned exit code and rejects
instruction-source/output overlap before copying. This is not a new
product-management runtime or a quality benchmark.

## Actual missing-executable integration

After the launch-error correction, a separate synthetic one-file fixture was
staged with the baseline arm. The command used Python 3.11.16 by absolute path
and a subprocess-only `PATH=/usr/bin:/bin`, where no `codex` executable exists.
No user configuration or global PATH was changed and no model task ran.

The invocation was `evals/run_local.py --case missing-executable --fixture-dir
<temporary-check-root>/raw --arm baseline --output-dir
<temporary-check-root>/runs`; web mode defaults to explicitly disabled.
The expected missing-executable error occurred during the version probe at
**2026-09-08 16:01:49 UTC** (2026-09-09 01:01:49 Asia/Seoul).

| Observed layer | Result |
| --- | --- |
| Runner CLI | Exit 2, `No such file or directory: 'codex'` |
| [Run metadata](missing-executable--baseline/metadata.json) | `runner_status: launch_failed`; version-probe `FileNotFoundError`; start/finish, elapsed and before/after hashes retained |
| Child task exit | `null`: no child result was invented |
| Model evidence | Empty events and stderr; no output artifact or model task |
| [Archive provenance](missing-executable--baseline/archive-provenance.json) | Archiver exits 0 with `run_status: launch-failed`, null source exit, complete original text and unchanged input |

This deliberately failed launch verifies the runner-to-archiver path. It is
not a twelfth planning run, a skill failure, or a successful model response.
The archive retains the synthetic request, prompt, metadata and empty logs.
Temporary paths are normalized; no missing output was manufactured.

## Environment and limits

After the final source-link correction, synchronization, Node/Python repository
validators, **73 Node tests** and **87 Python tests** pass. The five official
skill-creator metadata checks also pass using the existing temporary validator
environment; this adds no package or end-user dependency.

`npm pack` succeeds with 43 distributable files; source ZIP creation also
passes. A scratch ZIP was built before this final report and the final snapshot
is built separately under the new round directory. npm's normal package test
also checks extracted CLI consumption without the checkout. No release asset
or registry package is uploaded by these commands.

Use supported Python 3.11+ for these optional checks; the machine's system
Python 3.9.6 is below that requirement. The Node suite uses 22.23.2. As
documented in the [previous round](../../2026-09-09-overnight/checks/README.md),
the nested npm test command removes only inherited `npm_config_call`:

```sh
npx --yes --package=node@22 --call 'env -u npm_config_call npm test'
```

Existing earlier-round tarballs and source ZIPs are not overwritten. New
local artifacts use `dist/overnight-round3/`; they are not published release
receipts and do not change the public 0.4.0 install command.
