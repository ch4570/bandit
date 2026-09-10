# Independent service execution and whole-path audit

Audited settled runs: `15-supported-offer--bandit`, `16-dependent-handoff--bandit`, and `19-dependent-prerequisites--bandit`, under `/private/tmp/bandit-batchcaps.AF24cq/runs/`.

This audit uses each run's original inputs, output, metadata, captured tool records, runner prompt, and selected CLI event fields. Execution copies of inputs were accessed only to compute hashes. Incidental skill-reference text in a captured read response was disregarded as an evaluation standard. No current skills, criteria, grades, author package, protocol, other runs, product code, tests, or external actions were used. References below are relative to the audited run unless explicitly prefixed by its number. Line numbers include the final line even when the file lacks a trailing newline.

## Conclusions

- All 13 original input files match their recorded hashes, execution copies, and recorded post-run hashes. All three tool-export hashes match. Each run has four captured call/result pairs, including a completed arithmetic call whose returned values agree with the output's reported calculations. No fabricated arithmetic execution claim was found.
- Case 15 has two supported, bounded operational defects: its final-week allocation omits the preceding week's included question round, and its first-five-customer workload observation occurs after the proposed intake close. Correcting the final week to 440 customer-work minutes still fits the 660-minute limit; these defects do not demonstrate an impossible cohort.
- Case 16's selected four-order path fits the two separate design windows, preserves post-draft customer approval, and establishes printer compatibility before payment. No supported timing or arithmetic defect was found in that selected path.
- Case 19 preserves the eight adopted free bundles and their revision rights. Its four-unit latest-input Thursday path can fit the source task durations by pipelining production, checking, and delivery. It expressly leaves unresolved revision expiry and future staffing conditional; it does not establish that all existing obligations can already close by November 1.
- These are planning artifacts using synthetic evidence. Captured arithmetic proves arithmetic execution, not service delivery, demand, usability, tool compatibility, or actual operating speed.

## 1. Integrity and execution evidence

### Hash verification

For every row below, independently computed SHA-256 values for `original-input/<file>` and `workspace/input/<file>` equal both `metadata.json.input_sha256` and `metadata.json.input_after_sha256`.

| Run | File | Matching SHA-256 |
|---|---|---|
| 15 | channels-and-alternatives.md | `0d2bcd7080ae7d1af1a09ef6338f8ecb71ea22abf457ac5103f9b6ab95ffdb21` |
| 15 | customer-notes.md | `44cc27e33a683ad7c6f71c33607278183c7b8b2c2e49e119c7a4604b76afd4b6` |
| 15 | operations.md | `8f9532f21045919ffee120432efc5fa9823db291569f00d45382b876cc594fa9` |
| 15 | request.md | `cb2b6fba4ceee5375b134d4ca9a7c3b8fea273a0500c983507d5b267e863db11` |
| 16 | economics.md | `7f50a6dcc7b6a2a16dce37caefca463747e183fa74291720199344b31717f22e` |
| 16 | operations.md | `e3b1fc177f74d04a6a04af70b31facfd2022ab1423371ea013ad65ca38e3e3a5` |
| 16 | request.md | `f758032be79595a2373a566a7418fdee4ed1c04f2288db2ec8a8b77841721954` |
| 16 | research.md | `3ae661fd19859ac784dddc906ccf674ee92f4416c578d17fdb5c101b69cbe78a` |
| 19 | fixtures/01-창업자-메모.md | `a395eae2a30d742b769a91a1e7c3cce64b7b2b57a67316fee689679b0db4b46d` |
| 19 | fixtures/02-인터뷰-발췌.md | `244eca29cb5a3ed57e6e79b035d701a857594289c503aa16964e6d9fbac2cb79` |
| 19 | fixtures/03-제작-작업기록.md | `2c25bfdd34e176945c62b90b4920798f5e04932b20a46369c9e365b057411dc0` |
| 19 | fixtures/04-동아리-주고받은-내용.md | `915b57d0af36a114473409c8c5d269bc955127803983f109f658122ec86241e7` |
| 19 | request.md | `c182dc08f93a615a7f16d76e5ab21c5d0f53fe8427f4a614ebb16a412cd921fd` |

