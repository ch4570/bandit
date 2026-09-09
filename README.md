![BANDIT, a western raccoon with a red bandana, a pencil, and a product plan](docs/assets/bandit-hero.png)

# BANDIT

**An outlaw with a plan. Your next product move, made clear.**

[한국어](README.ko.md) · [Install](INSTALL.md) · [Commands & usage](#skill-commands-and-usage) · [Examples](examples/README.md) · [v0.4.0](https://github.com/ch4570/bandit/releases/tag/v0.4.0)

BANDIT is your product-planning partner: a sharp raccoon in a cowboy hat, armed with a pencil and a map. Bring an idea, an overloaded roadmap, or a half-written PRD. Leave with a useful decision and a plan someone can build.

## Saddle up

Run this **inside your project**:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz
```

Then ask your agent:

```text
$bandit-scope Help me turn this idea into a two-week MVP. Recommend the
smallest useful scope, explain the trade-offs, and draft the plan.
```

Requires **Node.js 22+ and npm**. Installs **five skills** into `.agents/skills/`, including all four specialist commands below. No Git, cloning, or Python setup. [Installation options](INSTALL.md).

**Upgrading from 0.2 or 0.3?** Run the 0.4.0 command above in the same project, then start a new agent session. Use the same `--global` or destination option if applicable. [Upgrade details](INSTALL.md#upgrade-from-02-or-03).

The npm registry release comes later; the command above installs directly from GitHub. If your agent does not recognize `$bandit-scope`, ask it to read `.agents/skills/bandit-scope/SKILL.md` for the default project installation. If you installed elsewhere, use `bandit-scope/SKILL.md` under the skills directory printed by the installer. Ask the agent to apply that file to your task; refresh or start a new agent session if necessary.

## Skill commands and usage

One installation gives you **four specialist skills and the general `$bandit` skill**. Choose a command and add your request. Each specialist has its own instructions and can be invoked directly.

| Command | When to use it | Expected deliverable |
| --- | --- | --- |
| [`$bandit-research`](#research) | Research customer problems, alternatives, demand, or an experiment | Evidence, assumptions, and the next useful test |
| [`$bandit-scope`](#scope) | Set MVP scope and feature priorities within your capacity | Included, deferred, and excluded work, trade-offs, and key dependencies |
| [`$bandit-specify`](#specify) | Create a spec or rewrite an existing one for a new direction | A coherent PRD, product rules, acceptance scenarios, and preserved evidence |
| [`$bandit-review`](#review) | Inspect a plan for consequential gaps or conflicts | Findings tied to source sections, consequences, and proposed corrections |
| [`$bandit`](#general-planning) | Combine planning tasks or let BANDIT choose the workflow | A plan or recommendation matched to your overall request |

Replace the example ideas and document paths with your own. Include existing sources, constraints such as time and team size, and the output you want.

### Research

```text
$bandit-research Research whether freelancers need a tool for getting client
approval on scope changes. Use available sources, separate facts from
assumptions, and propose the smallest next test of paid demand.
```

Get a focused evidence brief and experiment proposal. Free signups, stated interest, and actual payment support different claims; unavailable evidence remains unverified. Live research depends on your agent's tools. Without browsing, BANDIT can assess supplied sources and prepare a research plan. [Research guidance](skills/bandit-research/SKILL.md).

### Scope

```text
$bandit-scope Reduce the attached PRD to a two-week pilot for one developer.
Keep the complete request → client approval → result lookup journey.
Recommend what to defer and where a manual step is enough.
```

Get a complete first use case, kept and deferred scope, trade-offs, and material capacity assumptions. Essential permissions and recovery stay connected to the outcome they protect. [Scope guidance](skills/bandit-scope/SKILL.md).

### Specify

Create a new spec:

```text
$bandit-specify Write a spec for a shared vote with five participants. Define
response changes, a 2–2 tie with one missing vote, closing, and reopening.
Recommend draft rules for decisions we have not made yet.
```

Or rewrite an existing spec around a changed direction:

```text
$bandit-specify Rewrite docs/PRD.md for a free shared workspace instead of
our paid solo plan. Reorganize the document and replace obsolete rules
where needed. Cover permissions, onboarding, metrics, and acceptance
scenarios. Keep prior pilot results with their original price and conditions.
```

Get a new or revised PRD with actors, states, exceptions, and observable acceptance scenarios. The document can be restructured to fit the new direction; historical evidence retains its original meaning. Proposed defaults remain distinct from accepted decisions. [Specification guidance](skills/bandit-specify/SKILL.md).

### Review

```text
$bandit-review Review docs/PRD.md for permission, stale-version, and recovery
gaps. Cite the relevant sections and propose specific fixes.
Leave the original files unchanged.
```

Get findings within the requested scope, each explaining the evidence, consequence, and proposed correction. A review leaves the source documents intact and does not claim the product was tested merely because its plan was read. [Review guidance](skills/bandit-review/SKILL.md).

### General planning

For a request that spans several tasks, use the original `$bandit` command:

```text
$bandit Assess this app idea, recommend a two-week MVP, and turn the
chosen scope into a development handoff. Keep assumptions explicit.
```

BANDIT selects the relevant planning workflow. [General skill instructions](skills/bandit/SKILL.md).

For an ongoing plan or development handoff, the shared [evidence and decision guidance](skills/bandit/references/evidence-and-decisions.md) connects sources, assumptions, decisions, requirements, and checks. Small requests can remain a paragraph or short table. An optional [plan template](skills/bandit/assets/plan-template.md) helps when starting a new plan; [Usage](docs/usage.md) has more examples.

## A character with good judgment

BANDIT is direct, curious, and willing to make a recommendation. The hat stays on the cover; your PRDs stay clear and professional. It separates evidence from assumptions, keeps proposed decisions distinct from accepted ones, and checks the rules behind a feature.

Use your existing documents. A small decision can be a paragraph; an ongoing product can use linked requirements and checks. Planning work stays within the task you requested.

For every Codex project on this computer:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz --global
```

BANDIT provides the skills and their installer. Your agent supplies the model, research tools, and file access under its existing permissions and usage costs.

## Open the trail map

| Guide | What's inside |
| --- | --- |
| [Usage](docs/usage.md) · [한국어 사용법](docs/usage.ko.md) | Copyable prompts and practical handoffs |
| [Install](INSTALL.md) | One-command setup, updates, custom locations, and removal |
| [Examples](examples/README.md) | Fictional planning situations and worked outputs |
| [Meet BANDIT](docs/brand.md) | Character, voice, and visual identity |
| [Design](docs/design.md) · [Comparison](docs/comparison.md) | How the skill works and its upstream influences |
| [Validation](VALIDATION.md) · [Evaluation](evals/README.md) | Executed checks, raw task evidence, and limitations |

The earlier **PM Craft 0.1.0** evaluation contains 11 task runs. Its three paired cases did not establish a quality advantage over baseline or upstream, and used more reported input tokens. Those records retain their original name and version; they are not new BANDIT benchmark results.

[Contributing](CONTRIBUTING.md) · [Support](SUPPORT.md) · [Changelog](CHANGELOG.md) · [MIT](LICENSE)
