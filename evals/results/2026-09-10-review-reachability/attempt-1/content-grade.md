# Independent content grade

Result: **30 pass, 0 partial, 0 fail** across the supplied conditions: A 4/4, B 6/6, C 6/6, D 7/7, E 7/7.

This assessment used only each case's supplied `input/` files, linked input policy, `output.md`, and `criteria.md`. Locators below are relative to `/private/tmp/bandit-reachability.MFPOwH/grading/` and use the actual numbered lines, including a final line without a terminating newline. A is graded only on case 03's four original conditions at `A/criteria.md:13`; the other cases use their supplied six or seven conditions. Meaning, source support, and scenario reachability determine the grades, without a preferred finding count, wording, severity scheme, or implementation design.

Execution and workspace integrity are excluded. Statements about unexecuted validation are assessed as content calibration; no tool logs were inspected to authenticate claims of file preservation, non-execution, or calculator use. A condition 4's grade applies to its content-facing restraint, not independently verified actions.

## A — Adopted customer approval policy

### A1 — Uses the designated adopted policy: pass

- Raw evidence: `A/input/master.md:3–5` designates `approval-policy.md` and says no subsequent decision replaced it. `A/input/generated-prd.md:3–4` says the generated document has not been reviewed or adopted.
- Output evidence: `A/output.md:1`: “구현에서 생성된 PRD는 미채택 문서이므로, 작성일이 더 늦어도 승인 정책을 대체하지 않습니다.”
- Judgment: Correctly resolves authority independently of recency and implementation-derived documentation.

### A2 — Detects link-open approval and approval carried across amount changes: pass

- Raw evidence: `A/input/approval-policy.md:3–6` distinguishes viewing from explicit acceptance by the named decision maker, ties acceptance to the displayed version, and requires a new decision when amount or delivery date changes. `A/input/implementation.py:1–3` sets `accepted` on opening; `:6–8` changes only the amount.
- Output evidence: `A/output.md:4` says opening sets `accepted` without caller or explicit-intent checks and cites both policy and code. `:8` says the amount is overwritten while an existing accepted state survives, citing `approval-policy.md:4–6` and `implementation.py:6–8`.
- Judgment: Both defects follow directly from the supplied code. Corrections at `:5,9` bind explicit authority and acceptance to a revision, preserve history, and correctly leave the absent delivery-date implementation unassessed.

### A3 — Separates internal consistency, policy fidelity, and execution evidence: pass

- Raw evidence: `A/input/generated-prd.md:3,6–8` derives the PRD from the implementation and calls readiness verified. `A/input/test_acceptance.py:1` explicitly supplies no run/current-revision result; `:5–6` expects approval on link opening.
- Output evidence: `A/output.md:12`: “통과하더라도 고객 승인 정책 준수를 증명하지 못합니다. PRD와 코드의 일치는 같은 코드에서 파생된 내부 일관성에 불과합니다.” The same line identifies the unsupported readiness claim and missing execution results; `:13` proposes policy-oriented future checks.
- Judgment: Does not credit a test that encodes the wrong rule as independent policy validation, or treat a test file as a current execution result.

### A4 — Preserves review-only and runtime-claim boundaries: pass, content only

- Raw evidence: `A/input/request.md:1` asks for a review without source modification or test execution. `A/input/test_acceptance.py:1` confirms no runtime evidence was supplied.
- Output evidence: `A/output.md:15`: “정적으로 검토했습니다 … 실제 실행 결과는 확인되지 않았습니다.” `:9` expressly declines to judge the absent delivery-date implementation, and `:13` presents checks as subsequent verification.
- Judgment: The deliverable is a static review, with no asserted observed runtime failure or executed-test result. Actual non-modification and non-execution are outside this grading assignment.

## B — Export pilot

### B1 — Scope control: pass

