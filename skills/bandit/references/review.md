# Product plan review

Use this reference when the user requests critique, gap analysis, or a readiness assessment of product planning material.
Review the requested scope without changing the reviewed documents or product code.
Return findings in the conversation, or write a separate review artifact when requested.
A request to review is not a request to repair, implement, publish, or run an external experiment.

## Establish the review target

Identify the artifact, product version, and decision the review should inform.
Reuse context already supplied; do not turn a narrow PRD review into a discovery workshop.
Read linked domain documents where they may already define an apparently missing rule.
Use available code or execution evidence only when it helps answer the requested review question.
Do not claim to have inspected inaccessible documents, run the product, or interviewed customers.

Keep these sources distinct:

| Source | What it can establish |
|---|---|
| Current explicit user request | Intended changes within the request's scope |
| Adopted product decision or designated domain document | Applicable intended behavior, unless superseded |
| Historical proposal, example, or draft | Prior reasoning or an unadopted option |
| Code inspection | Behavior suggested by the inspected implementation |
| Execution evidence | Observed behavior for that environment, version, and scenario |
| Customer or market evidence | A bounded observation, not automatic authority to replace requirements |

A newer modification time does not make a file authoritative.
If equally applicable decisions conflict, report the conflict and its consequences.
Do not choose the easiest requirement merely because the existing code already implements it.

## Review for decisions that change the outcome

Focus on defects that could cause a different product to be built or a wrong decision to be made.
Read [specification](specification.md) only if a detailed domain or handoff review needs it.
Choose relevant lenses; do not produce a checklist of irrelevant omissions.

- Does the promised result have a complete path through the retained scope?
- Are the actors, domain objects, ownership, and meaningful state transitions unambiguous?
- Are permissions and shared actions defined at the level the product requires?
- Does a decision apply to the correct proposal, price, schedule, or result version?
- Can a relevant failed, duplicate, revoked, or outdated action be recognized and recovered from?
- Do requirements and acceptance criteria agree about the expected outcome?
- Do evidence, numeric units, populations, and observation periods support the stated claim?
- Are assumptions, recommendations, adopted decisions, and completed checks distinguishable?
- Does new information invalidate an old conclusion or leave a material claim untested?

When repeated actions are in scope, establish what makes them the same operation:
actor, target/version, intent, and content where relevant. Check exact retries
separately from reuse of an identifier with changed content. If applicable sources
do not decide whether that reuse replaces, conflicts, or starts another operation,
name the unresolved policy and its consequence; do not silently adopt the
implementation's behavior or report an already defined rule as missing.

Treat an intentionally deferred capability as a defect only if its absence breaks the included promise.
Do not report a rule as missing when another applicable source defines it.
A declared uncertainty is not itself a defect; assess whether the plan makes an unjustified commitment despite it.

## Write actionable findings

For each material finding, provide the shortest sufficient account of:

1. The concrete situation or trigger.
2. What the applicable artifact says, with a file/section or other stable locator.
3. The missing or conflicting decision and a plausible consequence.
4. The evidence supporting that conclusion and its limits.
5. A specific correction, or the decision that must be resolved.

Use exact quotes sparingly; a faithful paraphrase with a locator usually suffices.
State an inference as an inference rather than an observed failure.
When code and intended behavior differ, cite both sides and identify whether execution was observed.
Absence from one inspected file is not evidence of absence throughout the project.

Prioritize by consequence, without forcing a fixed finding count or numerical score:

- **Required decision or conflict:** materially different implementations or a broken core journey.
- **Unsupported claim or verification gap:** a conclusion exceeds the inspected evidence.
- **Optional improvement:** useful refinement that does not prevent the requested outcome.

If a finding depends on unavailable evidence, say what is unavailable and how it could change the conclusion.
Do not turn every uncertainty into a request for user confirmation.
Where the user delegated a recommendation, propose a reversible resolution and explain its tradeoff.

## Calibrate the conclusion

Name what was reviewed and how: document inspection, code inspection, or supplied execution results.
Summarize important strengths only when they constrain the findings or justify the conclusion.
If no material issue is supported, say so; do not invent defects to make the review look thorough.
Distinguish a coherent plan from demonstrated demand, working software, and release readiness.
For a narrow edit, a few findings or one paragraph can be the entire review.
Leave the original artifacts unchanged and identify the next useful correction or check.

Finish a narrow review when each requested lens has been checked against the
applicable sources, with findings or a supported no-issue conclusion and material
limits. Expand to a linked source when it could change a finding; do not add
unrequested lenses merely because more documents exist. Reopen affected findings
when new authority, evidence, or a failed check changes their basis.
