# Round 4 independent development grades

Case 15's two-run assessment appears first; the completed case 17 and case 16
assessments are appended below. All four listed runs are terminal.

These two completed case 15 runs were graded against the unchanged
[manual outcome pilot rubric](../../rubrics/15-manual-outcome-pilot.md), their
archived raw request/brief, full outputs and complete execution traces. Both
are synthetic, author-designed development checks. The task agents did not
receive the rubric, prior outputs or author diagnoses. The grader knew the arm
names, and root and grader discussed aggregate-versus-session budget
interpretation before the reported assessment. Grading was therefore not fully
insulated; the task agents received no such discussion.

Both proposals satisfy all five meaning-based criteria. This does not establish
actual service feasibility, demand, reliable compliance or a skill advantage.
In particular, a 360-minute budget is not proof of a workable minute-by-minute
schedule or guaranteed delivery under arbitrary response delays.

## Results

| Run | Criteria 1–5 | Complete output words / cap |
| --- | --- | ---: |
| [BANDIT research](pre/15-manual-outcome-pilot--bandit-research/output.md) | Pass, Pass, Pass, Pass, Pass | 491 / 600 — pass |
| [Baseline](pre/15-manual-outcome-pilot--baseline/output.md) | Pass, Pass, Pass, Pass, Pass | 451 / 600 — pass |

Counts were independently calculated with `text.trim().split(/\s+/).length`,
including Markdown tokens. Neither task trace contains a final-output counting
command. Both final outputs are complete and match the last recorded answer;
exit 0 is not used as a quality grade.

## Per-criterion findings

In this table, locators are lines of the corresponding linked `output.md`.
The raw files are byte-identical across arms. `input/request.md:1` requests a
manual final-outcome test, not interviews alone, and forbids actual execution.
`input/brief.md:8–18` defines the service, reachable owners and untested price;
brief:22–35 gives the free work and timing observations; brief:39–46 gives the
six sessions, cash limit, factual-input and owner-publication constraints.

| Frozen criterion | BANDIT research | Baseline |
| --- | --- | --- |
| 1. One bounded test delivering usable final material | **Pass**, 7–18: two relevant shops, one first item each and conditional repeats; photos/dimensions/condition/owner price; draft, owner review, one revision and final title/body/product information. Missing facts are not invented (15); owner sets price, approves and posts (10,16), with no account access or sales promise. | **Pass**, 7–22: two relevant shops with two initial items each, complete factual/photo inputs, owner confirmation/revision and final copyable material. Price and revision entitlement are stated; facts are clarified rather than guessed (18). Owners post; no account login, buyer-data collection or forbidden visit is required. |
| 2. Complete provisional workload, admission and overload control | **Pass**, 3,24–26: correct 119-minute historical total, approximately 30-minute mean and 50-minute maximum; budgets contact, setup, four complete 40-minute item cycles, settlement, follow-up and contingency. First two items exceeding 80 minutes reduce/stop repeat admission and reserve time for accepted work. This is a bounded provisional budget, not a proved capacity claim. | **Pass**, 3,19,22–24,28: approximately 30-minute historical mean and 50-minute maximum; budgets contact/setup, initial production, conditional repeat production, settlement, follow-up, revision contingency and analysis. Extra orders are accepted only if completion fits without consuming the protected allowance; maximum six items is a ceiling, not an unconditional promise. |
| 3. Two-week/contact constraints, delays, accepted work and cash | **Pass**, 14–20,26: only Mon/Wed/Fri responses; first and repeat intake cutoffs; incomplete facts defer admission, slow approval shifts to a scheduled workday, insufficient observation remains incomplete, and no final delivery within the period means a full refund. Accepted work gets reserve time. Existing tools, no paid recruitment/rewards and a 50,000-KRW cash ceiling; refundable receipts retained. | **Pass**, 11–24,34: scheduled evening contacts, complete-data admission, stated turnaround with delayed-reply adjustment, conditional extra work, and refunds for undelivered/unusable items. Slow replies or no intake opportunity do not become rejection. Planned spend is zero using existing tools, with exceptional spending capped at 50,000 KRW; no extra operator is assumed. |
| 4. Decision-changing measures, price, evidence and full effort | **Pass**, 3,8–9,15–18,24,30–36: separates paid orders, final delivery, approval, publication and paid repeats; publication denominator requires at least 48 hours after delivery and repeat denominator requires a new item/order opportunity. The 6,000-KRW unit offer is a proposed test, not proof of the five-item package. Tracks work through final delivery/follow-up; no incremental-sales, profit or scalable-automation claim. | **Pass**, 3,11–13,18–20,28–30: a proposed 12,000-KRW two-item purchase and 6,000-KRW repeat order, not a validated five-item package. Owner review/final delivery differ from observed publication and payment. Captures full item effort, reply waits and owner revision effort, plus contact/settlement; hourly unit arithmetic is provisional and full-cost profitability remains to be checked. |
| 5. Positive/negative/incomplete branches, calibration and scope | **Pass**, 1,20,30–36: provisional development branch requires actual first/repeat paid use plus the total effort cap; modify/stop/incomplete branches preserve missing opportunity and short-window limitations. Korean, 491 words; explicitly a proposal, not an executed test. | **Pass**, 9–13,30–34: proposed small-tool development, modify, stop and incomplete branches; threshold is an interim decision line, not universal validation. Insufficient intake/reply opportunity is not failure or development evidence. Korean, 451 words; the offer is a draft and no execution is claimed. |