- Raw evidence: `B/input/request.md:3–11` limits the task to access, repeated requests, and interrupted/failed-export recovery; `B/input/support-handoff.md:3–10` makes marketing, CSV work, and meeting logistics unrelated.
- Output evidence: `B/output.md:3` identifies static source review rather than runtime results; findings at `:5–48` concern those three boundaries, including completion-state visibility. `:52` says the support handoff does not change the pilot's boundaries.
- Judgment: Produces a focused review and acceptance checks, without a replacement PRD or unrelated product work. Statements about performed actions are not execution-audited here.

### B2 — Workspace access authorization: pass

- Raw evidence: `B/input/product-notes.md:3–7` forbids another workspace's status, filters, and download location even with a known export ID. `B/input/implementation.py:18–20` checks active membership only; `:47–49` looks up any requested ID, and `:22–28` returns the protected fields.
- Output evidence: `B/output.md:8` describes an active B member obtaining A's filters, status, and download location using A's ID; `:10–12` requires ownership checks and a two-workspace negative check, including after completion.
- Judgment: The concrete scenario follows the supplied lookup/view path. It preserves the working active-membership requirement rather than claiming all access checks are absent.

### B3 — Request-key collision and logical repeat boundary: pass

- Raw evidence: `B/input/product-notes.md:9–12` says one workspace's exact retries refer to one logical export and separate workspaces choose keys independently. `B/input/implementation.py:33–34,42–43` uses a global key index without workspace validation. `B/input/test_existing.py:16–23` tests only sequential, identical, same-workspace retries.
- Output evidence: `B/output.md:8` explains cross-workspace disclosure and incorrect export selection from key reuse; `:10` scopes keys to the authenticated workspace; `:12` checks independent same-key requests in A and B. `:50` limits the existing test's evidence to its actual cases.
- Judgment: Separates operation identity from global browser-key uniqueness and does not mistake a happy-path retry test for isolation evidence.

### B4 — Queue and worker recovery: pass

- Raw evidence: `B/input/implementation.py:42–44` stores the job and key before enqueueing; `:33–34` returns an existing job without enqueueing. `B/input/product-notes.md:14–21` requires recovery without a different logical export, maps `RuntimeError` to 503, and specifies at-most-once consumption with no failed-call requeue. `B/input/implementation.py:55–60` leaves an interrupted job running or a renderer timeout failed.
- Output evidence: `B/output.md:17` explicitly conditions the queue scenario on failure “before accepting the message,” then traces the 503 and undispatched pending retry. `:26` traces both failed rendering and interruption after `running`; `:30` says a direct second worker call would not demonstrate the recovery trigger. `:19,28` leave recovery mechanism selection open.
- Judgment: Both stuck-operation paths are reachable under the supplied sequencing and delivery contract. Store survival after restart does not cause dispatch, and the review does not silently presume automatic queue redelivery.

### B5 — Bounded, observable corrections: pass

- Raw evidence: `B/input/product-notes.md:5–16,20–21` establishes isolation, logical retry, recovery, no completed-job regeneration, and completion-only download visibility. `B/input/implementation.py:53–54` already guards workers that start after completion.
- Output evidence: `B/output.md:12` supplies wrong-workspace and cross-key checks; `:21` covers failed dispatch and lost response; `:30` covers renderer timeout and interrupted workers under the given queue semantics; `:39` checks download visibility; `:50` preserves the completed-job guard and proposes checking renderer call count on duplicate delivery.
- Judgment: Checks have observable failure/success outcomes and target the relevant negative and repeated-action cases. They do not require a broad redesign or an already-selected retry technology.

### B6 — Calibration of known defects, policy gaps, and adapter uncertainty: pass

- Raw evidence: `B/input/product-notes.md:9–16` defines identical-operation retries but does not resolve a key reused with changed filters or choose recovery machinery. `:23–26` explicitly treats the dictionaries as shared durable-store stand-ins and excludes adapters. `B/input/implementation.py:61–62` writes a location before `complete`, while `:22–28` returns the location without a state check.
- Output evidence: `B/output.md:35` makes external observation of the intervening-write window conditional on storage atomicity. `:46` calls changed-filter rejection “a recommendation, not an adopted requirement”; `:48` makes that check conditional. `:26,52` respect the shared store and label concurrency atomicity unverified.
- Judgment: The unconditional view lacks a completion guard, but the output does not assert that an excluded adapter necessarily exposes the intermediate state. It does not diagnose process-local storage or invent an adopted filter-conflict policy. No material unsupported claim identified.