Input hash records: all three `metadata.json:83`; post-run records: cases 15/16 `metadata.json:341`, case 19 `metadata.json:360`.

| Run | Recomputed `session-tools.jsonl` hash, matching `metadata.json:29` |
|---|---|
| 15 | `ff498d96262abafb8b94f609f9c5e0ce82e395c7f2d3946732a9d890429f6638` |
| 16 | `b9bf454a6e726f35547f50cac8474a53c6c4e54124027d48c504e2730017f22c` |
| 19 | `cc6c920480bd637750346584229ac814e64c677a69bda6cb0989a3c4f53f998a` |

The before/after workspace snapshot objects are identical in all three metadata files; all recorded snapshot-error and violation arrays are empty. Metadata records process and run exit code 0 and `integrity_status: passed` (cases 15/16: lines 10, 219–225; case 19: lines 10, 229–235). This supports absence of recorded workspace mutation, not complete visibility into every possible external action. Host-session `source_sha256`, runner, and capture-module hashes cannot be independently verified from the allowed files and were not presented as independently verified.

The saved final output matches the final CLI agent-message text after trimming trailing whitespace: case 15 `events.jsonl:12`, case 16 `events.jsonl:11`, case 19 `events.jsonl:12`. The `item_0` notices in cases 15/19 `events.jsonl:3` concern shortened skill descriptions; they are not failed arithmetic calls or failed final generation.

### Captured tool pairs and output claims

Each `session-tools.jsonl` has calls on lines 1, 3, 5, 7 and matching results on lines 2, 4, 6, 8. The first three calls are file discovery and reads; their underlying shell results report exit code 0. The fourth is in-memory JavaScript arithmetic, with a completed returned result. It is visible in the session export even though the selected CLI command events alone do not show it.

| Run | Arithmetic call ID, `session-tools.jsonl:7–8` | Output claim and actual returned evidence |
|---|---|---|
| 15 | `call_gnjIvamS6XXRkZENysEEnu9n` | `output.md:92`: reports arithmetic verification. Return includes contributions 43,933 / 53,103 / 80,613 won; break-even counts 26/32, 22/26, 15/18; scenario cash/economic amounts; 440/140/240 basic weekly loads, 1,240 basic total, 540 first-week-with-questions, 340 final-with-questions, and −34,740 at 20% refunds. The calculation really ran; the 340 figure has the scheduling omission discussed below. |
| 16 | `call_9b1VNsl47R2657tkqME79W7y` | `output.md:104`: reports executed calculations. Return includes first-window theoretical capacity 5, selected 4, design loads 140 and 80, operator 196 plus 44 reserve, four-sale cash +25,200, total economic −90,133.33, and repeat break-even price 50,343.6426 won. |
| 19 | `call_LMLGpuRSXxDYEttI5U0eZcKa` | `output.md:102`: identifies independent arithmetic and returned quantities. Return includes 10 bundles; weekly operator 360/320/300/240, audio 160/150/160/60; totals 1,220 and 530 minutes; latest-input audio 160; direct labor 25,000 won; economic cost 521,666.67; and revenue 24,000. |

The independent audit recomputed these material amounts and the corrected final-week plant load. Monetary rounding in cases 16/19 is consistent with the exact returns. No product/test execution was observed in the captured calls. All three `prompt.txt:2` prohibit product/test execution, browsing/contact, additional model sessions, and file changes; they do not prohibit the captured independent arithmetic.

## 2. Case 15 — six-week plant service

### Preserved resources and selected scope

The input separates the founder's September 14–18 preparation budget of 12 hours from the separately prepaid September 28–November 8 consultant contract: Monday/Wednesday/Friday 18:00–22:00, including holidays, 72 gross hours and 66 customer-work hours after one weekly hour of shared records (`original-input/operations.md:7–11`). The output correctly retains that six-week resource rather than shortening delivery to the preparation period (`output.md:7–16`).

The selected offer is one 89,000-won payment, no renewal, at most 20 people and three plants each, initial advice plus six weekly checks including the first week, closeout summary, and one gathered supplementary question per round (`output.md:7–14`). There is no observed purchase or validated processing speed (`original-input/customer-notes.md:3,20`; `original-input/operations.md:18,20`; `output.md:3,27–36,48`).

