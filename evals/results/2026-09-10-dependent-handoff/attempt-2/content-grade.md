# Independent content grade

## Scope and verdict

Read only the raw files under `grading-2/{A,B,C,D,E}/input/`, each case's `output.md`, and its `criteria.md`. A is graded only against the four case-05 conditions at `A/criteria.md:15`; B uses its six acceptance dimensions; C and D each use J12-1 through J12-7; E uses J13-1 through J13-7. All locators below are relative to `/private/tmp/bandit-interactions.ezd9Vq/grading-2/`; line ranges identify the exact supporting passage.

**Total: 30 pass, 1 partial, 0 fail across 31 conditions.** This is a content-only assessment of these synthetic answers, not an assessment of tool execution, workspace integrity, actual delivery, customer validation, or comparative skill quality. Statements that calculations or tests were executed receive no execution credit. A proposed acceptance check is assessed for usefulness, never treated as a passed test.

| Case | Conditions | Pass | Partial | Fail |
|---|---:|---:|---:|---:|
| A — small research | 4 | 4 | 0 | 0 |
| B — callback scope | 6 | 6 | 0 | 0 |
| C — connected launch plan | 7 | 6 | 1 | 0 |
| D — connected launch plan | 7 | 7 | 0 | 0 |
| E — offer consistency review | 7 | 7 | 0 | 0 |
| **Total** | **31** | **30** | **1** | **0** |

The partial is C/J12-5: its core offer calculations are correct, but its additional labor-inclusive customer-acquisition-cost instruction does not preserve the per-store denominator. This is a formula/wording defect, not an observed loss, an invented measurement, or evidence that the proposed price is wrong.

## A — case 05 only

### A-1 — Provisional segment and one feasible cheap test: pass

- Input: `A/input/request.md:1` asks a solo founder with no interviews or customer data to choose one customer group and the cheapest useful test this week before building an app.
- Output: `A/output.md:1–5` chooses working single-person households in one apartment complex who recently used a laundry, then a permission-dependent community/form test with ten residents. `A/output.md:7–9` supplies a concrete proposed pickup offer, free tooling, and a three-hour work limit.
- Judgment: this is one bounded interest/booking-intent test with a provisional segment. The invitation does not pretend an actual pickup reservation already exists. The three-thousand-won test price is explicitly a hypothesis, not a required or validated market price.

### A-2 — Hypotheses versus observations; interest versus payment/repeat: pass

- Input: `A/input/request.md:1` explicitly says there are no interviews or customer data.
- Output: `A/output.md:1,3,9` labels the segment, rationale, and price as unvalidated hypotheses. `A/output.md:13` says an application is not evidence of paid demand and distinguishes later payment/use and actual time/cost observations.
- Judgment: no historical observation, payment, or repeat behavior is invented. A future payment/use check is not represented as already completed validation.

### A-3 — Small request, no unnecessary questions: pass within content scope

- Input: `A/input/request.md:1` asks for no more than 200 words and says external search or file creation is unnecessary.
- Output: `A/output.md:1–13` directly supplies the recommendation without asking the user questions or assigning a broad research program. The saved answer contains 198 whitespace-delimited words, including Markdown tokens; it is within the requested cap under that explicit counting convention.
- Judgment: the answer remains small and immediately usable. Whether tools actually searched or created files is deliberately outside this verdict.

### A-4 — Decision-relevant observation without invented validation or universal cutoff: pass

- Input: `A/input/request.md:1` asks only to gain an initial sense of whether the idea is worth pursuing this week.
- Output: `A/output.md:11` defines eligible exposed residents and concrete item/time submissions, labels the 3-of-10 rule temporary, distinguishes zero, one-to-two, and insufficient exposure, and connects those outcomes to a manual-provider feasibility check or revision. `A/output.md:13` states what subsequent observations would change the next decision.
- Judgment: the thresholds are local proposed decision rules. They are not offered as universal demand-validation standards.

## B — six acceptance dimensions

### B-1 — Distinguishable decisions: pass

- Input: `B/input/request.md:3–7` asks separately for the first cohort, actual feature set, and expansion justification; `B/input/stakeholder-notes.md:22–23` requires an explicit review before more enrollment.
- Output: `B/output.md:1,5` selects the two willing small desks and the queue with measurement; `B/output.md:13–22` defines the shipped slice; `B/output.md:39–41` explains deferrals; `B/output.md:53–55` sets review and expansion conditions.
- Judgment: cohort, intervention, and expansion are separate decisions with reasons. The manual alternative is a conditional fallback, not an added feature commitment.

