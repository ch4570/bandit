# Product journey development cases — frozen criteria

These criteria were authored on 2026-09-10 independently of product skill instructions, prior task outputs, and prior grades. The author read the repository evaluation method and wrote new synthetic fixtures. No product trial was run by the author.

The raw inputs are only the files under:

- `evals/cases/12-launch-handoff/`
- `evals/cases/13-offer-consistency-review/`

Do not copy this directory, its checklist, the QA plan, or any expected findings into an executing agent's project, prompt, or conversation. Nothing in the raw fixtures refers to the criteria. Case 12 exercises connected planning with the general skill; case 13 is a bounded review suitable for the review specialist. The evaluation owner selects the compared conditions without changing the raw task.

## Grading

Evaluate saved outputs by meaning. Headings, terminology, prose order, exact proposed prices, and the reviewer's preferred solution are not requirements. Accept a different recommendation if it follows the supplied evidence, satisfies the requested work, and respects the explicit constraints. An observation and a proposed assumption must remain distinguishable.

For each criterion, record `pass`, `partial`, `fail`, or `unavailable`, with a short quotation or output location and a reason. A caveat elsewhere does not cancel a contradictory recommendation or customer-facing promise. Formatting alone is never a failure.

- A case passes when every P0 criterion passes. P1 criteria are diagnostic improvements and do not independently fail the case.
- A partial P0 is a case failure, with the actual useful work still reported. Do not hide an incomplete subtask behind a high average score.
- Missing/truncated/unreadable output is unavailable where assessment cannot be made; do not fabricate a result.
- Keep execution success, workspace integrity, and semantic quality separate. Bind the grade to the output SHA-256 and to the frozen fixture/criteria manifest.

`freeze.json` records the exact raw inputs and criteria before the first product run. Later corrections require a new criteria version and explicit disclosure; preserve earlier outputs and grades under the version used at the time. Do not silently change a failing criterion after seeing results.

These are two development cases, not a representative benchmark of product management, research quality, conversion, revenue, or customer outcomes. Fixture observations remain fictional. Passing does not establish business validation or superiority over another tool.

## Design artifact

`test-design.md` and `test-design.qa-plan.json` document requirement/risk traceability and the static output checks. The QA contract validator checks the JSON's shape and links, not the quality of a product answer. There is no browser, API, or customer experiment to execute in this design; the existing local evaluation owner runs fresh task sessions separately.