## Arithmetic and schedule adjudication

The observed item totals from `input/brief.md:28–31` are **20, 28, 50 and 21
minutes**: 119 minutes total, 29.75 minutes on average. Both outputs' rounded
mean and maximum are correct. They do not turn this four-item, single-shop
sample into validated capacity.

- Research output:24: 60 contact + 30 setup + (40 × 4) complete item work + 30
  payment/settlement + 40 outcome/decision + 40 reserve = **360 minutes**.
- Baseline output:24: 45 contact/conditions + 20 setup + 120 initial item work +
  40 publication/settlement + 60 optional repeat work + 45 delay/revision reserve
  + 30 analysis = **360 minutes**.
- Baseline output:30: 6,000 KRW × (60 / 20 minutes) = **18,000 KRW/hour** before
  excluded overhead/costs. It expressly treats this as an interim unit-effort
  line and requires a separate all-in profitability check, not observed profit.

The calendar and category budgets are not a complete per-session allocation.
It would be unsupported to add all research contact/setup minutes into the
first Monday and declare a demonstrated 90-minute session, or all baseline
contact/setup minutes and declare a demonstrated 65-minute session: the outputs
do not explicitly assign every minute of those aggregate categories there.
Later qualification, repeat offers and follow-up also require contact. Neither
answer prohibits distributing preparatory/production work within the permitted
evenings.

The passing workload judgments rest on complete provisional delivery budgets,
limited intake, protected contingency, conditional repeat admission and
communicated delay/refund routes—not on inventing a missing detailed calendar.
Actual session-level packing remains unverified. Slow replies can reduce the
number of completed/repeated items observed within two weeks; both outputs
allow fewer admissions or incomplete evidence rather than guaranteeing every
planned result. The rubric permits such provisional/staged budgets and does
not require an elaborate workflow or a particular service-level target.

No demonstrated numerical budget overrun or hard commitment to work outside the
six evenings was found. No material outside-rubric failure was established.
One minor evidence-precision issue is retained: research output:3 says payment
was not confirmed, while brief:35 specifically records no money received. The
same answer identifies that work as free and never counts it as a purchase, so
this does not change criterion 4's meaning-based pass.

## Provenance and scope integrity

The current rubric SHA-256 is
`fb6b96b148ed91dfc10b60161e3e908d820e495a6a26289fb7e68b142dfa588a`.
It matches [pre-run-manifest.json:17](pre-run-manifest.json). The manifest's raw
and selected-instruction digests also match the archived research inputs and
snapshot. Its own digest matches
[conditions-before-run.json:23](conditions-before-run.json), which declares both
arms before their recorded starts. These are local receipts, not signed or
independently timestamped attestations.

| Integrity check | Research archive | Baseline archive |
| --- | --- | --- |
| Raw before/after equality | metadata:30–32 and 47–49 match | metadata:30–32 and 42–44 match |
| Instruction before/after equality | metadata:34–38 and 51–55 match; all four archived files present and independently hash-matched | metadata:34,46 are empty snapshots |
| Actual task reads | events:5 lists permitted files; :7 reads request, selected entrypoint, research and durable-evidence guidance; :9 reads brief | events:7 reads request and brief; no PM skill read |
| Terminal state | events:11 `turn.completed`; metadata:44 exit 0 | events:9 `turn.completed`; metadata:39 exit 0 |
| Output retained | Final event:10 equals output; archive-provenance:45–49 hash matches | Final event:8 equals output; archive-provenance:45–49 hash matches |