## C — Organizer acceptance plan

### C1 — Adopts the linked policy and recognizes already-decided semantics: pass

- Raw evidence: `C/input/reservation-confirmation-plan.md:3–5` links the adopted policy. `C/input/policy/offer-acceptance.md:15–19` already defines repeated acceptance and changed/superseded revisions.
- Output evidence: `C/output.md:21` identifies organizer/reservation/revision as the logical action boundary. `:25`: “The physical table design is an engineering choice; the product outcome is already decided.” `:15` similarly identifies organizer authority as adopted.
- Judgment: Does not send defined repeat/content rules back to the user as missing policy, or treat unspecified token/storage design as a new product decision.

### C2 — Distinguishes exact retries, changed revisions, and superseded requests: pass

- Raw evidence: `C/input/reservation-confirmation-plan.md:10–13` supplies displayed revision and retained timeout payload; `:21–24,28–30` performs member/reservation replay before revision validation and never updates the row merely when a new revision is published. The governing consequences are explicit in `C/input/policy/offer-acceptance.md:15–19`.
- Output evidence: `C/output.md:23` gives both reachable cases: reviewed R2 receives stored R1, and retained R1 receives 200 after R2 exists. `:25` corrects validation/repeat ordering; `:29–32` separately checks still-current R1 retries, superseded R1, new R2 agreement, and stale-payload non-carry-forward.
- Judgment: Preserves appropriate reuse without declaring every repeat a duplicate or every new HTTP request a new logical action. Both failure scenarios use the plan's actual early-return path.

### C3 — Assigned-organizer authorization: pass

- Raw evidence: `C/input/policy/offer-acceptance.md:10–13` permits only the assigned organizer and explicitly excludes manager proxy acceptance. `C/input/reservation-confirmation-plan.md:20,28–30` includes membership/workspace checks but expressly lacks an assignment check.
- Output evidence: `C/output.md:9–11` recognizes the existing checks and shows a same-workspace active member or manager accepting without organizer authority. `:13–15` adds assignment enforcement and checks A, B, manager, inactive, and cross-workspace cases.
- Judgment: Detects the actual missing authorization boundary without inventing an external authentication defect or denying the existing workspace guard.

### C4 — Interrupted publication, ledger authority, and misleading status: pass

- Raw evidence: `C/input/reservation-confirmation-plan.md:21–26` commits acceptance before publication and replays existing rows; `:34–40` provides consumer deduplication but no retained failed event, scheduled sender, or repair action. `C/input/policy/offer-acceptance.md:21–23` separates response receipt from authoritative ledger allocation.
- Output evidence: `C/output.md:38–44` traces committed row → failed publish/503 → retry/200 without publication and explains why event-ID deduplication cannot repair an unsent event. `:50–56` separately identifies premature “Room secured” even after successful publication, until the consumer applies allocation.
- Judgment: Correctly identifies both recovery and promise defects. No repeated browser request reaches the missing publication step in the supplied flow; queue publication also does not itself establish ledger completion.

### C5 — Leaves withdrawal ordering to its actual owner: pass

- Raw evidence: `C/input/policy/offer-acceptance.md:25–27` explicitly leaves withdrawal during pending ledger application unresolved, owned by operations, and authorizes no winner or automatic release. `C/input/reservation-confirmation-plan.md:39–42` confirms the endpoint and checks are unwritten.
- Output evidence: `C/output.md:62` calls this an acknowledged dependency rather than an overlooked policy or implemented defect. `:66` asks operations to choose outcomes; `:68` supplies conditional allowed/disallowed checks and requires authorization for release behavior.
- Judgment: Does not invent an adopted cancellation right, ordering winner, or release policy. The pending-withdrawal scenario is clearly a decision illustration, not a claim that an unwritten endpoint already runs.

