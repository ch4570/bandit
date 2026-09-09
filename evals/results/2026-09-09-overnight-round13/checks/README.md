# Round 13 engineering verification

The [gate runner](run-checks.py) and [complete receipt](results.json) retain
14 command outcomes, UTC times, all stdout/stderr streams and before/after
hashes. All commands exit 0 on Node 22.23.2/npm 11.19.0 and Python 3.11.16.
They execute sequentially with closed stdin, npm offline, Python bytecode
writes disabled and the inherited `npm_config_call` removed.

| Check | Observed result |
| --- | --- |
| `node scripts/sync-skills.mjs --check` | 16 synchronized resources verified |
| `npm run validate` | Five skills, 34 skill files pass |
| `npm test` | 79 tests pass; no failures, skips, cancellations or todos |
| `python3 scripts/validate.py` | Five skills, 34 files pass |
| `python3 -m unittest discover -s tests -v` | 99 tests pass |
| Official metadata validator, each of five skill folders | All five pass |

The 40 monitored skill, installer, CLI, runner, archiver and runner-test files
stay unchanged during the gates. Existing suites create their normal temporary
fixtures and archive/package checks. Free bytes before/after each command are
recorded, not a peak-storage measurement. No tests or product source change in
this round; these checks are not the two native planning executions or their
semantic assessment.

The [separate npm pack](npm-pack.json) exits 0. The 43-file archive is
2,677,718 bytes with SHA-256
`7f8592028d1b2f350dd304526e57a550c4b133a0f93d5b971d2a133d67bb5f84`,
byte-identical to round 12. Its installation payload does not contain the
development cases, examples or evaluation records added here.

Final source ZIP and exact rebuild/inventory verification are recorded under
ignored `dist/overnight-round13/CHECKPOINT.json` after documentation is frozen.
Earlier same-version artifacts are not overwritten. This checkpoint preserves
earlier result files and historical PM Craft hashes; no network installation,
host discovery, new CI, commit or publication is claimed by these local gates.
