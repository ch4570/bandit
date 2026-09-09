# Round 12 engineering verification

The [sequential gate runner](run-checks.py) executes 14 commands, with complete
[status, UTC timestamps and hashes](results.json) and separate stdout/stderr
files. All commands exit 0. Node 22.23.2/npm 11.19.0 and Python 3.11.16 are the
recorded local runtimes. npm is offline, stdin closed and Python bytecode
writes disabled. The inherited `npm_config_call` is removed for the npm test
subprocess. Commands run one at a time after the disk-space interruption.

| Check | Observed result |
| --- | --- |
| `node scripts/sync-skills.mjs --check` | 16 synchronized resources verified |
| `npm run validate` | Five skills, 34 skill files pass |
| `npm test` | 79 tests pass; no failures, skips, cancellations or todos |
| `python3 scripts/validate.py` | Five skills, 34 files pass |
| `python3 -m unittest discover -s tests -v` | 99 tests pass |
| Official metadata validator, each of five skill folders | All five pass |

The gate receipt freezes 40 files: the 34 skill files, both installer
implementations, Node CLI entrypoint, runner, archiver and runner tests. Their
bytes remain unchanged during the checks. This is not a freeze of every
documentation file. Unit suites create their normal temporary fixtures and
package/archive checks; these are not native Codex planning runs or network
installation evidence. Free bytes before/after each command are reported, not
a claim about peak storage consumption.

The [separate npm pack](npm-pack.json) also exits 0. Its 43-file archive is
2,677,718 bytes, SHA-256
`7f8592028d1b2f350dd304526e57a550c4b133a0f93d5b971d2a133d67bb5f84`,
identical to round 11. Final source ZIP and exact current-source/inventory
verification are recorded under ignored `dist/overnight-round12/CHECKPOINT.json`
after documentation is frozen; previous same-version artifacts are not replaced.

[Seven focused mock tests](model-tests-summary.md) retain their unsupported
feature baseline and passing after implementation separately. The
[first fake CLI attempt](model-cli-smoke-report.md) has two config-wording
assertion failures; the [second](model-cli-smoke-v2-report.md) checks the
documented request contract and passes all 52 checks. Their raw streams,
the [exact harness correction](model-cli-smoke-correction.md),
synthetic fake invocation captures, original run directories and normalized
archives remain separate. No such calls are included in the 46 cumulative
native planning executions or treated as quality grades.
