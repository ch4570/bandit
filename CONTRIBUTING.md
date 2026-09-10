# Contributing

Start with a concrete product-planning failure or usability problem. A short example of the request, available evidence, actual output, and expected behavior is more useful than a proposal to add many new frameworks.

Read [the design](docs/design.md) and [evaluation guide](evals/README.md). BANDIT contains four specialist skills plus the general skill. Keep each entry point focused. Maintain shared references under `skills/bandit/`, then run `node scripts/sync-skills.mjs` to copy each specialist's needed resources. Edit the canonical references rather than their generated copies.

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

## Issues, child branches, and pull requests

Use the [improvement proposal](.github/ISSUE_TEMPLATE/feature_request.yml) for a focused improvement or the [bug report](.github/ISSUE_TEMPLATE/bug_report.yml) for reproducible incorrect behavior. Both use the same fields as the [pull request template](.github/PULL_REQUEST_TEMPLATE.md): task and stage, observed gap and raw evidence, expected behavior and acceptance criteria, change and alternatives, validation and limits, and related issue and branches. Carry that evidence into the PR and update it to describe the final change. Untested proposals are welcome when clearly labeled; bug reporters do not need to diagnose a fix.

Create a child branch from the intended base before implementation: `feat/issue-<number>-<slug>` for improvements or `fix/issue-<number>-<slug>` for fixes. Use `main` as the base for independent work. For a dependent change, branch from its parent feature branch and name that parent as the PR base; record dependencies and merge order. Keep each branch focused on its issue and preserve unrelated work.

Every PR records its base and head branches and links its issue. Use `Closes #<number>` when the change resolves the issue, or `Refs #<number>` for partial work. GitHub closes linked issues when the closing PR merges into the default branch; for dependent PRs, retain the issue link in the final PR to `main`. A small documentation correction can use a concise PR without a separate proposal.

## Make the change reviewable

- Describe the user task and the failure your change addresses.
- Keep existing accepted decisions and unrelated work intact.
- Include a small fictional reproduction when behavior changes. Do not publish customer material, credentials, or private workspace paths.
- Run checks relevant to the change and record the actual result. Follow the skill-quality checks below when instructions could affect decisions.
- Keep the [BANDIT identity](docs/brand.md) consistent without adding roleplay to real product documents.
- Update English and Korean user-facing guides when their instructions change. Translate meaning and product terminology, not sentence shape.
- Record release-facing changes in [CHANGELOG.md](CHANGELOG.md).

Structural validation proves package properties, not planning quality. A sample written to illustrate a rule is an example; a task executed with captured inputs and outputs is an evaluation. Keep those labels accurate. Avoid tests that only require an answer to repeat headings or phrases from the skill.

Use the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) to explain the final change and its evidence. A narrow documentation correction does not need a full model comparison.

## Repeat skill-quality checks

Run a fresh realistic trial for each affected skill whenever its behavior changes, and repeat representative skill trials before a release. Cover the affected stages explicitly: research, product planning, marketing planning, design handoff, and business-model planning. For release review, record which of these stages were exercised and which remain untested. These are planning and handoff checks; they do not demonstrate live customer demand, marketing performance, visual implementation quality, or business viability.

Use the [evaluation guide](evals/README.md#forward-test-method). An independent executing agent receives only the user request, raw fictional fixtures, and the skill with its references, in a fresh task. Keep expected results, assessment criteria, author diagnoses, and previous outputs outside that agent's context. Assess the saved output separately against observable meaning. A familiar case can check a regression; add an independently authored fresh case when assessing whether an improvement transfers to a new task.

Record the tested release or commit, skill command, host/model when known, inputs, actual outputs, assessment criteria, results, and limitations. Preserve every failed attempt and the criteria used for it. Disclose failures before revising criteria; keep revised criteria and reruns separate so they cannot erase earlier results. Link the evidence from the issue and PR. A passing process or package check is not a passing skill-quality assessment, and an example is not an executed trial.

These trials are contributor-run checks. The current CI and release workflows run structural, installer, and packaging checks; they do not schedule model evaluations. Before shipping, run all checks listed in [AGENTS.md](AGENTS.md), include the fresh skill-trial evidence in release review, and disclose missing coverage. Do not claim continuous or scheduled quality monitoring from these manual runs.

## Sources and scope

Use primary sources for factual research and pin references when discussing a particular version. Explain the limits of what a source supports. Preserve license notices when incorporating substantial external material.

A specialist must be usable from its own installed folder with all references available. Specification work covers both new plans and rewrites; assess substantial direction changes with a realistic existing PRD, not just a new-document prompt.

When changing packaging, check upgrades from both 0.2 and 0.3 to the current five skills. Retire only unchanged managed files from the old command set, preserve unrelated notes, and ensure a conflict in an active or retired skill leaves the entire installation untouched.

Propose major domain expansions in an issue first so maintainers can assess their fit. UI styling, implementation engines, personal task scheduling, and external account integrations are outside the current skill's core scope.
