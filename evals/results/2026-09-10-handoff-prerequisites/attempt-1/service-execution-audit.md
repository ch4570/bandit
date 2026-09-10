# Independent execution and promised-path audit

Scope: only settled runs `15-supported-offer--bandit`, `16-dependent-handoff--bandit`, and `17-pilot-commitments--bandit` under `runs/`. Evidence used: `original-input/**`, `output.md`, `metadata.json`, `session-tools.jsonl`, selected structural/final rows from `events.jsonl`; `workspace/input/**` was read only to hash its bytes. No current skill source, grading materials, prior outputs, issue history, protocol, or diagnoses were used as an audit standard. Skill prose incidentally embedded in tool read results was disregarded. No customer actions, product execution, or tests were performed. The audit independently recomputed arithmetic and calendar weekdays.

References below use `15`, `16`, and `17` for those three run directories; `raw/` means `original-input/`. Line numbers refer to the settled files, not formatted excerpts. Each JSONL record occupies one source-file line.

## Findings that change readiness

1. **15: the accepted initial-recovery path cannot accommodate the advertised 20-person cohort on its remaining staffed day.** This is a deadline/capacity mismatch despite correct weekly totals.
2. **15: the final late-input path exceeds the plan's remaining customer-work allocation.** Under the output's own allocation, 240 minutes become due in a 220-minute window; shifting the common-record allocation or predoing input-independent work might help, but the output does not make either arrangement.
3. **16: the ordinary draft → customer feedback → revision → output path is viable under the stated estimates and proposed admission conditions.** Its final customer access/recovery availability is not established; this is a handoff uncertainty, not proof that delivery or printing fails.
4. **17: existing free-customer obligations remain unresolved, but the output correctly treats their resolution as a precommit gate and preserves both call entitlements.** The one-paid-customer alternative is conditionally feasible; it is not an already staffed or customer-accepted launch. No unsupported overload conclusion follows from its unknown work or contingency reservations.

All three runs contain actual arithmetic execution and matching results. Material numerical results independently recompute correctly. Calculation execution does not establish that the proposed service paths can be performed on their deadlines.

## 15 — supported offer

### Confirmed resources, promises, and viable normal route

- Raw `operations.md:7–12`: preparation is 12 hours on 9/14–18; the separate, prepaid counselor contract covers 9/28–11/8, Monday/Wednesday/Friday 18:00–22:00, including holidays. Weekly gross capacity is 720 minutes; 60 minutes of shared records leave 660 customer minutes. No overtime, extra counselor, or post-11/8 operation is secured. The owner's 90 weekly minutes are administration, not substitute counseling.
- Raw `operations.md:18`: a period customer requires an initial 15 minutes, a 7-minute weekly photo check including week one, and a 5-minute closing summary. These are estimates, with longer questions expressly possible. Thus six weeks are `15 + 6×7 + 5 = 62` minutes per customer.
- Output `5`, `27–31`: proposed price is KRW 89,000, one payment, no automatic renewal, maximum 20 people, first advice plus six weekly checks plus closing summary, with short clarification questions. One purchaser still gets the service; minimum enrollment is not a cancellation condition.
- Output `38`, `46–48`: with complete input by 9/27, 10 initial reviews on Monday and 10 on Wednesday cost 150 minutes each; 20 weekly checks on Friday cost 140 minutes. Each fits the output's 220 customer minutes per staffed day. Weekly totals `440, 140, 140, 140, 140, 240` and total 1,240 are arithmetically correct. The gross contract continues after the owner's preparation ends; treating preparation day five as the end of service staffing would be wrong.
- Output `40`: ordinary weeks two through five can accept all 20 photos as late as Thursday 22:00 and perform the baseline `20×7 = 140` minutes on Friday, leaving 80 customer minutes. Unknown clarification time does not by itself prove overload.
- Output `41–44`: on-time final-week inputs arrive Sunday 11/1 and can be worked Monday 11/2 and Wednesday 11/4. The customer's final correction request must arrive Thursday 11/5 for Friday 11/6 support. This is a feasible sequence in principle. The output expressly screens out people who cannot make the last check by 11/5, rather than silently treating the interview's weekend-only F as available on weekdays. Raw `customer-notes.md:12` only confirms that F can read a weekday response later.