### B-2 — Capacity and external constraints: pass

- Input: `B/input/delivery-constraints.md:3–17` supplies 6/4/2 backend/frontend/QA days, additive feature estimates, and an extra 0.5 backend/0.5 QA day for measurement; `:19–26` rules out assumed provider approval, unconsented SMS, or unauthorized commercial/ownership changes.
- Output: `B/output.md:28–37` includes measurement in 3.5/3/1.5 days, leaving 2.5/1/0.5; it correctly identifies the email combination and SMS QA overruns. `B/output.md:19,22,41,45` treats safe correction/claiming and actual staffing dates as dependencies rather than supplied facts.
- Judgment: independent sums match. There is no invented second team or free integration. The answer explicitly declines to assume that a complete two-week observation period and later staffing fit automatically inside the September 30 shipping window.

### B-3 — Evidence drives the handoff: pass

- Input: `B/input/evidence.md:6–20` separates late-case attributions, interviews, SMS consent, and small/multi-branch readiness; `B/input/stakeholder-notes.md:3–13` separates willingness to pilot, prospect interest, and design/operations proposals.
- Output: `B/output.md:5–7` preserves those distinctions, uses the 31 handoff/17 ownership/14 contact-detail cases to justify testing visibility and ownership, and notes the small desks' 91% populated owner field and unknown segment-specific late counts.
- Judgment: the answer neither treats the eight interviews as outcome proof nor upgrades demo interest into a trial or purchase. It invents no confidence score.

### B-4 — Guardrails: pass

- Input: `B/input/delivery-constraints.md:19–26` requires consent/provider restrictions, existing branch access, named voluntary enrollment, disablement, and no new pricing or ownership policy. `B/input/evidence.md:17–20` leaves multi-branch ownership unresolved.
- Output: `B/output.md:5,11,19–20` includes named consented desks, branch permissions, no automatic branch/owner transfers, existing correction paths as a dependency, and non-destructive feature-flag disablement. `:39–41` defers SMS and multi-branch routing for the stated restrictions.
- Judgment: guardrails are proportionate to the small pilot; no unauthorized redesign is needed to accept its recommendation.

### B-5 — Observable learning: pass

- Input: `B/input/evidence.md:22–25` provides completion and ownership events but no reminder-viewing event; `B/input/stakeholder-notes.md:3–4` supplies Friday reviews and handoff notes.
- Output: `B/output.md:47–53` uses the same two desks' comparable 14-day baseline, due callback counts, mature 12-hour lateness, still-incomplete cases, per-desk reporting, handoff notes, missingness/workload differences, and operational/safety burden. It explicitly says events alone do not prove viewing.
- Judgment: the comparison is practical and outcomes are not confused with delivery or enthusiasm. Baseline availability and actual effect remain future observations, not claimed results.

### B-6 — Usable delivery handoff: pass

- Input: `B/input/request.md:9–13` asks for a practical scope handoff and unresolved decisions, not a PRD or execution. `B/input/homepage-refresh.md:7–9` says the agency budget is not transferable and the studied desks have not seen the campaign.
- Output: `B/output.md:5,19–22,45–55` gives customer-success enrollment/disablement responsibility, engineering dependencies, the ship date, observation-window uncertainty, and managing-director review. `:39–41,55` explains deferrals and keeps homepage material from driving product scope.
- Judgment: responsibilities and the bounded next step are sufficient without an expanded roadmap. The answer's proposed verification statements do not establish actual implementation behavior.

## C — connected launch plan

### C/J12-1 — Research changes a decision: pass

- Input: `C/input/research-records.md:7–16,20–32` describes six people/four cafés, three free assisted pilot cafés, 42 opportunities, absent reminder cross-tabs/baseline, and zero paid customers.
- Output: `C/output.md:13–18` accurately connects those records to a next-shift reading/owner-view service, preserves the distinct units, and correctly labels 20/42 as the share of all handoff opportunities. `:20–25` turns unknown buyer need, workplace access, payment, and unassisted use into feasible next questions.
- Judgment: no causal error-reduction, representative-market, or willingness-to-pay result is claimed. The numeric rate is 47.6%, correctly rounded.