Every file listed in each `archive-provenance.json` matches its archived digest;
all raw/instruction files also match the metadata before manifests. Neither
archive omits an input, instruction file or PNG (`archive-provenance.json:11–18`).
Metadata and, for research, events contain declared temporary-root normalization;
their archived hashes are therefore checked against the archived hash fields,
not equated to the different original log hashes. This review does not recreate
unretained host state or claim deterministic replay.

Both traces were read in full. They contain only local document reads/listing:
no rubric/diagnosis access, web research, outreach, document delivery, posting,
payment, live experiment, product execution/tests or file edits. The research
entrypoint and its relevant guidance were actually read, not merely present.
The baseline request retains literal `$bandit-research`, but its
[prompt.txt:1](pre/15-manual-outcome-pilot--baseline/prompt.txt) expressly directs
normal product-planning reasoning without loading a PM skill; the observed
trace follows that condition.

One tool recovery is preserved. Baseline events:5 attempts
`rg --files input instructions` and exits 2 because the baseline has no
`instructions` directory. Events:7 then successfully reads both raw inputs.
This does not make the completed final answer incomplete. No product execution
was used for grading; only artifact reads, hashes, word counts and arithmetic.

The two successes are observed proposal-level behavior on this one synthetic
case. They do not demonstrate that the instruction addition caused either
result, that the skill outperforms the baseline, or that the service would fit
real founder time and earn revenue in practice.

## Case 17 — reachable market

Run: [BANDIT research output](pre/17-reachable-market--bandit-research/output.md).
Graded against the unchanged
[case 17 rubric](../../rubrics/17-reachable-market.md), raw request/brief,
complete output and trace. No case-specific author diagnosis was supplied for
this assessment. **All five criteria pass; 432/600 whitespace-delimited words.**
This is an observed estimate/proposal, not market evidence or proof that the
revenue target is achievable.

| Frozen criterion | Grade and exact evidence |
| --- | --- |
| 1. Buying organization, not locations/users/order recipients | **Pass**, output:7–8 reconciles 210 + 170 − 90 = 290 unique locations and 150 + 30 + 10 = 190 organizations; only the organization is billed and recipient cafes/restaurants are excluded. Output:3,9 limits the estimate to the synthetic supplied lists, not a national market. Raw `input/brief.md:8–20,24–48` supports these units. |
| 2. Proposed eligibility vs listed descriptions | **Pass**, output:9 excludes 50 retail-only and 30 non-producer organizations, prioritizes the 62 advertising wholesale, and leaves the other 48 producers for qualification. It expressly says actual regular-wholesale/current-workflow eligibility is unknown. The 62–110 range is candidate coverage, not a proved eligibility interval; the 75% eligibility scenario at output:24 also does not treat all 62 as eligible. Raw brief:55–64 supplies only descriptions and missing workflow/payment observations. |
| 3. Reachable funnel, contact window and MRR target | **Pass**, output:10 uses 12 × 8 = 96 unique first contacts as an unobserved ceiling, not the whole list reached. It proposes 62 known-channel candidates plus 34 unknown-channel candidates, excluding repeat/branch inflation. Output:14 requires 40 active organizations at 60,000 KRW/month and 41.7% contact-to-year-end-active conversion; 64.5% if only 62 are valid. Output:28 preserves the December 6 cutoff and limited follow-up period. |
| 4. Conditional scenarios, sensitivity and timing | **Pass**, output:18–28 makes both eligibility rates and eligible-to-year-end-active conversion assumptions explicit, applies each once, and supplies three correctly rounded MRR scenarios plus target-crossing conditions. Conversion incorporates nonresponse, refusal, payment delay and pre-year-end churn. Fractional organization counts are expectations, not actual subscribers. Product readiness/adoption timing remains unmeasured; no demand, retention or profitable-acquisition result is claimed. |
| 5. Development decision, economical next observation and scope | **Pass**, output:1,32–36 defers full-product development. Sixteen listed candidates over September 14–27 fit two weeks' eight-new-organizations/week ceiling and existing 16-hour combined sales allowance. The proposed observation checks recent workflow, buyer access, the unchanged monthly offer, next-step agreements and elapsed effort with first-contact denominator 16. Seven agreements are only a provisional signal to a paid test, expressly not payment or a list-wide conversion estimate; actual paid use and adoption burden must subsequently support reconsidering development. Korean, 432 words, and explicitly unexecuted. |

