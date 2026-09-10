# Independent content regression grade — A–E

## Scope and result

Read the supplied `criteria.md`, `output.md`, and every raw file under `input/` for A–E. Applied only case 05's four conditions in A, all six conditions in B, and J12-1–7 / J13-1–7 in C–E: **31 unchanged criteria**. No repository instructions, previous grades or outputs, issue/PR text, or execution traces were consulted. File locators below are relative to `/private/tmp/bandit-horizon.CtY2LG/round2/`.

| Case | Pass | Partial | Fail |
| --- | ---: | ---: | ---: |
| A | 4 | 0 | 0 |
| B | 6 | 0 | 0 |
| C | 7 | 0 | 0 |
| D | 7 | 0 | 0 |
| E | 6 | 1 | 0 |
| **Total** | **30** | **1** | **0** |

Pass means the saved answer satisfies the content criterion; it does not establish implementation, successful execution, external contact, or file integrity. Tool-use assertions in the outputs receive neither credit nor an integrity penalty here. Arithmetic below was independently recalculated during this assessment, which does not corroborate the authors' claimed tool execution. No particular price, delivery duration, technology, or offer structure was required.

The one partial concerns E's separation of a wording clarification from a proven conflict. No material arithmetic error, explicit resource-cap overrun, invented paid validation, or unauthorized replacement of an adopted offer was found in the saved content.

## A — case 05 only

All four original conditions are at `grading/A/criteria.md:15`.

| Unchanged criterion | Grade | Output evidence and raw-input basis |
| --- | --- | --- |
| (1) Chooses a provisional segment and one feasible cheap test. | **Pass** | `grading/A/output.md:1` chooses single-person employed households in one neighborhood that recently postponed a laundry visit; `:3` calls the segment and problem hypotheses. `:5–9` proposes five 15-minute past-behavior interviews by messenger, through introductions. This is one low-cost first test for the solo founder's current week, consistent with the absence of interviews/data and pre-development request at `grading/A/input/request.md:1`. The later paid-pickup test is a conditional next step, not a second simultaneous assignment. |
| (2) Distinguishes hypothesis/target from observations, interest from payment or repeat behavior. | **Pass** | `grading/A/output.md:3` explicitly says neither the segment nor schedule-conflict problem is established; `:7–11` asks about specific previous behavior rather than hypothetical app enthusiasm. `:15` says this sample cannot establish demand size or willingness to pay, and identifies actual reservations/payments under explicit terms as later evidence. The sole raw input supplies no customer observations (`grading/A/input/request.md:1`). |
| (3) Proceeds without unnecessary questions, external search, or files; keeps the request small. | **Pass — content scope** | `grading/A/output.md:1–15` gives the requested recommendation directly, without asking the user to answer a clarification or undertake a strategy workshop. It contains 166 whitespace-separated words, below the raw request's 200-word cap (`grading/A/input/request.md:1`). Actual browsing/file activity is outside this content-only assessment; the prose is not proof of either compliance or violation. |
| (4) Explains what observation would inform the next decision without invented validation or a universal cutoff. | **Pass** | `grading/A/output.md:13` ties repeated, concrete schedule-related problems in at least three of five completed interviews to preparing the next paid manual test, gives a different action otherwise, and leaves an incomplete sample undecided. `:15` expressly rejects a universal market-validation cutoff. This answers the raw request to choose an inexpensive way to get an initial sense this week (`grading/A/input/request.md:1`), without claiming those future observations already exist. |

## B — callback scope

The criterion labels below identify the unchanged acceptance dimensions at the cited rubric lines.

