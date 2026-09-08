# Contributing

Start with a concrete product-planning failure or usability problem. A short example of the request, available evidence, actual output, and expected behavior is more useful than a proposal to add many new frameworks.

Read [the design](docs/design.md) and [evaluation guide](evals/README.md). BANDIT contains five specialist skills plus the general skill. Keep each entry point focused. Maintain shared references under `skills/bandit/`, then run `node scripts/sync-skills.mjs` to copy each specialist's needed resources. Edit the canonical references rather than their generated copies.

## Local development

Clone the repository and use Node.js 22+. The npm installer and its tests have no third-party dependencies; no dependency installation is required.

```sh
node scripts/sync-skills.mjs --check
npm run validate
npm test
```

For a packaging change, build and inspect the npm archive:

```sh
npm pack --pack-destination /path/to/temporary-directory
```

Keep generated archives out of source control. The repository also retains Python tooling for its manual-copy ZIP distribution; users of the npm installer do not need Python. Exercise installer changes against temporary directories, including a local modification conflict, rather than installing into an active agent environment to run a test.

## Make the change reviewable

- Describe the user task and the failure your change addresses.
- Keep existing accepted decisions and unrelated work intact.
- Include a small fictional reproduction when behavior changes. Do not publish customer material, credentials, or private workspace paths.
- Run checks relevant to the change and record the actual result. For skill instructions, also assess a realistic output when the change could affect decisions.
- Keep the [BANDIT identity](docs/brand.md) consistent without adding roleplay to real product documents.
- Update English and Korean user-facing guides when their instructions change. Translate meaning and product terminology, not sentence shape.
- Record release-facing changes in [CHANGELOG.md](CHANGELOG.md).

Structural validation proves package properties, not planning quality. A sample written to illustrate a rule is an example; a task executed with captured inputs and outputs is an evaluation. Keep those labels accurate. Avoid tests that only require an answer to repeat headings or phrases from the skill.

Use the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) to explain the final change and its evidence. A narrow documentation correction does not need a full model comparison.

## Sources and scope

Use primary sources for factual research and pin references when discussing a particular version. Explain the limits of what a source supports. Preserve license notices when incorporating substantial external material.

A specialist must be usable from its own installed folder with all references available. When changing packaging, check that a 0.2.0 installation can be upgraded to all six skills and that a conflict in any one destination leaves the other five untouched.

Propose major domain expansions in an issue first so maintainers can assess their fit. UI styling, implementation engines, personal task scheduling, and external account integrations are outside the current skill's core scope.