### Case 17 arithmetic and possible false positives

Independent calculation confirms:

- Locations: 210 + 170 − 90 = 290, also 150 × 1 + 30 × 3 + 10 × 5 = 290;
  buying organizations: 190; candidate ceiling: 62 + 48 = 110.
- First-contact ceiling: 12 × 8 = 96. Required active organizations:
  2,400,000 / 60,000 = 40; 40/96 = 41.67%; 40/62 = 64.52%.
- Output:24–26 scenarios yield 9.3, 22.505 and 39.5 expected active
  organizations, or 558,000, 1,350,300 and 2,370,000 KRW MRR. The output's
  rounded figures are consistent, not calculation errors.
- Output:28's optimistic eligible pool is 62 + (34 × 0.5) = 79; 40/79 =
  50.63%. If all 96 contacted organizations are eligible and half remain
  active paid subscribers, 48 × 60,000 = 2,880,000 KRW MRR.

The wording “62–110 candidates” does not override the same sentence's explicit
unknown full eligibility or turn 62 into an established eligible lower bound.
Likewise, comparing a 7/16 next-step signal with a 41.7% eventual paid
requirement does not by itself prove a viable funnel. The output does not make
that claim: it limits the signal to advancing to paid validation, says it is
not payment evidence, and requires further paid-use/timing evidence before
revisiting full development. These are retained qualifications, not failures
introduced by substituting a stronger claim than the answer makes.

No material outside-rubric issue was established. The proposed 16-hour check
does not prove contact response or buyer availability, and directory counts
plus assumed conversions do not establish demand or feasible implementation.

### Case 17 integrity

The current rubric digest
`4e7314ecba707e78b1b8dbba8af96d0064a2c897d9d4bc3f6f0b242f1c5e34dc`
matches [case17-before-run.json:15](case17-before-run.json). That local receipt's
raw and selected-instruction digests also match the archived files and metadata.
As the receipt states, this is not an independently signed timestamp.

All files listed in the case 17 archive's `archive-provenance.json` match their
archived SHA-256 fields. Raw inputs match metadata:30–32 and are unchanged at
47–49; the four instruction files match metadata:34–38 and are unchanged at
51–55. No input, instruction or PNG omission is recorded. The final event's
answer equals `output.md`.

The complete trace contains only the permitted listing at events:5 and raw
request/brief plus selected `bandit-research/SKILL.md`, research guidance and
durable-evidence guidance read at events:7. It ends at events:9 with
`turn.completed`; metadata:44 records exit 0. There is no word-count command,
web lookup, contact, signup/payment, experiment, file mutation or product-code
execution. The grade does not treat these integrity checks as evidence of
commercial quality or reliability.

## Case 16 — conflicting adopted authority and narrow PRD edit

Artifact: [actual saved PRD](pre/16-conflicting-authority--bandit-specify/after/docs/PRD.md).
Final response: [change summary](pre/16-conflicting-authority--bandit-specify/output.md).
Graded against the unchanged
[case 16 rubric](../../rubrics/16-conflicting-authority.md), original raw files,
actual after-state and full trace. **All five criteria pass.** The complete
saved PRD is **596/600 whitespace-delimited words**; the separate final summary
is 38 words. The draft guard rejections below are retained and are not scored
as delivered-artifact cap failures.

| Frozen criterion | Grade and exact evidence |
| --- | --- |
| 1. Exact equally adopted policy conflict | **Pass**, after/docs/PRD.md:45–50 identifies rule M-04 in membership policy M-04 versus rule C-03 in contribution policy C-09: the same remaining members, task-detail/activity-history surfaces and existing work/comment author names after v2 self-departure. It records the common approvers and rejects later adoption date as automatic supersession. Raw membership-departure.md:6–9,24–26 and contribution-records.md:6–9,19–21 substantiate the conflict. |
| 2. Disputed rule remains unresolved, with implementation consequence | **Pass**, PRD:30,45–51 leaves D-01 open, identifies the approvers' required choice of superseded rule, and gates name-display implementation/verification only. PRD:67–68 leaves the expected display value conditional. Neither policy source is changed and the feature is not represented as completely settled. |
| 3. Continue the agreed departure journey | **Pass**, PRD:27–43 requires self-action and target/impact confirmation; terminates only that membership; denies subsequent reads/writes including an already-open-page save with visible denial. Account/other memberships and organizational records, content, author IDs and timestamps remain intact. Proposed recovery handles completion, failure, duplicate action and unknown response without new infrastructure or whole-account deletion. Persistent author ID is distinct from the unresolved displayed name. |
| 4. Actual narrow edit and verbatim preservation | **Pass**, PRD:21–72 replaces only sections 3/4 with the bounded handoff. Independent byte comparisons confirm the entire prefix before section 3 and suffix starting at section 5 are unchanged, including original headings/history. Both policy files and request are byte-identical before/after. Both relative policy links resolve in the after-state; no second current plan, policy copy or unrelated file edit is present. |
| 5. Planned checks, historical scope, cap and short handoff | **Pass**, PRD:55–68 supplies observable confirmation, stale access, retained records/organization isolation and recovery scenarios; display remains conditional. PRD:70–81 retains V-01/V-02's original v1.8 staging passes and refuses to reuse them as self-departure/stale-save/name-display proof. Actual PRD is 596 words; output.md:1–3 briefly summarizes edits and the remaining question. No product implementation/test, external lookup or contact occurred. |

