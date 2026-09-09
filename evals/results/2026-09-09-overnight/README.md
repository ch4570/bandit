# Overnight development, round 2 — 2026-09-09

This round shortened repeated specification guidance, aligned shared wording
with requested structural rewrites, and added fresh checks for noisy experiment
data and successive access-policy changes. All nine task runs passed their
predeclared meaning-based conditions. Original instructions already passed the
paired checks: this shows no observed rubric-level regression, not a measured
quality gain.

These synthetic, author-designed diagnostics are not a hidden benchmark,
reliability estimate, comparison against another PM workflow, or evidence of
customer demand. The broader overnight effort continues; this directory
records one completed local round.

## What changed and why

- The `$bandit-specify` entrypoint points more concisely to its complete
  specification/change references. Its source shrank from **354 to 284
  whitespace-delimited words**, or 2,601 to 2,142 bytes. This is source length,
  not measured model-token use or token savings.
- The shared evidence contract preserves authoritative sources and terminology
  while matching structure to the request. The optional template also permits
  requested structural changes. Canonical edits were synchronized to the
  specialists; no generated copy was hand-edited.
- A source audit found duplication and tension between keeping existing
  structure and the existing rewrite guidance. No task failure was attributed
  to that wording. This is a consistency/maintenance refactor, not a claimed
  behavioral repair inferred from passing examples.
- The runner accepts raw `--fixture-dir` inputs for artifact sequences. Four
  mocked-runner tests check originals, scope preflight and failed-run records.
  These support skill evaluation, not a new product-management runtime.
- An onboarding audit found that INSTALL's future-update paragraph omitted
  host rediscovery. It now calls for rediscovery or a new session, matching
  existing English/Korean upgrade guidance. The public command remains pinned
  to 0.4.0; no release or registry publication occurred.

## Fresh task results

`pre` uses the starting `f4a376e` skill bytes; `post` uses the unreleased
refactor. Every specialist run here has only its own complete folder installed.
The general run has only the general BANDIT snapshot.

| Case and condition | Independent result | Artifact | Words |
| --- | --- | --- | ---: |
| 11 experiment integrity, pre research | 5/5 pass | [Decision](pre/11-experiment-integrity--bandit-research/output.md) | 299 |
| 11 experiment integrity, post research | 5/5 pass | [Decision](post/11-experiment-integrity--bandit-research/output.md) | 282 |
| 12 public-to-private, pre specify | 5/5 pass | [Actual PRD](pre/12-access-transition-1--bandit-specify/after/docs/PRD.md) | 757 |
| 12 organization-to-project, pre specify | 6/6 pass | [Actual PRD](pre/12-access-transition-2--bandit-specify/after/docs/PRD.md) | 859 |
| 12 public-to-private, post specify | 5/5 pass | [Actual PRD](post/12-access-transition-1--bandit-specify/after/docs/PRD.md) | 773 |
| 12 organization-to-project, post specify | 6/6 pass | [Actual PRD](post/12-access-transition-2--bandit-specify/after/docs/PRD.md) | 866 |
| 07 manual operating capacity, post scope | 4/4 pass | [Scope](post/07-concierge-capacity--bandit-scope/output.md) | 410 |
| 09 linked-policy review, post review | 4/4 pass | [Review](post/09-linked-policy-review--bandit-review/output.md) | 209 |
| 13 combined scope/handoff, post general | 5/5 pass | [Handoff](post/13-combined-issue-handoff--bandit/output.md) | 543 |

[Independent grades](grades.md) give criterion-level locators. Pre-run rubrics
for [07–08](../../rubrics/07-08-operations-and-evidence.md),
[09](../../rubrics/09-linked-policy-review.md),
[11](../../rubrics/11-experiment-integrity.md),
[12](../../rubrics/12-access-transition.md), and
[13](../../rubrics/13-combined-issue-handoff.md) were not revised after these
outputs. A separate grader saw rubrics and artifacts; task agents saw only
their requests, raw fixtures and selected instructions. Grading was not blinded
to condition names.

Case 11 distinguishes assignment from unequal exposure recording and
retransmitted purchases, applies the adopted support guardrail, and avoids
declaring an efficacy winner from immature outcomes. Both versions pass.
Case 13 reads the general entrypoint and its scope, specification, evidence
and change references, then supplies one scope/handoff answer. Actual routing
is recorded separately from semantic quality.

Cases 07 and 09 repeat earlier raw tasks after the shared reference changed.
Case 07's earlier run had all five skills available; this one is standalone.
These are coverage checks, not controlled estimates of an instruction effect.
No baseline or upstream arm was run in this round. The first round's two
passing baseline counterparts remain visible in its separate record.

## Actual artifact carry-forward

Each case-12 sequence starts from the same public-board PRD. Stage 1 rewrites
it as organization-private intake. Its completed input tree and resulting PRD
are preserved before staging stage 2. The second agent receives those exact
bytes, with only its new request and two raw documents overlaid, and rewrites
for project access plus recipient-specific external summaries.

Both chains were independently verified: stage 1's final PRD hash equals
stage 2's initial PRD hash, prior source documents stay byte-identical, and
instruction snapshots match within each chain. [Run summary](run-summary.json)
records hashes and overlay checks. No intermediate PRD was repaired, summarized
or replaced with an expected result.

Each stage is a **fresh agent**, not a resumed conversation. This tests artifact
accumulation, not conversation memory. Actual stage-1 PRDs differ between pre
and post, so stage 2 is not a controlled same-input comparison. Both chains
preserve public observations, bounded retention checks, and the former
organization-access result under their original conditions while distinguishing
new planned checks.

## Evidence integrity and limits

All nine runs used `codex-cli 0.153.4`, `--ignore-user-config`, `--ephemeral`
and host-default settings without a pinned model override. Each exited 0.
Read-only tasks left inputs unchanged; editable tasks changed only their PRD.
Instructions were unchanged during each task. Logs show no product
implementation, product tests, browsing or outreach.

Each archive keeps original inputs, instruction text, output, events, stderr,
metadata and SHA-256 provenance. All retained archive bytes were verified;
pre instruction hashes match the starting commit and post hashes match current
source. The general mascot PNG is hash-only in its archive, as declared by
provenance; its source hash was verified too. Restore PNG bytes separately for
an identical workspace. Historical PM Craft outputs and hashes were not edited.

Staging plus prompt restrictions is not a security boundary against every
outside filesystem read. Maintainers must exclude rubrics and future inputs,
and inspect actual traces. Process success and hash agreement are not semantic
grades. Single runs and unpinned host configuration cannot establish general
reliability or causal improvement.

## Engineering checks and failures

Resource synchronization, both repository validators, all five official
skill-creator metadata checks, **71 Node tests**, **79 Python tests**, `npm pack`
and source ZIP creation passed locally. Node tests used the supported 22 major
(22.23.2); optional Python used 3.11.16. No new cross-platform CI ran.

The [check record](checks/README.md) retains a Node/npx invocation failure and
its controls: inherited `npm_config_call` made nested npm reject its arguments
before BANDIT ran. Removing only that option allowed the full suite to pass;
injecting it under Node 26 reproduced the failure. Product and tests were not
changed to suppress it. Missing PyYAML was resolved in a temporary validator
environment only. A task-local missing `python` word-count command recovered
with `python3` and remains in its raw trace.

These are local unreleased artifacts, not updates to public release 0.4.0.
The [first round](../2026-09-08-overnight/README.md) separately records installer
fixes and their remaining final-check/syscall concurrency gap.
