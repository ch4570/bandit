# Independent service and execution audit

Audited on 2026-09-10. Scope is exactly the settled `15-supported-offer--bandit`, `16-dependent-handoff--bandit`, and `17-pilot-commitments--bandit` runs under `runs/`. This report uses only their `original-input/*`, `output.md`, `metadata.json`, `session-tools.jsonl`, selected execution-event fields, and hashes of `workspace/input/*`. No skill source, rubric, grades, prior outputs, issues, or protocol were used as audit criteria. Instruction prose embedded in historical read results was excluded from the substantive assessment. All business facts below are synthetic fixture facts, not observed real customer or vendor activity.

In references below, `15/output.md:78` means line 78 of `runs/15-supported-offer--bandit/output.md`; the same convention applies to 16 and 17. Input references always mean the immutable `original-input/` copy.

## Findings at a glance

| Run | Supported result | Remaining qualification |
|---|---|---|
| 15 | The proposed synchronized 24-person, six-week cohort fits the confirmed counselor windows at the stated base workload, and its financial tables reconcile. The representative's five preparation days do not end the separately prepaid counselor contract. | A first-week Wednesday recipient has no stated post-result photo-replacement route under the generic Tuesday cutoff. Administrative throughput and exception workload are unmeasured, not demonstrated overloads. Shorter products can also fit through different allocations. |
| 16 | Four drafts on 9/24, genuine customer review on 9/25–27, revision/export on 9/30, and delivery on 10/1 form a feasible dependent sequence. Operator quality review occurs before the designer's final window closes. | Printer-specific formatting requirements have no explicit collection deadline before final export. Compatibility with the existing template could avoid this issue; a necessary late reformat is not established. |
| 17 | Proposed price/volume calculations reconcile. Existing free customers' full support rights survive the 10/12 intake decision. Paid enrollment is expressly conditional on resolving support and other prerequisites. | Existing customers have not agreed to a weekday-only timetable, particularly the person whose first call is 10/16. No actual Saturday request or overload is recorded. September preparation time, return logistics, and the unselected booking mechanism still require confirmation. |

No arithmetic error in the consequential displayed amounts was found. None of the runs proves customer demand, actual service delivery, successful recovery, or launch readiness through an executed business test. Their actual recorded work is planning, source inspection, and arithmetic.

## Actual execution and evidence integrity

All three metadata files record process exit 0, run exit 0, captured session tools, eight tool records comprising four calls and four results, and no capture errors (`metadata.json:10`, `:15`, `:41–45`, `:225`). Every call has exactly one result with the same `call_id`; there are no unmatched calls in these exports. Each run includes three inspection/orchestration calls and one arithmetic call. Run 15's first orchestration call contains two shell reads, which is why its CLI events show four completed shell commands rather than three.

The observed shell commands completed with exit 0: 15 `events.jsonl:6,8,10,12`; 16 and 17 `events.jsonl:5,7,9`. Final messages agree with `output.md` after trimming terminal whitespace: 15 event line 14; 16 and 17 event line 11. Terminal `turn.completed` appears at 15 event line 15 and 16/17 event line 12.

Run 15 has an `item.type=error` event at line 3 stating that skill descriptions were shortened to fit the skills context budget. This is a recorded context-budget notification, not a failed shell command or failed terminal turn. It should not be silently omitted, nor treated as proof that execution failed.

The arithmetic is visible in the session-tool export even though it does not appear as a shell command in the CLI event stream. Absence from the latter would not establish absent calculation. The paired result payloads contain structured text with successful completion and numerical values, not merely a self-report in the final answer.

