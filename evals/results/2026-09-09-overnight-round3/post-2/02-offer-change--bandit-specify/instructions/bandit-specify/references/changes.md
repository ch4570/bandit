# Changes and new results within specification work

Use this reference to incorporate a changed request, a revised decision, or observed results into an existing plan.
Apply it as part of creating or rewriting a specification, not a separate user command.
Update the requested planning artifacts and their affected dependencies; preserve unrelated decisions.
When the user asks for a rewrite or changes the product direction substantially,
rebuild the document's structure and rules around that direction rather than only appending a delta.
For a small edit, a precise patch and a short explanation are enough.
Do not create a separate ledger, new plan, or approval sequence solely to record that edit.

## Establish the current baseline and delta

Read the user's current request, the relevant current decisions, and the evidence attached to the change.
Identify what is changing, what prompted it, and which product, audience, or version it affects.
Use the existing document as the baseline and respect designated domain sources of truth.
Keep or replace its structure according to the requested result; do not preserve an obsolete layout at the expense of a coherent new specification.
Distinguish a new instruction from a question, an unadopted suggestion, or an observation.
Do not infer the requested target from file modification time alone.

A current explicit request supersedes earlier product decisions within its stated scope.
Historical proposals do not overrule adopted requirements.
Observed code establishes current implementation, not authority to replace the user's intent.
New customer evidence can challenge a decision; it does not silently adopt a different product scope.
If a material conflict prevents the update, expose it and continue the unaffected work.
When a reversible choice is delegated, choose a reasoned default and label its status.

Summarize the delta before expanding the affected scope:

- Previous rule or conclusion.
- Requested new rule, or newly observed result.
- Reason and applicable evidence.
- Affected actors, objects, versions, or periods.

This may be a sentence rather than a table.

## Follow actual dependencies

Trace from the changed decision to relevant requirements, wording, calculations, experiments, and acceptance checks.
Use existing IDs or clear section references; add IDs only when continued cross-reference is useful.
Read the linked artifacts needed to verify the impact instead of assuming every mode is affected.

Examples of likely dependencies:

| Change | Inspect where applicable |
|---|---|
| Paid to free | Buyer and entitlement rules, prices, revenue assumptions, payment-dependent flows, demand experiments |
| Sharing introduced | Participant identity, access, contribution ownership, visibility, revocation, shared state |
| Proposal or quote revised | Version identity, covered terms, stale decisions, previously effective commitments |
| MVP scope reduced | Complete retained journey, prerequisites, manual handoffs, failure recovery, acceptance criteria |
| New experiment results | Population, measured behavior, denominator, period, criteria, conclusions supported by that evidence |

These are impact prompts, not authorization to add features or rewrite all listed areas.
State a dependency that lies outside the requested artifact instead of editing unrelated product code.
Plan updates do not authorize implementation or external actions.

## Apply the update without rewriting history

Make the new rule clear in the current section; do not leave an old price or permission as an equally current alternative.
Remove contradictory current wording while preserving relevant historical reasoning as superseded.
Do not erase an interview, calculation input, or experiment result because the decision it informed changed.
Keep stable IDs for continuing items and make replacement relationships explicit when meaning changes.
Use the project's existing history mechanism, or a brief dated delta for a durable plan.
Avoid maintaining two editable copies of the same rule in a plan and a domain reference.

Separate the statuses of recommendation, adopted decision, implementation, and verification.
A request to change the plan can adopt a new product rule without proving it is implemented.
An observed implementation difference can justify a repair recommendation without proving the old requirement was wrong.

## Reassess evidence and checks selectively

Bind prior evidence to the conditions under which it was obtained.
For each affected conclusion or check, identify whether the change alters the behavior, audience, price, version, environment, or measurement it depends on.
Leave unaffected results intact and explain material limits on reusing affected ones.

Use precise dispositions:

- **Still applicable:** relevant conditions and expected behavior are unchanged.
- **Historical only:** valid evidence about an earlier offer, version, or population.
- **Needs recheck:** the relevant requirement or conditions changed.
- **Contradicted:** new evidence directly challenges the earlier conclusion under comparable conditions.
- **Unresolved:** available evidence cannot determine applicability or outcome.

Do not relabel an old successful execution as a failure merely because the requirement changed.
Do not reuse payment willingness for a different price as if it had been measured there.
If price and sharing changed together, report the observed combined result without attributing causality to price alone.
When interpreting results, distinguish no eligible observation, incomplete observation, measurement failure, and an observed negative outcome.
Use [research](research.md) when the change requires substantive experiment interpretation or new research.

## Check and report the resulting plan

Read the changed sections together with their immediate dependencies.
Check for stale terms, contradictory scope, orphaned requirements, and acceptance criteria that still expect the previous behavior.
Use the shared [evidence and decision rules](evidence-and-decisions.md) for durable linked records.
Use [review](review.md) if an independent or broader planning review is part of the task.

Report the concrete changes, their important consequences, and the checks that now need attention.
Distinguish edits made from follow-up recommendations or inaccessible artifacts left unresolved.
Keep the next step proportional: it may be one open decision or one targeted check.
