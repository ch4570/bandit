# Round 8 — independent regression-probe grades

These are manual, meaning-based grades of three fresh synthetic TASK outputs
against the unchanged rubrics recorded in [post-before-run.json](post-before-run.json).
They provide bounded regression coverage after the evidence-guidance edit, not
a held-out benchmark, causal repair result, reliability estimate, or customer
validation. No TASK was run or retried during grading, and no rubric, fixture,
instruction, or answer was changed.

Word counts use whitespace splitting of the **complete archived output.md**,
including headings, lists, and tables; no region was excluded. All three requests
cap the answer at 600 words.

| Case / arm | Full-answer words | Fixed criteria |
| --- | ---: | --- |
| [13 — combined issue handoff / bandit](post/13-combined-issue-handoff--bandit/output.md) | 505 | 5 pass, 0 partial, 0 fail |
| [17 — reachable market / bandit-research](post/17-reachable-market--bandit-research/output.md) | 405 | 5 pass, 0 partial, 0 fail |
| [18 — onboarding investment / bandit-scope](post/18-onboarding-investment--bandit-scope/output.md) | 540 | 5 pass, 0 partial, 0 fail |

## 13 — combined issue handoff

Fixed rubric: [13-combined-issue-handoff.md](../../rubrics/13-combined-issue-handoff.md).
Locators below refer to the [complete answer](post/13-combined-issue-handoff--bandit/output.md).

1. **Pass.** Lines 3–14 choose the complete text-report-to-visible-resolution
   trial and introduce its developer handoff in the same answer. The old screen
   sketch retains proposal status; no workshop or separate command is required.
2. **Pass.** Lines 9–12 count 1.5 + 1 + 0.5 = 3 developer-days inside four,
   retain walkthrough time, explain cuts, and contrast manual messages/sheets
   and an intake-only scope. Line 24 treats missing implementation support and
   fixes as re-estimation risks and permits delaying first use, not guaranteed
   delivery within the spare day.
3. **Pass.** Lines 16–20 connect shelf, stable employee ID, shared saved report,
   current lead role, and explicit resolution note/action. Opening a report does
   not resolve it; the reporter later reads the same saved result. Existing
   identity/shelf/store integrations remain, and former staff lose access.
4. **Pass.** Lines 17–20 withhold success while the result is unknown, preserve
   input and the submission identifier, and make retries return/create only the
   same report. A separate report for recurrence or incorrect content is
   distinguished from retry. No offline queue or replacement database is made
   mandatory; line 24 explicitly leaves store support unverified.
5. **Pass.** Lines 14 and 22–24 label discretionary policies as recommended
   defaults and acceptance checks as planned, with no implementation/test
   success claimed. Scenarios cover reporting, permissions, shared resolution,
   and uncertain submission. The complete Korean answer is 505 words, and the
   recorded actions and unchanged input hashes support the requested read-only
   boundary.

Routing observation, separate from these grades: completed commands at lines
7 and 9 of [events.jsonl](post/13-combined-issue-handoff--bandit/events.jsonl)
read `instructions/bandit/SKILL.md`, `decisions.md`, `specification.md`, and
`evidence-and-decisions.md`; line 12 additionally reads `changes.md`. This
records file access, not proof that any one instruction caused the answer.

Additional factual findings: no material unsupported factual claim identified.
The suggested retry/storage behavior is a proposed requirement, not an assertion
that the existing store already implements it.

## 17 — reachable market

Fixed rubric: [17-reachable-market.md](../../rubrics/17-reachable-market.md).
Locators below refer to the [complete answer](post/17-reachable-market--bandit-research/output.md).

1. **Pass.** Lines 7–10 reconcile 290 unique locations to 190 buying
   organizations, exclude recipient cafes/restaurants as payers, and keep the
   estimate tied to the supplied lists rather than a national market.
2. **Pass.** Lines 8–9 prioritize the 62 listed wholesalers, retain 48
   channel-unknown producers as additional candidates, and exclude the 50
   retail-only and 30 non-producer organizations. The 62–110 range explicitly
   denotes potential candidates, not proven workflow-eligible buyers.
3. **Pass.** Lines 10 and 14 use the 12 × 8 = 96 unique-contact ceiling and
   40 active paying organizations at KRW 60,000/month, requiring 41.7%
   contact-to-year-end-active-paid conversion. Repeated contacts and December
   follow-up do not create extra reachable organizations.
