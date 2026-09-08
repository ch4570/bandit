# Product specification

Use this reference to create or rewrite product requirements someone can implement and verify.
Start at the requested feature or journey; a small change needs only its affected rules and checks.
Read the current plan, terminology, and designated domain documents before drafting.
The optional [plan template](../assets/plan-template.md) is for a new durable plan, not a replacement for an existing PRD.

## Create or rewrite the specification

Check relevant project documents for an existing specification. If one exists,
use it as the baseline; otherwise create the requested new plan. The presence of
an old spec is not a reason to ask the user to choose a different command.

When the user changes the product direction or requests a rewrite, rebuild the
document around the adopted direction. Reorganize sections, replace obsolete
rules, and revise scope, flows, metrics, and acceptance criteria together as
needed. Produce a coherent current specification, rather than an appended set
of changes that leaves conflicting rules in place. A narrow change can remain
a targeted edit; existing content does not make a full rewrite mandatory.

For changed decisions or new evidence, apply [change guidance](changes.md).
Carry forward unaffected requirements and preserve previous observations with
their original conditions. Old successful checks may become historical or need
rechecking; they do not become new results for the rewritten product. Use the
project's existing history mechanism or a concise historical section, without
forcing a separate ledger or a new approval step.

## Establish the intended behavior

Read the current user request and applicable adopted decisions before filling gaps.
Distinguish adopted requirements from old proposals, examples, and observed implementation.
Code can establish what currently happens; it cannot establish what the user now wants.
If a domain document is authoritative for a subject, reference it instead of maintaining a competing copy.

Identify the result the user needs, the actors involved, and the boundary of this change.
Carry forward explicit constraints such as time, budget, supported audience, or required compatibility.
When a reversible draft choice is delegated, choose a reasonable default and label it as proposed.
Ask only when a material conflict or ambiguous target prevents the requested specification.
Continue independent parts while such a decision is unresolved.

## Derive the domain model

Describe the product's objects and rules before organizing screens.
Include only objects that affect the requested outcome; do not introduce a generic CRUD model.
For each material object, establish its meaning, owner or association, important states, and lifecycle.
State relationships that change behavior: one response per participant, a decision about one proposal version, or a price belonging to one offer.
Keep domain rules separate from their presentation and from optional technical implementation choices.

Use the domain to find missing decisions:

- A group vote needs response ownership, eligibility, revision rules, aggregation, and a rule for reaching a decision.
- A change quote needs a proposal version, deciding party, covered amount and schedule, and the effect of a later revision.
- A reservation needs availability, who can hold or confirm it, expiry, and what happens when a competing action wins.

These examples are prompts to reason from the product, not mandatory models for unrelated products.

## Keep the smallest complete journey

Trace how an eligible actor enters, performs the core task, and recognizes the resulting outcome.
Include the prerequisite and dependent behavior needed for that journey to work.
Reducing scope must not remove the only way to finish, discover a failed action, or recover from a relevant failure.
State what is included, what is deferred, and any retained dependency on an existing capability.
Do not promise a working end-to-end result when the scope ends at a mockup or manual handoff.

For each meaningful transition, specify:

| Element | Decision to express |
|---|---|
| Actor and context | Who may initiate it, on which object, under what conditions? |
| Action | What does the person intend to do? |
| Rule | What must hold, and what conflicting state prevents it? |
| Result | What changes, what stays fixed, and what is visible to whom? |
| Failure and recovery | How does the person recognize a relevant failure and continue? |

A short paragraph can cover these elements; a transition table is optional.
Avoid listing every possible technical exception when it does not affect product behavior.

## Resolve permissions and shared state when relevant

Separate identity, possession of a link, membership, and permission to take a particular action.
Do not infer edit or decision authority from the ability to view a page.
For shared objects, identify who may read, contribute, change, decide, revoke, or delete only where those actions exist.
Explain whether an action affects one person's contribution or the shared result.
If revocation or expiry is in scope, specify its effect on existing access and previously recorded actions.
Choose the lightest identity mechanism that fits the product; sharing alone does not require account creation.

Where repeated or competing actions matter, specify their product outcome.
Examples include replacing one's earlier vote, rejecting an outdated decision, or preventing duplicate reservations.
Do not prescribe a database, locking mechanism, or framework unless the user needs that technical choice.

## Bind consequential actions to the right version

If a proposal, amount, schedule, document, or shared result can change, define what an acknowledgment or decision covers.
Distinguish viewed, acknowledged, accepted, rejected, and withdrawn only when those meanings differ in the product.
Viewing a link is not an affirmative decision unless the user explicitly defines that behavior.
Specify which changes require a new decision and what remains effective from the prior version.
Keep historical actions attributable to the actor and version on which they occurred.
Explain the actor's outcome when acting on a stale version; do not silently transfer acceptance to changed terms.

For amounts or deadlines that affect the result, define units, currency, period, timezone, and rounding where relevant.
Distinguish the payer from the user and the quoted amount from a collected payment.
Only add cancellation, refund, or expiry rules if this product's promise depends on them.

## Make acceptance observable

For each core promise, describe an initial condition, an action, and an observable result.
Add the failure or alternate case most likely to produce a different implementation if left unspecified.
Use outcome language such as “a participant's replacement response changes their contribution once.”
Avoid criteria such as “intuitive,” “correct,” or “production ready” without an observable meaning.
Where storage or synchronization matters, distinguish local feedback from persisted or shared state.

Link requirements to checks using existing IDs or clear local references.
For durable handoffs, use the shared [evidence and decision rules](evidence-and-decisions.md).
Record a proposed check as planned; a written acceptance criterion is not execution evidence.
State the relevant environment, version, or test data when a check's result depends on it.

## Finish the handoff

Check that scope, roles, rules, states, and acceptance criteria describe the same product.
Expose open decisions that could change behavior, with a proposed default when appropriate.
Separate implementation-blocking decisions from details that can remain flexible.
Report the resulting artifact, the material assumptions, and what has actually been checked.
Specification completeness does not establish customer demand, implementation completion, or release readiness.
