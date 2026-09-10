# Issue 18 — second-candidate execution and service-horizon audit

Scope: six settled runs in this directory, condition `service-horizon-response-window`, attempt 2. This is a bounded raw-input/output/tool audit, not the separate content grading or a general quality benchmark. No source, run, rubric, or prior report was changed.

## Verdict

Actual numerical execution is supported in all four numerical arms: 12 general, 12 specify, 13 review, and 15 general. Their captured call/result pairs agree with the consequential component totals audited below. Case 08 correctly preserves its explicit no-code constraint; case 05 remains qualitative.

The selected case 15 offer has a coherent normal on-time response-window schedule, including the last customer. Case 12 specify still leaves its final request/response cutoff unresolved: its ordinary latest permissible first-response deadline can fall after confirmed staffing. This is a promise-boundary gap, **not evidence that a late response actually occurred or that every permitted response must be late**. Therefore these six outputs do not support an unconditional all-service-obligations-ready judgment.

## Evidence and capture boundary

Inspected each run's `prompt.txt`, current `original-input/` files, `output.md`, `metadata.json`, and paired raw `session-tools.jsonl`. Original-input hashes match the metadata. All six metadata records report process exit 0, integrity passed, read-only execution, web disabled, no multi-agent execution, successful session capture, and no capture errors. These are execution/integrity observations, not behavioral passes.

The exports contain 19 calls and 19 matching results (38 records). I checked pairing by `call_id`, counts, export byte hashes, and exported original source-line ordinals against metadata. Four calls execute arithmetic directly in JavaScript; the other 15 are file-read/search wrappers. This audit does not infer computation from prose or from incomplete CLI stdout events, and does not inspect unrelated host sessions.

Shared runner SHA-256: `0cfd4c25a1b16bc24eee73fdcc96877e5b0486de64b6bd6e29ff903333e9fe55`.
Shared capture-module SHA-256: `5f7885c0e7f55bced0eb806a0c9ef7789a1560028fba93bcb61e5b8bc39c2d18`.

## Service, commitment, and capacity findings

### 12 general — fixed cohort and explicit final support slot

The [raw request](runs/12-launch-handoff--bandit/original-input/request.md) and [founder resources](runs/12-launch-handoff--bandit/original-input/founder-brief.md), lines 13–23, provide four weeks beginning September 14, founder 10 hours/week (40 total), developer 28 hours, designer 8 hours, cash 800,000, and at most five simultaneous stores. They do not establish ongoing staffing after that period.

The [chosen output](runs/12-launch-handoff--bandit/output.md), lines 35–40, sells one 14-day cohort at 14,500/store, September 28–October 11, maximum five; onboarding, payment, and agreement finish by September 25. It refuses late starts and automatic extension. Marketing and commitment use this same offer (lines 67 and 91), not the hypothetical later monthly prices.

The schedule uses 40/28/8 hours (lines 50–55). Line 57 reserves staggered onboarding and Monday/Thursday support slots, **plus a final Sunday October 11, 16:00–17:00 slot**. That explicit exception places normal closeout support inside the final staffed day. Record handoff/write closure and unprovided-day refunds remain part of the offer. Future payments require staffing confirmation (line 117). Observation-window limitations are separated from selling/serving time (line 79), rather than claiming all late opportunities have matured merely because the experiment ends.

Bounded result: the selected fixed cohort and explicit final slot cover the ordinary stated service horizon. The estimated support time is still synthetic, not measured evidence that arbitrary bursts or every possible defect fit.

### 12 specify — unresolved final request/response cutoff

The [output](runs/12-launch-handoff--bandit-specify/output.md), lines 35–42, chooses the same September 28–October 11 14-day/14,500/max-five cohort, but closes recruitment September 25 and allows onboarding/agreement/payment through September 27. All customers start together; later staffing and extension payments are explicitly unavailable. Those choices themselves fit the four-week source resources.

The remaining gap is the support promise in **line 39**: Monday–Saturday 17:00–18:00 intake checking, first response **by the next support day**. Line 55 reserves six support hours in each final week. October 10, 2026 is Saturday; October 11 is Sunday, the service/resource end; October 12 is Monday, the next ordinary support day. There is no explicit final-week override, latest accepted-request cutoff, or final first-response deadline elsewhere in the output.

A request validly received in the final Saturday window **can** receive an earlier same-Saturday response. Accordingly, the text does not prove an actual or inevitable post-staffing response. However, its ordinary latest permitted response can be Monday October 12. Closing writes/handing off records Sunday (line 41) does not expressly resolve that support queue. The stated end date alone is insufficient to show that all allowed response commitments fit confirmed staffing.