### Supported mismatch 15-A: recovery inputs arrive after the first two working days

Output `39` promises: “9/28 보완 요청→10/1 22시까지 재제출→10/2 첫 제안·첫 주 확인” and “이 경로도 20명 안에서 처리한다.” This is an accepted recovery path for enrolled customers, not merely a new customer who can be refused for submitting after the stated deadline. No count limit for recovery users, earlier staggered input deadline, or separate recovery reservation is stated.

Consider a single permitted scenario: all 20 enrolled customers need usable initial material, complete it at the permitted Thursday 10/1 22:00 deadline, and now require the promised initial advice and first-week check. Friday 10/2 is the only counselor window remaining before the promised first-week completion. It has 220 customer minutes under output `48`; required work is `20×(15+7) = 440` minutes, a 220-minute shortfall. Even reallocating the shared-record work cannot fit 440 minutes into the entire four-hour/240-minute Friday shift. Monday and Wednesday capacity, and the six-week total of 2,720 unused minutes in output `46`, are no longer usable for this input-dependent work.

This does **not** add the all-on-time cohort to an additional all-late cohort. It replaces the timing of the same 20 customers. Nor does it assume extra unknown question work. It uses only the output's promised baseline tasks and the raw measured/estimated minutes. Ten entirely late customers could fit 220 minutes before any other Friday obligations; if the plan retains all 20 customers' weekly checks on Friday, those checks already consume 140 minutes, leaving initial-review capacity for only five delayed customers (`140 + 5×15 = 215`). These are illustrations of the needed timing allocation, not a recommendation to revoke already accepted recovery rights.

Output `109` proposes notification and refunds for provider overload. That is a disclosed fallback, but it does not support the unqualified assertion that the 20-person recovery route can be delivered. Before accepting customers, a viable alternative is to change input deadlines or allocate bounded recovery slots with disclosed terms, reduce the cohort and recompute economics, or confirm additional staffing within authority. After acceptance, preserve the promised rights and use an agreed recovery/refund path; stopping future recruitment alone does not discharge them.

### Supported mismatch 15-B: the final late-input route leaves only Wednesday

Output `41` accepts final photos until Tuesday 11/3 22:00 and promises the final advice plus closing summary by Wednesday 11/4. Output `46` budgets `20×(7+5) = 240` final-week customer minutes; output `48` allocates 220 customer minutes to each working day. If all 20 customers use the accepted latest submission, Monday 11/2 has already passed; only Wednesday's 220 customer minutes remain before the output deadline. That leaves 20 minutes without an allocated slot. Friday 11/6 is after the final-result deadline and is reserved as the last correction-response route (output `42`).

This finding is narrower than 15-A. Raw `operations.md:9` fixes the records allowance weekly, not per day. Wednesday's **gross** four-hour shift is 240 minutes, so moving that day's common-record work to Monday/Friday could make the baseline 240 minutes fit, with no Wednesday buffer. Input-independent summary preparation might also reduce remaining work, if identified and timed. Neither arrangement is specified, and the output explicitly adopts 220 minutes/day. Do not describe the baseline final-late route as impossible under every permissible rearrangement of the raw contract; it is underallocated as written.

### Sensitivity and remaining unknowns

- Output `48` says doubling each weekly check from 7 to 14 minutes yields first-week 580 minutes with 80 weekly minutes left. Correct aggregate arithmetic, but the stated normal Friday allocation becomes `20×14 = 280` minutes versus 220. Monday/Wednesday each have 70 baseline spare minutes, so an explicit redistribution could fit the normal early-input case. It would not rescue the all-late recovery scenario, which becomes 580 minutes after Thursday input. Do not mistake the 80-minute weekly remainder for Friday usable capacity.
- Output `28`, `48`, and `109` acknowledge short clarification work, longer questions, and overload recovery. The exact time for missing-material checks, repeated correspondence, final correction requests, and owner refunds is unmeasured. The baseline mismatch above does not depend on assuming these unknowns consume any particular amount.
- Output `37` allocates two 45-minute administrative sessions, while `93` proposes 15 minutes of recruitment comments with a stated adjustment to the management allocation. This needs an actual allocation before use; it is not evidence of an unavoidable extra 15 minutes, because the output explicitly says to adjust the allocation.
- Output `111` proposes photo deletion within 30 days after 11/8. Ownership/access policy is supplied, but a timed deletion task is not allocated. This is an administrative closeout detail to confirm, not grounds to claim counseling has to extend beyond the contract.