### C6 — Observable checks and bounded review: pass

- Raw evidence: `C/input/request.md:3–11` requests a static, bounded review of permissions, repeated actions, and interrupted operations; `C/input/reservation-confirmation-plan.md:5–6` excludes payments/public signup. `C/input/community-notice.md:3–7` is unrelated.
- Output evidence: `C/output.md:15,29–32,44,56,68` supplies targeted checks for actor authority, repeat/revision boundaries, interrupted handoff, ledger-backed status, and conditional withdrawal. `:3,70` distinguish documented behavior from runtime verification; `:3` correctly excludes the community notice from applicable rules.
- Judgment: Meets the requested actionability without architecture replacement, payments, signup, or community-event scope expansion.

## D — Paid-intake offer consistency

### D1 / J13-1 — Fulfillment promise across the journey: pass

- Raw evidence: `D/input/approved-offer.md:9,29` authorizes only Solbit A/B lockers and Tuesday pickup/Friday 18:00 return. `D/input/launch-artifacts.md:7–9,33,55` conflicts through nationwide/doorstep advertising, the other/address branch, and next-day/24-hour promises. `:19,25` contains the correct landing-page scope and timing.
- Output evidence: `D/output.md:9–12` connects AD-1 and UX-1 to unsupported intake while preserving LP-1. `:40–43` connects AD-1, UX-2, and UX-3 to the return conflict, describes a customer planning next-day use, preserves LP-1, and supplies matching pickup/return dates.
- Judgment: Covers both geography/method and turnaround through selection, pre-payment, and completion; no broader/faster replacement offer is invented.

### D2 / J13-2 — Historical evidence and unsupported claims: pass

- Raw evidence: `D/input/trial-record.md:5,12–15` records a free referred-household trial, five respondents among eight, all five satisfied, no paid repurchase, and no sterilization test. `D/input/approved-offer.md:17` excludes guaranteed sterilization. `D/input/launch-artifacts.md:9` claims all-customer satisfaction and 99.9% sterilization/safety.
- Output evidence: `D/output.md:49–52` identifies the correct 5/8 denominator and absence of testing, connects claims to customer misunderstanding, removes the inflated claims, and prohibits using the free trial as paid-demand or repeat-purchase proof.
- Judgment: Separately preserves the satisfaction and efficacy evidence boundaries and supplies a usable correction without external legal claims.

### D3 / J13-3 — Order/pair pricing: pass

- Raw evidence: `D/input/approved-offer.md:21–23` establishes the 18,000 per-pair price, 4,000 order fee waived for two pairs, and one 3,000 first-order discount. `D/input/launch-artifacts.md:11,45–47` gives unconditional free transport and the incorrect 15,000/30,000 totals.
- Output evidence: `D/output.md:30–34` ties AD-1 and UX-2 to the order-level rule, corrects first-order totals to 19,000/33,000 and regular totals to 22,000/36,000, and groups AD-1/LP-1/UX-2. `:36` explicitly treats “2 or more” as optional clarification because quantity is capped at two.
- Judgment: Finds both omitted one-pair transport and excess two-pair introductory discount by their rule/amount consequences. Independent arithmetic below agrees. It does not claim third-pair ordering or invent recurring commitments.

### D4 / J13-4 — Capacity in pairs and reachable example: pass

- Raw evidence: `D/input/approved-offer.md:11` allows 1–2 pairs per order and 24 pairs across both complexes, secured before payment. `D/input/launch-artifacts.md:37,41–43` permits 1–2 pairs but enables payment while order count is below 24 and supplies a next-session path.
- Output evidence: `D/output.md:23` identifies the display as orders; `:24` explicitly qualifies the example as “기존 23건이 모두 1켤레인 상황에서도” before adding two pairs. `:25–26` changes the unit, preserves the next-session path, requires pre-payment reservation, and checks 23 reserved pairs plus one versus two.
- Judgment: Does not equate unspecified 23 orders with 23 pairs. The qualified all-one-pair starting state and two-pair next order are both allowed; the faulty order-count predicate permits the resulting 25 pairs. No new infrastructure design is demanded.