### Whole permitted cohort and dependencies

| Path | Source and output linkage | Audit result |
|---|---|---|
| Recruitment and entry | Free shop notices have September 18 copy deadlines and September 21 publication; community notice September 22 (`original-input/channels-and-alternatives.md:7–11`). Output prepares those assets, avoids adding follower counts into unique reach, assigns 90 founder minutes to intake/comment work, and accepts at most 20 confirmed-or-held slots (`output.md:101–107,117–118`). Payment and required material deadline is September 25 (`output.md:52`). | Coherent planning sequence. The 90-minute allocation is a proposal with untested processing speed; the number of unsuccessful applications is not capped, so its sufficiency is not established. No measured overload follows from that unknown. |
| Normal first week | All 20 initial reviews consume 300 minutes, scheduled 10 each on Monday/Wednesday (150 minutes each). Friday adds the first 20×7-minute check and 60 shared-record minutes (`output.md:44,53`). | Each stated day fits its 240-minute shift. Basic first week is 440 customer minutes; source estimates remain estimates. |
| Ordinary weeks | Sunday 20:00 photo input → Friday 22:00 result → following Sunday 20:00 gathered question → Monday 22:00 answer (`output.md:54`). | Normal 140-minute weekly photo check plus the preceding round's 100-minute question allowance can fit the contracted shifts. The plan distinguishes weekend submission from weekday answer availability. |
| Initial missing-material recovery, all 20 | Consultant requests improvements by September 30; latest complete replacement input October 4 at 20:00; re-review by October 7. First-week check is refunded if not provided. Output assigns Monday 100 question + 120 re-review minutes, Wednesday 180 re-review, Friday 140 check + 60 records (`output.md:59–61`). | Customer-work sum 300+140+100=540; daily elapsed loads 220/180/200 all fit 240. This reallocates the admitted 20 people; it is not an additional 20-person cohort. Prior incomplete reviews and clarification administration can add work, but their duration is not demonstrated to exceed remaining time. No further indefinite recovery is promised after October 4. |
| Final result and included question | Final photos November 1 at 20:00 → results/summary November 4 at 22:00 → final question November 5 at 20:00 → answer November 6 at 22:00 (`output.md:62–63`). Weekday response requirement is disclosed before payment; further new rounds are excluded. | The final question is triggered by an already-delivered final result, with a staffed reply window. The separate preceding round also lands in this week; see finding 15-A. |
| Failure and closeout | Stop new intake, notify affected customers, refund unprovided work if promised timing fails (`output.md:64`). End screen retains payment/refund contact but ends new consultation; photo deletion after 30 days is proposed (`output.md:120–124`). | Consultant work does not silently extend beyond the contract. Post-close payment contact/photo deletion have no quantified staffing allocation; the founder's continuing 90-minute weekly allowance exists in the input. This is an untested administrative allocation, not proof that no staff exist. |

### Supported findings

**15-A — final-week allocation misses the preceding round's questions.** The ordinary rule in `output.md:54` makes the October 30 result's questions due November 1 at 20:00 and answers due November 2 at 22:00. These are separate from the final-result questions due November 5 and answered November 6 (`output.md:62`). At the output's own 20×5-minute allowance (`output.md:48`), both rounds add 100 minutes each. Final-week customer work is therefore 240+100+100=440 minutes, not the 340 represented by `output.md:63` and `session-tools.jsonl:7–8` (`finalWithClarification`). This is an omitted dependency in the weekly allocation, not a false arithmetic-execution claim.

Impact is bounded: 440 remains below 660. A valid placement is Monday 100 preceding questions + 120 final-result minutes, Wednesday 120 final-result minutes, Friday 100 final questions + 60 shared records. Each day remains below four hours. Correct the allocation and terminal reserve; do not claim that the cohort necessarily misses its final deadline.

**15-B — first-five workload observation cannot reduce this closed intake.** `output.md:143` proposes measuring the first five customers' actual work and reducing remaining intake if work is slower. All cohort payments/materials close September 25 (`output.md:52,118`), before the consultant begins September 28 (`original-input/operations.md:8,10`; `output.md:12`). The observation is useful for delivery adjustments or later decisions, but there is no remaining normal intake to reduce when actual service work becomes observable. The output should use a pre-intake rehearsal or a genuinely staged intake if it wants this observation to protect admission decisions. Its existing delay/refund route remains available; the timing defect does not invalidate the conservative 20-person cap by itself.