No material outside-rubric issue was established. Calling the name rule an open
decision is not a failure to finish the requested artifact: the request
expressly permits unresolved decisions, and the independent agreed flow is
specified. Likewise, a preserved historical pass is not presented as execution
of the new acceptance scenarios.

### Case 16 byte preservation and provenance

The original [input/docs/PRD.md](pre/16-conflicting-authority--bandit-specify/input/docs/PRD.md)
and saved PRD were compared as byte buffers, not normalized text:

| Region or file | Independent result |
| --- | --- |
| Prefix before `## 3. 조직 탈퇴 흐름` | Exact match, 961 bytes; SHA-256 `d7e8f5c4c1d368332c23ae089bc77e71574bb38a1615fdb3950d556f9c7f7fce` |
| Suffix beginning `## 5. 기존 실행 기록` | Exact match, 733 bytes; SHA-256 `0a298ed4737ecc12c73d016e054b8922b86a7d48c1acd9f48441525e57fb20b1` |
| Membership/contribution policies and request | Before/after bytes and metadata digests match for all three |
| Only changed raw file | `docs/PRD.md`: original `53459c22e422c6eeccce7450936bed7cce45ccd723f2d81b0a54ced821de6685`; saved `1483e253f53b773bb16bea3ba20b06a7838af70c92bd8d5b09061c3731b29422` |

The current rubric digest
`1f4a6a67bfa52cd2df60fd4141ef7038454c2652d885e7f174ca15a69cb4e7d4`
matches [case16-before-run.json:17](case16-before-run.json). That local receipt's
raw and all eight instruction digests match the archived originals; it is not
an independently signed timestamp. Every file listed in the archive provenance
matches its archived hash. Original raw files match metadata:30–34; after files
match metadata:53–57. Instruction before/after manifests match at metadata:36–44
and 59–67. No original input, instruction or PNG is missing.

The permitted artifact is explicitly `input/docs/PRD.md` in prompt.txt:2 and
metadata:49. The full trace reads the selected entrypoint, specification,
changes and durable-evidence guidance at events:5, then all raw sources at
events:7. Later commands are document construction/count/preservation guards,
not supplied product code or product acceptance tests. There is no external
research, contact, rubric/diagnosis access or policy mutation in the trace.

### Case 16 count-guard recovery

| Completed event line | Recorded complete-draft count | Outcome |
| --- | ---: | --- |
| events.jsonl:10 | 692 | `AssertionError`, exit 1 before `p.write_text` |
| events.jsonl:12 | 640 | `AssertionError`, exit 1 before `p.write_text` |
| events.jsonl:14 | 607 | `AssertionError`, exit 1 before `p.write_text` |
| events.jsonl:16 | 603 | `AssertionError`, exit 1 before `p.write_text` |
| events.jsonl:18 | 596 | Guard passes; the counted PRD is written; exit 0 |

Each command places the complete-text `<=600` assertion before its file-write
operation. The first four rejected drafts therefore do not become saved PRDs.
The final saved bytes independently count to 596 using
`text.trim().split(/\s+/).length`, matching the task's successful count. Unlike
the case 15/17 outputs, this trace demonstrates actual pre-delivery counting
and revision, not just final cap compliance. The process then ends at
events:20 with `turn.completed` and metadata:50 exit 0. This one observed
recovery does not establish general counting reliability or a causal effect of
an instruction change; no rejected attempt or prior delivered failure is erased.
