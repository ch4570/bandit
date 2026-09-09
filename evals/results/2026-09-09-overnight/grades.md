# Round 2 semantic grades

Independent grading of nine completed runs against the predeclared rubrics,
using archived requests, raw fixtures, final artifacts, metadata and execution
events. No intended improvement, author diagnosis or source-change rationale
was supplied to the grader. Grade meanings are pass, partial and fail; semantic
equivalents count. No rubric or task artifact was changed while grading.

All nine final artifacts pass their applicable criteria. No material unsupported
claim, arithmetic error, false-positive review finding or incomplete final
artifact was identified. These are synthetic, author-designed development
diagnostics. Passing these cases is not evidence of customer demand, runtime
correctness, a quality advantage, or general reliability. The pre/post labels
identify recorded instruction snapshots; they do not establish a causal effect.

## Runs and actual word counts

Counts use whitespace-delimited words in the archived final artifact, not a
task agent's claimed count. Sequence runs are graded on `after/docs/PRD.md`;
their brief conversational summaries are not substitutes for the edited PRD.

| Run | Graded artifact | Words / limit | Criteria |
| --- | --- | ---: | --- |
| Pre 11 research | [output](pre/11-experiment-integrity--bandit-research/output.md) | 299 / 500 | 1–5 pass |
| Post 11 research | [output](post/11-experiment-integrity--bandit-research/output.md) | 282 / 500 | 1–5 pass |
| Pre 12 stage 1 | [PRD](pre/12-access-transition-1--bandit-specify/after/docs/PRD.md) | 757 / 900 | 1–5 pass |
| Pre 12 stage 2 | [PRD](pre/12-access-transition-2--bandit-specify/after/docs/PRD.md) | 859 / 900 | 1–6 pass |
| Post 12 stage 1 | [PRD](post/12-access-transition-1--bandit-specify/after/docs/PRD.md) | 773 / 900 | 1–5 pass |
| Post 12 stage 2 | [PRD](post/12-access-transition-2--bandit-specify/after/docs/PRD.md) | 866 / 900 | 1–6 pass |
| Post 07 scope | [output](post/07-concierge-capacity--bandit-scope/output.md) | 410 / 600 | 1–4 pass |
| Post 09 review | [output](post/09-linked-policy-review--bandit-review/output.md) | 209 / 400 | 1–4 pass |
| Post 13 general | [output](post/13-combined-issue-handoff--bandit/output.md) | 543 / 600 | 1–5 pass |

In the tables below, `output.md:N` or `PRD.md:N` identifies a line in that
column's linked final artifact. Source and event locators are relative to the
corresponding run directory. Every referenced run directory is linked above.

## 11 — Experiment integrity

Frozen [rubric](../../rubrics/11-experiment-integrity.md).
Pre artifact: `pre/11-experiment-integrity--bandit-research/output.md`.
Post artifact: `post/11-experiment-integrity--bandit-research/output.md`.

Raw checks: `input/exports/assignments.csv:2–7` totals 1,000 accounts per arm;
`input/exports/backend-outcomes.csv:2–3` supplies 95/93 paid accounts and 8/39
support accounts. `input/exports/client-events.csv:2–3` and
`input/instrumentation.md:8–15` explain exposure and delivery differences.
`input/experiment-plan.md:22–44` supplies the observation schedule and adopted
operating rule. These sources were inspected for both outputs.

| Criterion | Pre finding and locator | Post finding and locator |
| --- | --- | --- |
| 1. Assignment/outcome units and maturity | **Pass.** `output.md:3,9,11`: 1,000 per arm, 9.5%/9.3%, no completed seven-day observation; no final effect or statistical loss claim. | **Pass.** `output.md:5,11`: same denominators and purchase rates; three-day maximum follow-up; neither superiority nor inferiority established. |
| 2. Dashboard integrity | **Pass.** `output.md:7–9`: 124 B deliveries versus 93 distinct IDs, unequal exposure triggers, 950/620 exposures, balanced assignment and all-assignment outcome denominator. | **Pass.** `output.md:8,11`: duplicate deliveries and incomparable exposure conditions identified; exposure imbalance is not labeled assignment failure. |
| 3. Timing and repeated monitoring | **Pass.** `output.md:11`: three-day snapshot, September 26 review and no early efficacy rule; first apparent doubling is not a winner. | **Pass.** `output.md:11`: immature outcomes, planned September 26 review and unapproved first-doubling selection remain explicit. |
| 4. Account-based guardrail | **Pass.** `output.md:1,3`: 0.8%/3.9%, 39 accounts rather than 50 tickets; pause new B assignments, route current participants to A and record crossover. | **Pass.** `output.md:1,5`: same correct operating-rule application and crossover recording. |
| 5. Decision, economical check and limits | **Pass.** `output.md:1,13`: pause and inspect existing support records; causes and possible misclassification remain hypotheses; no live validation claim. | **Pass.** `output.md:1,3,14`: pause and inspect existing B support records; synthetic snapshot, unknown cause and unchanged settings are explicit. |