### Money and arithmetic execution

Raw `operations.md:24–32` makes the full counselor payment (1,080,000) and tool payment (30,000) sunk, leaves recruitment spending optional, charges 3.3% of original payments without refunding fees, charges 1,000 per paying customer even if refunded, and labels 5% a calculation assumption. Output `54–80` preserves these units and separates forward cash, cohort cash, and preparation labor.

Independently recomputed contribution is `P×0.917−1,000`: 43,933 / 53,103 / 80,613 for single / three-week / six-week models. Cash break-even with 30,000 proposed recruitment is 26 / 22 / 15; adding 240,000 preparation labor gives 32 / 26 / 18. Cohort scenarios at 8 / 16 / 20 customers exactly reproduce output `70–72`: forward cash 614,904 / 1,259,808 / 1,582,260; cohort cash −495,096 / 149,808 / 472,260; with preparation −735,096 / −90,192 / 232,260. The 10% refund scenario is 143,260 with preparation at 20 customers and break-even 19. Owner operating labor is expressly omitted (`76`), so these are not full economic profits.

Execution claim is output `80`. Actual pairs in `15/session-tools.jsonl`:

| Call ID | Call → result lines | Recorded execution |
|---|---|---|
| `call_5qMtzIBu3whKnXeoWaTXBObp` | 7 → 8; exported source rows 32 → 34 | JS expressions calculate model contribution/break-even and 8/16/24-person alternatives. Result contains the prices and financial rows above. The 24-person scenario is not the final selected 20-person scenario. |
| `call_VHuMeDvzEFocVFjj2LNdrF8f` | 9 → 10; exported source rows 38 → 40 | JS outputs the final 20-person object, computes `3960−1240`, refund-stress expressions, and acquisition arithmetic. Many final 20-person baseline fields are supplied as numeric literals, so this pair proves execution/returned values, not independent formula evaluation for every field. Independent recomputation here confirms those fields. |

Neither pair schedules input arrival against individual working windows. No schedule-execution or observed operational validation should be inferred from the arithmetic claim.

## 16 — dependent handoff

### Confirmed resources and accepted timeline

Raw `operations.md:3–10` separately secures 150 preparation minutes and 240 operator minutes during 9/21–10/2, plus exactly two designer windows: 9/24 and 9/30, 18:00–21:00, 180 minutes each. Neither designer-window minutes nor preparation/operator minutes can be transferred. Exact operator clock times within the 240 minutes are not source-confirmed; output `3` correctly labels its schedule and allocations as proposals.

Raw `research.md:7–8,14` establishes A/B's need to inspect an actual draft, evening availability from the day after draft arrival through 9/28 noon, and no advance approval. Output `9–20` keeps draft review and one revision for that segment. Raw `research.md:11–12` separately contains E's editable-draft interest and F's no-review interest. Output `13–14` preserves those alternatives and does not use F to erase A/B's review requirement.

The proposed dependency chain is coherent:

| Path stage | Prerequisite and resource | Audit result |
|---|---|---|
| Application and preproduction repair | Output `49–51`: complete source facts/photos/rights, initial missing-input request, 9/23 18:00 repair deadline, eligibility and payment before the first designer window. | Raw material ownership and required facts match `operations.md:12,18`. The early-response availability is expressly unconfirmed and screened before acceptance (`50`), preserving customers' known evening constraints. |
| Actual first draft | Output `52`: designer creates it 9/24 18:00–21:00; operator sends it at 21:00. | Four orders need `4×35=140` of 180 designer minutes. It does not create customer card designs during the earlier preparation period. |
| Customer review and latest feedback | Output `53–54`: customers review on 9/25–27 evenings; latest inquiry 9/27 20:00, operator response by 21:00, resulting clarification by 9/28 noon, consolidated instructions 12:00–13:00. | The actual draft precedes feedback, and 9/30 revision follows it. A customer who can read/respond on Sunday evening can complete this route. Unanswered/ambiguous instructions become cancellation/refund, not fabricated approval. |
| Revision and final output | Output `55–56`: one consolidated revision and export on 9/30; operator checks against sources/instructions; final delivery 10/1 18:00. | Four orders require `4×(15+5)=80` designer minutes, leaving 100 in that window for specified verification/provider-error handling. No mandatory new customer approval is introduced after the last designer window. |
| Download/recovery and print | Output `57–58`: access questions through 10/2 noon; response/retransmission by 15:00; customer recheck 17:00; substitute delivery/refund 18:00. Customer submits to printer by 10/5 noon. | Operator tasks end within the source's 10/2 operating period. Printing is customer-owned; the date and actual cost/receipt schedule require reconfirmation. Designer errors found after the final window have a disclosed refund route, not an invented additional designer day. |

