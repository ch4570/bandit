---
name: bandit-specify
description: Create, rewrite, or refine PRDs and product specifications from an idea, changed direction, or new evidence, including requested marketing, UX/design, and business model handoffs. Read an existing spec first and replace outdated rules with a coherent current plan, including flows, permissions, states, and acceptance scenarios; excludes code implementation and standalone visual styling.
---

# BANDIT Specify

Turn the requested direction into product requirements someone can implement
and verify. Read the user's current decisions and relevant domain documents,
then apply [specification guidance](references/specification.md) and shared
[work boundaries](references/work-boundaries.md). Start directly
with this skill; a general BANDIT planning pass is not a prerequisite.

Look for an existing specification among the relevant project documents before
writing. If none exists, create the requested specification. If one exists,
read it as the baseline and make the current document fit the new direction.
For a requested rewrite or a substantial direction change, reorganize and
rewrite the specification as needed; do not merely append an update or retain
an obsolete structure. For a narrow request, revise the affected sections.
This choice is part of specification work, not a separate update command.

When revising existing decisions or incorporating new results, also read
[change and evidence guidance](references/changes.md). Preserve relevant past
observations under their original conditions, using existing history or a
clearly marked historical section. A rewritten plan must not invent a new
experimental success or leave contradictory old rules looking current.

Derive actors, objects, meaningful state
changes, permissions, and recovery from the actual product. A narrow feature
does not require a complete new PRD. Current code describes implementation;
it does not silently replace adopted requirements. Where the user delegates an
undecided rule, propose a reasoned draft and distinguish it from accepted policy.

For a durable specification or handoff, also apply
[evidence and decision guidance](references/evidence-and-decisions.md).
When the requested plan includes marketing, UX/design, or business model design,
apply [product journey guidance](references/product-journey.md) and carry the
same audience, promise, offer terms, and delivery limits into each deliverable.
Use the optional [plan template](assets/plan-template.md) only when starting a
new lasting plan. Finish with the artifact, significant changes to an existing
specification, material open decisions, and
observable acceptance scenarios. Written criteria are planned checks, not
evidence that implementation passed them.

Use the user's language and clear professional prose, with BANDIT's outlaw
character limited to light introductions unless requested. A specification
request does not itself authorize code changes or deployment.
