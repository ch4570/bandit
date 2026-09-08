# Comparison and upstream reference

BANDIT is a focused alternative for app and service planning, not a demonstrated replacement for every PM skill library. We have not established comparative superiority. This document explains design choices and cites the upstream instructions that informed them; it does not report a model behavior benchmark.

## The pinned reference

The reviewed reference is [phuryn/pm-skills at commit `18468a95b427e70e258b51389796367c6f684e7d`](https://github.com/phuryn/pm-skills/tree/18468a95b427e70e258b51389796367c6f684e7d). Claims here concern that snapshot, not every later version.

| Choice | phuryn snapshot | BANDIT 0.4.0 |
| --- | --- | --- |
| Entry | A broad collection of specialized skills and associated commands | Four directly callable planning specialists plus a general entrypoint |
| Scope | Discovery, strategy, execution, research, analytics, and additional PM work | Research, MVP scope, specification writing and rewriting, and review for apps and services |
| Handoff | Artifact guidance is distributed across related skills and commands | Canonical evidence and decision guidance synchronized into self-contained specialists |
| Existing plan | Offers document creation and analysis workflows | Uses the existing plan as a baseline and rewrites requested content and structure while preserving unrelated decisions |
| Change work | Several task-specific workflows | Specification work includes changed rules, affected requirements and checks, and preserved historical evidence |
| Evidence of quality | Source instructions describe intended behavior | Examples and evaluation tasks define intended behavior; executed results are recorded separately |

The smaller surface is a maintenance and entry-point choice. It is not evidence of better output or lower token usage. BANDIT 0.2.0 introduced a character identity and npm installation; 0.3.0 added independent specialist commands; 0.4.0 clarifies MVP scope and combines new and revised specifications under one command. Historical PM Craft 0.1.0 runs do not measure those changes.

## Strengths to retain

The upstream library contains useful evidence-aware instructions. Its [market-sizing skill](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-market-research/skills/market-sizing/SKILL.md) asks for sources, explicit assumptions, uncertainty, and comparison of estimation approaches. Its [strategy-red-team skill](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-execution/skills/strategy-red-team/SKILL.md) warns against inventing objections and calls for engaging with the strongest version of a claim.

The [intended-vs-implemented skill](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-ai-shipping/skills/intended-vs-implemented/SKILL.md) connects documentation with implementation evidence. The [derive-tests command](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-ai-shipping/commands/derive-tests.md) distinguishes existing and proposed tests. It would be inaccurate to characterize the entire library as ignoring evidence or verification.

## Where BANDIT makes a different choice

**One definition per artifact.** At the pinned snapshot, [create-prd](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-execution/skills/create-prd/SKILL.md) and its associated [write-prd command](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-execution/commands/write-prd.md) describe different section sets. The command explicitly adds non-goals and prioritized acceptance criteria. BANDIT keeps specification guidance in one place so direct invocation and a broader planning task use the same core meaning. This source difference does not establish how a model would perform in either path.

**Check input meaning before scoring.** The pinned [prioritize-assumptions skill](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-product-discovery/skills/prioritize-assumptions/SKILL.md) describes confidence on a 1–10 scale and uses `(1 − Confidence) × Effort` without an explicit normalization step. BANDIT asks the agent to identify units, scales, missing inputs, and zero denominators before relying on a ranking. An ordinal score should not silently become a probability.

**Preserve what was actually observed.** The [new-product experiments skill](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/pm-product-discovery/skills/brainstorm-experiments-new/SKILL.md) groups pre-orders and waitlists in its willingness-to-pay discussion. BANDIT distinguishes free registration, price exposure, paid commitment, actual payment, and renewal throughout the handoff. A waitlist can still be useful; its evidence supports a narrower claim.

**Separate present behavior from accepted intent.** A document reconstructed from code is evidence of what the code appears to do. It is not independent proof that the user requested that behavior. BANDIT preserves this distinction when reviewing or updating a plan, and also distinguishes a test's existence from its observed result on a particular version.

## How to compare fairly

Use the same model settings, task, source snapshot, tool permissions, and time allowance. Give the upstream condition the relevant skills **and** command procedures rather than removing part of its normal workflow. If a host cannot execute a slash command, provide its instructions explicitly and record the adaptation.

For a new comparison, collect baseline model, pinned upstream, and pinned BANDIT outputs. The published September 7, 2026 runs evaluated PM Craft 0.1.0; their original inputs, output names, and results remain unchanged. Report incomplete tasks, unsupported claims, material errors, unnecessary questions, time, and measured usage. Preserve unsuccessful runs and separate installation checks from actual planning tasks. See [the evaluation guide](../evals/README.md) for the current cases and results, and [Validation](../VALIDATION.md) for checks already run.

The upstream project is [MIT licensed](https://github.com/phuryn/pm-skills/blob/18468a95b427e70e258b51389796367c6f684e7d/LICENSE). BANDIT's instructions are written for this focused workflow; when contributing upstream-derived text or code, preserve its required attribution and license notices.