The final input handoff (output `64`) lists draft version and customer revision instruction together with initial raw materials. These are available at different stages; the dated schedule makes their order clear. The designer should receive the initial source bundle before the first window and the customer-approved instruction bundle before the second. The audit does not treat the list as requiring impossible advance draft approval, because output `52–55` explicitly sequences draft before review.

### Downstream prerequisites and honest unknowns

Output `66` proposes a concrete PDF contract—105×148 mm A6, white margin, one item per page, embedded fonts, no mandatory crop marks/extra bleed—and requires the customer **before payment** to confirm access to a printer accepting it. This is a real admission gate, rather than an assertion that every printer accepts the proposed export. Raw `operations.md:27` only establishes one known print cutoff; output `58` leaves actual price, schedule, and receipt confirmation with the customer. With that gate satisfied, final files arrive before the known 10/5 noon cutoff and possible 10/10 use. Do not assume failed printing merely because its ultimate outcome is not yet observed.

Two remaining customer-timing questions should stay visible:

- The latest draft inquiry route gives the operator until 9/27 21:00 to answer and the customer until Monday noon to respond. Known availability is around 10 minutes per evening (`raw/research.md:14`), not an entire evening or Monday daytime. The output asks applicants to be able to satisfy the advertised confirmation schedule (`32`, `38`, `49–51`), but it does not explicitly reserve a second Sunday response opportunity after a late operator answer. The route is feasible if the customer's evening slot permits it; it is not proven for every interview participant. Do not automatically assume another 10-minute review is required or that the existing 10 minutes are exhausted.
- The 10/2 access-recovery route requires a noon report and 17:00 recheck, whereas raw A/B availability only covers the earlier draft-review interval through 9/28 noon. B also cannot make daytime calls (`raw/research.md:8`), although asynchronous daytime access is not directly ruled out. A universal inability to recheck on 10/2 cannot be inferred. The missing item is explicit post-delivery/recovery availability confirmation before acceptance, or a recovery schedule compatible with the customer's selected time. Output `57` is a proposed deadline, not evidence of customer availability.

Output `84–85` allocates 200 operator minutes, with 40 unassigned and additional screening, delivery/checking, inquiry/retransmission/refund assumptions stated. Those minutes are pooled across the operating period, not a source-confirmed daily roster. Unknown incremental inquiry or rejection work could exceed the assumptions but does not prove it will; stopping new orders protects future obligations, while already accepted orders still require the disclosed delivery/refund path. The record contains no observed customer workload or elapsed service times.

### Money and arithmetic execution

Raw `economics.md:3–5` sets 130,000 fixed cash cost, 3% fee, and a comparison excluding taxes/refunds. It values operator time at 20,000/hour and separates preparation from repeat operations. Output `89–98` carries that narrow basis, including the fixed cost when sales are zero. It does not imply that refunds are actually costless or that the no-refund comparison covers a failed cohort.

At two/four orders, cash is −52,400/+25,200; `104 + 24n` planned operator minutes gives repeat economic values approximately −103,067/−41,467 and preparation-inclusive values −153,067/−91,467. Four-order break-even prices round up to 50,688 for repeat work and 63,574 including preparation. These amounts and the window calculations are correct. The proposed 40,000 price remains a narrow paid experiment, not a demonstrated sustainable price.

Execution claim is output `98`. `16/session-tools.jsonl:7` invokes `call_7GJ79PwNqxVBvpUxFDa5X61g`; matching result is line `8` (exported source rows 32 → 34). The JS calculates rows for 0/2/4 orders, first/second-window workloads, spare operator time, cash break-even 4, and unrounded price thresholds 50687.285223367704/63573.883161512036. The returned values support the output and independently recompute. It is arithmetic, not a run of the service or a test of printer/PDF compatibility.