### C/J12-2 — Connected target, offer, and scope: pass

- Input: `C/input/request.md:5,12` identifies employee use/owner payment and asks for the first offer. `C/input/founder-brief.md:9–11,23` permits choosing the service and price while limiting it to single cafés of at most 12 employees and at most five supported stores.
- Output: `C/output.md:29–45` selects an A-like absence/reconfirmation problem, requires a buying owner and on-shift access, defines a dated 14-day paid offer and disclosed shared-document fallback, and separates scope, deferrals, and exclusions.
- Judgment: the first deliverable and buyer are concrete. The chosen duration and price are permitted proposals. D's unknown buyer and C's ranking demand remain eligibility questions rather than invented readiness.

### C/J12-3 — Usable, testable marketing: pass

- Input: `C/input/request.md:13` asks for wording, CTA, channels, and an experiment with counting/decision rules. `C/input/founder-brief.md:27–30` provides three reachable owners, five possible introductions, a permission-dependent community, and an employee account with unknown buyer composition.
- Output: `C/output.md:69–80` supplies customer wording and a compatible CTA, preserves channel-access limitations, and avoids counting membership/followers as reach. `:82–90` bounds the offer/use experiments, records appropriate owner/store/opportunity units, labels thresholds hypothetical, and specifies continue/change/stop or defer outcomes.
- Judgment: payment and repeated observed use are kept distinct from stated interest and later renewal intent. No experiment is credited as already run.

### C/J12-4 — Designable UX handoff: pass

- Input: `C/input/request.md:14` asks for the employee/owner flow, first use, and failed handoff; `C/input/research-records.md:12,14,20,36` supplies off-shift concerns, shared access, and reading/completion confusion.
- Output: `C/output.md:94–106` specifies role entry, shared shift identity, fields, first-use/empty content, explicit read acknowledgment, failed-save input retention/retry, revision-linked reacknowledgment, unresolved handoff, owner view, and recovery. `:35,61` conditions both web and manual delivery on meeting the same core rules.
- Judgment: a designer can sketch the behavior without inventing the product policy. The estimate and fallback still require a feasibility check, which the answer explicitly schedules; the check is not treated as executed.

### C/J12-5 — Interpretable economics: partial

- Input: `C/input/request.md:15,17` asks for interpretable cost-based model alternatives and visible assumptions. `C/input/costs-and-delivery.md:9–18` supplies collection fees, recurring support/storage, fixed cost, onboarding, unknown acquisition/lifetime metrics, and permission to propose another structure.
- Satisfied: `C/output.md:110–126` compares no-setup recurring billing with setup-plus-lower-recurring billing, names the buyer/unit/value and conditional choice, includes all supplied cost categories, distinguishes contribution from fixed-cost results in the table, and computes the dated first offer separately. All displayed offer contribution, fee, break-even, and support-sensitivity calculations reproduce within rounding.
- Defect: `C/output.md:90` says cash acquisition cost is `모집 지출/유료 점포 수`, then says to add `모집시간×25,000원` “여기에” for labor-inclusive acquisition cost. Literally, this adds a per-store amount to total recruitment labor. For recruitment spend S, hours H, and paid stores N, the comparable per-store expression is `(S + H×25,000)/N`, not `S/N + H×25,000`. No numeric CAC has actually been observed or misreported, but the written future calculation is dimensionally ambiguous/incorrect unless the common denominator is made explicit.
- Judgment: partial rather than fail because the requested offer economics and model comparison are substantially supplied and arithmetically correct. This is not a rejection of the price, period, business model, or explicitly hypothetical 15-minute support assumption.

### C/J12-6 — Feasible four-week plan: pass

- Input: `C/input/request.md:7,12,17,19` asks for the connected four-week handoff within time/cash caps and prohibits actual outreach/launch execution. `C/input/founder-brief.md:17–23` sets 10 founder hours per week/40 total, 28 developer hours, 8 designer hours, 800,000 cash, and the 100,000 tool reservation.
- Output: `C/output.md:49–63` provides sequenced weekly work, 40/28/8 totals, the five-store 3h20 onboarding allocation, explicit inquiry/closure time, conditional manual fallback, 560,000 cash allocation and 240,000 unallocated. The 60,000 fixed cost is included inside the tool reservation, not added twice. `:33–39,130` bounds service, closure, refunds, and post-window commitments.
- Judgment: there is no demonstrated cap overrun. The weekly allocations are estimates, and conditional feasibility/stop points are provided. Reading a proposed work item or future usability check does not establish that it has actually happened.