Neither answer separately prints `124−93=31` or `93/620=15%`. Both explain
the duplicate deliveries and incompatible exposure conditions, then use all
assigned accounts for the adopted outcome. That satisfies the meaning of
criterion 2 without requiring those literal calculations. No rubric-level
regression or improvement is established by these two passes.

## 12 — Access transition, stage 1

Frozen [rubric](../../rubrics/12-access-transition.md), Stage 1 only.
Pre artifact: `pre/12-access-transition-1--bandit-specify/after/docs/PRD.md`.
Post artifact: `post/12-access-transition-1--bandit-specify/after/docs/PRD.md`.

Applicable raw authority is `input/docs/private-intake-decision.md:5–15` and
`input/docs/data-policy.md:3–10`. Historical observations are
`input/docs/public-pilot.md:7–17`; the original PRD is also archived in `input/`.

| Criterion | Pre finding and locator | Post finding and locator |
| --- | --- | --- |
| 1. Coherent new product | **Pass.** `PRD.md:7–9,46–48`: replaces public behavior with internal intake; proposes a measurable 14-day pilot without adoption evidence. | **Pass.** `PRD.md:7–9,44`: coherent internal scope and proposed registration-to-review observation; no invented internal demand. |
| 2. Access and migration | **Pass.** `PRD.md:13–24,42`: current invited membership, old-account/link and other-organization denial, removal/stale-save handling, protected old URLs and copied-content limits. | **Pass.** `PRD.md:13–24,38–40`: same access boundary, denied-response protection, removal/stale saves and no promise to retract external copies or indexes. |
| 3. Policy/processing continuity | **Pass.** `PRD.md:30–38`: author-only intake editing, restricted processors, state sequence/no reopening, original attribution, exact 180-day retention and manual owner deletion. | **Pass.** `PRD.md:28–34`: retained author/processor rules and authoritative data policy; access loss does not reset retention or grant deletion. |
| 4. Historical evidence | **Pass.** `PRD.md:61–63`: E1 remains 36 recipients/21 writers/38 requests under public-v1; V1 historical pass and V2 bounded staging pass remain truthful. | **Pass.** `PRD.md:46,57`: same E1 provenance and counts; V1 historical success and V2 fake-clock/synthetic-data limits preserved. |
| 5. Bounded handoff | **Pass.** `PRD.md:30,46,48–57`: observable submission/editing, denial, removal/stale-save and policy-continuity checks; D3/D4 proposed; only PRD edited, under limit, no required new command/approval cycle. | **Pass.** `PRD.md:22,24,32,50–57`: reasoned draft defaults and observable submission/editing, old-link denial, stale saves and retention checks, all unexecuted; only PRD edited, under limit. |

No substantive Stage 1 defect was found in either final PRD. The later stage
does not replace or erase these separate Stage 1 grades.

## 12 — Access transition, stage 2

Frozen [rubric](../../rubrics/12-access-transition.md), Stage 2.
Pre artifact: `pre/12-access-transition-2--bandit-specify/after/docs/PRD.md`.
Post artifact: `post/12-access-transition-2--bandit-specify/after/docs/PRD.md`.

New raw authority is `input/docs/project-access-decision.md:5–15`; the original
data policy remains applicable. `input/docs/private-prototype-checks.md:7–15`
defines V3, its limits and the unadopted implementation shortcut.