## 17 — pilot commitments

### Existing obligations and precommit gates

Raw `operating-notes.md:3–7` gives two already confirmed free customers: 10/4 meeting, 14 days including that day through 10/17, up to two 15-minute calls each. One wants the first call on 10/16. They are separate from the interview's paid prospects. Weekly October resources are separate pools: 240 minutes field/turnover and 180 weekday minutes for phone, preparation, administration, and promotion. No extra employee/family support is confirmed.

Output `33–35` correctly identifies the Saturday 10/17 conflict with weekday-only phone staffing. It keeps the desired 10/16 first call and proposes individualized agreement by 9/29 to accept requests through 10/17 and extend delayed first/second calls to 10/19 and 10/20. It explicitly says agreement is required, prior rights do not change automatically, and without agreement the original promise needs actual resources that are currently unconfirmed. **Paid reservations must not be confirmed until this is resolved.** Closing recruitment does not remove the free customers' obligations (`35`).

This is a sound conditional branch, not proof of a solved obligation. The audit must not silently convert it into “free support ends Friday,” “both calls must be used early,” or “refund cancels the free customer's existing right.” A consensual extension is viable only if each affected customer can use the proposed later dates, accepts the change, and the operator reserves the necessary weekday time. The output calls for individual confirmation; that agreement has not happened in these records.

### Proposed paid route and last-day entitlements

- Output `24–29` proposes one paid customer's 10/10 60-minute meeting, 14 days including the first day through Friday 10/23, and up to two 15-minute phone calls, 59,000 paid once before the meeting, with no automatic renewal. It explicitly allows operation with one purchaser. Nothing is yet an accepted paid booking (`3`).
- Output `37` requires actual weekday call windows before payment and a last-day arrangement capable of taking the last 10/23 request and delivering support that same day; 18:00 request cutoff and 18:00–19:00 support is an example conditional on confirmed availability, not sourced staffing. Both unused paid call entitlements total 30 minutes and can fit in that one-hour window in principle. The record neither proves the customer can use that slot nor makes a contrary availability claim. Confirming the entire entitlement and booking mechanics belongs in this gate; a single-slot label alone would not prove it.
- Output `47`, `55`, `76`: unresolved terms accept inquiries only; schedule/support conditions plus customer acceptance are required for confirmed booking; silence or family indecision is not payment. Raw `interview-notes.md:6` limits Jaehun to Sunday morning, and output `13` correctly does not count him as suitable for the Saturday paid offer. Minseo/Eunkyoung have no confirmed 10/10 booking.
- Output `126`, `128`: the 10/12 decision occurs before paid support finishes; stopping future bookings preserves free agreed/original support and paid 10/23 support, plus explanation/recovery and refunds if the operator cannot perform. New starts require their own 14-day resources. These clauses preserve viable one-person operation and accepted rights instead of treating the decision date as a universal shutdown date.

### Remaining usable time, overlap, and resources

Output `104–113` reserves weekday work by week as 165 / 150 / 150 / 150 minutes against 180 each, and field work 150 / 75 / 0 / 0 against 240 each. Its raw-confirmed customer preparation and common administration costs are included. The 75 minutes per participant conservatively allocates one 15-minute turnover block even to the last/only customer; raw `operating-notes.md:7` says 15 minutes between meetings. This conservative allowance does not create a false feasibility claim.

All three customers' total call entitlement is `3×2×15 = 90` minutes. The table reserves free 60 minutes in each of three potential weeks (10/5, 10/12, 10/19) and paid 30 minutes in each of two weeks (10/12, 10/19): 240 reserved call minutes, with 150 minutes deliberately duplicated across potential request weeks. Output `111` explicitly calls this repeated contingency allowance, not extra entitlement. It is wrong to add those alternative request timings into 240 actual call minutes or require them all at once. In a late-call branch, unused earlier-week reservations cannot be transferred, but the later weeks still contain reserved capacity for the full remaining rights.

The base labor `225 field + 90 preparation + 90 maximum actual calls + 120 common admin + 60 promotion + 45 inquiries + 60 closeout = 690 minutes = 11.5 hours` matches output `113`. All reservations sum to 840 minutes/14 hours. Proposed weekday totals have 15 / 30 / 30 / 30 minutes unallocated. These are workload allocations, not confirmed clock-time bookings.

