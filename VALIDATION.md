# BANDIT validation record

Distribution checks and planning behavior are reported separately. Product
fixtures are synthetic. npm registry publication is deferred.

## Published BANDIT 0.2.0 — 2026-09-07

- [Release commit CI](https://github.com/ch4570/bandit/actions/runs/34133194874):
  **all ten jobs passed**. This includes Node 22/24 on Linux, macOS, and Windows,
  plus four optional Python helper jobs. An earlier Windows Python fixture
  compared LF text to CRLF source bytes; the test now checks archive bytes
  against the actual source file. The packager was unchanged by that correction.
- [Release packaging](https://github.com/ch4570/bandit/actions/runs/34133289107):
  **passed**, publishing GitHub assets for tag `v0.2.0` at commit
  `9a777251c8fde01cd3d99621898e0eff9d6120ac`. No npm registry publication ran.
- Downloaded all three release archives and verified their SHA-256 checksums.
  `bandit.tgz` and `ch4570-bandit-0.2.0.tgz` are byte-identical.
- [Public tarball installation receipt](evals/results/2026-09-07-bandit/public-install.json):
  the exact README `npx --yes` command passed with a fresh npm cache and only
  Node/npm/npx/sh on PATH, with neither Git nor Python available. It installed
  all ten skill files into a Korean/spaced project path, preserved existing
  project files, repeated without changes, and installed globally into an
  isolated CODEX_HOME. The real user's global skill directory was not used.
- [Optional Git shorthand receipt](evals/results/2026-09-07-bandit/github-install.json):
  `npx --yes github:ch4570/bandit` also passed with an explicit temporary project
  destination and fresh npm cache/config. Existing project files were preserved.

## BANDIT 0.2.0 — local checks, 2026-09-07

- Native Node installer, package, and validator suite: **30 passed** on macOS
  arm64 (Node 26.8.1, npm 11.19.0). The 20 installer tests also passed on Node 22.
- Node-only skill/package validation: **passed**, ten complete skill files,
  including the avatar and referenced resources.
- Optional Python helper/source ZIP suite: **40 passed**, Python 3.11 and 3.12.
  Python is not needed by npm consumers.
- OpenAI skill-creator validation: **passed** in an isolated development
  environment. Its PyYAML dependency is not part of the npm package.
- The npm artifact was packed and consumed outside the checkout. Its install
  did not create a skill through lifecycle hooks; the explicit CLI installed
  the complete skill and preserved the consumer's project files.
- The source ZIP was extracted outside the checkout and its Node CLI installed
  all ten skill files with an empty PATH, using an explicit Node executable.
- The final hero and avatar were visually inspected. The avatar uses an opaque
  parchment background. [Image prompts](docs/assets/IMAGE-PROMPTS.md) record the
  built-in image generation and background correction.

## Independent install review

A reviewer who did not write the Node installer used the README-style
`npx --yes <HTTP tarball URL>` command against a temporary HTTP server. The
review exercised Korean/spaced paths, preview without writes, custom CODEX_HOME,
conflict errors, and preservation of an existing package.json, package lock,
unrelated skill, and planning document.
The [review record](evals/results/2026-09-07-bandit/install-review.json) retains
the observed failures and successful versioned-URL update.

That review found a real update problem: npm reused a cached package when the
same mutable download URL served a new version. Adding `--prefer-online` did
not repair it in the tested npm version. Changing to a new versioned URL
successfully updated the same installation with the same npm cache.

The public installation command therefore uses a versioned GitHub release URL.
To update, copy the new release's command. We do not describe rerunning a
`releases/latest` alias as a reliable updater. This keeps first installation and
upgrades as one command without adding a self-update service or registry dependency.

## Current planning check

A [fresh BANDIT task](evals/results/2026-09-07-bandit/README.md) completed after
the rename and persona change. It stayed concise, recommended a provisional
segment and experiment, distinguished interest from paid demand, and produced
ordinary planning language. This single check is not a comparative quality claim.

## Reproduce

Node.js 22+ and npm:

```sh
npm run validate
npm test
npm pack
```

Optional Python 3.11+ source tooling:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build_bundle.py
```

[CI](.github/workflows/ci.yml) defines Node 22/24 jobs on Linux, macOS, and
Windows, plus checks for the optional Python tools. The [release workflow](.github/workflows/release.yml)
attaches npm tarballs, a source ZIP, and checksums to GitHub. It has no npm
registry publishing step.

## Historical PM Craft 0.1.0 results

The original [11 planning runs](evals/results/2026-09-07/README.md) and their
hashes retain the PM Craft name. In the three paired cases, all three arms had
11 pass and 1 partial judgments. PM Craft used more reported input tokens.
These are not newly measured BANDIT results.

The [original validation record](https://github.com/ch4570/bandit/blob/v0.1.0/VALIDATION.md)
contains the earlier 38-test Python suite and six successful CI combinations.

## Limits

Temporary install tests do not establish compatibility with every host or
filesystem. Planning quality depends on the model, context, and available tools.
No real customer research, public experiment, or production app was validated.
Rebranding and easier installation do not establish superior PM output.
