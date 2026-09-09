# Bounded-workflow development check — 2026-09-09

The candidate passed 5 of 6 task grades, the current skill 4 of 6, and the
no-BANDIT baseline 6 of 6. This small synthetic development check does **not**
establish a quality advantage or cost savings. The automated comparison is
`incomplete`: all runs report token usage, but the CLI does not report observed
model or reasoning-effort identity. Requested settings are not substituted for
those missing observations. Monetary cost and cost per successful task remain
unavailable, not zero. See [the generated summary](summary.json).

## Conditions and method

The [protocol](protocol.json) records the execution plan, not a preregistered
benchmark. Three synthetic tasks with ordinary irrelevant documents were
authored independently of the candidate instructions. They were held out from
that authoring pass; they are now public development fixtures. Each condition
ran twice on each task, with six counterbalanced order permutations. Independent
case lanes overlapped on one host, so elapsed time and cache effects are not
controlled causal measurements.

All 18 fresh ephemeral runs requested `gpt-6-astra`, reasoning `low`, CLI
`0.153.4`, disabled web search/multi-agent use, and a 240-second limit. Per-case
word budgets were 800/900/1,300. These are requested settings and prompt limits,
not provider billing caps. Current instructions are pinned to `a2d52c5`; candidate
instructions are the skill tree in this record's containing commit. Every run
records input, instruction, and runner hashes. Both skill conditions installed
all five siblings and selected the appropriate specialist; this is not a
standalone-specialist installation-cost experiment.

Executing models received only raw inputs and the applicable skill snapshot,
not criteria, diagnoses, future requests, or other outputs. Three independent
graders received anonymous Q labels, sources, and prewritten meaning criteria.
They did not receive conditions, instructions, or execution logs. Output style
could still provide clues; this is not an attested double-blind study. Grades
are bound to saved output bytes and, for rewrites, the PRD bytes. Anonymous labels
resolve through `blind_label` in [the manifest](comparison.json); grader `source/`
locators refer to the corresponding case's preserved `original-input/`.

## Observations, including failures

| Condition | Review | Scope | Rewrite | All grades | Input | Cached input (included) | Output | Summed run seconds |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| Baseline | 2/2 | 2/2 | 2/2 | 6/6 | 555,683 | 412,928 | 8,436 | 356.869 |
| Current | 0/2 | 2/2 | 2/2 | 4/6 | 648,558 | 447,872 | 9,339 | 390.310 |
| Candidate | 1/2 | 2/2 | 2/2 | 5/6 | 626,533 | 404,864 | 9,694 | 442.870 |

All processes exited zero and all workspace integrity checks passed. Quality
failure rates were 0/6, 2/6, and 1/6 respectively. The three failed reviews found
the principal isolation and recovery defects but omitted the prewritten
criterion distinguishing undefined same-key/different-filter policy from a
demonstrated defect. The failures were disclosed and retained; the rubric and
outputs were not revised to obtain a pass. See the original grades for
[review](grades/07-export-review/grades.md),
[scope](grades/08-callback-scope/grades.md), and
[rewrite](grades/09-pickup-prd-rewrite/grades.md).

The candidate's input total was lower than current, but its uncached input
(221,669 versus 200,686), output, and summed elapsed time were higher. No price
was inferred. There were no whole-task retries; all supplied attempts, including
quality failures, contribute to totals. Ordinary failed file lookups also remain
in raw events and their usage is not subtracted. Cached input is already inside
input; reasoning is already inside output. Cache-write counts were reported as
zero, not filled in for missing fields. Exact breakdowns remain in the summary.

Transcript inspection found no web, MCP, or collaboration-tool events. Native
multi-agent execution was disabled. All candidate runs explicitly read the
selected entrypoint and shared boundary reference. One current scope run showed
reference reads but no separate entrypoint-read command; automatic host injection
is not independently attested by this log. None of this measures development
grader/reviewer model cost, which was not available and is reported separately
as unavailable rather than folded into product-run totals.

## Actual continuation

A separate candidate-only session completed the initial rewrite, then resumed
the exact same thread with the held-back West-only/four-staffed-hour request.
Both turns passed integrity; independent content grading also passed. The
[receipt](continuation/metadata.json), prompts, raw events, and both PRD versions
are preserved. This was a persisted/resumed session, not an ephemeral run or a
second request preloaded into the first prompt.

The final session snapshot reports 311,598 input, 268,544 cached input, and 3,493
output tokens, with 179.996 summed seconds. The first-turn snapshot is already
included and must not be added again. This extra session is separate from the
matched comparison; it does not demonstrate comparative efficiency. Its actual
model identity and monetary cost remain unavailable too.

## Evidence and limits

Published runs preserve raw events, stderr, prompts, metadata, original inputs,
and final input artifacts byte-for-byte. Duplicate installed skill folders and
their large mascot assets are omitted from the published workspace copies;
instruction hashes and source revisions identify those snapshots. Full isolated
workspaces were retained locally. [The export inventory](evidence-sha256.json)
binds the 300 evidence files exported before this explanatory README was added.
No historical PM Craft or earlier BANDIT result was changed.

This check supports further investigation, not a savings claim, reliability
estimate, business validation, or proof that all planning tasks improve.
Independent static instruction review, Tier 1 validation, and a zero-finding
static security scan were additional development checks, not substitutes for
the task grades above.