### Financial reconciliation and bounded uncertainties

The output correctly preserves the non-refundable prepaid consultant/tool amount of 1,110,000 won, chooses 30,000 of the 90,000-won optional marketing budget, and separately values founder preparation at 240,000 won (`original-input/operations.md:24–32`; `output.md:68–89`). It applies the 3.3% fee and 5% refund assumption to initial payments and retains the 1,000-won per-paying-customer cost despite refunds. Contribution is 80,613 won; at 8/14/20 payments, future net cash is 614,904 / 1,098,582 / 1,582,260, cohort cash −495,096 / −11,418 / +472,260, and after preparation labor −735,096 / −251,418 / +232,260. Cash break-even 15 and preparation-inclusive break-even 18 fit the selected cap, without proving attainable demand. The 20% refund sensitivity gives −34,740 including preparation. Ongoing founder labor is expressly excluded rather than hidden.

The all-20 missing-first-check recovery would refund 12% of each initial price under `output.md:124`, or 213,600 won in total, rather than the baseline 5%/89,000-won assumption. This is a different realized scenario, not an arithmetic error in the explicitly labeled 5% baseline. Re-review effort and refund administration similarly should not be assumed absent or automatically counted twice.

One handoff detail remains underspecified: the first Friday check is scheduled after Monday/Wednesday initial advice, but initial photos are collected by September 25 and no fresh first-week photo deadline is stated (`output.md:52–54`). For an offer positioned as applying advice and then comparing changes (`output.md:31,36,96`), the first post-advice observation and its timing should be explicit. The source does not mandate a minimum observation interval, so this is a missing operational detail, not a demonstrated impossible time interval.

## 3. Case 16 — four-order card service

### Whole selected path

The source reserves two independent designer windows of 180 minutes, September 24 and September 30, with no transfer of unused time, and keeps founder preparation 150 minutes separate from subsequent order operations 240 minutes (`original-input/operations.md:3–10`). Output preserves those boundaries and selects a 40,000-won, at-most-four-author offer, up to three A6 cards per author, one viewed draft, one gathered revision, and a print PDF (`output.md:18–24,28–40,89`).

1. **Input and latest accepted entry.** Applications close September 22 at noon, complete material/payment September 23 at 20:00, after one missing-input request. September 22–23 evening response availability is an eligibility condition. Late orders do not start in the second design window (`output.md:33–34,45`). Unknown availability of other interviewees is not assumed equivalent to A/B's known availability.
2. **Actual draft before customer review.** September 24 production uses 4×35=140 designer minutes; operator sends previews after 21:00. A/B can review from the next day through September 28 noon, in the evenings (`original-input/research.md:14`; `output.md:35–36`). No “advance approval” substitutes for seeing a draft. Other applicants must share that availability.
3. **Approval and second production.** Up to four feedback lists are gathered September 28 in 32 operator minutes. September 30 revision/export is 4×(15+5)=80 designer minutes, with 100 designer minutes left for errors, plus a separately budgeted 20-minute operator final comparison in the same three-hour window (`original-input/operations.md:19–23`; `output.md:37–38`). Sequentially allowing 80 production + 20 comparison still leaves 80 elapsed minutes for feedback-dependent designer work; the stated 100 is remaining designer work capacity, not a promise that every one of those minutes can occur after a fully batched comparison. The plan does not require consuming all 100, and per-order checking can overlap the designer's next order.
4. **Supported print output before commitment.** A6 105×148 mm, one page per product and embedded-font PDF are specified. Before payment the customer must confirm the selected printer accepts that contract; additional bleed/crop requirements are assessed for eligibility then (`output.md:81`). This addresses the downstream prerequisite before the final revision window. Source print deadline is October 5 noon, printing/shipping excluded (`original-input/operations.md:27`). The output does not assume that arbitrary printer requirements discovered after September 30 can still be produced.
5. **Final delivery, usable review, inquiry, downstream action.** PDF by October 1 at 18:00; access/print-setting inquiries through October 2 at 18:00; operator reply/re-send/refund October 2 at 20:00–21:00; customer independently checks current printer conditions and submits by October 5 noon (`output.md:39–41,64,78–81`). No unstaffed later redesign is promised. Actual printing and market use remain customer actions, not observed or guaranteed service results.
6. **Recovery and closeout.** A September 27 reminder precedes the September 28 approval deadline. Silence never becomes approval: no response or unresolved factual content leads to refund and termination. Submitted revision instructions expressly authorize finalization of that draft plus those changes. Unfixed production errors or subsequently discovered nonperformance trigger stop-use advice and full refund instead of imaginary extra design staffing (`output.md:46–49`). Operator/designer mistakes do not consume the customer's correction entitlement (`output.md:23`).