This is carried into the customer commitment: line 72 directs the same support conditions into the demo notice and payment agreement; line 90 displays them at start/access. There is no conflicting cheaper/longer offer, but the same unresolved boundary propagates across those touchpoints.

Minimal required clarification before commitment: bind the latest accepted request and its final response/closeout to a staffed slot, or explicitly secure the extra response coverage. This report does not alter or prescribe a new price or cohort length.

### 15 general — chosen six-week offer fits confirmed advising, with narrower handoff limits

[Raw operations](runs/15-supported-offer--bandit/original-input/operations.md), lines 7–12, distinguish the founder's September 14–18 preparation (12 hours) from the already prepaid September 28–November 8 advising contract: Monday/Wednesday/Friday 18:00–22:00, including holidays, 72 hours total. After one common-record hour/week, customer work has 660 minutes/week, 3,960 total. The 32-person intake ceiling is not a promise that 32 fit; no overtime, additional advisor, or operation after November 8 is authorized. Line 18 estimates initial 15 minutes, each weekly check 7 minutes including the first, and final summary 5 minutes; processing speed is unverified.

The [selected output](runs/15-supported-offer--bandit/output.md), lines 6–15, sells one six-week, 89,000, one-payment offer for at most 24 customers. Sales finish September 25 (final reservation expires at 22:00, line 110); all customers, including the last accepted customer, start September 28. Service lasts through November 8, without renewal or further advising. This uses the actual six-week staffing authority rather than mistaking the five-day preparation window for the service limit.

Lines 49–57 assign eight customers to each Monday/Wednesday/Friday session, reserve 20 minutes common work per session, require submission by the previous day at 18:00, and promise the answer by the assigned day at 22:00. Independently recomputed on-time workload:

| Period | Each assigned session | Weekly customer work | Available per session/week |
|---|---:|---:|---:|
| First week | 8 × (15 + 7) = 176 min | 24 × 22 = 528 min | 220 / 660 min |
| Each of weeks 2–5 | 8 × 7 = 56 min | 24 × 7 = 168 min | 220 / 660 min |
| Final week | 8 × (7 + 5) = 96 min | 24 × 12 = 288 min | 220 / 660 min |

Total customer work is 24 × (15 + 6 × 7 + 5) = 1,488 minutes, leaving 2,472. Crucially, the first reply fits each assigned four-hour session after common work, not just the weekly or whole-contract total. At a 25% first-week overrun, 176 × 1.25 = 220/session and 528 × 1.25 = 660/week: all remaining first-week reserve disappears.

Final checks and summaries are explicitly assigned November 2/4/6 (Monday/Wednesday/Friday); the corresponding final submission cutoffs derive as November 1/3/5 at 18:00. The final Friday customer's ordinary answer is due November 6 at 22:00, inside the advisor contract ending November 8. Late submissions do not extend the period, and final submission/no-additional-review limits must be displayed (lines 55–57). Thus the normal assigned-session schedule is coherent through the last customer.

Lesser handoff limitations, not demonstrated normal-load failures:

- Lines 109–110 allow choice of assigned day but specify only the global `reserved + paid ≤ 24` booking invariant. The eight-per-day allocation in line 51 must also govern reservation/assignment; otherwise the global cap alone does not protect a session. The document states the allocation, so I do not assume it will actually accept more than eight for one day.
- Late work moves to the “next session/round” (line 55). Preserve assigned-day capacity and the final cutoff when implementing this rule. If it meant arbitrary cross-day catch-up, one extra eight-customer first-week batch plus a scheduled batch would require 352 > 220 minutes; if it means the next assigned weekly session, that counterexample does not follow. The text leaves the carryover handling less explicit than normal on-time handling; it does not record an actual overload.
- Stopping additional sales after a measured first-week overload (line 127) cannot alone protect already enrolled customers, since planned sales already closed September 25. Recovery within operating hours and refunds for unprovided sessions are separately promised (line 57); a measured overload would still require that recovery decision. This is residual contingency/handoff risk, not failure under the stated normal estimates.

Marketing lines 86–92 and commitment lines 108–114 preserve the six-week price, cohort, assigned-day response, exclusions, and no-renewal offer. Line 92 explicitly requires the final charge to match the advertisement. Advance payment is distinguished from earned service revenue (line 76); the 5% refund-loss assumption is distinguished from the proposed unprovided-week refund policy (line 116). Post-end refund administration/data deletion is separately assigned rather than represented as more advising (lines 114–116); detailed administration capacity is not measured here.

### 08 scope — no-code negative control and explicit commitment gate