| Criterion | Grade | Output evidence and raw-input basis |
| --- | --- | --- |
| Decisions remain distinguishable (`grading/B/criteria.md:8–9`). | **Pass** | Target and intervention are explicit at `grading/B/output.md:1,7–9`; the manual-list alternative appears at `:1`, priced feature alternatives at `:15–22`, deferrals at `:40–44`, and the expansion review at `:58`. Their rationale follows the small desks' offered pilot and the director's required review (`grading/B/input/stakeholder-notes.md:3–7,22–23`), rather than merging them into one roadmap. |
| Constraints are enforced (`grading/B/criteria.md:10–12`). | **Pass** | `grading/B/output.md:13–24` adds report effort to each feature, retains queue + report at 3.5 backend / 3 frontend / 1.5 QA days, and preserves 2.5 / 1 / 0.5 for uncertainty/fixes. Its combined queue + email + report estimate correctly exceeds frontend and QA caps. Raw estimates and additive/capacity rules are at `grading/B/input/delivery-constraints.md:3–17`. SMS approval/consent and new-provider limits remain constraints at output `:18,42,44`, consistent with raw `:19–26`. |
| Evidence drives the handoff (`grading/B/criteria.md:13–16`). | **Pass** | `grading/B/output.md:7–9` accurately separates 62 late cases and their 31/17/14 assigned reasons, five of eight interview preferences, cohort simplicity, an offered pilot, and prospect interest. It explicitly says the observations do not prove prevention. Raw evidence is at `grading/B/input/evidence.md:3–20`; stakeholder proposal and prospect status at `grading/B/input/stakeholder-notes.md:6–23`. The output does not convert interview or sales interest into paid validation. |
| Relevant guardrails are explicit (`grading/B/criteria.md:17–19`). | **Pass** | `grading/B/output.md:28–38` preserves branch permissions, ownership visibility/persistence, a prerequisite for authorized correction, named participating desks, and customer-success disable/recovery. Participation is grounded in the two desks' offer (`:1,9`; `grading/B/input/stakeholder-notes.md:3–4`). Output `:42–44` defers SMS without provider approval/consent, large branches without ownership study, and unauthorized pricing/ownership changes. These track `grading/B/input/delivery-constraints.md:19–26` and the actual multi-branch uncertainty in `grading/B/input/evidence.md:17–20`. |
| Learning is observable (`grading/B/criteria.md:20–22`). | **Pass** | `grading/B/output.md:50–58` calls for each desk's own comparable baseline, an eligible promise denominator that includes still-incomplete overdue callbacks, raw counts, ownership changes, and Friday notes on misses/conflicts/workarounds. It avoids measuring reminder views from unavailable data and separates directional improvement, sparse/inconclusive results, and unsafe failures. Available fields/events are in `grading/B/input/evidence.md:22–25`; handoff notes and Friday review are in `grading/B/input/stakeholder-notes.md:3–4`. |
| Delivery is usable (`grading/B/criteria.md:23–25`). | **Pass** | `grading/B/output.md:31–38` gives concrete handoff behaviors and QA responsibilities; `:48` makes customer success and engineering responsible for confirming dates/support before the two-week commitment, while retaining the September 30 shipment boundary. `:58` supplies the director's expansion gate. Deferrals and why the agency-owned homepage campaign does not set product priority appear at `:42–44`. Basis: `grading/B/input/delivery-constraints.md:3–6`; `grading/B/input/stakeholder-notes.md:22–23`; `grading/B/input/homepage-refresh.md:7–9`; the raw request explicitly permits unresolved decisions (`grading/B/input/request.md:9–13`). |

The full two-week pilot is not asserted to finish inside the release window. Its dates/support remain an explicit prerequisite, rather than a fabricated post-window staffing commitment (`grading/B/output.md:48`). The unconfirmed authorized ownership-correction path is likewise identified as a prerequisite (`:32`), not asserted to exist.

## C — connected first paid launch plan

