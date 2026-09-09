# Round-10 local verification checks

All 14 recorded commands completed with exit 0. These are structural,
unit/package-test and metadata checks, separate from the fresh case-21 planning
outputs; they do not establish planning quality, demand or general reliability.

| Check | Observed result | Complete output |
| --- | --- | --- |
| Resource synchronization | 16 specialist resources verified | [stdout](sync.stdout.txt) |
| `npm run validate` | Five skills, 34 files, no errors | [stdout](node-validate.stdout.txt) |
| Full Node suite | 78 pass; zero failures, skips, cancellations or TODOs | [stdout](node-tests.stdout.txt) |
| Python repository validator | Five skills, 34 files, no errors | [stdout](python-validate.stdout.txt) |
| Full Python unittest suite | 92 pass; no failures or skips | [stderr](python-tests.stderr.txt) |
| Official metadata validator | All five skills valid | [bandit](metadata-bandit.stdout.txt), [research](metadata-bandit-research.stdout.txt), [scope](metadata-bandit-scope.stdout.txt), [specify](metadata-bandit-specify.stdout.txt), [review](metadata-bandit-review.stdout.txt) |

Runtime probes record Node **22.23.2**, npm **11.19.0**, and Python **3.11.16**
for both the optional tooling and existing development-only validator environment.
The cached Node-22 executable is used directly, including for the npm CLI;
its binary directory is prepended to child PATH so npm's scripts use that Node.
Inherited `npm_config_call` is removed. No new Node download or integration
installation was requested.

[results.json](results.json) retains every exact argv, working directory, UTC
start/finish time, exit status, launch-error field, and separate stdout/stderr
filename and SHA-256. All 28 output-file hashes were independently checked
against that receipt. Node-test stderr is empty; Python unittest reports on
stderr and has empty stdout. Empty stream files are retained rather than omitted.
The receipt SHA-256 is
`fdd8f5477ad20ef275d1f151f20cf9d8a5bfa0f573bbaccf30d0580b7dd9d6d0`.

The [one-off runner](run-checks.py) executed the following command families from
the repository root, using the absolute interpreters recorded in the receipt:

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

The runner buffers output until checks finish, then writes exclusive new log
files. Its recorded before/after hashes agree for all 34 skill files plus
`lib/installer.mjs`, `bin/bandit.mjs`, and `install.py`: no retained product-byte
change was observed. Official quick validation uses the existing temporary
development environment, not a new user installation dependency.

No new fault diagnostic, network integration, planning TASK, or standalone
release `npm pack`/source-ZIP build was run for this verification. The existing
full suites exercise their own temporary package/archive fixtures; those are
not final round-10 distribution artifacts. Final packaging remains a separate
step after the evidence and documentation are complete. No new CI or
cross-platform result is claimed.