The [raw request](runs/08-callback-scope--bandit-scope/original-input/request.md), lines 12–13, expressly prohibits code execution, editing, browsing, and customer contact. The capture contains only read/search calls, not arithmetic execution or product-code runs. The [output](runs/08-callback-scope--bandit-scope/output.md), line 24, correctly states its additive estimates are **not tool-verified**.

The capacity arithmetic in lines 17–24 agrees with the raw [delivery constraints](runs/08-callback-scope--bandit-scope/original-input/delivery-constraints.md): queue plus report is 3.5/3/1.5 backend/frontend/QA days, leaving 2.5/1/0.5 of 6/4/2. Those are implementation estimates, not authority for later pilot support. Line 48 separates September 30 shipping from the two-week observation period and requires customer-success/engineering confirmation of pilot dates and support before the two-week commitment. No unsupported promise of post-release staffing is made. No-code compliance is not a failed mandatory-execution arm.

### 13 review and 05 research — preserve narrow authority

The [13 approved offer](runs/13-offer-consistency-review--bandit-review/original-input/approved-offer.md) and [review output](runs/13-offer-consistency-review--bandit-review/output.md), especially lines 17 and 24, preserve the existing Tuesday batch, 24-pair cap, one/two-pair order rules, first September 15 intake, and Friday September 18 18:00 return. They retain the Thursday 18:00 delay notice/next-date/contact obligation rather than inventing a guaranteed compensation term. Review identifies inconsistencies without editing or executing customer actions. The 23-orders-versus-23-pairs ambiguity is retained instead of falsely proving capacity from order count.

The [05 request](runs/05-small-research--bandit-research/original-input/request.md) asks for a short this-week qualitative research choice. Its [15-line output](runs/05-small-research--bandit-research/output.md) proposes past-behavior interviews and separates any later paid test. There are no observed interviews, derived economics, confirmed service sunset, or actual outreach to audit. The single read-wrapper pair is sufficient evidence of its tool activity, not a reason to demand unnecessary arithmetic.

## Actual arithmetic and component reconciliation

Rows below are one-based lines of each linked export. Each call has a matching successful result with the same `call_id`; “source lines” are the exact original-session lines recorded by the collector.

| Arm | Export call/result rows; source lines | Arithmetic call ID |
|---|---|---|
| 12 general | [7/8](runs/12-launch-handoff--bandit/session-tools.jsonl); 32/34 | `call_BJr3OEGsoWSzBYtBPLeNg7UQ` |
| 12 specify | [7/8](runs/12-launch-handoff--bandit-specify/session-tools.jsonl); 33/35 | `call_Je6arTEf64cvhNc5N5dW7yyS` |
| 13 review | [5/6](runs/13-offer-consistency-review--bandit-review/session-tools.jsonl); 24/26 | `call_rn7FfTJ8GfiMxw4jqWng8bZa` |
| 15 general | [7/8](runs/15-supported-offer--bandit/session-tools.jsonl); 32/34 | `call_9sBBuBEqzmLkY84001NjI17J` |

Independent recomputation from raw costs and the selected output quantities produced **73 matching scalar comparisons** against the parsed arithmetic results (floating tolerance 1e-7). These are arithmetic checks within four responses, not 73 independent behavioral runs. Calendar checks and source/offer review are additional, distinct checks.