### Capacity, money, and limits

The source's normal operator order work is 12+8+4=24 minutes; four orders use 96. Output adds the mandatory 48 shared minutes, 8 draft-dispatch minutes, 20 final-comparison minutes, 24 final-inquiry minutes, leaving 44 of 240 as reserve (`output.md:91`). Admissions are bounded at eight applications/four orders; rejected notifications, posting, payment records, and closeout are assigned within the shared block. Screening or unusually complex rejected applications may consume more than assumed; the raw measurements do not establish their exact time, so this does not demonstrate overload. More complex inquiries/reminders/cancellations explicitly use reserve.

Both paid designer windows and the 10,000-won template fee remain fixed even at zero orders (`original-input/economics.md:3–7`). Cash formula `n×40,000×0.97−130,000` gives −130,000 / −91,200 / −52,400 / +25,200 at 0/1/2/4 orders. Planned repeat operations 196 minutes are worth 65,333.33 won; initial preparation 150 minutes is 50,000. Four-order economic results −40,133.33 excluding preparation and −90,133.33 including it are correct; using the entire reserve gives −104,800. Repeat break-even price at four orders is 50,343.64 won, approximately the reported 50,344 (`output.md:93–104`; arithmetic call above).

The source excludes refunds/taxes from the comparison and the output retains that boundary. Loss from cancellations is not included in the no-refund baseline; it is not thereby denied. The output also says post-October-10 usage aggregation time is not yet secured (`output.md:108`), so its target of three actual users is a future decision criterion, not a completed observation or fully staffed post-pilot research claim. No supported selected-path defect was found.

## 4. Case 19 — theatre audio/PDF pilot

### Adopted obligations, units, and prerequisites

F4-A/B accept two deliveries for each of four adults, eight free bundles total, with first inputs October 6 noon → delivery October 8 at 22:00 and second inputs October 20 noon → delivery October 22 at 22:00. Each bundle includes one same-script/same-role pause or reading-error correction; no correction expiry was adopted (`original-input/fixtures/04-동아리-주고받은-내용.md:7–17`). Output preserves these rights and limits the conditional new offer to two individually paid bundles (`output.md:4–6,30–39,58–63,83`). It does not turn two roles or two pause variants into one production unit.

Input limits preserve all three source conditions simultaneously: no more than two pages, 24 counterpart lines, and three minutes of counterpart audio. Output is one audio file plus one large-text PDF, with role/version/pause markers. Source task durations are 15 operator minutes for input checks, 35 audio-producer minutes, 10 operator checking minutes, 10 operator delivery/basic-question minutes, and correction reserves of 5 operator/10 audio minutes, plus weekly common work 40/20 (`original-input/fixtures/03-제작-작업기록.md:7–25`; `output.md:30–36`).

The output assigns permissions, format/pause definition, individual delivery route, and download/access-revocation/deletion checks before the first production, and receipt/fee/refund conditions before a new paid commitment (`output.md:43–52,118,122,155`). Screen-lock playback remains untested and is not advertised as guaranteed (`output.md:124`). These are future gates, not claims that tool compatibility or payment infrastructure was already verified.

### Full-batch normal, latest-input, and correction paths