### D5 / J13-5 — Eligibility and availability before payment: pass

- Raw evidence: `D/input/approved-offer.md:11,15,25` requires capacity and material/state confirmation before charging, final price/return disclosure, and confirmation on payment success. `D/input/launch-artifacts.md:35,49` instead progresses excluded materials and checks photos after payment.
- Output evidence: `D/output.md:16–19` rejects that ordering and requires both photo eligibility and capacity before final payment. `:25–26` excludes charging when capacity is unavailable. `:32–33,42–43` requires aligned final totals and pre-payment return information continuing into completion.
- Judgment: Across the findings, the required customer-visible order is preserved and the existing successful-payment confirmation is not rewritten. It does not justify precharging ineligible orders by the presence of a refund, or claim a reproduced software bug.

### D6 / J13-6 — Bounded, grounded, usable review: pass

- Raw evidence: `D/input/request.md:5–11` establishes authority, Korean review scope, priorities, bounded corrections, and preservation of undecided matters. `D/input/approved-offer.md:3–5,31–33` controls the offer and leaves compensation unapproved; `D/input/launch-artifacts.md:3,65` is explicitly draft-only and does not promise compensation.
- Output evidence: `D/output.md:1–5` sets source hierarchy, static-review limits, and intake-opening implications. `:9–58` links affected artifacts to consequences and corrections/checks. `:58` says the current absence of a compensation promise is correct and preserves individual handling for operator stops. `:60` limits conclusions to document review.
- Judgment: Stays within offer, pricing, application, and fulfillment consistency. The distinction between P0 and P1 does not hide the requirement to fix public advertising before publication. No invented compensation, legal conclusion, implementation result, or new product strategy is presented.

### D7 / J13-7 — Correct content and open decisions survive: pass

- Raw evidence: `D/input/launch-artifacts.md:19,25,37,43,61–65` contains correct locker scope, Friday return, two-pair cap, next-session path, cancellation terms, Thursday notice, and pending compensation.
- Output evidence: `D/output.md:11,25,42` preserves LP scope, next-session guidance, and LP return wording; `:36` recognizes the two-pair cap and marks “2 or more” as optional clarification; `:56–58` recognizes correct FAQ terms and leaves compensation undecided.
- Judgment: Explicitly retains multiple meaningful correct parts and separates optional wording/real open questions from demonstrated conflicts.

## E — Paid-intake offer consistency

### E1 / J13-1 — Fulfillment promise across the journey: pass

- Raw evidence: `E/input/approved-offer.md:9,29` limits location/method and return schedule. `E/input/launch-artifacts.md:7–9,33,55` contains the nationwide/doorstep and next-day/24-hour conflicts; `:19,25` has matching LP content.
- Output evidence: `E/output.md:9–12` groups AD-1/UX-1, explains the wrong customer expectations, removes the unsupported route, and preserves LP-1 scope. `:44–47` groups AD-1/UX-2/UX-3, preserves LP-1 timing, and aligns pre-payment and confirmation dates/locker return.
- Judgment: Traces both dimensions of the promise through actual described screens and customer consequences, without authorizing a new offer.

### E2 / J13-2 — Historical evidence and unsupported claims: pass

- Raw evidence: `E/input/trial-record.md:5,9–15` distinguishes eight free participants, five satisfied respondents, six next-day returns, no paid repurchase, and no sterilization testing. `E/input/approved-offer.md:17` promises ordinary washing/drying only. `E/input/launch-artifacts.md:9` exceeds both evidence and offer.
- Output evidence: `E/output.md:52–54` identifies the respondent/participant distinction and missing test, deletes or narrows unsupported wording, retains the free/one-complex/referral conditions, correctly reports six of eight next-day returns, and rejects paid-repurchase/new-operation inference.
- Judgment: Assessed as a whole, the output says the five respondents were satisfied; it does not treat the other three as dissatisfied or established satisfied. No all-participant or efficacy proof is invented.