| Run | Arithmetic call and paired export lines | Recorded result and independent reconciliation |
|---|---|---|
| 15 | `call_ASl26RliNp2FODl2s7kHHGz0`, `session-tools.jsonl:7–8` (source ordinals 32 and 34) | Executes contribution, break-even, 8/16/24-customer financial scenarios, startup workload, total workload, and refund sensitivity. Result includes 80,613 contribution per six-week customer, 528 first-week minutes, 1,488 total minutes, and 584,712 full-cost balance at 24. Independent recalculation agrees. The three-week contribution's floating-point result `53102.99999999999` correctly displays as 53,103 won. |
| 16 | `call_fPaCqKupVhCvozPzaN2bVT3y`, `session-tools.jsonl:7–8` (ordinals 31 and 33) | Executes revenue, fees, operator labor, separate preparation labor, capacity, and break-even formulas. At four orders: 25,200 cash balance; −34,800 after recurring operator time; −84,800 after preparation; 140 and 80 designer minutes; 180 operator minutes. Independent recalculation agrees. |
| 17 | `call_dVWV1O9RLfuYvICXQHcnV1fF`, `session-tools.jsonl:7–8` (ordinals 33 and 35) | Executes fixed-cost, price/volume, budget, monthly-tool scenarios, effective hourly balance, and target-price formulas. Results include 163,000 base cost, 175,000 at two paid customers, 3,000 balance at 89,000, and 222,500 price for the assumed 20,000/hour target. **`hours:13.5` and the weekly array `[150,180,180,90]` are supplied literals**; the hours derivation is a descriptive string, not evaluated code. Independent audit calculations verify those totals below, but the historical call alone is not independent calculation of them. |

Run 15 also supplies 35/41/62-minute product totals as constants before using them in calculations, and run 16 supplies the derived 33-minute operator rate. Their underlying derivations reconcile with their inputs and labeled added assumptions. None of these computational records tests the realism of an assumed duration.

All 12 originals and corresponding workspace inputs have identical SHA-256 hashes and match both metadata input maps (`metadata.json:83–88`, `:341–346`). All three current session-tool file digests match `session_tools.export_sha256` at metadata line 29. The metadata reports workspace integrity passed with no violations (`:219–223`); this audit independently checked the allowed input files rather than rereading all workspace instruction files. Host-session source files and the capture module were outside scope, so their recorded hashes were not independently revalidated. File hashes identify the preserved evidence; they are not proof of tool-trace completeness outside the captured scope.

## 15 — supported offer

### Confirmed resources and proposed customer path

The representative has 12 preparation hours on 9/14–18 and only 90 minutes per week for later reception/accounting. Separately, a counselor has been prepaid for six weeks, 9/28–11/8, on Monday/Wednesday/Friday 18:00–22:00, including holidays. One of 12 weekly hours is reserved for common records: 11 hours = 660 customer minutes per week and 3,960 total. Extra counselors, overtime, and service after 11/8 are not authorized (`15/original-input/operations.md:7–12`).

| Stage | Output's proposed path | Audit against confirmed facts |
|---|---|---|
| Preparation and reach | 12-hour preparation allocation; copy due 9/18; stores post 9/21; neighborhood post 9/22; no paid recruitment spend. | Preparation totals 2+3+3+2+2 = 12 hours (`15/output.md:124–130`). Store and group dates, posting counts, no customer-list transfer, and no DM rights match the fixture (`channels-and-alternatives.md:7–11`; output `:95–101`). Zero advertising is an authorized choice from an unspent maximum budget, not removal of an unavoidable cost. |
| Application and commitment | One adult purchaser, maximum three plants, one package; suitability review precedes a payment invitation; pending invitations count against 24 seats; actual successful payment confirms registration. | The price of 89,000, 24-seat limit, hold expiry, refund rules, and new restrictions are identified proposals within the representative's authority (`operations.md:10,12,16,20`; output `:7–14,110–116`). The recorded interviews contain no sales and no recruitment-use consent; output does not convert them into leads or paid demand (`customer-notes.md:3,20`; output `:22,101`). |
| First result | Initial photos by 9/27; 12 first reviews on Monday 9/28 and 12 on Wednesday 9/30; Friday 10/2 first weekly check. | Work occurs inside the counselor's actual contract, not during the representative's preparation window. First-week base = 24×15 + 24×7 = 528 minutes (`output.md:78,82`). |
| Ongoing use | Weeks 2–5: Sunday photos/questions, Monday check, Thursday 18:00 short question cutoff, Friday answer. | Monday check requires 24×7 = 168 base minutes, leaving room across the three sessions. Short-question and exception handling have not been measured separately; whether included in seven minutes or drawn from slack needs operational observation. This is an uncertainty, not evidence the 660-minute cap is already exceeded (`operations.md:18`; output `:79,132`). |
| Correction and recovery | Tuesday 18:00 resubmission, Wednesday result. Last week explicitly sequences 11/3 → 11/4 → 11/5 → 11/6. Late initial data gets a 9/29 cutoff. Missing data is not guessed; missed delivery receives an in-contract recovery proposal or refund. | The final-week sequence fits actual weekdays and preserves a customer question opportunity before the final Friday answer (`output.md:80,84–86`). The first-week Wednesday branch requires clarification, below. |
| Closeout | Last answer and summary 11/6; service period ends 11/8; no renewal or new advice after final day; photos scheduled for deletion 11/8; weak recruitment does not cancel paid service. | 11/6 is the final Friday inside a contract ending Sunday 11/8. New intake closure does not remove existing paid obligations (`output.md:10,114–118,136–138`). Representative-run refunds, record closure, and deletion must use the continuing administrative allowance; no actual completion is recorded. |

