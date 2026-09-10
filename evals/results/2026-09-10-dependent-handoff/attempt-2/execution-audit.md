# Independent execution and accepted-path audit

Audit date: 2026-09-10. Scope: exactly the seven settled runs listed below under `/private/tmp/bandit-interactions.ezd9Vq/runs-2/`.

The five outputs claiming arithmetic execution have matching recorded calculation calls and returned results. All seven tool-export hashes match their metadata. All 26 original-input files and their corresponding workspace/input copies match the recorded input hashes; before/after input hashes also agree. The outputs describe proposed work, not real customer activity. No observed tool call performs customer contact, publishing, payment, product implementation, or a customer experiment.

The main proposed service paths fit the supplied resource windows or explicitly retain an unresolved activation gate. I found narrower allocation and deadline ambiguities, principally in the plant service's delayed-input/recovery paths. They do not establish an observed delivery failure or an unavoidable overload of the raw confirmed staffing.

## Scope and evidence method

Read material was limited to these runs' original-input files, output.md, metadata.json, session-tools.jsonl, and selected events.jsonl records. Workspace/input copies were read only for hashing. Repository skill sources, grading material, other runs, and issue/PR text were not inspected. Skill instruction prose embedded in historical read-tool output was not used as an audit rule.

References below are relative to the named run. `input/...` in citations means the preserved `original-input/...`, not a changed working document. Line numbers are physical file lines. A session-tools row is one physical JSONL line; source-session line numbers come from metadata's exported-source list. Host session files themselves were outside scope, so their source hashes were not independently verified.

I paired calls and results by exact `call_id`, inspected the computation text and returned values, compared selected CLI event records, and independently recomputed material sums and resource-window arithmetic. CLI stdout omission is not evidence that a calculation did not execute. A returned literal is also not the same as a program recomputing that literal from its components.

## Export and input integrity

Each export below was freshly SHA-256 hashed and equals `metadata.json:29`. Every run has process/runner exit code 0, metadata integrity `passed`, no reported violations, and a CLI final-message event matching output.md after trimming terminal whitespace.

| Run | Verified export SHA-256 | Calls / results | Input copies checked | Input hash maps / integrity line | Final / completed event lines |
|---|---|---:|---:|---|---|
| 05-small-research--bandit-research | `2da296bcbfc3badcebc45a0aaab0cbce0201a893a9cb61654c985c4daccc6519` | 2 / 2 | 1 original + 1 workspace | metadata:79, 787 / 455 | events:9 / 10 |
| 08-callback-scope--bandit-scope | `f1ca4fb94de7631d86db932d23a3d92b523e3c2941cfef327e0feeaa04b091f9` | 3 / 3 | 5 original + 5 workspace | metadata:81, 833 / 481 | events:11 / 12 |
| 12-launch-handoff--bandit | `5fe65b775fa6cb7491de79111eb597e7940026933c908910048589f9826c17fd` | 3 / 3 | 4 original + 4 workspace | metadata:81, 339 / 217 | events:12 / 13 |
| 12-launch-handoff--bandit-specify | `59a24f2f577bb19b0001cf80d7f265dd80b81c1e026021ea71c7d049985d0790` | 4 / 4 | 4 original + 4 workspace | metadata:83, 824 / 477 | events:12 / 13 |
| 13-offer-consistency-review--bandit-review | `c61e98b4e6f5d7a2bfc3367ca3a8aa6b15757bb102c37e033eda1319663d19e8` | 3 / 3 | 4 original + 4 workspace | metadata:81, 822 / 475 | events:25 / 26 |
| 15-supported-offer--bandit | `0690c23cf1f2134558ee37a7d85d0045b36c876ae7ef625a92caed170dea24e0` | 4 / 4 | 4 original + 4 workspace | metadata:83, 341 / 219 | events:12 / 13 |
| 16-dependent-handoff--bandit | `3c83d0844c6a979c8e9a83a16832169101f9624a2ff577284fe4fe1692132406` | 3 / 3 | 4 original + 4 workspace | metadata:81, 339 / 217 | events:12 / 13 |