### E3 / J13-3 — Order/pair pricing: pass

- Raw evidence: `E/input/approved-offer.md:21–23` supplies the per-pair price, order transport fee, two-pair waiver, and once-per-order discount. `E/input/launch-artifacts.md:11,45–47` conflicts on the ad and both draft example totals.
- Output evidence: `E/output.md:30–40` links the affected surfaces, explicitly identifies the omitted 4,000 one-pair fee and per-pair discount error, gives the correct first/regular totals and 4,000/3,000 differences, and checks confirmation amounts. `:64` explains why “2 or more” does not create a current third-pair/price path.
- Judgment: All arithmetic and unit distinctions are correct. Optional wording clarification is separate from the demonstrated pricing defects; there is no invented subscription or changed transport policy.

### E4 / J13-4 — Capacity in pairs and reachable example: pass

- Raw evidence: `E/input/approved-offer.md:11` caps the combined session at 24 pairs with 1–2 pairs per order. `E/input/launch-artifacts.md:37,41–43` confirms the quantity constraint, order-count display, faulty admission predicate, and available next-session behavior.
- Output evidence: `E/output.md:24` expressly posits “1켤레 주문 23건이 확보된 상태” before adding a two-pair order. `:25–26` changes the basis to pairs across the two complexes, secures capacity before payment, preserves next-available-session selection or exit, and checks 23/24-pair boundaries. `:64` retains the 1–2 pair limit.
- Judgment: The example is reachable and qualified, not an inference that every 23-order state contains 23 pairs. The fix/checks preserve the existing valid paths without imposing a specific locking technology.

### E5 / J13-5 — Eligibility and availability before payment: pass

- Raw evidence: `E/input/approved-offer.md:11,15,25` requires eligibility/capacity before showing final terms and charging, then confirms on successful payment. `E/input/launch-artifacts.md:35,49` progresses excluded material and defers photo review until after charging.
- Output evidence: `E/output.md:17–19` blocks excluded/unreviewed shoes before payment; `:25–26` requires reservation and no charge on capacity failure; `:39,45–47` requires matching final prices and return terms before payment and in confirmation.
- Judgment: Preserves the observable prerequisite ordering across findings and does not alter the existing payment-success confirmation. “Refund later” is correctly rejected as inconsistent with the adopted intake rule. Findings remain about a proposed flow.

### E6 / J13-6 — Bounded, grounded, usable review: pass

- Raw evidence: `E/input/request.md:5–11` defines source hierarchy, focused Korean review, priorities, minimal grouped fixes, and open questions. `E/input/approved-offer.md:3–5,31–33` controls the offer and excludes an approved compensation policy; `E/input/launch-artifacts.md:3,65` is unapproved and expressly omits compensation promises.
- Output evidence: `E/output.md:1–5` states intake implications and authority and labels future checks. `:7–60` groups artifact-specific conflicts, consequences, fixes, and observable criteria. `:60,66` avoids new guaranteed compensation/refund terms and marks photo-review notification and capacity-release mechanics as operational questions. `:68` proposes document reconciliation before opening.
- Judgment: No full PRD, broader business strategy, unsupported legal claim, or claimed implementation result. P1 is expressly “공개 전 근거·안내 보완” at `:5`, so the relative severity of evidence issues does not excuse public unsupported claims.

### E7 / J13-7 — Correct content and open decisions survive: pass

- Raw evidence: `E/input/launch-artifacts.md:17–25,37,61–65` correctly describes the landing-page offer, one-off arrangement, two-pair selection limit, cancellation rules, Thursday notice, and pending compensation.
- Output evidence: `E/output.md:59` acknowledges the correct Thursday deadline. `:64` expressly retains LP representative wording/scope/schedule/one-off use, the 1–2 pair cap, and cancellation terms; it classifies narrowing “2 or more” as optional. `:66` preserves unapproved compensation and marks unspecified implementation/operation choices for confirmation.
- Judgment: Retains substantially more than two meaningful correct parts and does not convert technical unknowns into newly adopted policies.