### Capacity and money recomputed

Base weekly customer minutes at 24 are **[528, 168, 168, 168, 168, 288]**, totaling 1,488. First-week slack is 132 minutes after the common-record reservation; total six-week slack is 2,472. A 25% first-week increase gives exactly 660. Even at session level this can fit: base Monday/Wednesday first reviews are 180 minutes each and Friday checks are 168; common records can be allocated within the remaining session minutes. At 25% on each task block these become 225/225/210, leaving 15/15/30 for 60 total record minutes. This is a feasible allocation, not proof real workloads remain within 25%.

For a synchronized first week, 32×22 = 704 exceeds 660; the theoretical no-buffer limit is floor(660/22) = 30. The output's statement about 32 applies to this synchronized period-service start. It does **not** establish that 32 customers cannot buy any other permitted product.

Available alternatives must remain visible:

- Thirty-two single orders can, for example, use 18×35 = 630 customer minutes in one week and 14×35 = 490 in a second week, with still more spreading available. Their full-cost balance at the proposed reference price is 32×43,933−1,350,000 = **55,856**.
- Thirty-two three-week customers can be split into 16 starting in week 1 and 16 in week 4. Weekly base minutes become **[352,112,192,352,112,192]**; the full-cost balance is **349,296**. This allocation fits the counselor's confirmed six-week window, though willingness to accept the later start and actual exceptions remain to be tested.
- The output compares the shorter products at the **same 24 customers**, where their full-cost balances are −295,608 and −75,528. Those comparisons are correct (`output.md:49`); they do not prove six weeks is the only financially feasible use of the prepaid resource. Its choice is a price/duration hypothesis, not an established customer optimum.

All cost calculations use the fixture's VAT-excluded comparison basis. Per-customer contribution is `price×0.917−1,000`, charging the nonreturnable 3.3% payment fee, modeled 5% gross refund, and storage/send cost even for refunded customers. Contributions are 43,933 / 53,103 / 80,613. Cash-cost break-even is 26/21/14; including preparation labor it is 31/26/17. Prepaid nonrefundable fixed cash cost remains 1,080,000+30,000 = 1,110,000 for every product, plus 240,000 imputed preparation labor. At 24 six-week customers, 2,136,000 revenue less 70,488 fees, 106,800 modeled refunds, 24,000 individual costs and 1,350,000 full comparison cost leaves 584,712. At a 10% refund assumption it leaves 477,912. These match `15/output.md:41–63` and the arithmetic result.

The output correctly distinguishes the **forward additional cash contribution** from full cohort profit. Representative operating labor is expressly missing, so the result is not proven sustainable profit. The 5% calculation assumption is also kept separate from the newly proposed consumer refund terms (`output.md:61,116`).

### Narrow unresolved branches, not a demonstrated global overload

1. **First-week resubmission sequence is incomplete for a Wednesday first-review recipient.** The output allocates 12 first reviews to Wednesday 9/30, while its general resubmission deadline is Tuesday 9/29 18:00 (`output.md:82–84`). If that first review reveals that a replacement photo is needed, this customer cannot follow the advertised Tuesday → Wednesday correction sequence after receiving it. The date ordering is confirmed; that a particular customer needs a replacement is not. There is first-week slack and Friday service, so this is a missing branch/cutoff, not proof that the cohort cannot be delivered. The plan should distinguish pre-review missing-data completion from correction requested by the first result and place the latter before 10/2 without assuming off-contract work.
2. **Administrative throughput is a proposal, not a measured capacity.** The 90-minute recruitment-week allocation gives 60 minutes to intake/seat/payment work and 30 to posting/comments (`output.md:101`). At 24 paid customers that is only 2.5 administrative minutes per payer before accounting for nonconverting applicants, but the source provides no per-application timing. An overload cannot be asserted from that absence. The stated closure/queue rule and prepayment cap can reduce intake; whether it still meets all invitation deadlines is an operational check.

