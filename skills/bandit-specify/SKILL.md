---
name: bandit-specify
description: Create, rewrite, or refine PRDs and product specifications from an idea, changed direction, or new evidence. Read an existing spec first and replace outdated rules with a coherent current plan, including flows, permissions, states, and acceptance scenarios; excludes code implementation and standalone visual styling.
---

# BANDIT Specify

Turn the requested direction into product requirements someone can implement
and verify. Read the user's current decisions and relevant domain documents,
then apply [specification guidance](references/specification.md). Start directly
with this skill; a general BANDIT planning pass is not a prerequisite.

Use an existing specification as the baseline; otherwise create one. For a
requested rewrite or changed direction, rebuild its current rules and structure
as needed. A narrow request needs only affected sections. Both use this command.

For changed decisions or new evidence, also read
[change guidance](references/changes.md), preserving observations under their
original conditions and keeping superseded rules distinct from the current plan.

Derive actors, objects, meaningful state changes, permissions, and recovery from
the actual product. A narrow feature
does not require a complete new PRD. Current code describes implementation;
it does not silently replace adopted requirements. Where the user delegates an
undecided rule, propose a reasoned draft and distinguish it from accepted policy.

For a durable specification or handoff, also apply
[evidence and decision guidance](references/evidence-and-decisions.md).
Use the optional [plan template](assets/plan-template.md) only when starting a
new lasting plan. Finish with the artifact, significant changes to an existing
specification, material open decisions, and
observable acceptance scenarios. Written criteria are planned checks, not
evidence that implementation passed them.

Use the user's language and clear professional prose, with BANDIT's outlaw
character limited to light introductions unless requested. A specification
request does not itself authorize code changes or deployment.
