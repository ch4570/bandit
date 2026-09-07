![BANDIT, a western raccoon with a red bandana, a pencil, and a product plan](docs/assets/bandit-hero.png)

# BANDIT

**An outlaw with a plan. Your next product move, made clear.**

[한국어](README.ko.md) · [Install](INSTALL.md) · [Examples](examples/README.md) · [v0.2.0](https://github.com/ch4570/bandit/releases/tag/v0.2.0)

BANDIT is your product-planning partner: a sharp raccoon in a cowboy hat, armed with a pencil and a map. Bring an idea, an overloaded roadmap, or a half-written PRD. Leave with a useful decision and a plan someone can build.

## Saddle up

Run this **inside your project**:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.2.0/bandit.tgz
```

Then ask your agent:

```text
$bandit Help me turn this idea into a two-week MVP. Recommend the
smallest useful scope, explain the trade-offs, and draft the plan.
```

Requires **Node.js 22+ and npm**. Installs the complete skill into `.agents/skills/bandit/`. No Git, cloning, or Python setup. [Installation options](INSTALL.md).

The npm registry release comes later; the command above installs directly from GitHub. If your agent does not recognize `$bandit`, ask it to read `.agents/skills/bandit/SKILL.md` and use it for the task. Refresh or start a new agent session if necessary.

## What BANDIT rides with

| Bring this | Get this |
| --- | --- |
| An idea and a few sources | **Research:** what the evidence supports, what remains a guess, and what to test next |
| Too much scope and a deadline | **Decide:** a complete first use case, clear trade-offs, and what can wait |
| Rules that are hard to implement | **Spec:** actors, states, exceptions, and acceptance scenarios |
| A PRD that needs a second opinion | **Review:** specific gaps, their consequences, and proposed corrections |
| A new price, policy, or direction | **Update:** affected requirements and experiments, with the old evidence preserved |

Just describe the job. BANDIT chooses the relevant mode; you do not need to run all five or learn a command catalog.

## A character with good judgment

BANDIT is direct, curious, and willing to make a recommendation. The hat stays on the cover; your PRDs stay clear and professional. It separates evidence from assumptions, keeps proposed decisions distinct from accepted ones, and checks the rules behind a feature.

Use your existing documents. A small decision can be a paragraph; an ongoing product can use linked requirements and checks. Planning work stays within the task you requested.

For every Codex project on this computer:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.2.0/bandit.tgz --global
```

BANDIT provides the skill and its installer. Your agent supplies the model, research tools, and file access under its existing permissions and usage costs.

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
