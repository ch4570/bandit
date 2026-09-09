# Round 14 engineering verification

The [gate runner](run-checks.py) and [complete receipt](results.json) record
14 commands, UTC times, stdout/stderr and before/after source hashes.
All exit 0 on Node 22.23.2/npm 11.19.0 and Python 3.11.16. Commands run
sequentially with closed stdin, npm offline, Python bytecode writes disabled
and inherited `npm_config_call` removed.

| Check | Observed result |
| --- | --- |
| `node scripts/sync-skills.mjs --check` | 16 synchronized resources verified |
| `npm run validate` | Five skills, 34 skill files pass |
| `npm test` | 79 pass; no failures, skips, cancellations or todos |
| `python3 scripts/validate.py` | Five skills, 34 files pass |
| `python3 -m unittest discover -s tests -v` | 99 pass |
| Official metadata validator, each skill folder | All five pass |

All 40 monitored product/tooling files stay unchanged during these gates.
The suites create their normal temporary fixtures. Recorded available space
at command boundaries is not peak-storage measurement. No source or test
implementation changes in this round.

The [separate npm pack](npm-pack.json) exits 0 and produces 43 files,
2,677,718 bytes, SHA-256
`7f8592028d1b2f350dd304526e57a550c4b133a0f93d5b971d2a133d67bb5f84`.
It is byte-identical to the round-13 candidate exercised by the
[six-fixture offline integration](integration-audit.md). Root independently
compares all 44 mirrored integration files with scratch originals, all 45
frozen source hashes, both source archives and all 19 command outcomes.
These reads do not rerun installation or change its evidence.

Final ZIP creation and exact rebuild/inventory verification are recorded in
ignored `dist/overnight-round14/CHECKPOINT.json`, after documentation is frozen.
The verifier checks all current payloads, safe regular archive paths, checksum
sidecars, linked-document inclusion and preservation of the previous result,
raw/rubric/sequence, example, skill and historical evidence files. Earlier
same-version archives remain untouched.

These local gates are not semantic grades, public-release availability,
host-discovery proof, new CI, a commit or publication. There are no new native
planning executions in round 14.
