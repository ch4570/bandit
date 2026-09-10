## Task and stage

Name the user task, skill command, and relevant stage: research, product planning, marketing planning, design handoff, business-model planning, or installation.

## Observed gap and raw evidence

Identify the BANDIT release or commit tested. Link the request, raw fixtures, and actual output or logs supporting the problem; mark untested assumptions explicitly. A short before/after scenario is enough for a narrow documentation correction.

## Expected behavior and acceptance criteria

State the resulting behavior and how a reviewer can tell the change works.

## Change and alternatives

Explain the final change, its scope, and relevant alternatives or trade-offs. Mention affected decisions, references, installation behavior, or public instructions; keep English and Korean onboarding consistent. Include source and license notices where needed.

## Validation and limits

List checks actually run with their results and evidence links, then planned or omitted checks and remaining risks. Distinguish structural tests, installer checks, illustrative examples, and executed skill trials.

For skill behavior changes, link fresh independent trials using only the request, raw fixtures, and skill references. Preserve failed outputs and the criteria used to assess them; disclose failures before changing criteria. State the host/model when known and the limits of any quality or comparison claim. See [Contributing](https://github.com/ch4570/bandit/blob/main/CONTRIBUTING.md#repeat-skill-quality-checks).

## Related issue and branches

- Issue: `Closes #<number>` for completed work; `Refs #<number>` for partial work.
- Base branch: `main` or the parent feature branch.
- Head branch: `feat/issue-<number>-<slug>` or `fix/issue-<number>-<slug>`.
- Dependencies: related PRs and merge order, if any. GitHub closes linked issues when the closing PR merges into the default branch.
