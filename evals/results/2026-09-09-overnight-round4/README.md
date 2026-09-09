# Overnight development, round 4 — 2026-09-09

Four fresh runs extend the previous round's checks to a manual-service pilot
proposal requiring final delivery, a narrow PRD edit with conflicting adopted
policies, and a reachable-market estimate. All satisfy their five fixed meaning-based
criteria. The baseline also passes. No new behavioral defect warrants another
instruction change from these results, so the five skills remain byte-identical
to round 3's final source.

These are synthetic, author-designed development checks, not a held-out
benchmark, reliability estimate, causal improvement claim, or evidence of
customer demand. The broader overnight effort continues. This record does not
erase earlier length failures, denominator partials, or web-coverage limits.

## Results

| Case and arm | Independent result | Artifact | Words / cap |
| --- | --- | --- | ---: |
| 15 manual outcome pilot, standalone research | 5/5 pass | [Proposal](pre/15-manual-outcome-pilot--bandit-research/output.md) | 491 / 600 |
| 15 same raw task, baseline | 5/5 pass | [Proposal](pre/15-manual-outcome-pilot--baseline/output.md) | 451 / 600 |
| 16 conflicting authority, standalone specify | 5/5 pass | [Actual edited PRD](pre/16-conflicting-authority--bandit-specify/after/docs/PRD.md) | 596 / 600 |
| 17 reachable market, standalone research | 5/5 pass | [Estimate](pre/17-reachable-market--bandit-research/output.md) | 432 / 600 |

[Grades](grades.md) contain criterion-level locators and limitations;
[run summary](run-summary.json) records hashes and observed execution details.
Counts split the complete requested artifact on whitespace, including Markdown
tokens. Case 16's short final summary is 38 words; its cap applies to the actual
PRD, not that summary. `pre` means the source at the start of this round, not a
claim that a new correction followed. No `post` condition or upstream run was
needed here.

## What these checks add

**Manual delivery, not an interview substitute.** Case 15 requires usable final
listing material for shop owners, within six one-hour evenings and a cash cap.
Both proposals budget intake, production, clarification/revision, delivery,
follow-up and contingency, with conditional repeat admission and delay/refund
routes. This exercises a manual outcome proposal after the research guidance
changed in round 3. It does not prove that change caused the result: the
baseline also supplies a bounded test.

Both budgets total 360 minutes. Neither is a complete per-session allocation
or proof of actual capacity under arbitrary reply delays. The aggregate
category budgets do not establish a particular overlong Monday; grading does
not invent an unprovided calendar either. These remain provisional, staged
proposals. Actual delivery, publication, payment and profitable operation were
not observed.

**Conflicting authority plus a narrow real edit.** Case 16 differs from earlier
adopted-versus-unadopted and explicit-supersession cases. Both policy documents
are adopted for the same version, audience and surfaces, with the same approvers,
but prescribe incompatible departed-author name displays. The edited PRD keeps
that decision open rather than selecting the later date or inventing distinct
audiences. It continues the agreed membership/access/content rules and labels
additional recovery behavior as a proposal.

Only sections 3 and 4 change. The prefix containing the title, preamble and
sections 1–2, and the suffix containing sections 5–6, remain byte-identical.
The two historical staging checks stay attached to their original conditions;
they do not become proof of the new self-departure behavior. All other raw
files are unchanged. This is an actual document edit, not implementation or
runtime access-security verification.

**Reachable buyers instead of an ornamental market total.** Case 17 reconciles
290 listed locations to 190 buying organizations, distinguishes potentially
relevant descriptions from verified workflow eligibility, and limits new
contacts to the supplied twelve-week schedule. The output identifies a ceiling
of 96 first contacts and the 40 active paying organizations required for the
stated MRR. Its numeric scenarios expose qualification and conversion
assumptions instead of treating directory entries or proposed commitments as
customers. The follow-up is a proposed observation, not executed research or
validated revenue.

## Preserved intermediate failures

Case 16 actually counts complete candidate PRDs before writing. Four candidate
guards reject **692, 640, 607 and 603 words**; each exits before its write call.
The next candidate has **596 words**, passes the count and unchanged-section
assertions, and is saved. All rejected candidate text and errors remain in
the trace. These are recovered editing attempts, not four delivered cap
failures. They establish observed counting in this editable-artifact run,
not reliable cap compliance for all future chat-only answers or a token-saving
mechanism. Round 3's two delivered over-limit outputs remain failures.

The baseline's initial `rg --files input instructions` exits 2 because no
instruction directory is installed. It then reads both raw files successfully.
That recovery is retained and does not make its completed answer incomplete.

## Pre-run records and limits

The [case 15 receipt](pre-run-manifest.json) was retained in round 3 before any
case 15 task, and [conditions](conditions-before-run.json) declare both arms
before their starts. Separate [case 16](case16-before-run.json) and
[case 17](case17-before-run.json) receipts hash each raw fixture, rubric and
complete selected skill before launch. All match the retained artifacts.
These local records are not signed or independently timestamped attestations.

Task agents receive only their raw inputs and assigned instructions; the
baseline has no PM snapshot. Rubrics, author diagnoses and previous outputs
remain outside their workspaces. A separate grader sees the artifacts and
rubrics and knows arm names. Root and grader discussed the distinction between
aggregate budgets and explicit session assignments; grading is not represented
as blinded or insulated from that calibration. No rubric was revised after
seeing these outputs.

All four use `codex-cli 0.153.4`, ephemeral fresh tasks, ignored user config,
explicitly disabled web search and host model defaults without an override.
Case 16 permits only its PRD edit; the other cases are read-only. Instructions
remain unchanged, and the traces show no product implementation/tests, external
research, outreach, payments or experiment execution. Document-edit/count
scripts are not product tests. Process completion and hash agreement are
separate from semantic grades; single unpinned runs cannot establish general
reliability or a skill advantage.

## Engineering checkpoint

Resource synchronization, both repository validators and all five official
skill metadata checks pass. **73 Node tests** pass on Node 22.23.2 and **87 Python
tests** pass on Python 3.11.16. The machine's older system Python is not used.
As in round 3, the nested npm command removes inherited `npm_config_call`; the
temporary metadata-validator environment introduces no end-user dependency.
No new engineering code or product-skill bytes changed in this round.

`npm pack` and source ZIP creation pass, separately from these behavioral
findings. This round's final local artifacts use `dist/overnight-round4/` so
earlier same-version artifacts are not overwritten. Earlier artifacts and the
historical PM Craft evidence are preserved. No commit, CI run, public release
or registry publication occurred; the public install command remains pinned
to 0.4.0.