4. **Pass.** Lines 16–26 expose eligibility, conversion, year-end retention,
   population, and price across three conditional scenarios. Approximately
   KRW 300,000–2,250,000 MRR and the 53.3%/80.8% conversion break-even conditions
   follow the stated assumptions. Rounded customer/revenue expectations are
   labeled; sales, implementation, and adoption timing remain unmeasured.
5. **Pass.** Lines 1 and 28–32 defer full-product investment and propose a
   first-week, eight-organization observation within eight founder hours.
   Eligibility and specific paid-trial scheduling would inform a smaller next
   commitment; the proposed threshold is not validation, and a scheduled start
   is explicitly not payment. The full Korean memo is 405 words and its recorded
   commands only read supplied files.

Additional factual findings: no material unsupported factual claim identified.
The scenario range is assumption-driven, not a statistical interval or demand
forecast. Proposed contact and payment observations remain unexecuted.

## 18 — onboarding investment

Fixed rubric: [18-onboarding-investment.md](../../rubrics/18-onboarding-investment.md).
Locators below refer to the [complete answer](post/18-onboarding-investment--bandit-scope/output.md).

1. **Pass.** Lines 5–9 use the complete 16-account cohort: 12 stored-import
   shops but nine usable stock checks. No attempt/event count is promoted to
   account success or adjusted for nonexistent missing/maturing outcomes.
2. **Pass.** Lines 8–13 distinguish five rescued successes from four successes
   without rescue and zero support. Issue notes are not treated as causal
   evidence. The six paying incumbents remain separate from the free pilot;
   neither their payments nor download requests establish renewal or lift.
3. **Pass.** Lines 15 and 23–25 compare 24 report-engineering hours with
   26 import-review hours, keeping founder time separate. They reserve the
   observed 120 report minutes plus 120 for other customer work, initially
   postpone all eight admissions, and condition at most two sequential
   admissions on measured capacity within four hours. The 25-minute report
   estimate and roughly 303-minute eight-shop scenario remain hypotheses.
4. **Pass.** Lines 1 and 15–25 commit the week to bounded report download and
   fairly recognize import review's usability case. The answer retains the
   paid report obligation and manual fallback, specifies consequential cuts,
   and does not assume nominal engineering fit establishes delivery or savings.
5. **Pass.** Lines 23 and 27 time one reporting cycle including assistance and
   fallback inside the founder budget. Report effort remaining at least
   120 minutes would undermine the capacity rationale and prompt reconsideration;
   later admissions also require usable-outcome/support observations. This is
   a proposed check, not a result. The complete English answer is 540 words;
   recorded commands only inspect supplied files.

Additional factual findings: no material unsupported factual claim identified.
A read-only recomputation of the supplied CSV confirms 35 attempts, 14 stored
events across 12 shops, nine usable shops, seven rescued shops including five
usable ones, and 365 support minutes. The rubric does not require displaying
all those event counts when no event-to-shop inference is made.

## Provenance and limits

For all three cases, current raw fixtures and archived input bytes match the
pre-run raw hashes; current rubric hashes also match that receipt. Metadata
records terminal exit 0, disabled web search, read-only execution, and unchanged
before/after input and instruction maps. Inspected traces show file enumeration
and reads, not implementation, product tests, contacts, or external actions.
Those structural observations support provenance and scope checks; the meaning
grades above come from reading the answers against the inputs.

The specialist archives each retain their four instruction files. Case 13 used
the normal general-arm layout, not specialist `--standalone`; the rejected
initial CLI plan and its correction are disclosed in
[general-launch-correction.md](general-launch-correction.md). Its metadata
records ten original general instruction files. The archive retains nine files
and records the mascot PNG by hash only, explicitly noted in
[archive-provenance.json](post/13-combined-issue-handoff--bandit/archive-provenance.json).
All retained instruction bytes match the pre-run skill map and their run
metadata; the omitted image was not byte-verified from this archive.

These three answers show no failure under their fixed criteria in this review.
That does not establish arbitrary-task correctness, repeatability, or that the
round-8 instruction edit caused the passing outcomes. No mechanism or magnitude
of improvement is inferred from the grades.