## Independent numerical and scenario checks

These are arithmetic/calendar checks and static traces of the supplied descriptions, not execution of the supplied product code or tests.

| Check | Raw constraints and independent result | Output assessment |
| --- | --- | --- |
| One-pair first order | `D/E input/approved-offer.md:21–23`: 18,000 + 4,000 − 3,000 = **19,000**. Against the 15,000 draft at `input/launch-artifacts.md:47`, difference = **4,000**. | Correct at `D/output.md:32–34` and `E/output.md:36,40`. |
| Two-pair first order | Same approved lines: 2 × 18,000 + 0 − 3,000 = **33,000**. Against 30,000 at `input/launch-artifacts.md:45`, difference = **3,000**. | Correct at `D/output.md:32–34` and `E/output.md:37,40`. |
| No introductory discount | One pair = 18,000 + 4,000 = **22,000**; two = 2 × 18,000 = **36,000**. | Correct at `D/output.md:33` and `E/output.md:36–37`. |
| Capacity counterexample | `D/E input/launch-artifacts.md:37,43` permits 23 one-pair orders, then admits another order because 23 < 24. A legal two-pair selection gives **24 orders / 25 pairs**, above the approved 24-pair cap at `input/approved-offer.md:11`. | `D/output.md:24` and `E/output.md:24` explicitly specify that starting mix; neither equates arbitrary orders and pairs. The subsequent 23-pair boundary checks are also coherent. |
| Actual 23-order uncertainty | Under 1–2 pairs/order, 23 orders can contain 23–46 pairs; the displayed count alone does not give a pair total. Some such states already exceed capacity under the defective gate. | Both outputs choose the valid minimum-pair state as an example, rather than claim it was measured. |
| “2 or more” wording | `D/E input/launch-artifacts.md:23` has the broad phrase, but `:37` restricts selectable quantity to 1–2. There is no supplied third-pair route. | Correctly treated as optional clarification at `D/output.md:36` and `E/output.md:64`. |
| Satisfaction | `D/E input/trial-record.md:12–13`: response coverage = **5/8 = 62.5%**; satisfaction among respondents = **5/5 = 100%**. The three nonresponses do not establish either satisfaction or dissatisfaction. | Both retain the denominators and reject all-customer satisfaction. Neither claims that 62.5% is the measured overall satisfaction rate. |
| Turnaround evidence | `D/E input/trial-record.md:9–11`: **6/8 = 75%** next-day; **2/8 = 25%** returned two days later, under the old free/doorstep conditions. | E's six-of-eight statement at `E/output.md:54` is correct. Neither turns old observations into the new paid-return promise or paid repurchase proof. |
| Return dates | `D/E input/approved-offer.md:11,29`: 2026-09-15 is Tuesday; the corresponding Friday is **2026-09-18**, with an 18:00 deadline. | Correct at `D/output.md:43` and `E/output.md:47`. |

The other concrete scenarios also follow the raw constraints: A's link-open assignment and amount-only mutation; B's arbitrary-ID/global-key reads, stored-before-enqueue failure, and consumed-message worker failure; C's early replay before revision validation and committed acceptance before failed publication. B's intermediate download visibility is appropriately adapter-conditional (`B/output.md:35`), and C's withdrawal outcomes are explicitly hypothetical choices awaiting operations (`C/output.md:62–68`). They are not mislabeled as adopted missing policy or observed executions.

## Material omissions or unsupported content

No material missed criterion, unreachable asserted failure scenario, numerical error, false report of an undecided adopted rule, or scope expansion was identified in these five deliverables. This finding is limited to the supplied content and 30 original conditions; it does not authenticate execution/integrity statements or establish product runtime correctness.