## 16 — dependent handoff

### The main dependency chain is actually placed inside available windows

Confirmed operator resources are 150 preparation minutes on 9/14–18 and a separate 240 operating minutes on 9/21–10/2. The designer has exactly two nontransferable windows, 9/24 and 9/30, each 18:00–21:00 and 180 minutes (`16/original-input/operations.md:3–10`). A/B cannot approve before seeing a draft, and can review in the evenings starting the day after draft arrival through 9/28 noon (`research.md:14`).

The proposed route is source-consistent:

1. Allowed room post on 9/21 and reminder on 9/22 → information, images, permissions, evening availability checked → completed data and payment by 9/23 22:00. Only four eligible orders receive invitations (`16/output.md:35–45,54–55`). The 32-member room is not treated as 32 reachable buyers.
2. On 9/24 the designer spends 4×35 = **140** minutes producing drafts. Operator delivery by 21:30 uses operator time within its separate date range, not an extra designer window (`output.md:56,95`).
3. Customer review occurs **9/25–27 evenings**, after actual drafts. Feedback or approval is due 9/28 noon; operator consolidation then feeds the second window. No pre-approval is substituted for review (`output.md:37,57–58,64`).
4. On 9/30, revisions and final exports take 4×(15+5) = **80** designer minutes, 18:00–19:20. Operator QA is booked 19:20–19:40 while the designer is still available. This leaves 80 clock minutes after QA for corrections and re-export. The table's 100 nonbooked designer minutes include the 20-minute operator-review interval; it should not be interpreted as 100 minutes after QA (`output.md:59,96`).
5. Final files arrive by 10/1 18:00; customers download and test-print. Through 10/2 the operator can resend files or help with settings. After the designer's final window the plan does not invent more designer availability: a major production error triggers stop-use and full refund (`output.md:60–61`).
6. Customers choose/pay their own printer and must arrange submission before the recorded 10/5 noon deadline, then use the cards at the 10/10 market. Printer price/availability and market-day assistance are not guaranteed (`output.md:39,62,125`).

This provides a feasible review/correction handoff for four eligible customers. It does not require the unused 9/24 minutes to roll into 9/30 or the operator to perform designer work.

### Economics, assumptions, and fallback

Operator base order time is 12+8+4 = 24 minutes. The output labels its added nine minutes per order for draft sending, final comparison, and reminders/exceptions. Thus 48+4×33 = **180**, leaving 60 of 240 operating minutes. The scheduled 20-minute QA interval is slightly more than the modeled 4×4 = 16 minutes, which the 60-minute reserve can accommodate; it is not an overrun of the confirmed total. Unknown extra contact volume is not an observed overload. Five orders would consume 175 of 180 first-window minutes, so refusing a fifth is an explicit buffer choice (`16/output.md:91–100`).

Both 60,000 designer windows are **committed costs whether or not orders occur**, not necessarily already prepaid; the raw fixture does not say payment has happened. With the 10,000 template fee, fixed cash cost is 130,000 (`economics.md:3,7`). The proposed price is not a customer commitment. At 1/2/4 completed, nonrefunded orders, the cash balances are **−91,200 / −52,400 / +25,200**. Operator minutes are 81/114/180 and imputed labor costs 27,000/38,000/60,000. Recurring economic balances are **−118,200 / −90,400 / −34,800**. Adding 50,000 preparation labor gives **−168,200 / −140,400 / −84,800**. All match the output and tool record.

Cash break-even at 40,000 is four customers; recurring economic break-even would be six and first-run economic break-even eight under that same extrapolated cost structure. Both exceed the offered cap; this is not permission to accept those counts. The four-order recurring break-even price is 48,969.07, reasonably described as about 48,970 (`output.md:102–112`). Refunds, taxes and unplanned spending are explicitly outside these tabulated scenarios. Proposed full refunds therefore reduce realized cash but are not silently treated as free operations.

The plan preserves confirmed orders even with one sale, declines incomplete late orders instead of moving first production to 9/30, and uses cancellation/refund rather than inventing approval or a post-window revision service (`output.md:68–72`). The post-window refund fallback does **not** supply a corrected card by the market; it is a defined limitation of this offer. Actual recovery and refund execution are not recorded.

### Printer-format prerequisite remains unplaced