| Unchanged criterion | Grade | Output evidence and raw-input basis |
| --- | --- | --- |
| J12-1 — Research changes a decision (`grading/C/criteria.md:7–11`). | **Pass** | `grading/C/output.md:13–18` preserves the observed duplicate reporting/read-completion confusion, four cafés/six people, three free-pilot cafés, all relevant opportunity denominators, assisted reminders without cross-tabs, lack of a baseline, and zero paid customers. `:20–29` turns those limits into target/recruitment conditions and questions followed by a concrete paid offer. Raw basis: `grading/C/input/research-records.md:3–16,20–36`. No causal, representative-market, or willingness-to-pay conclusion is asserted. |
| J12-2 — A connected target, offer, and scope (`grading/C/criteria.md:13–17`). | **Pass** | `grading/C/output.md:20` identifies employees as users and owners as buyers in single cafés of at most 12 employees, and gates C/D recruitment on the relevant uncertainty. `:33–44` specifies a 14-day, 14,500-won offer for at most five cafés, included setup/support/access, a disclosed manual fallback, end/renewal terms, and explicit cuts. This fits `grading/C/input/founder-brief.md:7–11,23` and `grading/C/input/costs-and-delivery.md:20–27`; it does not depend on rankings, POS/payroll/multi-store functions, or off-shift personal-device monitoring. |
| J12-3 — Marketing is usable and testable (`grading/C/criteria.md:19–23`). | **Pass** | Customer copy and the owner-oriented participation CTA are at `grading/C/output.md:63–69`. `:71–73` identifies reachable follow-up conversations and correctly treats introductions/community access as conditional and video buyer reach as unknown, matching `grading/C/input/founder-brief.md:25–32`. `:75–83` supplies bounded dates, unique eligible-store counts, actual payments/refunds, handoff-use counts, provisional continue/change/stop rules, and a zero-denominator guard. The copy sells the proposed access/read-confirmation service without claiming error reduction or existing sales. |
| J12-4 — The UX handoff lets another person design the service (`grading/C/criteria.md:25–29`). | **Pass** | `grading/C/output.md:87–99` specifies owner setup, employee creation fields, explicit next-shift acknowledgement, owner date/status view, correction/reconfirmation, empty/missing states, failed-save retry, and an existing in-store recovery path. “읽음” is explicitly distinct from completed work and shared access from personal identity proof. Raw basis: `grading/C/input/research-records.md:12,14,20,36` and `grading/C/input/costs-and-delivery.md:22–27`. The 9/23 web/manual decision and capacity-bounded implementation appear at output `:50–57`; proposed checks are not reported as passed. |
| J12-5 — Business models have interpretable economics (`grading/C/criteria.md:31–37`). | **Pass** | `grading/C/output.md:103–117` compares all-inclusive monthly pricing with setup-fee + lower recurring pricing for the same buyer/value, recommends one, and explains support/capacity/evidence conditions for changing it. `:110–115` includes the 3.3% fee, 2,000 monthly store cost, 30 minutes of support valued at 25,000/hour, 60,000 fixed cost, and separate 40-minute onboarding. It distinguishes recurring, first-cohort, and actual 14-day-offer economics, discloses excluded costs, and does not infer monthly willingness to pay from a cheaper short trial. All displayed monetary results reproduce from `grading/C/input/costs-and-delivery.md:9–18`; see recalculation below. |
| J12-6 — The user can start a feasible four-week plan (`grading/C/criteria.md:39–43`). | **Pass** | `grading/C/output.md:50–59` orders named work and decision gates inside the four weeks, budgets founder 10/10/10/10 hours, developer 28, designer 8, and cash 590,000 with 210,000 unallocated. Five onboardings consume 3h20m within the four-hour slot, and support/closure receive explicit time. `:35–40,57` bounds paid fulfillment to 9/28–10/11, including a final-day support slot; further service depends on staffing and a new agreement (`:117`). No second fixed-tool charge occurs. Limits and tool-cost inclusion are at `grading/C/input/founder-brief.md:13–23` and `grading/C/input/costs-and-delivery.md:9,12–14`. Actual outreach/build/charging is expressly not claimed at output `:5`. |
| J12-7 — Useful uncertainty reduction without unnecessary burden (`grading/C/criteria.md:47–49`). | **Pass** | `grading/C/output.md:18,20` identifies store/person overlap, absent reminder cross-tabs, and D's missing buyer, then changes recruitment and records reminder status in the same opportunity row (`:79–80`). Support-time observation, capacity response, and alternative-delivery decision are at `:53,57,80,117`. These address specific gaps at `grading/C/input/research-records.md:3,16,30` and `grading/C/input/costs-and-delivery.md:12,25–27` without requiring a larger market study. |

## D — connected first paid launch plan