Raw `quotes-and-costs.md:13` offers 33,000 rental for 10/4–17, if requested by 9/29, with return 10/18 10:00. It is not booked. Output `44`, `84`, `111` retains the need to confirm the rental and the return/travel time. The last meeting is 10/10, and the output labels “screen not needed for phone support” as an operating assumption, so returning the screen before the phone period ends is a viable alternative if that assumption holds. No rental extension is automatically necessary merely because support continues to 10/23. Return travel is unmeasured and not included in the 14 hours; source October field capacity still exists on 10/18, so unknown travel does not prove overload.

Other honest limits: the September part of the first preparation/promotion week has no independently quantified raw time allowance (the raw limit says “October”); applying 180 minutes to the whole 9/28–10/4 week is a proposed planning cap. Printing/posting, last-day phone clock times, actual manual-contact costs, and any refund processing after 10/25 need confirmation. A refund requested at the end of Friday 10/23 could fall in the following October week under the proposed three-business-day rule, but raw October weekly administrative capacity remains; the output's four-week table does not prove either that this task is reserved or that it cannot be performed. Last support/refund completion, not the 10/12 decision, is the stated closeout prerequisite (`128`).

### Billing, costs, and actual calculation pair

Raw `quotes-and-costs.md:3,7–15` gives VAT-inclusive amounts, a nonproratable already paid 110,000 room month, the actual 33,000 short rental quote, a 44,000 **per-account per-month** messaging tool with unresolved minimum months, 8,000 fixed printing, and 6,000 **per participant**, including both free customers. Output `84–102` preserves these units and avoids assuming 14-day prorating of monthly charges.

Base is `110,000 + 33,000 + 8,000 + 2×6,000 = 163,000`; cost at 0/1/2 paid people is 163,000/169,000/175,000. The nine price/count cash results in output `94–96` independently match; at 59,000 with one paid person the result is −110,000, while incremental contribution is 53,000. Conditional break-even counts at 39,000/59,000/79,000 are 5/4/3 and are not recommended enrollment counts. The budget `169,000 + 50,000 + 81,000 = 300,000` correctly includes the sunk room cost. Holding the customer's full payment separately supports the proposed full-refund exposure without counting it as spendable owner capital.

Output `102` correctly computes total cost for one paid customer plus 1/2/3 tool months as 213,000/257,000/301,000 and says not to subscribe before confirming the minimum. The word “monthly” is not treated as a known one-month total commitment. Two months alone fit within 300,000 but would exceed the stated 50,000-reserve budget when combined with that reserve; the output does not claim that branch is approved/affordable or recommend subscribing. Manual contact is expressly not assumed free. These are cash comparisons excluding labor/unknown costs (`98`), not an all-in profitable business case.

Execution claim is output `115`. `17/session-tools.jsonl:7` invokes `call_x4ykxu5MPTuyIS2kqedCFyWy`; line `8` is the matching result (exported source rows 38 → 41). This actually runs `python3 -c` for arithmetic, returning `exit_code:0`, fixed/variable costs, nine scenario results, break-even counts, 1–4-month sensitivities, 690 base minutes, and 14 reserved hours. The weekday arrays are supplied literals, while cost and hour sums are evaluated. This is not product code or a product test. No calendar booking, customer agreement, or demand result was executed.

## Integrity and execution inventory

The following SHA-256 values were independently recomputed. Each input hash matches both the immutable original fixture and `workspace/input` bytes, plus the metadata's before/after input entries. This is 12 matching input pairs. Metadata locations: `15/metadata.json:85–89,343–347`; `16/metadata.json:83–87,341–345`; `17/metadata.json:83–87,341–345`.