Total: 22 call/result pairs, 44 exported records, 26 original inputs and 26 workspace input copies. Hash agreement establishes consistency with the preserved metadata, not independent authenticity of an unexamined host session. Metadata workspace integrity additionally reports no changes; this audit independently rehashed inputs rather than every installed instruction/resource.

## Actual computation evidence and user boundaries

| Run | Exact calculation call and paired evidence | Observed computation/result | Boundary conclusion |
|---|---|---|---|
| 05 research | None in its two exported pairs | File reads/listing only | Raw request:1 asks for one customer group and one cheap check, ≤200 words; external search/file creation unnecessary. Output:1–13 remains a short proposal. No actual recruitment, form creation, booking, or payment is evidenced. |
| 08 scope | None in its three exported pairs | File reads/listing only | Raw request:9–13 explicitly forbids file edits, browsing, contact, and running code. Output:37 correctly says its arithmetic was not tool-verified. Read-only shell commands did execute through JavaScript tool orchestration; no calculation script, product code, or tests executed. This distinction is more precise than claiming that no executable tool mechanism ran at all. |
| 12 general | `call_5qPqAg1prbbUhMq4wHkUKF3g`, session-tools:5→6; source-session lines 27→30 | Ratios 28/42, 20/28, 20/42; model contributions 13,543 / 3,873; break-even 5 / 16; pilot −10,895.1667 per shop and −114,475.8333 for five after fixed cost; sensitivity 19,793 / 13,543 / 1,043 | Raw request:19 authorizes planning only, prohibits originals/outreach/publication/payment/experiment execution. Arithmetic is not prohibited. Output:128's calculation execution claim is supported, subject to the literal-value qualification below. |
| 12 specify | `call_1DfqvHn6r3eGATIMu10U3LRa`, session-tools:7→8; source 33→35 | Same monthly contributions; first-five-shop results −75,618.3333 / −27,268.3333; budget 535,500 and remainder 264,500 computed by addition/subtraction; conservative pilot −17,145.1667 / −145,725.8333 | Same request boundary as 12 general. Output:108 is supported by actual computation. No product or customer experiment executed. |
| 13 review | `call_DRGuD9dAsw1LeuOFxWvgGDKE`, session-tools:5→6; source 34→36 | Normal one/two-pair prices 22,000 / 36,000; first-order totals 19,000 / 33,000; 23+2=25 against 24 | Raw request:11 requests review only and prohibits originals, outreach, real orders/payment. Local arithmetic is allowed. Output:22, 42 describe actual arithmetic; output:70's absence of product-code/tests/transactions is consistent with the trace. |
| 15 general | `call_e4KbzQR6HbPEa2jP3vO3kCsM`, session-tools:7→8; source 36→38 | Per-customer contribution 53,103; cash/economic break-even 22 / 26; supplied week-minute array summed to 1,536, remainder 2,424; 32-customer economic result 319,296; 15% refund sensitivity 130,496 | Raw request:11 prohibits development, account creation, contact and ad execution. Arithmetic is permitted. Output:95's execution claim is supported. |
| 16 general | `call_SYjHG9HHcW6cCYtzSlKwKrm0`, session-tools:5→6; source 27→30 | Capacity floor(180/35)=5; production 175 / 100 minutes; operations 168; five-order cash +64,000, recurring-labor result +8,000, preparation-inclusive −42,000; break-even 4 / 5 / 7 | Raw request:3 prohibits web search/customer contact and restricts evidence to attachments. Output:99's execution claim is supported. No sale or delivery occurred in this run. |

For the two runs without calculation calls, the complete observed call IDs are:

- 05: `call_wczApDJU8rsrBiK758B3c97g` (session-tools:1→2; source 14→17), `call_Ord9sLNL7kUhARVTle3Vx5Ks` (3→4; source 19→22). CLI command-completion events are lines 6 and 8.
- 08: `call_9KMH9PVJ7rzN2sqf4ydIxMdn` (1→2; source 14→17), `call_RY0W9bEBEQSSVNJCbBBvQlCX` (3→4; source 19→22), `call_sIyFGnzrbsqHfWjuoffQo62P` (5→6; source 24→27). CLI command-completion events are lines 6, 8 and 10.

In 12 general and 16, the CLI stream records a shell file read at events:11 from the same enclosing execution call, while the session export additionally records the JavaScript calculation and result. In 12 specify and 15, events:10 is the final shell read and events:12 is the final answer, with the arithmetic present in the session export between them. In 13, the last read completes at events:24 and the final answer is events:25, again with arithmetic in the session export. These are concrete counterexamples to equating missing CLI calculation rows with non-execution.

Calculation limits: 12 general passes `budget.total:560000` and `unallocated:240000` as literals instead of summing budget components in that call. Its calculated engineering/design totals use a different decomposition from the final weekly table, although both total 28 / 8 hours. 15 supplies `[352,464,224,304,192,0]` as literals, then sums them; it does not execute a deadline-sensitive scheduling check. I independently recomputed the final budget components and weekly workload; they agree. Tool execution establishes the recorded calculation, not that every operational assumption or every displayed total was independently verified by that call.

## Accepted paths and resource windows

### 05 — small research

Output:5–11 proposes showing a priced but explicitly non-booking invitation to ten eligible residents, collecting a specific item/time, then deciding whether to ask a laundry business about feasibility. Output:7 explicitly says it is not a real reservation, and output:13 withholds paid-demand validation. Thus there is no accepted pickup/delivery service entitlement to capacity-test. Three hours and the 3,000-won price are proposed constraints, not observed operating performance. Requiring a complete laundry fulfillment schedule would exceed the raw request for one inexpensive early check.

### 08 — callback scope

The proposed path is shift start → existing branch-scoped queue → visible ownership/claim → existing callback completion → saved state for the next shift; missing contact details use the existing manual process, and feature disablement retains records (output:11–22). Named willing small desks are supported by stakeholder-notes:3–4; multi-branch prospects are not accepted (output:5; evidence:17–20).

The selected queue plus measurement needs backend/frontend/QA 3.5 / 3 / 1.5 days, leaving 2.5 / 1 / 0.5 against raw 6 / 4 / 2. The email combination exceeds frontend/QA and SMS is provider/consent blocked (delivery-constraints:3–21; output:28–41). My recomputation agrees; the original agent intentionally did not run arithmetic.

The build window ends September 30, but the two-week observation is not claimed complete then. Output:45 explicitly leaves activation dates/support coverage unresolved and refuses to assume later staffing. Output:49 also allows the last due callback's 12-hour lateness threshold to mature. This is a conditional handoff, not a fully booked later service. No extra two-week staffed period should be inferred as confirmed, and no actual desk was enrolled by the run.

### 12 general — launch handoff

Raw windows: founder 10 hours each week, 40 total; developer 28 total; designer 8 total; five simultaneous shops; four-week cash ceiling 800,000 (founder-brief:13–23). The selected offer is 14 days, September 26–October 9, with approval/payment/40-minute onboarding by September 25, no late entry, explicit manual fallback before payment, and no extension beyond confirmed resources (output:31–39, 130).

Normal path: owner accepts offer and access → onboarding → employee records while working → next shift explicitly marks read → owner sees dated status → October 9 record copy → customer error/non-delivery report by October 10 noon → correction/refund by October 11 18:00 (output:33–39, 94–106). The output intentionally provides a later customer response window before closeout; it does not require approval of a result before that result exists.