`16/output.md:80` promises margins/trim marks matching both the template and the customer's confirmed printer conditions. Yet the application and folder specification do not collect printer specifications or give them a pre-9/30 cutoff (`:54–55,76`), and the raw journey says the maker selects a printer after receiving the finished file (`operations.md:27`). If the selected printer requires a different bleed/margin/export setup, that prerequisite could surface only after the last designer window.

This is a **conditional handoff gap**, not a confirmed impossibility: the existing A6 template may already be accepted by the selected printer, and the output expressly leaves printer choice/confirmation with the customer. A complete preparation decision should either collect necessary print requirements before the final window or define the supported PDF specification and make customers choose a compatible printer. No evidence establishes that an incompatible printer was actually selected.

## 17 — pilot commitments

### Existing entitlements and proposed new terms are distinct

The two free customers already have a 60-minute meeting on 10/4 plus up to two 15-minute calls during the inclusive 14 days ending **10/17**. One has asked for a first call on **10/16**. They are separate from interview participants, and no paid customer is confirmed (`17/original-input/operating-notes.md:3–5`). The source guarantees only October resources: weekly 240 minutes for onsite meetings/turnover and a separate 180 weekday minutes for calls, preparation, administration and promotion. These budgets cannot be traded (`:7`).

The output's paid proposal starts 10/11 and ends 10/24, which is also exactly 14 calendar days including the first day. It proposes weekday appointments, with possible calls on 10/16 and 10/23, and requires actual compatible slots to be shown before reservation confirmation (`17/output.md:26–34,73–80`). Those restrictions can be proposed for **new** paid customers. The output explicitly refuses to apply them retroactively to the free customers and states that lack of agreement leaves the original obligation in place.

Both support endpoints, 10/17 and 10/24, are Saturdays. An endpoint on Saturday does not prove that both calls must occur that day, or that a customer has requested an unsupported weekend call. The free customer asking for a first call on Friday 10/16 still has a second-call entitlement; two mutually acceptable calls on Friday are not forbidden by the raw fixture, which imposes no minimum spacing. Conversely, one Friday call plus a hypothetical second call after 10/17 would not fulfill the original period. The schedule agreement is therefore an unresolved prerequisite, not an already demonstrated breach or an already solved promise.

### Path from recruitment through support and closeout

| Stage | Proposed action | Audit status |
|---|---|---|
| Before commitment | Confirm the two free customers' usable support slots; verify the paid slots and booking/contact procedure; review return travel and preparation time. | Output expressly gates paid confirmation and even publication on these checks (`17/output.md:5,32–34,49,63`). No completed confirmations are recorded. |
| Recruitment | One permitted apartment notice during 9/28–10/10 and a post on the operator's personal group account; one 20-sheet print bundle; no resident list or bulk messages. | Permissions and units match `interview-notes.md:10` and `quotes-and-costs.md:10`. Posting on 9/28 is a plan, not an executed external action. |
| Customer prerequisites | Show contents, date, total, support limits, cancellation terms; collect only contact, desired onsite/call times, goal and payer relationship; family review may happen on a Sunday morning; no payment while unsettled. | Does not require weekday approval from Sunday-only interview participant Jaehoon or treat family consultation as a purchase (`output.md:65,69–80`). Actual compatible onsite/call and preparation slots still need confirmation. |
| Confirm, pay, meet | Proposed cap two paid customers; confirm all slots first; proposed bank transfer before the onsite start; 60-minute practice and booklet; no copied photos, repair, or device transfer. | Price, payment mechanism and cancellation policy remain proposed. The room rental exists, but specific reservations and transaction handling are not demonstrated as completed (`output.md:3,26–30,73`). |
| Telephone help and changed appointments | Deliver each customer's remaining calls within their own 14-day period; new customers get agreed weekday slots; free customers retain old terms unless they agree to a different schedule. | The 10/16 request is preserved. Changed appointments cannot extend beyond the promised term without an agreed resolution. Weekday-only capacity is not silently equated with permission to rewrite free entitlements (`output.md:32–34`). |
| Intake decision and closeout | 10/12 decides further intake; existing free service continues through 10/17 and paid service through 10/24. Unfulfillable commitments require individual alternative/refund agreement. Return equipment, avoid unnecessary contracts, settle accounts and explain contact-data handling. | Correctly does not close existing service on the decision day, convert refunds into automatic discharge, or claim support completion/repeat purchase can be known on 10/12 (`output.md:109–122`). These are remaining actions, not completed recovery. |