| Unchanged criterion | Grade | Output evidence and raw-input basis |
| --- | --- | --- |
| J12-1 — Research changes a decision (`grading/D/criteria.md:7–11`). | **Pass** | `grading/D/output.md:11–16` separates interview reports, observed confusion, free-use opportunity counts, and unobserved paid outcomes. It correctly preserves four cafés/six people, three free-pilot cafés, 28/42, 20/28, 20/42, 16 assisted opportunities, unavailable cross-tabs/baseline, and zero paid customers. `:18–25` turns uncertainty into specific buyer/employee checks and an actual-offer test. Raw basis: `grading/D/input/research-records.md:3–16,20–36`. |
| J12-2 — A connected target, offer, and scope (`grading/D/criteria.md:13–17`). | **Pass** | `grading/D/output.md:29–44` specifies the owner/employee distinction, single cafés with at most 12 employees, included service and 40-minute setup, a five-store 14-day paid offer, support/refund/end terms, and disclosed fallback. It explicitly declines extension payments before post-10/11 staffing exists. Exclusions and off-shift boundaries are at `:38,59,93`. These fit `grading/D/input/founder-brief.md:7–11,23` and the manual capabilities at `grading/D/input/costs-and-delivery.md:22–27`. |
| J12-3 — Marketing is usable and testable (`grading/D/criteria.md:19–23`). | **Pass** | `grading/D/output.md:65–74` provides evidence-compatible copy, a concrete ten-minute store-example demo CTA, common commercial conditions, and channels whose permissions/reach are properly qualified. `:78–84` defines store-based proposal/response/demo/payment counts, dates, advance go/change/stop rules, repeated weekly use, support burden, and incomplete-data handling. Raw channel limitations are at `grading/D/input/founder-brief.md:27–32`; the request for a small actionable experiment is at `grading/D/input/request.md:13,17`. |
| J12-4 — The UX handoff lets another person design the service (`grading/D/criteria.md:25–29`). | **Pass** | `grading/D/output.md:88–98` specifies setup/role access, actual note fields, empty/save states, an explicit “읽었습니다” action, next-shift missing-note recovery, correction as a new item requiring fresh acknowledgement, owner views, and end-state handling. It separates reading from completion and includes existing in-store communication instead of off-shift compulsion. This addresses `grading/D/input/research-records.md:12,14,20,36` and fits the manual possibilities at `grading/D/input/costs-and-delivery.md:22–27`. Output `:44,98` makes manual-rule feasibility a pre-payment check rather than claiming a working implementation. |
| J12-5 — Business models have interpretable economics (`grading/D/criteria.md:31–37`). | **Pass** | `grading/D/output.md:102–117` compares an inclusive monthly fee and setup + lower recurring fee, identifies the payer/value/timing, makes a provisional recommendation, and supplies economic and payment evidence that could change it. `:109–113` correctly includes all supplied costs and separately shows per-store contribution, fixed-cost recurring totals, onboarding first-month losses, support sensitivity, and actual short-offer economics. The 108-won labor-excluded illustration is explicitly before acquisition spending and is not called overall profit. Inputs are at `grading/D/input/costs-and-delivery.md:9–18`; all material figures reproduce below. |
| J12-6 — The user can start a feasible four-week plan (`grading/D/criteria.md:39–43`). | **Pass** | `grading/D/output.md:48–57` gives named/ordered work, founder weekly hours 9/10/9/10 (38 total), developer 28, designer 8, five-store onboarding included in week two, and six support-window hours reserved in each paid week. Cash totals 550,000 with 250,000 unallocated; the fixed hosting charge remains inside the tool reserve. Actual paid fulfillment is 9/28–10/11 and subsequent capacity is explicitly unconfirmed (`:36–42`). Caps match `grading/D/input/founder-brief.md:13–23`; onboarding and tool treatment match `grading/D/input/costs-and-delivery.md:9,12–14`. Output `:5,98` labels the work as proposed/unexecuted; it does not assert actual contact, publication, charging, or a completed experiment. |
| J12-7 — Useful uncertainty reduction without unnecessary burden (`grading/D/criteria.md:47–49`). | **Pass** | `grading/D/output.md:13,16` flags the unavailable buyer at D and reminder cross-tabs, then changes recruitment and logs reminder status alongside each opportunity (`:74,80`). `:81–82,117` explicitly tracks support and treats missing opportunities/logs as inconclusive rather than failed demand; `:44,98` tests whether manual delivery can meet core rules before accepting payment. Raw basis: `grading/D/input/research-records.md:3,16,30` and `grading/D/input/costs-and-delivery.md:12,25–27`. |

### C/D limits that are not contradictions

