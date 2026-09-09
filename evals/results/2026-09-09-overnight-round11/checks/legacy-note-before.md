# Custom core destination: retained before-fix evidence

This is a benign local CLI correctness regression, not PM behavior evidence or a fault-injection test. `INSTALL.md` permits a custom exact general-skill folder name except active or retired specialist names. In the retained [installer source](installer-before.mjs), lines 463–465 install the requested bundle and then warn whenever the parent contains a `pm-craft` directory, without checking whether that directory is the requested general skill itself.

## Direct CLI observation

The [one-shot reproduction](legacy-note-before.mjs) ran the absolute local Node executable and repository `bin/bandit.mjs` against fresh disposable fixtures. Runtime: Node **v22.23.2**, macOS arm64. All 12 commands terminated with exit 0 and empty stderr. Their exact argv, timestamps, stream-file names, returned reports, ownership marker, and path/type/byte-hash inventories are retained in [the raw result](legacy-note-before-results.json).

Both custom destinations, `pm-craft` and `PM-Craft`, were tested in separate parents:

| Step | Observed before the fix |
| --- | --- |
| JSON preview before installation | No legacy note; no files created |
| JSON installation | False separate-PM-Craft note |
| JSON repeat | Same false note; installed inventory unchanged |
| JSON preview after installation | Same false note; installed inventory unchanged |
| Normal text repeat | Same false note; installed inventory unchanged |

The note says that a separate PM Craft installation was left untouched and suggests manually removing it, even though the path is the general BANDIT skill just installed. Both installed markers name `bandit`. On this filesystem the lowercase legacy path and mixed-case core path resolve to the same directory. The defect is misleading guidance; these runs did not show an installation failure or deleted payload.

The independent positive control used `core-planner` beside a genuine pre-existing `pm-craft/SKILL.md` synthetic sentinel. Preview and installation correctly reported the separate folder; its path/type/content inventory stayed identical.

The CLI fixture is retained at `/TEMP/SYSTEM/bandit-round11-legacy-before-HX1Kre`. Commands used explicit scratch destinations and closed stdin, without shell execution, network access, host skill installation, fault injection, or scratch deletion. The repository was only read by the CLI.

## Regression frozen before product changes

One new [regression test](../../../../tests-node/install.test.mjs) at line 215 covers both custom names through all five steps, with marker identity and repeat/preview inventory checks. The existing separate-PM-Craft positive test at line 204 remains unchanged.

The [targeted runner](legacy-note-targeted-before.mjs) executed:

```text
/Users/DEVELOPER/.npm/_npx/52027bd8fc0022aa/node_modules/node/bin/node --test '--test-name-pattern=PM Craft' tests-node/install.test.mjs
```

Result: **2 selected tests, 1 pass, 1 fail, 0 skipped; exit 1**. The genuine-sibling control passed. The new test failed at its aggregate note assertion, showing all eight incorrect warnings across the two custom names. See [unaltered stdout](legacy-note-targeted-before.stdout.txt), [stderr](legacy-note-targeted-before.stderr.txt), and [command/status/hash receipt](legacy-note-targeted-before-results.json). This targeted run is not the full installer suite.

The source and test hashes were equal before and after the failing run. Product edits were authorized only after it terminated; this receipt and raw before-fix files must remain unchanged.

| Artifact | SHA-256 |
| --- | --- |
| `installer-before.mjs` and installer used by both runs | `6c2555e1c09d3efa416ae63ab7870143271bfed7f035f91287d01580ff2456ec` |
| Frozen `tests-node/install.test.mjs` | `4a2259d68f57107f270efec164304115f226f98a127cc006878d2220cf2f4a46` |
| `legacy-note-before-results.json` | `4f6a8c35aa2378279dfc7cb166d0163712d4fb582ce9bc3c45cb97a5182ee3c5` |
| `legacy-note-targeted-before.stdout.txt` | `a4a47401f077044c734352e8a0601f8e3bea1cfc97c543a278c3e141bf8e66c8` |

This establishes the local warning mismatch and a focused failing regression. It does not establish Windows behavior, general race safety, new release readiness, or any skill-quality improvement. Python has no corresponding legacy-warning branch and was not changed or tested for this issue.