### Independent time reconstruction and valid alternative allocations

The output reserves 75 onsite minutes per customer. The raw fixture says 15 minutes **between** customers, so two consecutive meetings minimally require 60+15+60 = 135 minutes, not 150. Allocating 150 is an explicitly conservative choice, not an arithmetic error. Two free customers on 10/4 and two paid customers on 10/11 each fit the relevant 240-minute week. Three would take 210 minutes with only between-customer cleanup or 225 under the output's conservative method; onsite time alone does not establish the paid cap of two.

The proposed weekly weekday envelopes independently recompute to:

| Week | Minutes | Scope of this envelope |
|---|---:|---|
| 9/28–10/4 | 60 free preparation + 30 management + 60 promotion = **150** | Publication before October has no separately confirmed September hours; see unresolved prerequisites below. |
| 10/5–11 | 60 paid preparation + 60 free-call allowance + 30 management + 30 promotion = **180** | Worst-case free-call allowance; it is not an observed booking. |
| 10/12–18 | 60 free-call allowance + 60 paid-call allowance + 30 management + 30 decision = **180** | Both full call allowances represent an upper envelope, not extra call entitlements. |
| 10/19–25 | 60 paid-call allowance + 30 management = **90** | Continued support after the 10/12 intake decision. |

There are only four customers × two calls × 15 minutes = **120 actual entitlement minutes** across the whole pilot. Adding the weekly envelopes counts some of those same 120 minutes in alternative possible weeks; it must not be used as an actual total of 240 call minutes. The output makes this distinction expressly (`17/output.md:47`). The known 10/16 first-call request makes an all-free-calls-in-the-earlier-week scenario even more conservative; that is not harmful overbooking evidence.

Using the output's conservative per-customer times, total work is independently verified as:

`4×(75 onsite + 30 preparation + 30 calls) + 4×30 management + 90 promotion + 30 decision + 30 return = 810 minutes = 13.5 hours`.

The weekly envelope table omits a separate return allocation while the total-labor calculation includes 30 minutes for it (`output.md:49,105`). This needs placement, but it does not prove an unavoidable overload. For example, if the two paid customers each take one 15-minute call on 10/16 and one on 10/23 as suggested, paid calls require only 30 minutes in each week. Even with all 60 free-call minutes in 10/12–18, that week's weekday tasks are 60+30+30+30 = **150**, leaving 30 minutes for additional suitable weekday work. The Sunday return trip itself still needs a confirmed travel/resource allocation; the source does not explicitly classify it as weekday work or onsite-meeting turnover. The output calls this an item to verify, not free labor.

No customer request timings or handling measurements establish an observed >180-minute week. It would be incorrect to infer overload by forcing every duplicated upper-bound call allowance, all possible extra contact, and return travel into the same resource block while ignoring available booking choices. Conversely, the base arithmetic does not establish a fully confirmed appointment book.

### Costs, contract periods, and budget

The room's 110,000 is already paid for **the entire October month**, nonrefundable midmonth, and included in the total 300,000 personal cash limit (`quotes-and-costs.md:7`; `operating-notes.md:9`). It cannot be prorated to the first 12 or 14 days. The output correctly includes it in every scenario.

The rental vendor has quoted **33,000 for 10/4–17**, provided application occurs by **9/29**, with return **10/18 at 10:00**. No order has been made. This is a conditional available offer, not a completed reservation. The normal 30-day price is 66,000; choosing the offered short rental reduces planned expenditure by 33,000. A 2,400/day extension requires stock confirmation and is not a committed resource (`quotes-and-costs.md:8,13`; output `:89`). Because no onsite visit is promised after 10/11 and later help is by phone, return on 10/18 is not intrinsically incompatible with paid support through 10/24. The output properly requires checking that later telephone support can be delivered without the rented display.

One print bundle is 20 sheets for 8,000, not 8,000 per sheet. Booklets/consumables cost 6,000 for each free **and** paid participant. Base pilot cost is therefore `110,000+33,000+8,000+2×6,000 = 163,000`. At paid count n, it is `163,000+6,000n`. At prices 49,000/69,000/89,000, the zero-paid balance is always −163,000, one-paid balances are −120,000/−100,000/−80,000, and two-paid balances are −77,000/−37,000/+3,000. Mathematical cash break-even is 4/3/2; the first two counts are above the proposed operational cap and do not authorize taking those extra bookings.