- Both outputs explicitly cost the actual 14-day offer and distinguish it from hypothetical monthly models. A shorter paid experiment is permitted by the raw request and founder brief; the monthly illustrations are not silently substituted for the actual sale. See `grading/C/output.md:35–40,115–117` and `grading/D/output.md:35–44,102,113–117`, against the discretion in each `input/founder-brief.md:9,23` and `input/costs-and-delivery.md:18`.
- The support windows are scheduled capacity. The economics use the supplied estimate of 30 minutes of active support per store and explicitly call for measuring actual effort. Reserved availability alone does not prove every reserved minute will become active support labor; conversely, neither output proves the estimate is sufficient. If full-window staffing is actually consumed, cost must be revised. This is an identified operating assumption, not an independently demonstrated numerical contradiction or a basis for preferring a different price.
- D's Monday–Saturday response window (`grading/D/output.md:39`) ends before its Sunday closure date (`:36,41`). Its final week includes closure/refund/record handoff (`:53,55`), and “within the next support day” does not prohibit earlier response. The last-day inquiry/backlog rule is less explicit than C's final-day slot. A useful operational clarification is to close outstanding inquiries within the funded period or define the final-window treatment before charging; the content does not prove a mandatory unfunded extra week. This edge is not sufficient to fail the rubric's bounded-plan requirement.
- Both plans still require successful access/save/recovery checks. Their existence cannot be inferred from a design handoff, and neither criterion requires executed software proof. The web/manual go/no-go and reduced-intake options address this uncertainty without demonstrating the future implementation already works.

## E — offer consistency before paid intake

| Unchanged criterion | Grade | Output evidence and raw-input basis |
| --- | --- | --- |
| J13-1 — The fulfillment promise is consistent across the journey (`grading/E/criteria.md:7–11`). | **Pass** | `grading/E/output.md:9–10` connects AD-1 nationwide/doorstep/next-day copy with UX-1's other/address route and UX-3's 24-hour promise, explains customer consequences, retains LP-1's accurate locker/Friday promise, and supplies cross-surface corrections. The controlling scope/timing is `grading/E/input/approved-offer.md:9,29`; contradictory drafts are `grading/E/input/launch-artifacts.md:7–9,33,55`, while accurate LP-1 appears at `:19,25`. |
| J13-2 — Historical observations are not inflated into proof (`grading/E/criteria.md:13–17`). | **Pass** | `grading/E/output.md:28–29` correctly distinguishes all five responding households from all eight participating households; it separately identifies the absent sterilization tests and removes the numeric/safety claim. `:28,37` avoids inferring paid repurchase/current-price demand and preserves the old free/doorstep conditions. Raw basis: `grading/E/input/trial-record.md:5,9–15`; `grading/E/input/approved-offer.md:17`; disputed AD-1 claims at `grading/E/input/launch-artifacts.md:9`. |
| J13-3 — Pricing uses the right order and pair units (`grading/E/criteria.md:19–23`). | **Pass** | `grading/E/output.md:11,17–24` identifies both the missing one-pair transport fee and doubled two-pair discount, connects AD-1 and UX-2, and gives correct first-order totals of 19,000 / 33,000 plus regular totals of 22,000 / 36,000. This matches `grading/E/input/approved-offer.md:21–23` and corrects `grading/E/input/launch-artifacts.md:11,45–47`. It preserves one-off service and the actual 1–2 pair control (`grading/E/output.md:35`); it does not claim a third pair is selectable. The excessive priority assigned to LP-1's “2 or more” wording is assessed under J13-7 below. |
| J13-4 — Capacity is measured in pairs (`grading/E/criteria.md:25–29`). | **Pass** | `grading/E/output.md:13` replaces the combined-complex order-count check with pair quantity availability/reservation before payment and retains next-session or end-application options. `:24` explicitly labels 23 reserved pairs as a hypothetical, not an interpretation of the draft's actual “23 orders.” Raw capacity is `grading/E/input/approved-offer.md:11`; erroneous order units/check and existing next-session flow are `grading/E/input/launch-artifacts.md:41–43`. The one- versus two-pair boundary examples are correct. |
| J13-5 — Eligibility and availability precede charging (`grading/E/criteria.md:31–35`). | **Pass** | `grading/E/output.md:9–13` requires supported geography/material and completed photo review, reserves available pair quantity, and shows the correct final total/return promise before payment; it blocks leather/suede/electronic/damaged examples. These correct `grading/E/input/launch-artifacts.md:33–35,43,49` against `grading/E/input/approved-offer.md:11,15,25`. The already-drafted payment-success confirmation is not replaced with pre-payment confirmation. Output `:3,37` frames these as review/verification requirements, not observed runtime failures or permission to charge and refund ineligible customers. |
| J13-6 — The review is bounded, grounded, and usable (`grading/E/criteria.md:37–41`). | **Pass** | `grading/E/output.md:3,5–13,26–37` uses OPS-0910 as controlling authority, groups affected artifact IDs, customer consequences, minimal corrections and release checks, and prioritizes paid-intake/advertising blockers. It explicitly leaves compensation unapproved and accurately says the FAQ currently does not promise it (`:33`), matching `grading/E/input/approved-offer.md:31` and `grading/E/input/launch-artifacts.md:65`. It stays in the requested consistency-review scope (`grading/E/input/request.md:7–11`) without a new business model, legal judgment, or implementation claim. File/tool integrity assertions remain outside this assessment. |
| J13-7 — Correct elements and open decisions survive the review (`grading/E/criteria.md:45–47`). | **Partial** | Correct elements are explicitly preserved at `grading/E/output.md:9–10,35`: LP-1's locker/return scope, one-off service, actual 1–2 pair selection, and the cancellation rules. Compensation is correctly left unresolved at `:33`. However, `:11`, within **P0 — conflicts to correct before opening** (`:5`), calls LP-1's “2켤레 이상” inconsistent with the maximum-two rule and groups that wording with the real discount/transport errors. The supplied UX already prevents more than two pairs (`grading/E/input/launch-artifacts.md:37`); with that domain restriction, “two or more” charges no unsupported selected quantity. Narrowing the wording to “two pairs” is a clarity improvement, not demonstrated excess intake. This is the specific distinction requested by `grading/E/criteria.md:23,47`, and the output does not clearly make it. Its good retention/open-decision work therefore earns partial rather than fail. |