### C/J12-7 — Useful uncertainty reduction: pass

- Input: `C/input/research-records.md:3,16,20,30,32` contains overlapping people/stores, an absent D buyer, assisted use without cross-tabs, and free-condition reactions. `C/input/costs-and-delivery.md:12,25–27` makes support estimates and manual delivery limitations explicit.
- Output: `C/output.md:18,25,29,86–90` uses those limitations to qualify recruitment and separately record assisted/unassisted handoffs and real support minutes. `:61,88,126` supplies fallback/stop or revision points if delivery or support assumptions do not hold.
- Judgment: uncertainty reduction is specific and lightweight. No broader study or real-customer validation is required to pass this planning criterion.

## D — connected launch plan

### D/J12-1 — Research changes a decision: pass

- Input: `D/input/research-records.md:7–16,20–32` supplies the interviews, free assisted pilot, opportunity table, and missing causal/payment evidence.
- Output: `D/output.md:11–17` preserves four cafés/six people, 42 opportunities/28 memo opportunities/20 read opportunities/16 assisted opportunities, the different denominators, absent cross-tabs/baseline, free-condition responses, and zero paid customers. `:21–28` proposes decision-relevant buyer, access, and shared-versus-individual acknowledgment checks.
- Judgment: the counts and rates reproduce; no interview or pilot result is promoted into causal or paid-demand proof.

### D/J12-2 — Connected target, offer, and scope: pass

- Input: `D/input/request.md:5,12` asks for the user/buyer problem and offer. `D/input/founder-brief.md:9–11,23` authorizes a proposed service/price within single-store, employee, and supported-store caps.
- Output: `D/output.md:3–5,19,30–40` identifies the target situation, employee and owner roles, fixed dated paid offer, onboarding/payment readiness order, support/termination boundaries, retained features, exclusions, and disclosed manual fallback.
- Judgment: the first paid offer is coherent with the research and source constraints. The 14-day structure is a permitted choice, not a defect or a required model for other answers.

### D/J12-3 — Usable, testable marketing: pass

- Input: `D/input/request.md:13` asks for copy, CTA, reachable channels, measures, and next actions. `D/input/founder-brief.md:27–30` constrains access and known buyer reach.
- Output: `D/output.md:58–77` supplies compatible copy, a concrete CTA, bounded direct outreach with deduplication, conditional introductions/community access, and proposal/payment/first-value/repetition/economics stages with counting units and advance decisions. It separates insufficient observation, zero payment, one-case learning, and potential follow-up.
- Judgment: this is a practical proposed experiment. Audience reach, completed payments, and renewal are not invented.

### D/J12-4 — Designable UX handoff: pass

- Input: `D/input/request.md:14` requests sketchable flow and first/failure states; `D/input/research-records.md:12,14,20,36` grounds shared access and the reading/completion distinction.
- Output: `D/output.md:81–91` provides participation/role entry, first use, empty states, recording fields, failed-save recovery, explicit shift acknowledgment, correction records, read revocation/history, and owner review with unresolved handoff actions. `:112–121` labels acceptance checks as planned and makes implementation/manual feasibility a pre-charge condition.
- Judgment: policy and states are sufficiently concrete for design. No identity architecture or successful runtime behavior is assumed solely from those requirements.

### D/J12-5 — Interpretable economics: pass

- Input: `D/input/costs-and-delivery.md:9–18` specifies the fee, storage, support wage/minutes, fixed cost, one-time onboarding, and unmeasured long-run inputs; `D/input/request.md:15` asks for two arrangements and a reversible recommendation.
- Output: `D/output.md:95–106` compares owner-paid no-setup recurring service and setup-plus-lower-recurring service, gives contribution and whole-cohort recurring/first-month results, includes fee on setup receipts and onboarding, and separately costs the actual 14-day experiment using full monthly variable/support costs. It provides capacity/margin and support-based revision conditions.
- Judgment: the displayed results reproduce within rounding. Both models' first-cohort losses are visible, founder labor is valued, and hypothetical future economics are not presented as established profit or measured LTV/CAC.

### D/J12-6 — Feasible four-week plan: pass