Window check: week 2's five onboardings consume 200 minutes, inquiry coverage 300, and payment/start checks 100 = 600 minutes. Week 4 inquiry coverage 300 + shop closeout 150 + weekend correction/refund 120 + decision notes 30 = 600 minutes (output:59). The other weekly caps and developer/designer totals also match (output:51–57). Unlike the plant consultant, the raw founder resource is a weekly allocation rather than fixed weekday-only shifts; assigning weekend closeout inside the final week does not invent a new worker or a fifth week. The budget components sum to 560,000 with 240,000 unallocated (output:63).

Narrow unresolved promise: output:37 says inquiries receive an answer by the next support day, using Monday–Friday 17:00–18:00. An ordinary usage inquiry arriving after the last Friday review could point to Monday October 12, while output:130 disallows staffing from October 12 onward. The explicit weekend path is for errors/non-delivery, not unambiguously every ordinary question. State a last ordinary-inquiry cutoff or say that the reserved weekend closeout also answers those remaining accepted inquiries. This is a deadline ambiguity; no inquiry arrival or missed answer was observed, and unknown inquiry effort does not prove overload.

The monthly A/B offerings are future model comparisons, not additional accepted monthly subscriptions. The run correctly keeps their economic figures separate from its discounted 14-day experiment (output:110–130).

### 12 specify — launch handoff

The raw resource limits are identical to 12 general. This variant sells September 28–October 11, requires consent by September 23, onboarding September 24–25 and payment by September 25, and rejects late entry (output:32–34). Employee/next-shift/owner state transitions and corrections appear at output:83–91. The manual alternative must satisfy the same rules before it is sold (output:40, 52).

Support is deliberately limited: Monday/Wednesday/Friday 17:00–18:00, last inquiry October 9 at 17:00, with October 11 17:00–18:00 for final replies/export/closeout; records are then exported and access ends (output:36). Those hours lie within the final founder week, and the weekly totals remain 10 / 10 / 10 / 10 hours (output:44–54). There is no raw confirmed requirement that every service day carry an inquiry window, nor an included customer approval round after final export. The earlier support cutoff is therefore a proposed limited-service term, not by itself proof of a broken dependency.

Qualification: the one-hour final window combines outstanding replies, exports, refunds and access closure, but those tasks have no item-level estimates or required number of customer responses in the raw input. The total support assumption of 30 minutes per shop per month is not a per-inquiry cost and cannot legitimately be multiplied by five to prove an end-window overload. The handoff would be more verifiable if it allocated the final hour and described export/access failures, especially because there is no later staffed day. This is unverified closeout capacity, not measured or mathematically established overload. Do not invent a mandatory post-export customer approval interaction that this offer does not include.

The 535,500-won budget plus 264,500 unallocated equals the 800,000 ceiling. Both the conservative 14-day labor accounting and the monthly model arithmetic have matching execution evidence (output:54, 95–108).

### 13 — offer consistency review

This run is a review of approved conditions and unapproved drafts, not an adopted new service plan. The authority is OPS-0910 and the trial is historical synthetic evidence (approved-offer:3–5; launch-artifacts:3; output:3).

Approved normal path: A/B registered locker and eligible photos/materials → one/two pairs → pooled pair capacity secured before payment → correct VAT-inclusive total and return terms shown → Tuesday collection → wash/dry → same selected locker by Friday 18:00. Delay notice is due Thursday 18:00 with a new estimate/contact; compensation remains unapproved (approved-offer:9–33).

Output:24–52 traces and corrects the wrong-area/material acceptance, post-payment photo review, orders-versus-pairs capacity, and 24-hour return claim. First-cycle dates September 15/18 are calendar-correct. The 23+2=25 example is explicitly hypothetical, not an observed queue (output:38), and the check uses the actual 24-pair combined capacity. It does not reinterpret 24 orders as capacity. Output:68 leaves review wait time and reservation-release timing as decisions needing confirmation, which matches the input's lack of those commitments. Unknown cleaning labor or future compensation cannot be converted into a proven capacity failure. The review preserves supported scope/FAQ terms and does not change the source documents.

