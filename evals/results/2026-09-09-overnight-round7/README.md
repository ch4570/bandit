# Overnight development, round 7 — 2026-09-09

Four fresh TASKs revisit a known reporting partial and add an actual PRD rewrite
in a new domain. The cumulative overnight count is **36 executions**, not 36
successful answers. This round changes evaluation fixtures and interpretation
guidance, not the five skills, installers, or runner. Earlier outputs, failures,
partial grades, and artifacts remain intact.

## A partial score is not a diagnosis

The [metric-reporting audit](checks/metric-reporting.md) rechecks case 02 from
its raw observations. Prior outputs correctly retained the populations,
opportunities, time windows and simultaneous changes. They did not miscalculate
repeat use or claim a causal price effect. The repeated partial was omission of
two explicit broader-denominator comparisons under the original rubric's
established interpretation. The original grader had disclosed that ambiguity.

The [fresh repeated pair](grades-02.md) again receives **pass, pass, partial,
pass** under that unchanged interpretation. The full specialist PRD is
[900/900 words](pre/02-offer-change--bandit-specify/output.md); the baseline is
[722/900](pre/02-offer-change--baseline/output.md). Neither trace shows a counting
command, so cap compliance is not proof of a particular counting mechanism.
The old over-limit outputs and partials are not rescored.

Evaluation guidance now separates an incorrect claim, a missing material
condition, and an omitted rubric-requested comparison. New rubrics should tie
required meaning to the task and accept equivalent counts/prose unless a
particular artifact is actually required. This does not soften existing criteria
after observing results or justify a universal ratio checklist in the skills.

## New domain: a library's pickup reminders

[Case 19](../../cases/19-library-pickup-reminders/request.md) asks for a real edit
of `input/docs/PRD.md`, replacing manual SMS with an automated, staff-visible
queue. The adopter has not decided whether to offer enrollment to the existing
50 readers or all 250 cardholders. Supplied disjoint groups distinguish 30 ready
index-hold opportunities, 14 SMS-reached readers, 18 early pickups across all
opportunities and 23 before expiry. The 20 without a ready hold are not failures;
the other 200 cardholders have not been observed. The seven-day hold policy,
consent, account access, physical collection and continuing email remain adopted.

Both arms edit the named PRD and recommend continuing with the original 50.
The [specialist artifact](pre/19-library-pickup-reminders--bandit-specify/after/docs/PRD.md)
is **795/800 words**; the [baseline artifact](pre/19-library-pickup-reminders--baseline/after/docs/PRD.md)
is **741/800**. These are complete edited-file counts, not short final-summary
counts. Both use provisional support allocations totaling the supplied 90
minutes and leave five-day development feasibility unmeasured. No SMS or
enrollment rollout, product implementation, or product test is executed.
The artifact links above point to `after/`; final summaries retain their
task-workspace-relative paths, whose `input/` targets in an archive are originals.

The [pre-run rubric](../../rubrics/19-library-pickup-reminders.md) allows either
rollout choice if its evidence, requirements and operating bounds are coherent.
It does not require every calculable fraction or a predetermined verdict.

[Independent grading](grades-19.md) finds both satisfy its five criteria, but
does not call the specialist artifact error-free. It labels a reader-based
14/18 denominator as “attempts,” although attempt counts are absent, and gives
Nora's adoption the report's September 9 date without source support for that
approval date. These are unsupported local claims, not measured facts or
cosmetic preferences. The broader reader/opportunity counts and proposed
rollout remain correctly bounded. The errors stay in the archived artifact
and the grading record; no successful score erases them or establishes repair.

## Execution and evidence boundaries

The [case-02 receipt](case02-before-run.json) and
[case-19 receipt](case19-before-run.json) freeze raw, rubric and selected
instruction hashes before their respective executions. Each TASK is a fresh
ephemeral process with only raw inputs and, for the specialist, its standalone
complete folder. The baselines have no PM instruction snapshot. Host model
defaults are unchanged but unpinned; web search is explicitly disabled.

Recovered command problems remain in the traces: the case-02 baseline lists an
absent instruction directory before reading the raw inputs; the case-19
baseline also has a recovered listing exit 2. In the case-19 specialist, a
missing `python` command did not perform the intended follow-up edit, although
the enclosing shell command returned 0 because the subsequent `wc` succeeded.
A later `python3` edit succeeds and counts the final PRD at 795 words. These
are recovered execution details, not erased failures or extra planning TASKs.

The original PRDs and other raw evidence are retained separately from edited
artifacts. The [facts-only execution audit](run-summary.json) verifies original
and archived bytes independently of semantic grading; its author also designed
case 19 and is not claimed as that case's independent grader.
This synthetic author-designed set is not a held-out benchmark,
reliability estimate, instruction-caused improvement, superiority result, or
customer evidence. No skill edit is justified by the case-02 reporting partial
alone, and no instruction change was made in this round.

## Engineering checkpoint

Full suites pass [78 Node tests](checks/full-node.txt) on Node 22.23.2 and
[92 Python tests](checks/full-python.txt) on Python 3.11.16. Resource sync,
both repository validators, and all five official metadata checks
[pass](checks/validation.txt); these are not planning-quality scores.
`npm pack` and source ZIP creation pass separately from task grading.
The [check receipt](checks/README.md) records commands and distinguishes the
initial packaging check from the final local source artifacts.

This round's final local artifacts use `dist/overnight-round7/`, preserving all
earlier same-version builds. No commit, new CI run, public release or registry
publication occurs. The public install command still pins 0.4.0.
