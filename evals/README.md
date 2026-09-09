# Development evaluations

BANDIT is evaluated on concrete planning work, separately from installer and
package checks. Inputs are fictional, and all claimed observations inside them
are supplied fixture data. They are not real customer results.

**Historical [PM Craft 0.1.0 results](results/2026-09-07/README.md)** — 11 completed
task runs, preserved outputs and transcripts, independent meaning-based grades,
and an explicitly inconclusive quality comparison. PM Craft used more reported
input tokens in the three paired cases; no token-savings claim is made.

Those outputs and hashes are preserved under the original PM Craft name. They
are not new BANDIT measurements. To reproduce the historical PM Craft arm,
use the runner from git tag `v0.1.0`. The current runner supports the general
`--arm bandit` and the four directly invoked specialist arms.

A [focused BANDIT 0.2.0 forward check](results/2026-09-07-bandit/README.md)
records the rebranded skill performing one small planning task. It is not a
repeat of the three-arm comparison.

The [BANDIT 0.3.0 specialist checks](results/2026-09-08-bandit-commands/README.md)
exercise all five direct `$bandit-*` invocations in fresh local projects.
Their outputs, logs, and installer upgrade receipt are recorded separately.

The [BANDIT 0.4.0 scope and specification checks](results/2026-09-08-bandit-scope-specify/README.md)
record three fresh tasks: scope selection, a new specification, and an actual
existing-PRD rewrite. Original inputs and the rewritten artifact are preserved
separately. These are development checks, not a new comparative benchmark.

The [bounded-workflow development comparison](results/2026-09-09-bounded-workflows/README.md)
records 18 fresh runs plus a separate actual two-turn continuation. It preserves
three failed quality grades, missing runtime identity, and unavailable monetary
cost. It does not establish cost savings or superiority over baseline.

The [review feedback loop](results/2026-09-09-merge-feedback/README.md) retains two
corrective rounds: 2/4 then 4/4 blind task grades, including both initial failures.
Its eight raw runs and unchanged criteria are preserved separately. Runtime
identity and monetary cost remain unavailable; this is not a savings benchmark.

## Cases

| Case | Planning task |
| --- | --- |
| [01 — multiple decisions](cases/01-multiple-decisions/request.md) | Specify separate lodging/date votes in one accountless trip |
| [02 — offer change](cases/02-offer-change/request.md) | Specify changed price and sharing rules; interpret pilot evidence |
| [03 — intent review](cases/03-intent-review/request.md) | Review adopted policy against a newer code-derived PRD and an unexecuted test |
| [04 — incomparable scores](cases/04-incomparable-scores/request.md) | Scope priorities when RICE units, confidence, and effort are incompatible |
| [05 — small research](cases/05-small-research/request.md) | Recommend one cheap test without customer data or a workshop |
| [06 — existing spec rewrite](cases/06-existing-spec-rewrite/request.md) | Rewrite an existing PRD for free team collaboration while preserving approval rules and historical evidence conditions |
| [07 — export review](cases/07-export-review/request.md) | Narrow access, idempotency, and recovery review with unrelated support material |
| [08 — callback scope](cases/08-callback-scope/request.md) | Multiple delivery decisions constrained by evidence, capacity, and consent |
| [09 — pickup PRD rewrite](cases/09-pickup-prd-rewrite/request.md) | Rewrite a changed pilot direction while preserving historical observations and operating constraints |
| [10 — reservation review](cases/10-reservation-review/request.md) | Distinguish adopted organizer/revision rules from an unresolved withdrawal decision and interrupted ledger handoff |

The [rubric](RUBRIC.md) for cases 01–05 was written before those recorded runs.
It grades observable meaning, including failures, rather than matching headings.
Case 06 is checked against its request and the original and rewritten artifacts;
it has no independent rubric score. The cases reflect
design concerns already used to create the skill: they are development checks,
not a hidden or representative benchmark of all PM work.

Cases 07–09 were authored independently of the bounded-workflow candidate, with
ordinary noise documents. They were held out from that instruction-authoring
pass, not from future development now that they are public. Their
[meaning-based criteria](criteria/2026-09-09-bounded-workflows/README.md) stay
outside the executing agent's inputs. Case 09 has a separately stored
[second user message](follow-ups/09-pickup-prd-rewrite/request.md); deliver it only
after the initial task, in the same conversation. The fresh-session runner does
not implement resume; record an actual continuation separately and do not add
its cumulative session snapshots together.

Case 10 was authored independently of candidate instructions and prior grades.
Its [criteria](criteria/2026-09-09-merge-feedback/10-reservation-review.md) remain
outside the raw fixture directory. Once used for feedback, it is a public
development case, not a held-out benchmark for subsequent instruction edits.