At two paid customers, total spend 175,000 plus 60,000 reserve and 65,000 unallocated equals 300,000. Forward cash required for this no-tool plan is 65,000 beyond the already paid 110,000, against 190,000 remaining original funding, so it does not depend on collecting the proposed 178,000 revenue in advance. The displayed 3,000 surplus is before labor, unpriced extra communications, and tax settlement (`output.md:99–101`), not an owner wage.

The SMS tool is 44,000 per account-month with the **minimum number of months still unanswered**. Output defers signup and does not claim a free substitute has been verified. One/two/three monthly charges would bring spend to **219,000 / 263,000 / 307,000**. Adding the proposed 60,000 reserve gives **279,000 / 323,000 / 367,000**; thus two months already require consuming reserve/unallocated capacity, while three exceed original funding before reserve. The historical arithmetic output contains both series; the final answer displays only the spend series (`output.md:103`). None of those scenarios establishes the actual minimum contract term.

At the output's 13.5-hour assumption, 3,000/13.5 = **222.22 won/hour**. Recovering 175,000 outlay plus 13.5×20,000 labor from two paying customers needs **222,500 per paying customer**. Both reconcile with the tool and final output. The 20,000 hourly target is explicitly a new assumption because the raw operator has not chosen a target. The 89,000 sale price is an affordability/demand hypothesis, not validated willingness to pay.

### Prerequisites still open, not confirmed contradictions

- **Existing-call scheduling:** agreements have not been obtained; the paid launch remains conditional. The source does not guarantee weekday-only acceptance by the free customers or prescribe a minimum gap between calls. Both facts must be preserved.
- **September preparation:** the raw time promise is for October. Posting beginning 9/28 and taking the rental offer by 9/29 need September effort which is not separately quantified. Some first-week preparation could fit 10/1–2, but that does not by itself resource a 9/28 post or a 9/29 booking. The request asks for this week's promotion, so zero September availability also cannot be asserted. This is an unconfirmed time allocation to resolve before commitment.
- **Booking/contact and return:** the SMS contract is deliberately not taken, and no free tool is assumed available; a workable contact/booking procedure, possible extra communications cost, actual room/meeting slots, and the 10/18 10:00 return trip remain to be confirmed. The output names these checks. Neither an unpriced optional tool nor an unknown duration is itself an established expense/overload.

## Evidence hashes

The following original-input digests also equal the matching workspace-input digest and both metadata before/after input maps.

| Run | Input | SHA-256 |
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

| Run | Evidence file | SHA-256 |
|---|---|---|
| 15 | output.md | `3a27fe3c6873846e0019218e6b6ca2d12e003da351fced6ad6a0feae80031c52` |
| 15 | metadata.json | `77b948058725b0a0e484b584fa62145b2ddd8628fe7027535549265a731cdd93` |
| 15 | session-tools.jsonl | `20058f37c2dd8ef9e85d37b5f67529b4159e16be4b08ad736cdc3ea2fb9fe859` |
| 15 | events.jsonl | `3d6e1051b46ac817b20d9419e1587ab6861f9c6fc314ddbbd041b0610153c4dd` |
| 16 | output.md | `0aea96094eefa0b7cfa5c924a5e09053eae32be50553194215c7c5c006dc21fc` |
| 16 | metadata.json | `7fe6e01c1530d989e86cd3e7cdee3f6ad2fb67cb8af3fdcae3d8b4d38995989d` |
| 16 | session-tools.jsonl | `a5880f25d8a2a866f6086bff562ecd7b0918658339099f3cc66022c1df147bbf` |
| 16 | events.jsonl | `f2d3874793beaf96704768f83e246514daa080e4f0f07802929136e5e64b6b4e` |
| 17 | output.md | `307ba8ddd162028b8942922e0b9dfb1e929627ea7ea2484afac7c24f4860e75c` |
| 17 | metadata.json | `617411a6c623a1bfcc617aa5148fe96721284880dcf40f5280a82669bf274ca5` |
| 17 | session-tools.jsonl | `4910f485beb8e94b4e5f40c33f31cb8f200005892c368520bbeedbdaabedaf64` |
| 17 | events.jsonl | `34869bb9989833c41a4259d341671b3b7cd22d57a042a6ad9252a4d10016f7a3` |

Only this report was written by this audit. The settled evidence, workspace inputs, and business systems were not changed.
