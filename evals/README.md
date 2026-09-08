# Development evaluations

BANDIT is evaluated on concrete planning work, separately from installer and
package checks. Inputs are fictional, and all claimed observations inside them
are supplied fixture data. They are not real customer results.

**Historical [PM Craft 0.1.0 results](results/2026-09-07/README.md)** — 11 completed
task runs, preserved outputs and transcripts, independent meaning-based grades,
and an explicitly inconclusive quality comparison. PM Craft used more reported
input tokens in the three paired cases; no token-savings claim is made.

Those outputs and hashes are preserved under the original PM Craft name. They
are not new BANDIT 0.2.0 measurements. To reproduce the historical PM Craft arm,
use the runner from git tag `v0.1.0`. The current runner supports the general
`--arm bandit` and the five directly invoked specialist arms.

A [focused BANDIT 0.2.0 forward check](results/2026-09-07-bandit/README.md)
records the rebranded skill performing one small planning task. It is not a
repeat of the three-arm comparison.

The [BANDIT 0.3.0 specialist checks](results/2026-09-08-bandit-commands/README.md)
exercise all five direct `$bandit-*` invocations in fresh local projects.
Their outputs, logs, and installer upgrade receipt are recorded separately.

## Cases

| Case | Mode and decision |
| --- | --- |
| [01 — multiple decisions](cases/01-multiple-decisions/request.md) | Specify separate lodging/date votes in one accountless trip |
| [02 — offer change](cases/02-offer-change/request.md) | Update price and sharing rules; interpret pilot evidence |
| [03 — intent review](cases/03-intent-review/request.md) | Review adopted policy against a newer code-derived PRD and an unexecuted test |
| [04 — incomparable scores](cases/04-incomparable-scores/request.md) | Prioritize when RICE units, confidence, and effort are incompatible |
| [05 — small research](cases/05-small-research/request.md) | Recommend one cheap test without customer data or a workshop |

The [rubric](RUBRIC.md) was written before the recorded runs. It grades observable
meaning, including failures, rather than matching headings. The cases reflect
design concerns already used to create the skill: they are development checks,
not a hidden or representative benchmark of all PM work.

## Forward-test method

An independent agent receives only the user's request, raw fixtures, and the
skill with its relevant references. It receives no rubric, desired answer,
suspected defect, or previous output. Product inputs stay read-only and no
customer outreach or live experiment is run.

For paired diagnostic runs, each condition receives the same case and output
cap in a fresh Codex CLI task:

1. Baseline reasoning without a PM skill.
2. [phuryn/pm-skills](https://github.com/phuryn/pm-skills/tree/18468a95b427e70e258b51389796367c6f684e7d)
   at the pinned commit, with relevant command procedures and referenced skills.
3. The instruction snapshot under test (PM Craft in the historical record,
   BANDIT in current runs).

The CLI adaptation reads slash-command instructions as text and applies the
actual user's scope first. The complete upstream checkout is available for
referenced dependencies; we do not compare against an isolated skill while
withholding the workflow that gives it essential context.

## Run a case yourself

The runner uses your installed, authenticated Codex CLI and its normal account
usage. It is opt-in and is not part of the default CI tests. Repository tools
need Python 3.11+. Installations of Codex with different CLI flags may require
adapting the runner; the recorded runs identify the CLI version.

```sh
python3 evals/run_local.py --case 04-incomparable-scores --arm bandit-decide --output-dir /absolute/path/to/new-runs
python3 evals/run_local.py --case 04-incomparable-scores --arm baseline --output-dir /absolute/path/to/new-runs
```

Specialist arms are `bandit-research`, `bandit-decide`, `bandit-specify`,
`bandit-review`, and `bandit-update`. These copy all six skill folders into
the isolated project's `.agents/skills/` and invoke the selected `$bandit-*`
name in the prompt. Inspect the execution log to confirm the agent read that
entrypoint. The general `bandit` arm retains the explicit instruction snapshot
method used by the earlier runner.

For upstream, use a clean checkout at the pinned commit:

```sh
git clone https://github.com/phuryn/pm-skills.git /absolute/path/to/upstream
git -C /absolute/path/to/upstream checkout 18468a95b427e70e258b51389796367c6f684e7d
python3 evals/run_local.py --case 04-incomparable-scores --arm upstream --upstream /absolute/path/to/upstream --output-dir /absolute/path/to/new-runs
```

Each run preserves the prompt, input and instruction hashes, final output,
events, error output, exit code, and elapsed time. Existing run directories are
never reused. Review full outputs against the fixed rubric before revising the
skill. Report partial results and failed runs alongside successes.

## Interpretation limits

These tasks do not test fresh market research, real stakeholder negotiation,
longitudinal decisions, enterprise strategy, games, or statistical expertise.
One run per condition cannot measure reliability or establish causal performance
differences. Host-default model settings and shared-system overhead also limit
comparisons of usage and elapsed time. A correct baseline is evidence that the
model can already perform that task; it is not a reason to hide its result.

See [Validation](../VALIDATION.md) for packaging checks and [Comparison](../docs/comparison.md)
for the narrower, source-based design claims.