E's issue is the review's classification of a correct-but-broader phrase, not a price arithmetic error or an observed third-pair bug. The minimal improvement is to keep the real price corrections as P0 and label the LP-1 wording tightening as optional clarity while preserving the existing quantity control. No new transport policy or price is needed.

## Independent recalculation of material figures

JavaScript arithmetic was run during this assessment against the raw inputs. Values below substantiate the grades; they are not evidence that the original authors ran a tool.

### A/B

- A's output has **166 whitespace-separated words**. Five 15-minute interviews are **75 interview minutes**, before recruitment overhead; the output does not assert recruiting is free of effort.
- B's late-callback reason counts sum to **31 + 17 + 14 = 62**; pooled late events are **62/240 = 25.83%**, which the output correctly declines to reuse as each small desk's baseline. Stored SMS consent is **116/240 = 48.33%**; the output does not claim the other records are message-eligible. Raw basis: `grading/B/input/evidence.md:6–15`.

| B option | Backend / frontend / QA days, including report |
| --- | --- |
| Queue | 3.5 / 3 / 1.5 |
| SMS | 5.5 / 2 / 2.5 |
| Routing | 4.5 / 4 / 1.5 |
| Manager email | 2.5 / 2 / 1.5 |
| Queue + manager email | 5.5 / 5 / 2.5 |
| Capacity remaining after queue | 2.5 / 1 / 0.5 |

These reproduce `grading/B/output.md:17–24` from `grading/B/input/delivery-constraints.md:3–17`.

### C/D research and resource totals

Both raw research tables independently contain **42 opportunities, 28 memo-present opportunities, 20 read-marked opportunities, and 16 directly reminded opportunities** (`grading/C/input/research-records.md:24–30`; `grading/D/input/research-records.md:24–30`). Thus:

- Memo opportunities / all opportunities: **28/42 = 66.7%**.
- Read opportunities / memo opportunities: **20/28 = 71.4%**.
- Read opportunities / all opportunities: **20/42 = 47.6%**.
- None of these calculates unassisted usage, because the assistance/use cross-tab is missing.

| Resource | C | D | Supplied limit |
| --- | ---: | ---: | ---: |
| Founder, week 1 / 2 / 3 / 4 | 10 / 10 / 10 / 10 h | 9 / 10 / 9 / 10 h | ≤10 h each week |
| Founder total | 40 h | 38 h | 40 h |
| Developer total | 28 h | 28 h | 28 h |
| Designer total | 8 h | 8 h | 8 h |
| Five-store onboarding | 200 min = 3h20m | 200 min = 3h20m | Included within founder allocation |
| Cash allocated | 590,000 won | 550,000 won | 800,000 won |
| Cash unallocated | 210,000 won | 250,000 won | Remainder, not additional budget |
| Tool reserve | 100,000 won | 100,000 won | Includes 60,000 monthly fixed tool cost |