| Criterion | Pre finding and locator | Post finding and locator |
| --- | --- | --- |
| 1. Targeted supersession | **Pass.** `PRD.md:7–20,66`: current organization/project membership and owner exception replace broad reading; processors remain project-limited; shortcut rejected. | **Pass.** `PRD.md:7,13–24,50`: same current access boundary, owner exception and restricted processors; original authorship and organization-ID shortcut confer no extra authority. |
| 2. Migration and movement | **Pass.** `PRD.md:9,20,30,40`: one project, owner-only unassigned project, owner movement, current checks and preserved records/retention; reasoned automatic card revocation and new authorization. | **Pass.** `PRD.md:13,24,28,32,40`: owner-only unassigned/movement, fresh destination authority and preserved record/retention; explicitly proposed coordinated movement and revocation prevent silent external authorization transfer. |
| 3. External scope | **Pass.** `PRD.md:36–42`: authorized managers, one verified email, summary/status only, no editing or URL-bearer access, updates/revocation and copied-content limits. | **Pass.** `PRD.md:38–42`: same authorized summary scope, identity boundary, updates, recipient changes and next-access revocation; internal fields and external editing excluded. |
| 4. Unaffected rules | **Pass.** `PRD.md:26–32,44`: author-only intake editing, processor transitions, no reopening, data-policy authority and 180-day/owner-delete rules survive movement and revocation. | **Pass.** `PRD.md:7,9,28–34`: data-policy authority, attribution through the linked policy, processor/author rules, no reopening, exact retention and owner-only deletion preserved. |
| 5. Evidence accumulation | **Pass.** `PRD.md:62–68`: E1/V1/V2 retain original meanings; V3's four reads remain historical successes, denials remain bounded evidence, stale saves/project isolation unexecuted, retention not rerun. | **Pass.** `PRD.md:46–52`: same historical meanings; four reads including two outside HR, three other-organization denials and one removed-account new-page denial are preserved without inventing stale-save evidence. |
| 6. Observable outcomes and scope | **Pass.** `PRD.md:48–58`: outsider denial, owner-only unassigned access, stale actions, movement, intended-recipient reading, field limits and revocation checks; only carried PRD changed, under limit. | **Pass.** `PRD.md:56–65`: same changed outcomes including open-page removal and open-card revocation; proposed rules/current policy/unexecuted checks remain distinct; only carried PRD changed, under limit. |

### Actual sequence accumulation

Independently calculated hashes confirm each stage 2 consumed its own actual
stage-1 result byte for byte. These are not two unrelated plausible outputs.

| Sequence | Stage 1 `after/docs/PRD.md` = stage 2 `input/docs/PRD.md` SHA-256 |
| --- | --- |
| Pre | `1b2007e5b87311f0362f1709ff7ca7db43502fb6ecf459e9caf302a09d106f8e` |
| Post | `9f77e27882d4767098dcde25d769591f78df137e6c1194a26bb68d436856f162` |

Within each sequence, the instruction hash manifest is identical across
stages. The carried data policy, private-intake decision and public-pilot
source also match byte for byte. Stage 2 adds exactly the project decision
and prototype-check documents alongside its replacement request. Grades above
assess the resulting content; hash equality alone is not a quality test.

## Post 07 — Concierge capacity

Frozen [rubric](../../rubrics/07-08-operations-and-evidence.md), case 07.
Artifact: `post/07-concierge-capacity--bandit-scope/output.md`.
Raw constraints and estimates: `input/brief.md:8–18,38–61`.

| Criterion | Finding and exact output locator |
| --- | --- |
| 1. Provisional five-day launch | **Pass.** `output.md:1,28`: concrete manual pilot and five-day allocation including one-day verification. `output.md:9,30` leave operational feasibility unverified and conditional. |
| 2. Separate operations budget | **Pass.** `output.md:7,9`: separate two-request/two-pickup/two-return caps; 36 minutes plus 24 minutes for exceptions; unconstrained 108-minute peak correctly exceeds 60. |
| 3. Lending safeguards | **Pass.** `output.md:5–6,13,17–22`: eligibility/damaged drill, receipt versus confirmation, item conflicts, inspection before availability and affected-promise notification preserved. |
| 4. Cuts and prelaunch check | **Pass.** `output.md:26,30`: substantive cuts, concrete mixed-work/failure rehearsal and unexecuted status; reduced intake if capacity fails; no implementation performed. |

## Post 09 — Linked-policy review

Frozen [rubric](../../rubrics/09-linked-policy-review.md).
Artifact: `post/09-linked-policy-review--bandit-review/output.md`.
Raw basis: `input/docs/PRD.md:13–19,40–63`,
`input/docs/booking-policy.md:8–68` and `input/docs/discovery-notes.md:4–13`.

| Criterion | Finding and exact output locator |
| --- | --- |
| 1. Linked policy authority | **Pass.** `output.md:3–5`: accurate P1–P4 application; explicitly rejects treating delegated rules as missing. Full source read at `events.jsonl:7`. |
| 2. Adopted boundary | **Pass.** `output.md:6`: newer discovery remains unadopted; no excluded capability becomes a required repair. |
| 3. Calibrated findings | **Pass.** `output.md:1,3–8`: supported no-material-issue judgment with accurate source-specific reasons. No actual incompatible rule or invented omission found. |
| 4. Verification/task limits | **Pass.** `output.md:8–10`: document-only review, unchanged sources and planned future checks; no runtime/release/demand claim or mandatory approval workflow. |