## Forward-test method

An independent agent receives only the user's request, raw fixtures, and the
skill with its relevant references. It receives no rubric, desired answer,
suspected defect, or previous output. Product inputs stay read-only by default.
The optional `--edit-artifact` run uses a writable workspace and instructs the
agent to edit only the named input artifact; before/after hashes check whether
it respected that scope. No customer outreach or live experiment is run.

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
python3 evals/run_local.py --case 04-incomparable-scores --arm bandit-scope --output-dir /absolute/path/to/new-runs
python3 evals/run_local.py --case 04-incomparable-scores --arm baseline --output-dir /absolute/path/to/new-runs
```

Specialist arms are `bandit-research`, `bandit-scope`, `bandit-specify`,
and `bandit-review`. These copy all five skill folders into
the isolated project's `.agents/skills/` and invoke the selected `$bandit-*`
name in the prompt. Inspect the execution log to confirm the agent read that
entrypoint. The general `bandit` arm retains the explicit instruction snapshot
method used by the earlier runner.

To check a real artifact rewrite, permit the PRD named in case 06:

```sh
python3 evals/run_local.py --case 06-existing-spec-rewrite --arm bandit-specify --edit-artifact input/docs/PRD.md --output-dir /absolute/path/to/new-runs
```

The runner retains original inputs under `original-input/` for every arm and
keeps the resulting workspace and raw logs, including failed runs. Review the
resulting PRD and the before/after evidence, not just the agent's final reply.

New runs distinguish `process_exit_code` (the Codex process result),
`integrity_status` (`passed`, `failed`, or `unavailable`), and `quality_status`
(`not_evaluated` until a separate assessment). The runner's `exit_code` is
nonzero for a process failure, an unauthorized workspace change, or an unavailable
snapshot. A successful process is not a passing planning assessment.

Workspace snapshots record regular-file hashes, permission bits, directory entries,
and link targets. The workspace root is recorded as `.` so its permission changes
are violations too. POSIX hosts use descriptor-relative directory traversal and
no-follow opens; other hosts record `portable-quiescent` traversal and require
a workspace without concurrent writers. Observed changes during a snapshot make
it unavailable. This does not provide an atomic snapshot against arbitrary
background writers. Only content changes to the named existing
`--edit-artifact` file are allowed; its deletion or replacement with a link is
a violation. Other created, modified, deleted, or type-changed paths are listed
in `violations`, including files outside `input/` and changed skill instructions.
Snapshot errors and caught execution failures remain in metadata. No workspace
paths are silently excluded. This is a post-run scope check, not an OS guarantee
that the agent could never access paths outside that workspace. Historical
metadata is preserved unchanged and does not retroactively gain these checks.

For upstream, use a clean checkout at the pinned commit:

```sh
git clone https://github.com/phuryn/pm-skills.git /absolute/path/to/upstream
git -C /absolute/path/to/upstream checkout 18468a95b427e70e258b51389796367c6f684e7d
python3 evals/run_local.py --case 04-incomparable-scores --arm upstream --upstream /absolute/path/to/upstream --output-dir /absolute/path/to/new-runs
```

Each run preserves the prompt, input and instruction hashes, final output,
events, error output, exit code, and elapsed time. Existing run directories are
never reused. Review full outputs against the applicable rubric or case request
before revising the skill. Report partial results and failed runs alongside
successes.

## Controlled usage comparisons

Pin the model, its supported reasoning effort, output budget, and timeout for
every condition. Replace `MODEL_ID` with an available model; no model or price
is baked into BANDIT. For example:

```sh
python3 evals/run_local.py --case 04-incomparable-scores --arm bandit-scope --condition current --model MODEL_ID --reasoning-effort low --timeout-seconds 600 --max-output-words 700 --replicate 1 --attempt 1 --output-dir /absolute/path/to/current-r1
python3 evals/run_local.py --case 04-incomparable-scores --arm baseline --condition baseline --model MODEL_ID --reasoning-effort low --timeout-seconds 600 --max-output-words 700 --replicate 1 --attempt 1 --output-dir /absolute/path/to/baseline-r1
```

Use `--skills-dir /absolute/path/to/frozen-checkout/skills` to test a particular
instruction snapshot with the same specialist invocation. The runner copies
that snapshot and records hashes. Specialist runs still install the complete
supplied bundle; they are not measurements of a standalone-only installation.
Keep fixtures identical, repeat each condition, and counterbalance execution
order. Retain every attempt in a new run directory, including failed retries.
The runner does not retry or upgrade models automatically.

The requested `execution_settings` are separate from runtime-observed model and
effort in `telemetry`. Missing observations remain null. The parser reads Codex
CLI lifecycle/usage events and retains diagnostics for incomplete streams.
CLI `turn.completed.usage` is a cumulative session snapshot: retain the last
valid total, never add successive snapshots. Direct App Server notifications
are a separate unsupported event format. Input
already includes cached input; output includes reasoning. Optional missing
breakdowns remain unknown and are never added to input/output totals again.
The [Codex non-interactive documentation](https://learn.chatgpt.com/docs/non-interactive-mode.md)
describes the JSONL lifecycle. The checked CLI `0.153.4`
[emits the session's total usage](https://github.com/openai/codex/blob/3d2ee51ca2d5db578f328aa75e20aa22c0197c9a/codex-rs/exec/src/event_processor_with_jsonl_output.rs#L122).
A schema change requires parser validation, not inferred counters. This runner
starts fresh ephemeral sessions; it does not resume threads. A resumed session's
total must not be treated as the incremental cost of that invocation.

Web search and native multi-agent execution are disabled equally across these
controlled runs. Usage covers top-level CLI events; it is not automatic billing
accounting for every descendant or external service. The timeout stops the
direct CLI process and reports unverified descendant cleanup. The word limit is
a prompt instruction, not a token cap. Neither limit enforces provider billing.

Grade saved outputs separately, without revealing condition names to the
reviewer or giving the executing model the rubric. Bind each grade to the actual
output hash and, for rewrites, the edited artifact hash. Use a manifest such as
this **synthetic schema example**, replacing IDs, paths, and hashes with recorded
evidence:

```json
{
  "schema": "bandit.comparison/v1",
  "conditions": ["baseline", "current", "candidate"],
  "runs": [
    {
      "id": "current-scope-r1-a1",
      "directory": "current-r1/04-incomparable-scores--bandit-scope",
      "condition": "current",
      "case": "04-incomparable-scores",
      "replicate": 1,
      "attempt": 1,
      "quality": {
        "status": "passed",
        "evidence": "grades/scope-r1.md: acceptance checks and limitations",
        "output_sha256": "REPLACE_WITH_RECORDED_SHA256"
      }
    }
  ]
}
```

Include the matching baseline/candidate rows and all replicates/attempts. The
example above alone is intentionally incomplete. Set quality to `unavailable`
when it has not been assessed; process success is not a grade. Add
`quality.artifact_sha256` for the named rewritten artifact. Relative run paths
are resolved from the manifest's directory.
Run metadata must explicitly record `editable_artifact`: `null` for answer-only
tasks, or the relative `input/` path for rewrites. Missing artifact mode leaves
quality unavailable. Metadata must also record a supported runner `arm` and its
`invocation` (the exact `$bandit-*` command for specialists, otherwise `null`).
The arm, invocation, and instruction hashes must remain the same across
replicates and retries within each condition/case; different cases and
intentional conditions may use different routes.

```sh
python3 evals/compare.py /absolute/path/to/comparison.json --output /absolute/path/to/new-summary.json
```

The output must be new and outside every listed run directory; raw runs remain
unchanged. Different
settings, fixtures, versions, unmatched cells, duplicate attempts, unbound
grades, or missing usage/observed identity make the comparison incomplete with
reasons. Descriptive observations remain available without a superiority claim.

For currency estimates, optionally supply `--pricing` with a recorded JSON
object containing `model`, `currency`, `effective_date`, `source_url`,
`input_per_million`, `cached_input_per_million`, and `output_per_million`.
Use verified rates applicable to the observed model and run date. Missing or
incompatible pricing leaves cost unavailable; BANDIT does not invent prices.
Cost per successful task includes all attempts in the numerator and counts each
task/replicate once in the denominator only when its bound quality grade passes,
both exit codes are zero, and integrity passes. Zero successful tasks
have no finite cost-per-success result. Report success rate, usage, elapsed time,
and task mix alongside this number; keep development grading costs separate.

## Interpretation limits

These tasks do not test fresh market research, real stakeholder negotiation,
longitudinal decisions, enterprise strategy, games, or statistical expertise.
One run per condition cannot measure reliability or establish causal performance
differences. Historical host-default settings, unavailable runtime observations,
cache conditions, and shared-system overhead also limit comparisons of usage
and elapsed time. Explicit requested settings improve control but do not attest
the provider's backend identity. A correct baseline is evidence that the
model can already perform that task; it is not a reason to hide its result.

See [Validation](../VALIDATION.md) for packaging checks and [Comparison](../docs/comparison.md)
for the narrower, source-based design claims.
