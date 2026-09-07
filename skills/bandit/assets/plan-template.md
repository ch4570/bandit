<!-- Optional template for a new durable product plan. Each {{...}} is an intentional fill slot. Replace slots with supported content or an explicit open question; remove unused sections and this note. Existing plans keep their own structure. -->
# {{Product or initiative}}

**Purpose:** {{Decision or deliverable this plan supports}}
**Scope and version:** {{Affected product, audience, and current version or date}}
**Status:** {{Draft, recommended, or adopted; distinguish implementation and verification below}}
**Related source documents:** {{Links to applicable domain rules or existing decisions, if any}}

## Product decision

{{What is being proposed or changed, why, and the user's relevant constraints.}}

| Choice | Reason and supporting source | Alternative or tradeoff | Status |
|---|---|---|---|
| {{Material choice}} | {{Evidence, instruction, or labeled assumption}} | {{What is deferred or rejected and why}} | {{Proposed or adopted}} |

## User and outcome

{{Who performs the task, in what situation, which current alternative they use, and what completing the task means.}}

**Core journey:** {{Entry → core action → observable outcome, including a prerequisite or handoff when needed}}
**Included:** {{Smallest complete scope}}
**Deferred:** {{Excluded work and consequences of deferring it}}
**Constraints and dependencies:** {{Time, resources, existing capabilities, or external dependencies that change this scope}}

## Evidence and assumptions

| Claim | Source and context | What it supports | Limit or open question |
|---|---|---|---|
| {{Material claim}} | {{Source locator, date or period, relevant population}} | {{Observed, reported, calculated, or assumed conclusion}} | {{What remains untested or uncertain}} |

{{For material calculations, show input values or ranges, units, periods, formulas, and sources. Add stable IDs only when useful for continued cross-reference.}}

## Domain rules

{{Describe the objects, relationships, ownership, and lifecycle that determine this product's behavior. Keep presentation and technical implementation choices separate.}}

| Actor and situation | Action | Rule or precondition | Result and visibility |
|---|---|---|---|
| {{Relevant role and object state}} | {{Intended action}} | {{Eligibility, permission, or domain rule}} | {{State change and who can observe it}} |

**Shared or versioned actions:** {{If relevant: identity, contribution ownership, what a decision covers, and how changed or revoked access affects it}}
**Failure and recovery:** {{Relevant failed, duplicate, stale, or interrupted action and how the user can continue}}

## Requirements and acceptance

| Requirement | Initial condition and action | Observable expected result | Related decision |
|---|---|---|---|
| {{Core promise; optional existing ID}} | {{Actor, state, and action}} | {{Outcome, including a material alternate case}} | {{Decision or section reference}} |

{{Where relevant, state whether visible feedback is local, persisted, or shared; define the meaning of amounts, deadlines, and versions.}}

## Verification

| Target | Method and applicable context | Execution status | Result and evidence |
|---|---|---|---|
| {{Requirement or hypothesis}} | {{Method, environment/version or population/period}} | {{Planned or executed}} | {{Pending, supported, contradicted, inconclusive, or invalid; source when executed}} |

{{A proposed check is not a completed check. A document review, code inspection, and observed execution establish different things.}}

## Experiment, if needed

**Question and hypothesis:** {{What decision this experiment can inform}}
**Observed behavior:** {{Interest, use, payment, reuse, or other behavior being measured}}
**Population and observation window:** {{Eligibility, recruitment, duration, and relevant limitations}}
**Metric:** {{Numerator, denominator, unit, and data source}}
**Criteria and next action:** {{Supported, contradicted, inconclusive, or invalid conditions; distinguish targets from observations}}
**Constraints:** {{Relevant budget, guardrail, or stop rule}}

## Open decisions and next action

| Open item | Why it matters | Proposed default or next check |
|---|---|---|
| {{Unresolved rule or hypothesis}} | {{Effect on scope, behavior, or confidence}} | {{Reversible recommendation or needed evidence}} |

**Next useful action:** {{One concrete action and what it will resolve}}

## Changes, if this plan is being updated

{{Dated delta: what changed, why, and which previous decision it supersedes. Preserve relevant historical evidence in its original context.}}

| Affected item | Updated rule or conclusion | Earlier evidence or check disposition |
|---|---|---|
| {{Decision, requirement, or check}} | {{Current meaning}} | {{Still applicable, historical only, needs recheck, contradicted, or unresolved; why}} |