## Post 13 — Combined scope and handoff

Frozen [rubric](../../rubrics/13-combined-issue-handoff.md).
Artifact: `post/13-combined-issue-handoff--bandit/output.md`.
Raw authority/estimates: `input/brief.md:8–25,33–45,49–69`;
the sketch remains unadopted at `input/draft.md:3–4`.

| Criterion | Finding and exact output locator |
| --- | --- |
| 1. Combined result | **Pass.** `output.md:3,5,15–23`: one complete first-trial scope and implementable handoff; proposed map/screens are not obligations; no workshop or separate command required. |
| 2. Capacity and cuts | **Pass.** `output.md:9,11,13,32`: 1.5 + 1 + 0.5 = 3 days; meaningful cuts/alternatives; recovery/fix work unestimated, no proven four-day delivery. |
| 3. Complete shared journey | **Pass.** `output.md:19–23`: stable shelf/reporter identity, current employee/lead rights, explicit noted resolution and direct reporter access to saved status. |
| 4. Interrupted submission | **Pass.** `output.md:21,23`: success follows durable saving, uncertain outcomes retain input/retry, same attempt does not duplicate, recurrence is a new report; no offline queue or new database architecture required. |
| 5. Acceptance and limits | **Pass.** `output.md:15,25–30`: recommended details and planned observable reporting/permissions/resolution/recovery checks; `output.md:5,22` avoid demand or software-verified physical-correction claims. |

### Actual general routing, separate from output quality

The authoritative archived `input/request.md:1` contains literal `$bandit`.
Although `metadata.json` has `invocation: null`, `events.jsonl:7` records reading
`instructions/bandit/SKILL.md` with the fixtures. `events.jsonl:9` records the
scope (`decisions.md`), specification and durable-evidence references;
`events.jsonl:12` adds change guidance. No specialist invocation or mandatory
multi-stage workshop appears. These are actual read observations, not quality
claims inferred from filenames or completion.

## Scope, instruction integrity and recoveries

All nine runs have final process exit code 0. Independently recalculated hashes
match all archived raw inputs, all present instruction files, and every
sequence `after/` file against its metadata manifest. Metadata records no
instruction mutation. Each of the four sequence stages changed only
`docs/PRD.md`; all other runs left product inputs unchanged. No product
implementation or product test execution appears in the traces. Word counting
and editing the authorized PRD are artifact operations, not product tests.

| Run | Selected entrypoint / relevant guidance reads | Raw-source reads |
| --- | --- | --- |
| Pre 11 | `events.jsonl:7` | `events.jsonl:9` |
| Post 11 | `events.jsonl:7` | `events.jsonl:9,11` |
| Pre 12 stage 1 | `events.jsonl:7` | `events.jsonl:9` |
| Pre 12 stage 2 | `events.jsonl:7` | `events.jsonl:9` |
| Post 12 stage 1 | `events.jsonl:7` | `events.jsonl:9` |
| Post 12 stage 2 | `events.jsonl:5,7` | `events.jsonl:5,7,9` |
| Post 07 | `events.jsonl:5` | `events.jsonl:9` |
| Post 09 | `events.jsonl:5` | `events.jsonl:7` |
| Post 13 | `events.jsonl:7,9,12` | `events.jsonl:7` |

Preserved process limitations:

- Post 12 stage 1 `events.jsonl:18` reports `python` missing, exit 127.
  `events.jsonl:20` recovers with `python3`, completing the final 773-word PRD.
  This is a recovered tool failure, not a failed product test or incomplete
  final specification.
- Sequence traces preserve initially overlong drafts and their subsequent
  reductions: pre stage 1 `events.jsonl:12–20`, pre stage 2 `:12–17`, post
  stage 1 `:12–20`, post stage 2 `:12–18`. Only the completed artifact is
  graded for the final word limit. Pre stage 1's final trace `wc -w` reports
  894; the archived artifact has 757 whitespace-delimited words. Both are
  below the limit, and this report consistently uses whitespace splitting.
- Post 13 metadata lists `bandit/assets/bandit-avatar.png`; `events.jsonl:5`
  shows that binary existed in the task workspace, but it is absent from the
  archived instruction directory. Its bytes could not be independently
  rehashed from this archive. All present instruction files match their
  recorded hashes; the general routing observation is supported by text reads.

No substantive outside-rubric defect or partial/fail criterion was found in
these nine completed outputs. Recoveries and archive visibility limits remain
separate from those semantic grades. This record does not convert written
acceptance scenarios, structural validation or the two sequence carry-forward
checks into executed product verification.