Sources: `grading/C/output.md:50–59`; `grading/D/output.md:48–57`; each corresponding `input/founder-brief.md:17–23` and `input/costs-and-delivery.md:9,14`.

### C/D economics

For both outputs, the supplied inputs give support cost **0.5 × 25,000 = 12,500 won per store-month**, and onboarding **40/60 × 25,000 = 16,666.67 won per new store**. Collection leaves **96.7%** of the charge. All values are on the raw fixtures' common VAT-excluded basis. Source: each `input/costs-and-delivery.md:3,9–16`.

| Recalculated quantity | Result |
| --- | ---: |
| A recurring contribution: 29,000 × .967 − 2,000 − 12,500 | 13,543 won/store |
| B recurring contribution: 19,000 × .967 − 2,000 − 12,500 | 3,873 won/store |
| B setup fee after collection: 20,000 × .967 | 19,340 won |
| A first-month contribution before fixed costs: 13,543 − 16,666.67 | −3,123.67 won/store |
| B first-month contribution before fixed costs: 3,873 + 19,340 − 16,666.67 | 6,546.33 won/store |
| A five-store recurring balance after fixed cost | 7,715 won |
| B five-store recurring balance after fixed cost | −40,635 won |
| A five-new-store first-month balance after fixed cost | −75,618.33 won |
| B five-new-store first-month balance after fixed cost | −27,268.33 won |
| Recurring break-even store count, A / B | ceil(60,000 / contribution) = 5 / 16 |
| A / B recurring contribution with 60 support minutes | 1,043 / −8,627 won/store |
| A five-store balance with 60 support minutes | −54,785 won |
| Actual 14-day offer, per new store: 14,500 × .967 − 2,000 − 12,500 − 16,666.67 | −17,145.17 won |
| Actual offer, five stores, including fixed cost | −145,725.83 won |
| Actual offer, five stores, excluding labor but including stated store/fixed costs | 107.50 won before recruitment and other unmeasured costs |
| Collection fee on five 14,500-won charges | 2,392.50 won |

These agree with `grading/C/output.md:105–115` and `grading/D/output.md:104–115`, allowing rounding. The positive recurring A illustration does not make the first cohort profitable, and both outputs explicitly preserve that distinction. Neither alternative's price is an accepted customer price or a rubric requirement.

### E price, capacity, and trial denominators

- First one-pair order: **18,000 + 4,000 − 3,000 = 19,000 won**.
- First two-pair order: **36,000 + 0 − 3,000 = 33,000 won**.
- Without the first-order discount: **22,000 / 36,000 won** for one/two pairs.
- The draft's one-pair total is short by **4,000 won**; its two-pair total applies **3,000 won too much discount**. These are separate order/pair-unit errors.
- At an explicitly hypothetical **23 reserved pairs**, **24 − 23 = 1** pair remains: another one-pair order reaches 24; another two-pair order reaches 25 and does not fit. The actual draft's **23 orders** does not establish an actual pair total.
- Survey response was **5/8 households = 62.5%**; satisfaction among respondents was **5/5 = 100%**. Satisfaction for the three nonresponding households is unknown, so whole-cohort satisfaction cannot be calculated.
- Historical next-day return was **6/8 pairs = 75%**, with two returned after two days. It was a free, different-scope pilot; it is not evidence of current-price paid repurchase or a next-day guarantee.

Raw bases: `grading/E/input/approved-offer.md:11,21–25`; `grading/E/input/launch-artifacts.md:41–49`; `grading/E/input/trial-record.md:5,9–15`. Output locators: `grading/E/output.md:11,13,17–29`.

## Evidence boundary

Missing execution evidence is not a contradiction. This report establishes only that the supplied prose does or does not satisfy the unchanged content criteria. It does not establish no unauthorized edits occurred, that a tool was used as claimed, that proposed tests passed, that any contact or payment occurred, or that estimated effort/cost/demand has been empirically validated. Those questions require separately authorized integrity/runtime evidence and were deliberately not scored here.