### 15 — supported plant offer

Raw windows must remain distinct: founder preparation September 14–18, 12 hours; founder administration thereafter 90 minutes/week; consultant September 28–November 8, Monday/Wednesday/Friday 18:00–22:00 including holidays, 12 hours/week, with one hour/week common records and 11 customer hours (operations:7–12). The preparation cutoff does not end the separately prepaid consultant contract.

Selected path: two cohorts of 16 begin September 28 and October 5. Initial photos precede the start; three weekly results include the first week; after the last result, customers can submit one final question and receive a later closeout summary. Cohort A final weekly result October 16 → weekend question by October 18 → final answer/summary October 23. Cohort B final weekly result October 23 → weekend question by October 25 → closeout October 30 (output:37–50). This accommodates F's stated weekend availability (customer-notes:12). It neither requires a question before its result nor mistakes the founder's preparation end for service end.

With 15-minute initial review, three seven-minute weekly checks, added seven-minute final question and five-minute closeout, each customer consumes 48 planned minutes. The weekly totals independently recompute to 352, 464, 224, 304, 192, 0; their sum is 1,536 versus 3,960 customer minutes (output:56–69). All ordinary weeks fit 660 minutes, but the last part of an accepted week matters:

| Accepted condition | Remaining work/window using raw availability | Assessment |
|---|---|---|
| Normal complete Sunday inputs in the overlapping week of October 5 | 16×22 + 16×7 = 464 minutes across Mon/Wed/Fri; 660 weekly customer minutes | Fits. |
| Necessary photo material for both cohorts becomes usable only at the permitted Tuesday end | Up to 464 minutes then remain for Wed/Fri's raw 480 staffed minutes | Can fit if the common-record hour is placed Monday and the later shifts are allocated accordingly. The fixed output claim of 220 customer minutes/day instead gives only 440, a 24-minute shortfall in that chosen allocation. It requires reallocation or a narrower late-input rule; it is not a 464>480 raw-resource overload. |
| Cohort A final-question clarification arrives Wednesday end in the week of October 19 | All 16×(7+5)=192 final-question/closeout minutes could remain for Friday; that is below both raw 240 and output 220 minutes | Fits on the stated base estimates. Cohort B's 16×7=112 weekly minutes can be handled Wednesday once Tuesday photos are usable. Do not also move that already-usable workload to Friday without a stated dependency. |

Output:50 allows photo supplement through Tuesday and final-question supplement through Wednesday. Actual supplementary effort is not measured (operations:18; output:56). The 464-minute Tuesday scenario leaves only 16 raw minutes beyond base work if all common records happen Monday. That is limited headroom, not a measured overrun: neither universal late arrival nor any particular additional effort occurred in this run. Conversely, simply quoting the full week's 196-minute spare capacity fails to check whether it remains available after required inputs arrive. The output's 6/5/5 scheduling example and 220-minute daily allocation do not themselves resolve this case (output:67).

Delay-recovery qualification: output:50 permits business-caused recovery through November 6 and refunds if impossible. For the weekend-only customer, a delayed last management result delivered November 6 cannot then receive a weekend response and a staffed consultant reply: the last contracted operating shift is that Friday. A fully serviced delayed path would need the last management result by October 30, customer response by November 1, permitted clarification by November 4, and closeout by November 6, or an earlier equivalent chain. The output does not explicitly propagate revised question deadlines or name this latest result cutoff. Its refund fallback means it does not unconditionally promise impossible recovery, but the full delayed-delivery branch is not established merely by saying “finish by November 6.” Treat recovery as conditional on the entire chain fitting, otherwise apply the stated incomplete-service refund; do not call a November 6 result alone complete service.

The six-week product in output:30 is an unchosen alternative and explicitly identifies its end-of-contract follow-up problem. It must not be counted as an accepted six-week entitlement. The repeat-billing option is rejected. Economic figures are planning assumptions, not observed payments; collection, refunds and founder unpaid time are distinguished (output:73–95).

