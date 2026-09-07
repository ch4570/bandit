# Recorded development results — 2026-09-07

**No comparative quality advantage was established.** In the three paired cases,
baseline, pinned upstream, and PM Craft each received 11 pass, 1 partial, and
0 fail judgments against the same 12 conditions. Two additional PM Craft tasks
passed their eight conditions but had no comparison arm.

These are small, synthetic development checks shaped by the concerns used to
write the skill. They are not hidden tests or an estimate of general PM ability.

## Outputs and grades

| Case | Baseline output | Upstream output | PM Craft output | Rubric outcome |
| --- | --- | --- | --- | --- |
| 01: separate votes | Not run | Not run | [Forward output](01-multiple-decisions--pmcraft-forward/output.md) | PM Craft: 4 pass |
| 02: offer change | [Output](02-offer-change--baseline/output.md) | [Output](02-offer-change--upstream/output.md) | [Output](02-offer-change--pmcraft/output.md) | Each: 3 pass, 1 partial |
| 03: intent review | [Output](03-intent-review--baseline/output.md) | [Output](03-intent-review--upstream/output.md) | [Output](03-intent-review--pmcraft/output.md) | Each: 4 pass |
| 04: incomparable scores | [Output](04-incomparable-scores--baseline/output.md) | [Output](04-incomparable-scores--upstream/output.md) | [Output](04-incomparable-scores--pmcraft/output.md) | Each: 4 pass |
| 05: small research | Not run | Not run | [Output](05-small-research--pmcraft/output.md) | PM Craft: 4 pass |

Read the [01/04 grading](grades-01-04.md) and [02/03/05 grading](grades-02-03-05.md)
for excerpts, line references, judgments, and limitations. Graders knew the arm
names; this is independent output review, not blind grading. No scores were
added for following a preferred template or producing more text.

Case 02's partial condition applies equally to all three arms: each correctly
used four repeat users out of six people with a repeat opportunity, preserved
the other cohorts, and rejected a causal price claim. None explicitly explained
both alternative denominators, four out of fourteen senders and four out of
twenty-four registrants, as the rubric requested. This is a reporting omission,
not an observed incorrect rate. We retained the stricter judgment rather than
loosening the rubric after seeing the outputs.

In case 04, baseline and upstream calculated A's standalone value of 640 while
explicitly saying it was based on sessions/month and could not rank the other
options. That was valid bounded arithmetic and was not penalized. PM Craft's
omission of the arithmetic is not evidence of greater accuracy.

## Execution and source provenance

Ten CLI runs completed with exit code 0 using Codex CLI **0.153.4**, fresh task
workspaces, `--ignore-user-config`, `--ephemeral`, and a read-only sandbox. No
model override was supplied. The precise backend model revision and reasoning
settings were not pinned or recorded; matching CLI defaults is a narrower
condition than a controlled, pinned-model benchmark.

The three paired cases used the same request, raw input, and output cap in each
arm. The [runner](../../run_local.py) provided the appropriate upstream entry
procedures and made the full clean upstream tree available for dependencies.
Slash commands were read as instructions; native plugin installation or slash
command dispatch was not tested.

PM Craft instruction hashes match [source commit d34df23](https://github.com/ch4570/pm-craft/tree/d34df23cbe5568ea22f1a28ca19e0bd841fa8dcd/skills/pm-craft).
Upstream is [phuryn/pm-skills at 18468a9](https://github.com/phuryn/pm-skills/tree/18468a95b427e70e258b51389796367c6f684e7d).
The runner supplied no rubric, expected answer, author diagnosis, or prior output.
Recorded commands read the permitted inputs and instruction snapshots. Input
hashes remained unchanged; no provided product code or tests were executed.

Case 01 was a separate fresh subagent forward test with the skill, request, and
brief only. Its harness differs from the CLI cases and its settings were not
recorded in equivalent detail. It is not used for timing or usage comparisons.

## Raw artifacts and publication handling

Each CLI output directory includes its unchanged final output, `prompt.txt`,
`metadata.json`, `events.jsonl`, `stderr.txt`, and the exact `input/` snapshot.
Metadata records input and instruction hashes, command, elapsed time, and exit
code. The [run summary](run-summary.json) collects output hashes, reported usage,
and completed read commands. There were no failed CLI runs in this recorded set.

Case 01's public output changes only two machine-specific input link targets to
portable relative paths. Its [metadata](01-multiple-decisions--pmcraft-forward/metadata.json)
records the transformation and both hashes. Grading documents also use portable
path references; their judgments and excerpts are retained.

Upstream text appears in the upstream tool transcripts. It remains covered by
Pawel Huryn's [MIT license](UPSTREAM-LICENSE.txt). It is reference material in
the evaluation record, not part of the installed PM Craft skill.

## Usage and what remains to improve

The CLI reported the following input-token totals:

| Paired case | Baseline | Upstream | PM Craft |
| --- | ---: | ---: | ---: |
| 02 | 41,944 | 46,362 | 69,603 |
| 03 | 41,666 | 51,901 | 58,818 |
| 04 | 41,753 | 43,687 | 44,053 |

PM Craft used more reported input tokens in each paired case. These totals
include cached and repeated host context across calls; they are not skill file
lengths, billable-token totals, or a cost estimate. Per-run output usage and
elapsed time are preserved in the raw records. Concurrent runs, caching, host
overhead, and unpinned backend settings prevent a reliable latency ranking.

The results support keeping the skill's explicit contracts and further testing
reference selection. They do not justify claiming superior planning quality or
token savings. Next useful evidence is held-out work with conflicting documents
and decisions evolving across turns, a pinned model, repeated runs, and blind
grading. No real customer research or production application was validated here.