- Input: `D/input/founder-brief.md:17–23` sets the weekly/total labor and cash caps. `D/input/request.md:7,12,17,19` requires connected sequencing now, within capacity, without actual execution.
- Output: `D/output.md:32–54` provides fixed service dates, readiness/onboarding/payment order, limited support and final closure, weekly work, totals of 40/28/8 hours, five-store onboarding of 3h20 and support estimate of 2h30, and 535,500 reserved cash with 264,500 remaining. `:54` distinguishes refund liquidity and avoids double-counting the 60,000 fixed cost. `:119–121` closes the loop and leaves future staffing unresolved.
- Judgment: the itemized sums are within the stated caps. Allocations are estimates, not proof of execution; unknown inquiry volume or implementation effort is not a demonstrated time-budget contradiction. Conditional rejection/manual fallback is explicit.

### D/J12-7 — Useful uncertainty reduction: pass

- Input: `D/input/research-records.md:3,16,20,30` supplies overlapping samples, missing buyer access at D, assisted use, and missing cross-tabs. `D/input/costs-and-delivery.md:12,25–27` leaves support load and automation unmeasured.
- Output: `D/output.md:11–17,21–28` makes those limitations change recruitment and acknowledgment/access questions. `:74–77` records real support and handoff evidence with intervention flags; `:104–106,121` connects overruns and feasibility results to model/scope changes or refusal to charge.
- Judgment: the plan uses specific, bounded observations without requiring a new broad research program.

## E — offer consistency review

### E/J13-1 — Fulfillment promise consistent across journey: pass

- Input: `E/input/approved-offer.md:9,29` adopts only Solbit A/B lockers and Tuesday pickup/Friday 18:00 return. `E/input/launch-artifacts.md:7–9,33,55` conflicts in AD-1, UX-1, and UX-3; LP-1 at `:19,25` is accurate.
- Output: `E/output.md:26–32` identifies nationwide/doorstep scope and selection conflicts; `:46–52` joins AD-1's next-day promise and UX-3's 24-hour promise to the accurate LP-1 schedule, customer consequence, and cross-screen correction.
- Judgment: both geography/method and timing are traced through the journey, with accurate LP-1 material retained. No faster or nationwide service is invented as a fix.

### E/J13-2 — Historical observations not inflated into proof: pass

- Input: `E/input/trial-record.md:5,12–15` says eight free-trial households, only five survey responses, five satisfied respondents, no paid repurchase solicitation, and no sterilization test. `E/input/approved-offer.md:17` excludes a sterilization guarantee; `E/input/launch-artifacts.md:9` makes the inflated claims.
- Output: `E/output.md:54–62` separately identifies the denominator error and absent test basis, explains the misleading customer consequences, and supplies deletion or a properly qualified historical statement. It keeps free-trial satisfaction separate from paid demand.
- Judgment: corrections are specific and usable; no external legal violation or actual customer validation is asserted.

### E/J13-3 — Correct order/pair pricing units: pass

- Input: `E/input/approved-offer.md:21–25` defines one order-level transport fee, two-pair fee waiver, and one 3,000 discount per first order. `E/input/launch-artifacts.md:11,23,45–47` exposes the AD/UX conflicts and otherwise compatible LP structure.
- Output: `E/output.md:7–20` finds the waived one-pair fee and duplicate two-pair discount, joins AD-1/LP-1/UX-2, and gives 19,000/33,000 first-order totals and 22,000/36,000 regular totals. It clarifies “two pairs” against the existing quantity cap.
- Judgment: arithmetic and units are correct. Clarifying LP copy is not misrepresented as evidence that three pairs can currently be selected.

### E/J13-4 — Pair-based capacity: pass

- Input: `E/input/approved-offer.md:11` sets a combined 24-pair cap and 1–2 pairs per order with capacity secured before payment. `E/input/launch-artifacts.md:37,41–43` correctly limits quantity selection but erroneously counts available orders.
- Output: `E/output.md:36–42` identifies the wrong unit, requests quantity-aware combined reservation before charging, and preserves next-session or exit behavior. The 23 one-pair orders plus a two-pair request is expressly hypothetical, followed by a 23-pairs-reserved boundary check.
- Judgment: `23 + 2 = 25` is correct. The actual displayed 23 orders are not asserted to equal 23 pairs, and no new infrastructure is demanded.