### 16 — dependent card handoff

Raw windows: preparation 150 minutes September 14–18; separate operator order work 240 minutes September 21–October 2; designer 180 minutes September 24 18:00–21:00 and another 180 September 30 18:00–21:00, with no transfer between windows or other designer days (operations:3–10). A/B can review for about ten evening minutes starting the day after their draft arrives through September 28 noon; they cannot preapprove (research:7–14).

Latest accepted normal path: complete material September 23 noon and payment by 18:00 → draft production September 24 → preview by September 25 noon → customer review September 26/27 evenings → consolidated confirmation by September 28 noon → clarified instruction by September 29 → revision/export September 30 → final PDF by October 1 noon → error/access report by October 2 noon → operator closeout/refund by October 2 18:00 → customer independently submits to a printer before the currently confirmed October 5 noon intake deadline and uses the cards October 10 (output:30–39, 61–65).

Capacity is checked in each actual designer window: 5×35=175 ≤180 for initial cards, leaving five minutes; 5×(15+5)=100 ≤180 for revisions/export, leaving 80 for designer-side checking/errors before that window ends. Five confirmed orders use 48+5×(12+8+4)=168 operator minutes, leaving 72 of 240; preparation components total 150 separately (output:30, 33–38, 87–88). No elapsed September 24 capacity is reused after late feedback.

The output expressly rejects September 30 new drafts because no subsequent staffed revision window exists (output:41). Missing/late material is not charged, excess capacity cannot pay, and missing/unclear confirmation causes cancellation/refund rather than silent approval (output:43–50). Post-delivery design errors lead to refund, not an unstaffed designer promise; access problems use an existing-file resend. In-window designer checking and the later customer error-report window are different activities. The original input does not require an additional customer approval round after final export.

Two uncertainties are labeled rather than treated as proven violations: preview transmission is assumed bundled into the eight-minute feedback work (output:34), and rejected/incomplete applicants or refunds can consume some of the 72-minute operator reserve. The raw input provides no arrival volume, refund frequency, or extra-response duration, so it cannot establish that those reserves are exceeded. First-window five-minute production slack is thin and measured rehearsal rates may vary, but the proposed five-order base chain fits.

The optional October 10 usage form is asynchronous and expressly promises no later consultation; review time must be separately secured before a next selling decision (output:110). Printing/delivery and a future cohort are not included entitlements (operations:27; economics:9; output:39, 107, 110). Thus neither requires inventing post-October-2 operator service or another designer contract. The financial result honestly remains −42,000 with preparation at five delivered orders; capacity is not raised to the seven-order preparation-inclusive break-even (output:95–99).

## Settled conclusions and limits

1. Calculation execution is affirmatively proven for 12 general, 12 specify, 13, 15 and 16 by exact paired calls/results. Its absence from CLI stdout is immaterial. In 05 and 08, no calculation call is present in the complete exported records; 08's raw prohibition explains its deliberate arithmetic-verification limitation.
2. Recorded actions stay within planning/review work, with no observed external mutation or real customer activity. All preserved inputs remain hash-consistent. The review's future scenarios, conditional schedules and thresholds are not executed product tests or customer outcomes.
3. Main service chains are substantially concrete. 15's Tuesday recovery allocation needs a narrow correction/clarification, and its broad November 6 fallback needs dependency-aware cutoffs if used for full service. 12 general's last ordinary-inquiry deadline is ambiguous. 12 specify's one-hour closeout remains unquantified. These conclusions are narrower than alleging confirmed staffing overload or observed failed service.
4. Unknown workload is not a measured overload. Optional products, optional later feedback collection, and future monthly models are not accepted present commitments. Earlier usable customer inputs must retain their available earlier processing windows. Explicit refund/decline paths can end an infeasible service attempt without claiming successful delivery.

Only this audit file was written. No inputs, outputs, metadata, exported tools, events, repository sources or other agents' files were changed.