| Run | Input | Matching SHA-256 |
|---|---|---|
| 15 | channels-and-alternatives.md | `0d2bcd7080ae7d1af1a09ef6338f8ecb71ea22abf457ac5103f9b6ab95ffdb21` |
| 15 | customer-notes.md | `44cc27e33a683ad7c6f71c33607278183c7b8b2c2e49e119c7a4604b76afd4b6` |
| 15 | operations.md | `8f9532f21045919ffee120432efc5fa9823db291569f00d45382b876cc594fa9` |
| 15 | request.md | `cb2b6fba4ceee5375b134d4ca9a7c3b8fea273a0500c983507d5b267e863db11` |
| 16 | economics.md | `7f50a6dcc7b6a2a16dce37caefca463747e183fa74291720199344b31717f22e` |
| 16 | operations.md | `e3b1fc177f74d04a6a04af70b31facfd2022ab1423371ea013ad65ca38e3e3a5` |
| 16 | request.md | `f758032be79595a2373a566a7418fdee4ed1c04f2288db2ec8a8b77841721954` |
| 16 | research.md | `3ae661fd19859ac784dddc906ccf674ee92f4416c578d17fdb5c101b69cbe78a` |
| 17 | interview-notes.md | `c0c1bc5ef4815e85641b64fd6a433922918a0c8c0bad8445132b29178ccfe51e` |
| 17 | operating-notes.md | `efa95f9c017e318b0356498164807f2b9bf9ec24e74e9498b6c841c03c54fcb3` |
| 17 | quotes-and-costs.md | `b03d5b5552b3f496eda587e401126b9c302193fd3d18e201a9739e313671c8c9` |
| 17 | request.md | `a8241aaf8465c2e9220f90b1eb8c1f7d92d0c4325324a57c3845198f26b3c86b` |

Each tool export matches `metadata.json:29`:

| Run | Matching `session-tools.jsonl` SHA-256 | Calls/results |
|---|---|---|
| 15 | `65f6947841cb850664ea069a2c7d3b1ea7b4c6ee74a91d9ccea4cc13e0ebd547` | 5/5; 10 records |
| 16 | `6926a630893823aa7a3185a3357b7b4cf145b61c04c2ac0b0ec86347537cff35` | 4/4; 8 records |
| 17 | `58a829874161c0adf0e3aea4b8f95cd818f009a40a5e3b65ccb2961049ed9b36` | 4/4; 8 records |

All 13 calls have matching result IDs in the export. Besides the calculation pairs already identified, the read/discovery pairs are:

| Run | Call ID | Call → result export lines |
|---|---|---|
| 15 | `call_bSrHYPC8v8j9D3q6Cx3fpmLq` | 1 → 2 |
| 15 | `call_mCX24eqqGvbx7TkcBpgfnaa0` | 3 → 4 |
| 15 | `call_ZcArAE9K7Q0U14JAyudoUgYy` | 5 → 6 |
| 16 | `call_QRNlzJ4rwpfoUouX1EbHlXx1` | 1 → 2 |
| 16 | `call_ZEocGVGOnDgVeJM904FLz7cJ` | 3 → 4 |
| 16 | `call_nAdF2WFs2iRvVhMJPqwOsujf` | 5 → 6 |
| 17 | `call_faV9HpRlmOLBYcYPTPElEcJT` | 1 → 2 |
| 17 | `call_hYoXvt53C6XihRS8pTRBmwBA` | 3 → 4 |
| 17 | `call_y6s6SYBkqpKBh3DGsuSMvoja` | 5 → 6 |

Selected final-event checks show `output.md` equals the final agent-message text after trimming trailing whitespace: `15/events.jsonl:11`, `16/events.jsonl:11`, `17/events.jsonl:13`. Terminal events at lines 12/12/14 record completion. Independently computed output hashes are:

- 15: `dc3d31a6470a8fb0d4d41426cd493aad4f03b0c264cea4df822b3c5dc26478c2`
- 16: `b6709a2e84f27e79303734b73eb734f8bf41ced30dd9361ecd517f31b011d615`
- 17: `1cef2f7446d837e61b64b221f87f2a51de690aa9bd729e96832a7e6334d5b1f1`

These output hashes are new audit fingerprints, not matches against an absent metadata output-hash field. The host source-session hashes (`metadata.json:27`), runner/capture-module hashes, and skill hashes were not independently verified because their underlying sources are outside the allowed audit reads. Export matching confirms the settled export's integrity against its metadata, not a complete reconstruction of every host-session event. In particular, the CLI JSON event stream alone does not show all arithmetic calls: metadata explicitly warns of this (`session_tools.cli_event_coverage`, line 16). Claims of “no calculation execution” based only on visible shell events would be contradicted by the matching session-tool records.