### E/J13-5 — Eligibility/availability before charging: pass

- Input: `E/input/approved-offer.md:15,25` requires material/condition eligibility and capacity before final-price/return-promise payment and success confirmation. `E/input/launch-artifacts.md:35,49` lets excluded materials proceed and delays photo checking until after payment.
- Output: `E/output.md:26–32` identifies both issues and requires pre-payment photo/material eligibility, then capacity and final confirmation. `:40,46–52` adds quantity blocking and visible final return promises; `:20` includes consistent completion-price checking.
- Judgment: the sequence is observable and grounded. Draft screen behavior is not described as a reproduced runtime bug or excused by a later refund.

### E/J13-6 — Bounded, grounded, usable review: pass

- Input: `E/input/request.md:5–11` establishes source hierarchy and the bounded review-only task; `E/input/approved-offer.md:5,31` states that unapproved text does not supersede the offer and compensation is undecided. `E/input/launch-artifacts.md:65` says the FAQ deliberately omits an approved compensation claim.
- Output: `E/output.md:1–3` identifies release blockers and the authority hierarchy; `:5–62` supplies affected IDs, conflicting facts, customer effects, priority, minimal corrections and checks. `:68–70` keeps compensation and other genuine operational questions unresolved and assigns the next document review.
- Judgment: this remains a claims/flow/pricing/fulfillment review, not a new strategy or implementation. It correctly recognizes that the FAQ does not already promise compensation. Execution/integrity statements are not independently verified here.

### E/J13-7 — Correct elements/open decisions survive: pass

- Input: `E/input/launch-artifacts.md:17–27,37,43,61–65` contains accurate locker/return and one-off-service copy, a valid 1–2 limit and next-session path, correct cancellation/delay material, and a deliberately open compensation item.
- Output: `E/output.md:40,50,66–68` retains multiple correct elements, distinguishes FAQ/contact-detail clarification from established contradictions, and leaves compensation and review/release timing unanswered where the source is silent.
- Judgment: the review does not rebuild all correct material or invent a policy to close a genuine open decision.

## Independent arithmetic audit

These calculations were recomputed for this grading, independently of any output's claim to have used a tool. They verify numerical consistency with supplied assumptions, not the truth of those assumptions.

### A and B

- A's ten-resident exposure target and 0/1–2/3+ branches are hypothetical rules, not measured conversion. The answer is 198 whitespace-delimited words.
- B queue/report: `(3 + 0.5, 3, 1 + 0.5) = (3.5, 3, 1.5)`; remaining `(6,4,2) − (3.5,3,1.5) = (2.5,1,0.5)`.
- B queue/email/report: `(5.5,5,2.5)`; SMS/report: `(5.5,2,2.5)`; routing/report: `(4.5,4,1.5)`. Reported fit/overruns agree with the source estimates (`B/input/delivery-constraints.md:8–17`; `B/output.md:28–37`).

### C and D research, labor, and cash

- Pilot source totals: opportunities `14+12+16=42`; memo opportunities `11+5+12=28`; read opportunities `8+2+10=20`; assisted opportunities `5+4+7=16`. Rates: `28/42=66.7%`, `20/28=71.4%`, `20/42=47.6%` rounded. The answers label the denominators they report correctly (`C/output.md:16–18`; `D/output.md:17`).
- Five-store onboarding: `5×40/60 = 3⅓ hours = 3h20`. Full monthly five-store recurring support: `5×30/60=2.5 hours`. C's stated first-offer support hypothesis is instead 15 minutes/store for 14 days; it is explicitly an assumption (`C/output.md:124`), with actual-minute recording at `:88`.
- C staffing: founder `4×10=40`; developer `8+12+4+4=28`; designer `6+2=8`. Cash `100,000+100,000+120,000+30,000+10,000+200,000=560,000`, leaving `240,000`.
- D staffing: founder `4×10=40`; developer `12+12+2+2=28`; designer `5+3=8`. Cash allocations/reserves `100,000+100,000+120,000+30,000+10,000+3,000+100,000+72,500=535,500`, leaving `264,500`. Refund reserve is not asserted to be an incurred operating expense.

### C and D commercial calculations

Using the source's 3.3% fee, 2,000 store-month variable cost, 30 monthly support minutes at 25,000/hour, 60,000 monthly fixed cost, and one-time 40-minute onboarding:

- Monthly support labor: `30/60×25,000 = 12,500`.
- Onboarding labor: `40/60×25,000 = 16,666.666…` per store.
- A monthly contribution: `29,000×0.967 − 2,000 − 12,500 = 13,543`.
- B monthly contribution: `19,000×0.967 − 2,000 − 12,500 = 3,873`.
- A five-store recurring result: `5×13,543 − 60,000 = 7,715`; B: `5×3,873 − 60,000 = −40,635`.
- A first-month per-store contribution: `13,543 − 16,666.666… = −3,123.666…`; first five-store result `−75,618.333…`.
- B net setup receipt: `20,000×0.967 = 19,340`; first-month per-store contribution `3,873+19,340−16,666.666… = 6,546.333…`; first five-store result `−27,268.333…`.
- Recurring fixed-cost break-even: `ceil(60,000/13,543)=5` stores for A; `ceil(60,000/3,873)=16` for B. These are arithmetic thresholds, not measured commercial feasibility.
- C actual 14-day offer with its explicit 15-minute support assumption: `14,500×0.967−2,000−6,250−16,666.666… = −10,895.166…` per store; five stores minus fixed cost `−114,475.833…`.
- D actual 14-day offer with full monthly support/variable cost: `14,500×0.967−2,000−12,500−16,666.666… = −17,145.166…` per store; five stores minus fixed cost `−145,725.833…`.
- A support sensitivity at 15/30/60 minutes: `19,793 / 13,543 / 1,043` contribution per store; B at 60 minutes: `−8,627`. All displayed rounded values agree (`C/output.md:112–126`; `D/output.md:99–108`).

C's CAC wording at `C/output.md:90` is the exception: total recruitment labor must share the paid-store denominator if the intended output remains cost per acquired store. An unknown N is not a reason to invent one; the zero-payment branch correctly avoids division by zero.

### E pricing and capacity

- One pair, regular: `18,000+4,000=22,000`; first order: `22,000−3,000=19,000`.
- Two pairs, regular: `2×18,000+0=36,000`; first order: `36,000−3,000=33,000`.
- Hypothetical capacity: `23 pairs + 2 pairs = 25 pairs > 24`; a one-pair request at the same hypothetical state reaches exactly 24. These calculations preserve pair/order units and agree with `E/input/approved-offer.md:11,21–23` and `E/output.md:15–16,38–42`.

## Remaining limitations and calibration

1. **C's CAC instruction needs a common denominator.** The partial is confined to a future formula's unit problem. No measured CAC, offer-price arithmetic failure, or actual business loss is inferred from it.
2. **C's “B의 첫 달 흑자” phrase needs careful interpretation.** `C/output.md:122` follows a table explicitly showing positive *per-store first-month contribution* (`:118`) and negative recurring whole-cohort economics. The independently calculated five-store first month is still negative after fixed cost. In context I do not count a second proven contradiction or claim that the answer demonstrated an overall first-cohort profit; the wording would be clearer with its contribution qualifier preserved.
3. **Support windows and actual support labor are different inputs.** C reserves inquiry-handling time (`C/output.md:37,59`) while its example costs an assumed 15 active support minutes per store (`:124`); D similarly bounds support windows and separately estimates actual minutes (`D/output.md:36,52,106`). Neither source establishes actual inquiry volume, whether every window is exclusively occupied, or the long-run staffing cost of availability. Those assumptions deserve reconciliation during the expressly planned measurement. They are not enough to demonstrate a four-week cap overrun or justify imposing a new price, model, or service length.
4. **Implementation/manual feasibility remains conditional.** C and D require nontrivial access, saved state, and recovery behavior. Their pre-charge checks and manual/no-sale fallback make the plan conditional; no supplied input proves the estimate either sufficient or impossible. Planned checks are not execution evidence. B likewise leaves correction-path and staffing confirmation open.
5. **No real-world outcome is established.** Inputs are synthetic; interview statements, assisted free use, future outreach, proposed thresholds, and draft release checks remain what they are. This grade neither requires real customer validation for answer-only work nor presents these answers as such validation.
6. **Integrity and execution are excluded.** No tool log, skill source, previous run/report, issue text, workspace mutation record, or external source was inspected. Whether A/B actually avoided tools or C/D/E actually ran the claimed calculations is not adjudicated by this content report.