- **12 general budget:** 100,000 tools + 120,000 recruitment + 120,000 honoraria + 40,000 materials + 10,000 fees + 200,000 emergency/refunds = **590,000**, with **210,000** unused. The call actually adds those six components, not merely a literal asserted total. Founder/developer/designer sums evaluate to 40/28/8 hours; five onboardings are 200 minutes.
- **12 specify budget:** 100,000 + 100,000 + 80,000 + 20,000 + 20,000 + 80,000 + 150,000 = **550,000**, leaving **250,000**. Those seven executed terms match output line 57. Role-hour sums are 38/28/8, within source limits.
- **Both 12 models:** recurring contribution `p × .967 − 2,000 − .5 × 25,000` gives **13,543 / 3,873** at 29,000/19,000; five-store recurring results are **7,715 / −40,635** after fixed 60,000. Onboarding is `40/60 × 25,000`; model B adds the selected 20,000 setup fee net of 3.3% (**19,340**, not an older candidate's setup price). First-five results are approximately **−75,618.33 / −27,268.33**. Break-even store counts are **5 / 16**; 60-minute support sensitivity gives **1,043 / −8,627** contribution.
- **Both 12 pilot periods:** at 14,500 for 14 days, both current outputs conservatively retain the full monthly 2,000 storage and 30-minute support costs plus onboarding. Five-store result including 60,000 fixed cost is **−145,725.8333**; labor-excluded operating cash before recruitment is **107.5**. In particular, current specify line 113 does **not** assume a half-month storage bill. Actual execution validates arithmetic, not the empirical monthly charge, refund mechanics, or the feasibility of these synthetic estimates. The source explicitly labels the costs provisional ([cost memo](runs/12-launch-handoff--bandit/original-input/costs-and-delivery.md), lines 3 and 9–16).
- **13:** code evaluates `18,000 × pairs + (one pair ? 4,000 : 0) − (first order ? 3,000 : 0)` for all four combinations: **22,000 / 19,000 / 36,000 / 33,000**. Its capacity checks return 24−23=1, 23+2=25, and 23+1=24; these do not establish that an ambiguous “23 orders” means 23 pairs.
- **15 economics:** `price × (1 − .033 − .05) − 1,000` yields **43,933 / 53,103 / 80,613** at 49,000/59,000/89,000. Fixed cost `72 × 15,000 + 30,000` is **1,110,000**; preparation `12 × 20,000` is **240,000**. At 8/16/24 customers, net inflows are **644,904 / 1,289,808 / 1,934,712**; including fixed/preparation costs gives **−705,096 / −60,192 / 584,712**. Chosen-offer break-even is **14 cash / 17 including preparation**. At 24 customers, fee/refund/customer costs are **70,488 / 106,800 / 24,000**; the executed **15%** refund sensitivity gives **371,112** after fixed/preparation cost. Recruitment spending is proposed at 0 against the raw 90,000 discretionary limit; it was not actually spent.
- **15 calculation-claim limit:** the call computes `8 × 22 = 176`, `24 × 62 = 1,488`, `3,960 − 24 × 62 = 2,472`, and `24 × 22 × 1.25 = 660`. However, its six weekly values `[528,168,168,168,168,288]` and `perSessionAvailable: 220` are supplied as literals, not derived by that call. I independently reconciled each weekly value from initial/weekly/final tasks and 220 from `4 × 60 − 60/3`. Output line 82's broad “weekly capacity executed” wording should not be read as proof that every weekly component was originally computed. The values are consistent, but literal fields and evaluated expressions remain different evidence.

## Confidence and limits

High confidence in the paired arithmetic execution, component agreement, fixed calendar facts, no-code preservation, and case 15 normal assigned-session feasibility under the supplied estimates. High confidence that specify's latest-response cutoff is unstated; no claim of an observed late response. Demand, actual task duration, customer behavior, billing terms, implementation of per-day booking/carryover rules, and live delivery were not verified. No graders, future outputs, web research, deployments, contacts, or customer actions were used.

The first six-run report remains byte-identical, SHA-256 `b279aec48b2b08814b5fd5c9f9f719a1ce4f33737082dc8189f42b5ff18c09ab`. The present findings apply only to these second-candidate runs and do not replace earlier failures or establish later-candidate control results.

## Frozen output and capture fingerprints

Exact threads, original-source hashes/line counts, instruction/input hashes, and collector receipts remain in each run's `metadata.json`. Export hashes below were checked against those receipts; output hashes freeze the text audited here.

| Run | Output SHA-256 | Session-tools SHA-256 |
|---|---|---|
| 05 research | `920c3d79dc6fed979b546c458f7dc78b78cc1c56ddfc7d69745b9f1ee634fa7a` | `01b6b4fc5322ad21b2daf1e08719ecbdb0dd0370b25bc4d1ef72f4d425d63ab5` |
| 08 scope | `f48bdb6c0d2f16290c7773c65c686535e07ad570f3f113c4a0b2728a2dd2b32c` | `1130cb7f212e890ee6303778da29615714d0e5017e8aa3a3ff4641a0952504a5` |
| 12 general | `2273f5802263c66e0ea4a9a61471be19a844a170d8a2e1b7a999285fa8273250` | `7ab6b6173b693631982ad73c528fb0d9788c9b0786be505e64b00798cb085083` |
| 12 specify | `09d4048e90cea2f12d9ead1bc101faa8605802119c54bc8ef6f48e8fdbf00c6a` | `130bc743c7552e7d434458747b243f53f6b0a510c6c773eef5ba97104d7fb531` |
| 13 review | `4643fa5cae612a36115bd46d2bbadcee3573c77377305258f6bd1e19c516a641` | `f4c1755f55fdc4733ebfa3f0b6567f6600108e7438011d8c2ddba1786408d00b` |
| 15 general | `e6921aa205d0f7e4f1352bb5418b93ef65b49cfefc781c6dbbd61eea6ee49e55` | `331082610917153a5b1d40559965d058b04384f5f967abe935beac3d336687b2` |
