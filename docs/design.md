# Design

BANDIT helps an agent make the next product decision and preserve its meaning through requirements and later changes. Version 0.3.0 provides five directly invocable specialist skills and the general `$bandit` skill for apps and services.

## Separate commands, shared planning principles

Users select a specialist for a specific task or use the general skill for work that spans tasks:

| Command | Responsibility |
| --- | --- |
| [`$bandit-research`](../skills/bandit-research/SKILL.md) | Examine evidence and assumptions; design the next useful investigation or experiment |
| [`$bandit-decide`](../skills/bandit-decide/SKILL.md) | Compare options, choose scope, and explain a recommendation |
| [`$bandit-specify`](../skills/bandit-specify/SKILL.md) | Turn product meaning into actors, rules, states, and acceptance scenarios |
| [`$bandit-review`](../skills/bandit-review/SKILL.md) | Inspect a bounded artifact without editing it; distinguish defects, evidence gaps, and optional improvements |
| [`$bandit-update`](../skills/bandit-update/SKILL.md) | Follow a changed decision or observed result into the affected plan |
| [`$bandit`](../skills/bandit/SKILL.md) | Select the planning workflow for a general or combined request |

Each specialist has its own `SKILL.md`, metadata, and all referenced resources. It works directly without requiring the general skill to run first. Users can install the whole set at once, or copy a complete specialist folder independently.

The reference sources remain under `skills/bandit/`. Maintainers run `node scripts/sync-skills.mjs` to copy the resources each specialist needs, including resources referenced by another reference. `node scripts/sync-skills.mjs --check` verifies those copies. This keeps one maintained definition of a rule while each distributed skill remains self-contained.

The commands are not a mandatory sequence. A price change need not generate a market report, and a review need not produce a replacement PRD. The optional plan template supports new ongoing work; existing artifacts take precedence.

## Keep different claims distinct

The evidence behind a claim determines how it can be used. A competitor page supports a statement about what the vendor publishes. A customer observation may support a particular workflow problem. A calculation follows stated inputs. A proposed target remains a decision criterion until it is measured.

For current product behavior, distinguish a statement in documentation, behavior inferred from code, and behavior observed in an executed check. Keep accepted user requirements separate from all three. Otherwise a bug recovered from code can accidentally become the new specification.

Important relationships should remain traceable:

```text
Evidence supports a claim.
A decision uses that claim and records its trade-off.
A requirement carries the decision into product behavior.
A check states what would verify that behavior, or records what was observed.
```

Not every task needs every link or a set of IDs. Research can end with an unresolved assumption. A small review can point to an existing paragraph. The goal is to preserve meaning, not to create paperwork.

## Define the product's actual objects and rules

A vote needs a participant, a decision or round, and a policy for changing or closing the response. Approval needs an authorized actor and the version being approved. A return tracker must distinguish an expected amount, a seller's status, and a user's actual confirmation.

These distinctions guide the agent to find gaps hidden by generic record templates. State transitions include their material conditions, effects, failure behavior, and recovery. The spec describes enough logical data meaning to make the rule implementable, while leaving architecture choices to the appropriate task.

Cutting scope should retain a complete first use case and the conditions that make it trustworthy. Framework scores can assist comparison when their inputs share units and meaning. A numeric threshold does not automatically authorize a build decision or a change in product policy.

## Preserve history when decisions change

An update follows the changed decision into requirements, permissions, business assumptions, metrics, checks, and user-facing claims where relevant. Unrelated sections and prior evidence remain intact. Results keep the conditions under which they were collected; changing the price today does not make yesterday's trial a test of that price.

Reuse the project's existing source-of-truth boundaries. If separate documents own commercial assumptions and transaction rules, maintain those links rather than silently centralizing everything into a new file.

## Keep delivery within the request

When a user delegates a reversible draft choice, make a reasoned recommendation and label it. Ask when a material target is ambiguous or explicit constraints conflict, and continue independent work when possible. Do not make each specialist a new permission checkpoint.

BANDIT's responsibilities end at the requested product artifact or assessment. It can hand accepted rules and open decisions to implementation or UI work. It does not require another specialist skill, and its use does not authorize customer outreach, purchases, account mutations, code changes, or deployment.

## A recognizable partner, a plain working voice

BANDIT's cowboy hat, red bandana, pencil, and map give the project a recognizable character. The working voice stays direct and useful: recommend a next move, explain the trade-off, and be precise about uncertainty. Product documents use the user's language and terminology. Western roleplay is optional and belongs only where the user requests it. See [the brand guide](brand.md).

## Packaging and evaluation are separate

A dependency-free Node.js installer distributes all six skills through npm tooling. Running `npx --yes https://github.com/ch4570/bandit/releases/download/v0.3.0/bandit.tgz` from a project installs the six sibling skill folders under `.agents/skills/` without Git or Python. The versioned archive works before npm registry publication. The installer protects local modifications. The host model and available tools execute the skill instructions.

Structural validation can check package metadata and references. Installer tests can verify filesystem behavior. Neither proves good PM judgment. [Evaluation](../evals/README.md) covers realistic product tasks, including preservation of a good existing plan and behavior under changed assumptions. [Validation](../VALIDATION.md) records which checks actually ran.

## What would justify the next version

The historical PM Craft 0.1.0 paired development cases produced no demonstrated
quality advantage over baseline or upstream. PM Craft also used more reported
input tokens on those cases. They remain labeled with their original version;
the BANDIT rename does not create new behavior evidence. The next evidence should come from held-out tasks with noisier
sources and decisions that evolve across several turns, with a pinned model and
blind grading. Preserve baseline successes and report regressions.

Improve reference selection if repeated runs show unnecessary reading while
retaining the evidence and change semantics. Add a specialist, script, or integration
only when a concrete recurring task demonstrates the need. A larger catalog is
not the success criterion for this focused skill.