| Path | Full permitted cohort and remaining work | Audit result |
|---|---|---|
| Normal first/second free deliveries | Four complete inputs Tuesday noon, checked before producer handoff. Producer works Tuesday 19:00–22:00, operator checks Wednesday, Thursday remains correction/delivery margin (`output.md:60–65`). | 4×35+20=160 producer minutes fits one 180-minute shift. Four customers are not eight first-week productions; second delivery occurs two weeks later. |
| All four initial inputs require recovery | Missing fields advised Tuesday by 15:00; latest complete replacement Thursday 17:00; operator checks before 19:00. Four productions and common work use 160 minutes, followed by actual checking/delivery before Thursday 22:00 (`output.md:67–69`). | Feasible at the source durations; see explicit pipeline below. The same four orders move from Tuesday to Thursday. Earlier incomplete-input inspection/recontact may add operator effort; its exact extra amount is not measured. Do not add another four full productions or silently treat initial checking as zero. |
| Input after Thursday 17:00 or over limits | No automatic existing deadline guarantee; operator communicates effects and a feasible adjusted date. Existing free participation is not unilaterally cancelled (`output.md:71`). | This is an explicit unresolved adjustment path, not demonstrated completion on the original deadline. It preserves old rights while requiring later scheduling. |
| Included first-round corrections | Thursday October 8 result → proposed request gathering by Monday October 12 at 18:00 → producer Tuesday October 13 → delivery Wednesday October 14 (`output.md:75`). | Requests follow receipt of actual results. Four correction reserves use 40 producer/20 operator minutes. The proposed deadline is not an already-agreed expiry. |
| New paid two-bundle path | Complete input Tuesday October 13 noon → production that evening → delivery Wednesday October 14 at 18:00 → request Thursday October 15 noon → production/delivery Thursday (`output.md:77`). | Tuesday producer load with all four prior corrections, both new productions and the 20-minute common block is 40+70+20=130 minutes. New corrections consume another 20 minutes Thursday. Customer availability in the short Wednesday-to-Thursday review window is an explicit admission condition; it is not inferred from async delivery alone. |
| Included second-round corrections | October 22 result → proposed requests October 26 at 18:00 → production October 27 → revised delivery October 28 (`output.md:76`). | All four corrections use 40 producer minutes. No earlier invented expiry silently removes this entitlement. |
| Errors discovered after October 28 revisions | Reports by October 29 noon → up to four 10-minute producer fixes from 19:00, checked and delivered by 20:00 → customers able to review by 20:30 may report another up-to-four-error batch → 40 producer and 20 check minutes before 22:00 (`output.md:79`). | The explicit two-stage batch is schedulable. The second round has a 90-minute remaining window and its stated 40+20 minutes fit; delivery has remaining time. This does not imply unlimited recursive corrections or prove every participant can review within 30 minutes. |
| Final general inquiry and closeout | Last general inquiry October 30 noon → operator answer 18:00 → follow-up October 31 noon → answer 18:00. Unagreed revision expiry, late requests, or repeat audio errors requiring later producer work must secure a separate owner/date/cost; support is not marked closed without resolution (`output.md:81–83,159`). | General-message closeout has usable response windows and flexible operator availability. Remaining audio obligations after October 29 are expressly conditional; the plan does not claim that an unstaffed November producer already exists. |

**Constructive proof for the all-four latest-input batch, retaining downstream checking and delivery.** Operator input checking can occupy Thursday 17:00–18:00 (4×15). Conservatively put all 20 producer common minutes at 19:00–19:20. The four 35-minute audio productions then end at 19:55, 20:30, 21:05, and 21:40. After each output exists, operator checking plus delivery/basic questions can occupy 20 minutes: 19:55–20:15, 20:30–20:50, 21:05–21:25, and 21:40–22:00. These operator blocks do not overlap. Thus adding the source's downstream steps does not prove a deadline miss. This is an audit construction using source estimates, not an observed run of the service; the final item has no slack under this conservative placement. Customer-specific PDF preparation details and real processing speed remain to be confirmed within the proposed workflow, rather than assigned invented extra durations.

### Weekly reservation and financial reconciliation

The normal plan reserves operator minutes 360/320/300/240 against weekly 480 and producer minutes 160/150/160/60 against weekly 360 (`output.md:89–98`). Its totals reconcile:

- Ten bundles: operator baseline including one correction each is 10×40=400 minutes, plus 160 common and 660 explicitly allocated operations = 1,220.
- Producer baseline including one correction each is 10×45=450 minutes plus 80 common = 530.
- First-round correction work moves to week two; second-round correction work to week four. Week two's 150 producer minutes includes both new paid corrections as well as prior free corrections. No correction reserve was recycled as extra sales during its live obligation.
- The two additional four-error rounds on October 29 are contingency work beyond the included-correction baseline. They add 80 producer minutes, taking week four from 60 to 140, below 360. At the source's correction allowance, two additional operator batches add 40 minutes, taking 240 to 280, below 480. If fully used, those identified extra minutes alone add about 36,666.67 won at the internal valuation; other late-contact effort remains unmeasured. The output explicitly labels its table normal fulfillment, so the baseline total 530 is not an arithmetic claim that all contingencies are free.

Cash is correctly separated from valued labor: 160,000 collaboration + 40,000 tools = 200,000 committed, 100,000 reserve, zero ads; total cap 300,000 remains unchanged if money comes in (`original-input/fixtures/01-창업자-메모.md:13–18`; `output.md:100`). Direct valued labor is 40/60×15,000 + 45/60×20,000 = 25,000 won per bundle. Margins at 8,000/12,000/25,000/30,000 prices are −17,000/−13,000/0/+5,000 before shared costs. Two successful, unrefunded 12,000-won orders produce 24,000 revenue. Normal-plan economic cost is 1,220/60×15,000 + 530/60×20,000 + 40,000 = 521,666.67; the 160,000 cash collaboration payment is not added again. These are correct baseline/scenario calculations (`output.md:134–145`), not observed profitability.

### Rights, marketing, and unresolved completion

The plan distinguishes club permissions already obtained from future marketing access: first use only enables a future decision whether 별무리 forwards a notice; 느린막's October-12-onward draft review is not publication approval. Neither promises recruits, future purchase, or public examples (`original-input/fixtures/04-동아리-주고받은-내용.md:11,19,25`; `output.md:112`). A permitted individual introduction route remains to be secured; without it the new paid test remains unexecuted. That is a stated gate rather than invented channel access.

Files go only to their participant, without group-buyer access to other actors' materials. 느린막 source/working/shared files are due for deletion within seven days after the pilot, by November 8; output proposes deletion November 1 while staffed, retains aggregate-only retrospectives, disallows publicity reuse without separate consent, and does not promise remote deletion of participant downloads (`original-input/fixtures/04-동아리-주고받은-내용.md:17`; `output.md:128–130`). If support remains open, both usable support materials and the existing deletion deadline must be resolved together. The output flags that conflict rather than proving its resolution; new sales are gated, and existing obligations cannot be declared done merely because the pilot calendar ends.

### Theatre action restrictions and captured conduct

The raw request limits this task to planning and expressly prohibits app/site implementation, account creation, posting recruitment, and actual contact/payment/contracts (`original-input/request.md:9`). Runner `prompt.txt:2` additionally prohibits browsing, product/test execution, file changes, and extra model sessions. Metadata records read-only sandbox, web disabled, multi-agent disabled (`metadata.json:47–79`).

The complete eight-row captured export contains only these four calls and matching returns:

| Export lines | Call ID | Captured action |
|---|---|---|
| 1–2 | `call_x6G7uat38rqfFqe5VtC92z7e` | `pwd; rg --files input instructions/bandit` |
| 3–4 | `call_kYc22n8OckdScn863QUb6jAl` | Read request, instruction snapshot entry, and raw fixtures. Instruction text was not used as this audit's standard. |
| 5–6 | `call_OglP3t0PDwxQKbTXn8nFhMyV` | Read the routed instruction references. |
| 7–8 | `call_LMLGpuRSXxDYEttI5U0eZcKa` | In-memory arithmetic, returning the quantities listed above. |

Selected CLI command completions (`events.jsonl:6,8,10`) corroborate the three read actions; final artifact is `events.jsonl:12`. Captured tools contain no implementation, account creation, customer contact, posting, payment, contracts, product/test execution, browser/search, or subagent action. Metadata's unchanged workspace snapshots and empty violations support that bounded observation. They do not prove that all conceivable off-trace actions were impossible; the audit does not make that stronger claim. Output `:6,102,147,155,157` appropriately describes a planning artifact, actually executed arithmetic, and otherwise unexecuted verification/launch work.
