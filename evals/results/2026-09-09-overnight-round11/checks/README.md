# Round-11 local verification checks

All 14 recorded commands completed with exit 0. These are local structural,
unit/package-test and metadata checks, not planning-quality or customer evidence.

| Check | Observed result | Complete output |
| --- | --- | --- |
| Resource synchronization | 16 specialist resources verified | [stdout](sync.stdout.txt) |
| `npm run validate` | Five skills, 34 files, no errors | [stdout](node-validate.stdout.txt) |
| Full Node suite | 79 pass; zero failures, skips, cancellations or TODOs | [stdout](node-tests.stdout.txt) |
| Python repository validator | Five skills, 34 files, no errors | [stdout](python-validate.stdout.txt) |
| Full Python unittest suite | 92 pass; no failures or skips | [stderr](python-tests.stderr.txt) |
| Official metadata validator | All five skills valid | [bandit](metadata-bandit.stdout.txt), [research](metadata-bandit-research.stdout.txt), [scope](metadata-bandit-scope.stdout.txt), [specify](metadata-bandit-specify.stdout.txt), [review](metadata-bandit-review.stdout.txt) |

The full Node output records both the existing genuine-PM-Craft-sibling check
and the new custom-`pm-craft`/case-alias destination regression as passing
tests 23 and 24. This is the observed 79-test suite, not a count inferred from
adding a test.

Runtime probes record Node **22.23.2**, npm **11.19.0**, and Python **3.11.16**
for both optional tooling and the existing development-only validator environment.
The cached Node-22 executable is used directly, including for the npm CLI;
its binary directory is prepended to child PATH. Inherited `npm_config_call`
is removed. This round's copy of the previous one-off runner additionally sets
`npm_config_offline=true`; update notices and Python bytecode writes are disabled.
No runtime download or dependency installation was requested by this harness.

The recorded checks ran from **2026-09-08T19:27:42.807401+00:00**
through **2026-09-08T19:27:57.949367+00:00**.
[results.json](results.json) retains each exact argv, working directory, UTC
start/finish time, exit status, launch-error field, and separate stdout/stderr
filename and SHA-256. All **28** stream hashes were independently recomputed.
Node-test stderr is empty; Python unittest reports on stderr and has empty
stdout. Empty streams are retained.

| Recorded item | SHA-256 |
| --- | --- |
| [Results receipt](results.json) | `3dd6a16c584373d1ec34094beae7d4e2c7cccaf99f33e5e92fd4b1fb0842110b` |
| [One-off runner](run-checks.py) | `22d154997b128e257ab1155a2a4e233a3b845c979d8702514db185203d1e93d9` |
| Tested `lib/installer.mjs` | `9fc6f906b9dc563a66d55662fe4bdb6b0be37b7108e996d1a443cd6ace39bfd6` |
| Tested `tests-node/install.test.mjs` | `4a2259d68f57107f270efec164304115f226f98a127cc006878d2220cf2f4a46` |
| Unchanged `install.py` | `29e2ae73652dbba226a8f60889e995d4e70f07eab514513430e5a5aa26d8fe45` |

The [runner](run-checks.py) uses these command families from the repository root,
with the exact absolute executables retained in the receipt:

```text
node --version
node npm-cli.js --version
python3.11 --version
validator-environment-python --version
node scripts/sync-skills.mjs --check
node npm-cli.js run validate
node npm-cli.js test
python3.11 scripts/validate.py
python3.11 -m unittest discover -s tests -v
validator-environment-python quick_validate.py skills/<each of the five skills>
```

Command output was buffered until all checks finished, then written to exclusive
new files. The recorded before/after maps agree for all **37** monitored files:
34 skill files plus `lib/installer.mjs`, `bin/bandit.mjs`, and `install.py`.
Their actual bytes were rechecked against the completed receipt. The 34-file skill
sorted-entry map digest remains
`471a85742d3858b5383ad9d51953f60cc755783af0e5b96495f7fe85c1cde7c7`.
This establishes unchanged monitored bytes during verification; it is not a
whole-repository freeze while other documentation work continues.

Official quick validation reuses the existing temporary development environment;
it does not add a user installation dependency. The full suites exercise their
own temporary package/archive fixtures. No standalone release `npm pack`,
source-ZIP build, new fault probe, network integration or planning TASK was run
for this verification. Final packaging is a separate step owned by the main
task after documentation is complete. No CI or cross-platform result is claimed.
