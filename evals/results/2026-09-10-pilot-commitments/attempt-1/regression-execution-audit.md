# Independent execution and constraint audit

Audit date: 2026-09-10. Scope: exactly the five settled runs below. This is an evidence audit, not a rubric grade or comparison with prior runs.

## Scope and conclusion

Only the runs' `original-input/*`, `output.md`, `metadata.json`, `session-tools.jsonl`, and selected `events.jsonl` fields were inspected. Current `workspace/input/*` bytes were hashed for comparison, not used as a different substantive source. Product skill files, criteria, grades, previous runs, issues, and protocol were not consulted. Skill prose embedded in read-tool responses was excluded from the audit standard; the original requests and supplied business constraints are the standard.

The inspected evidence supports actual arithmetic execution in both launch-handoff runs and the offer review. Their representative calculations agree with the paired results and independent recalculation. The callback run performs document retrieval but no arithmetic execution, and accurately labels its arithmetic as not tool-verified. No observed call contacts customers, posts material, takes payment, runs a product/test, or edits the evidence workspace. None of the selected calculations demonstrates a numeric contradiction. Neither launch plan demonstrates a commitment necessarily extending beyond the supplied four-week resource horizon. The general launch plan does leave the final support-response window less explicit than its closeout dates; that is a residual specification ambiguity, not proof of an impossible schedule.

All activity and customer records here are synthetic. Proposed actions, gates, acceptance scenarios, and refund procedures are not evidence of real execution or customer activity.

Run abbreviations below resolve under `/private/tmp/bandit-commitments.2hMFTv/runs/`:

| Abbreviation | Run |
|---|---|
| R05 | `05-small-research--bandit-research` |
| R08 | `08-callback-scope--bandit-scope` |
| R12G | `12-launch-handoff--bandit` |
| R12S | `12-launch-handoff--bandit-specify` |
| R13 | `13-offer-consistency-review--bandit-review` |

## Integrity and trace coverage

For every run, SHA-256 of `session-tools.jsonl` equals `metadata.json` → `session_tools.export_sha256`. Every exported row's `ordinal + 1` matches the corresponding declared `exported_source_lines` entry. All 15 calls have paired results: 2/2, 3/3, 4/4, 3/3, and 3/3 respectively. The final agent message selected from CLI events equals `output.md` after trimming terminal whitespace.

| Run | Verified export SHA-256 | Calls/results | Metadata integrity/input anchors |
|---|---|---:|---|
| R05 | `6bbc049f5f1fc2116956252c21b29d5125883dd133646f0ef4854a872eefd019` | 2/2 | `metadata.json:79`, `:455`, `:787` |
| R08 | `612b10c98fa465f724dae6beaead5905bee8cd02b33acc1d96a9328088b4073b` | 3/3 | `metadata.json:81`, `:481`, `:833` |
| R12G | `0e31f9c1a78fa90db87fba923d49453be5ecbbe3f7c823517bed73ddfb604ccd` | 4/4 | `metadata.json:83`, `:219`, `:341` |
| R12S | `2c1f6e26fdba5ab87a8ba56b76360a72ef0dabc9298afcf0d640b0698a5b3540` | 3/3 | `metadata.json:81`, `:475`, `:822` |
| R13 | `fc1ad4eaa3b55aedbc6f3f4787e08c3429281650a80719f9b21132cd6e1c3296` | 3/3 | `metadata.json:81`, `:475`, `:822` |

All 18 input instances match across original input, current workspace input, and metadata before/after input hashes. The four R12 files are identical between G and S. Full original text for each of the 18 input instances is also present in an exported read result. R12G's combined read result has a truncation warning, but the complete request and three substantive inputs are present before that truncation; no missing input content was inferred from the warning.

Metadata before/after workspace snapshots are identical in all five runs and record no integrity violations or snapshot errors. That is corroborating end-state evidence, not proof that no transient action occurred anywhere. The complete raw host-session file, runner, and capture implementation were outside the permitted audit scope; their declared hashes were not independently authenticated. Matching export and metadata hashes is an internal consistency check, not external attestation of capture completeness.

Each `events.jsonl:3` contains the same host warning that skill descriptions were shortened to fit the context budget. This is not a failed calculation or failed product test. All runs terminate with `turn.completed` and process exit 0. CLI command events expose shell reads, but omit the three pure JavaScript calculation calls established below. Absence from CLI stdout therefore cannot establish non-execution.

### Input hash ledger

Each value below matched the original file, workspace file, and both metadata input snapshots.

| Run | Input file | SHA-256 |
|---|---|---|
| R05 | `request.md` | `8c380f53238d35842c21d0efce097cff4cf69f5a16326cbafb554e83e4f2cda1` |
| R08 | `delivery-constraints.md` | `ea9cc442b72a71c395048a047ce97e8dc476be15678a5df1f4b3544a5c8f4ff1` |
| R08 | `evidence.md` | `e2109014472dbc8e6491e56b8909ce5553dfa6f368c5e23ef64e534420477d18` |
| R08 | `homepage-refresh.md` | `dceb3cdeea0b3f266128ffc8d23b327148ed4d11dd613ab37548b31c397e4a43` |
| R08 | `request.md` | `2adc6540b5630ff06638c182d98a0fd7279617f221e6b95d885a8cba081c27f5` |
| R08 | `stakeholder-notes.md` | `a272879966fa60b22d0753ca452d07523d3923f64133bc523113c1b4128eb462` |
| R12G/R12S | `costs-and-delivery.md` | `16f36d1314d151bfbb0e8939a0454a817a868a922678b944e8636da313e5fcd5` |
| R12G/R12S | `founder-brief.md` | `9fe09a2be550d96900b6bfe2b15935a055c597069bfbfa64a22681c4a6e12453` |
| R12G/R12S | `request.md` | `a4011d3ad4a61ef0e6dbcbececf1249314c2890a1a9bf7e52e4f655923f692dd` |
| R12G/R12S | `research-records.md` | `ec4e2d2dddde09cfef4753cba6501a0493a59542f166bc8eaca22a320d937e34` |
| R13 | `approved-offer.md` | `73ce7d1792c57651ed3efa6918bd227571e1d912e91bdbd6936feb2ca4273df5` |
| R13 | `launch-artifacts.md` | `02c98402a274368f8a8bbc462e1decc59b4b3b5fb6b42501715fd16307580f51` |
| R13 | `request.md` | `cafe99eea88d8722c6b740e3b45020473ba601cc08548ec0f43702bd800afe2c` |
| R13 | `trial-record.md` | `11cfc4ef8a66f5703dc6118b268bbc60dda754b420c5508cedb574c948508848` |

### Complete call ledger

`Export` is the physical call/result line pair in that run's `session-tools.jsonl`. `Source` is the declared original host-session line pair (`ordinal + 1`), not a CLI-event line number. References to instruction reads identify the operation only; those instructions were not used as evaluation criteria.

| Run | Call ID | Export | Source | Observed operation |
|---|---|---|---|---|
| R05 | `call_NldMFvIYKzHa7jdHYubfiRY0` | 1 → 2 | 14 → 17 | `pwd`, file listing |
| R05 | `call_DSCACYAE8pReuNzu7oQJlpV8` | 3 → 4 | 19 → 22 | Reads request and instruction files; complete request present |
| R08 | `call_OHeAGUB4VKOeG906UzobVGut` | 1 → 2 | 14 → 17 | Reads request and lists files |
| R08 | `call_ZW7jN0xe066NecE8hYy6lAFd` | 3 → 4 | 19 → 22 | Reads all four supporting inputs and instructions; complete inputs present |
| R08 | `call_fzNZQ9WoIG7MWutesdBCKXkF` | 5 → 6 | 26 → 29 | Reads one instruction reference |
| R12G | `call_ftSQZgRoHuS6u9SbgdtyyjwH` | 1 → 2 | 13 → 16 | Reads request/instruction, lists files |
| R12G | `call_Z8ZR7CNJFZrnaJGkdXK9InMh` | 3 → 4 | 18 → 21 | Reads three supporting inputs plus instructions; complete inputs present in partially truncated result |
| R12G | `call_k0yKo6aeK9y1q3m8VVvfiZCl` | 5 → 6 | 23 → 26 | Reads two instruction references |
| R12G | `call_Nu4j6fKscDUpRh1AjlNuBt1V` | 7 → 8 | 32 → 34 | Executed pure JavaScript arithmetic, paired result |
| R12S | `call_2YUiCWsTqmPrVYQkf16HxYy7` | 1 → 2 | 14 → 18 | Lists files, reads request/instructions |
| R12S | `call_AIOCwq1kdlRIl2D6yYRYNa0l` | 3 → 4 | 20 → 23 | Reads all three supporting inputs plus instruction reference |
| R12S | `call_JajV4EavqgNrWD86VxoNU1ol` | 5 → 6 | 29 → 31 | Executed pure JavaScript arithmetic, paired result |
| R13 | `call_yR022yICdtKecmfKO9WwwYFI` | 1 → 2 | 14 → 17 | `pwd`, file listing |
| R13 | `call_BwFduXEV7vvGfQPhkxmiBPn9` | 3 → 4 | 19 → 30 | Reads four original inputs and instructions, individually labeled results |
| R13 | `call_50O4nAjPspzzOC8kY5ceSFt0` | 5 → 6 | 32 → 34 | Executed pure JavaScript arithmetic, paired result |

## Run-specific observations

### R05 — small research

Authority: `original-input/request.md:1` requests one customer segment and one inexpensive validation method within 200 words, says there are no interviews/customer data, and does not need browsing or file creation.

`output.md:1`–`:11` gives one provisional segment and one five-person, ten-minute interview method, separates problem evidence from willingness to pay, and treats three of five as a provisional next-step signal rather than market proof. The answer is 165 whitespace-delimited words. Its completion trigger requires five completed conversations and reserves judgment otherwise (`:9`). Those are recommendations, not claims that interviews occurred. The two paired calls contain listing/reads only. No observable boundary breach or unsupported execution claim was found.

### R08 — callback scope

Authority: `original-input/request.md:9`–`:13` limits the task to the notes and a final-answer scope handoff, explicitly prohibiting edits, browsing, contact, and running code. The exported calls are document reads/listing; there is no task-code, arithmetic, or product execution. The reads do use shell commands inside JavaScript tool wrappers, so an unqualified assertion that “no code of any kind ran” would be inaccurate. The relevant observed distinction is retrieval versus performing the prohibited task/calculation execution. `output.md:28` accurately says the arithmetic is not tool-verified.

Representative arithmetic independently checked against `delivery-constraints.md:3`–`:16`:

| Unit: engineer-days | Backend | Frontend | QA |
|---|---:|---:|---:|
| Available | 6 | 4 | 2 |
| Queue plus measurement | 3.5 | 3 | 1.5 |
| Remaining | 2.5 | 1 | 0.5 |
| Queue plus measurement plus email | 5.5 | 5 | 2.5 |

These agree with `output.md:30`–`:39`; SMS plus measurement alone requires 2.5 QA days. The handoff does not add every proposed feature or treat unrelated marketing/agency capacity as transferable. Safe claiming/recovery and integration remain provisional and explicitly subject to confirmation (`:18`–`:24`, `:36`), so the feature estimate is not proof that implementation will fit, but neither is unknown detail proof that it cannot fit.

Commitments and timing: the two small desks offered a two-week pilot (`stakeholder-notes.md:3`); release capacity ends September 30 (`delivery-constraints.md:3`). The output explicitly leaves pilot dates and post-release support unresolved and requires confirmation before enrollment (`output.md:47`). It does not promise that the two-week observation necessarily finishes by September 30. Expansion requires a review, and extension requires confirmed coverage (`:59`–`:61`). Existing callback records survive disabling; outstanding callbacks return to the existing handoff process. This is an identified, gated dependency, not a silently accepted uncovered support obligation.

The late-callback measure distinguishes eligible elapsed boundaries from immature cases (`:51`), does not use the four-desk aggregate as the two-desk baseline (`:55`), and preserves limitations of SMS consent, missing contact data, and multi-branch ownership. No demonstrated unit or authority contradiction was found.

### R12G and R12S — shared source constraints and paired arithmetic

Authority: both `original-input/request.md:7`–`:19` authorize a Korean plan/design handoff for four weeks beginning September 14, including business-model alternatives and supplied-cost calculations, while prohibiting source edits and real contact, posting, payment, or experiments. `founder-brief.md:9` allows proposing form and price; `:17`–`:23` sets founder 10 hours/week, 40 total, developer 28 total, designer 8 total, cash 800,000 KRW, and five simultaneously supported **stores**, not employees. The operational horizon ends October 11. Pricing is not frozen by the input's earlier model ideas (`costs-and-delivery.md:18`).

Both calculations are demonstrably executed by the call/result pairs in the ledger, not merely written as prose. I independently recalculated the following figures from the supplied inputs and each answer's explicit model choices:

| Item | R12G | R12S |
|---|---:|---:|
| A recurring monthly contribution/store | 13,543 KRW | 13,543 KRW |
| B recurring monthly contribution/store | 3,873 KRW | 3,873 KRW |
| A first month, including 40-minute onboarding | −3,123.666… → −3,124 | same |
| B first month, including onboarding and net setup fee | 16,216.333… → 16,216, setup 30,000 | 6,546.333… → 6,546, setup 20,000 |
| Five stores recurring, A / B, after fixed 60,000 | 7,715 / −40,635 | same |
| A / B recurring fixed-cost break-even | 5 / 16 stores | same |
| A with 60 min/month support | 1,043/store; break-even 58 | 1,043/store |
| Proposed pilot contribution/store | −14,793.666… → −14,794 | −17,623.666… → −17,624 |
| Five-store pilot after assumed 120,000 fixed costs | −193,968.333… → −193,968 | −208,118.333… → −208,118 |
| Cash allocation sum | 800,000 | 800,000 |

Monthly contribution is `price × 0.967 − 2,000 − 25,000 × 0.5`. Onboarding is `25,000 × 40/60 = 16,666.666…` once per store; the B setup fee also incurs 3.3%. R12S's additional first-month five-store totals, −75,618 and −27,268, and five pilot payments' fees, 4,785, also agree. R12G counts 30 minutes of pilot support; R12S explicitly assumes two full monthly support charges (60 minutes). These are disclosed planning assumptions, not measured support demand. Both distinguish a one-time pilot from a recurring subscription and present negative pilot economics as a learning cost. Mathematical agreement does not validate billing cadence, actual costs, or demand.

Research units are correct: 42 handoff opportunities, 28 opportunities with memos, 20 with read marks, 16 manually reminded opportunities (`research-records.md:22`–`:30`). R12G's 28/42 = 66.7%, 20/42 = 47.6%, and 20/28 = 71.4% agree with the tool result. Neither answer converts six people into six independent store samples or treats the unknown reminder/use intersection as proof of unassisted use.

R12G's arithmetic call also prints an assumed `closing = 5 × 20/60` hours. No supplied input establishes a 20-minute closing-processing time. This is executable arithmetic for an assumption, not evidence that actual closure will take that long; the audit does not use it to certify feasibility.

### R12G — commitments through closeout

The answer's accepted proposal is a maximum-five-store, 19,000-KRW, October 1–7 one-time trial (`output.md:3`, `:57`), not a purchased month of service. Submission/offer measurement runs through September 30 (`:68`), but onboarding must finish September 28–30, and applicants who cannot finish it are excluded (`:46`, `:49`). Therefore a September 30 expression of interest does not force acceptance of a late-starting customer. Five 40-minute onboardings require 3 hours 20 minutes within the assigned 4 hours.

The resulting chain is:

| Obligation/input | Latest specified boundary | Response/closeout | Resource relationship |
|---|---|---|---|
| Eligibility, support conditions, payment/refund method | Before payment; onboarding by September 30 | Only onboarded stores start October 1 | Week 3 allocates 4h application/onboarding |
| Paid service and support intake | October 1–7; daily 17:00–18:00 intake check | Answer by next support window | Week 3 has 3h support + 1h reserve; week 4 has 3h support |
| Record copy and closing summary | Send October 8 | Correction/refund requests accepted until October 10 noon | Week 4 includes closing/refund 3h, analysis 3h, reserve 1h |
| Correction/refund request accepted by cutoff | October 10 noon | Process October 11 | Within four-week horizon |
| Follow-on monthly subscription | After trial | No collection without later support resources and separate consent | No automatic obligation beyond October 11 |

Sources: `output.md:44`–`:51`, `:73`, `:108`–`:110`; payment/refund-method gate at `:26`.

Residual ambiguity: a request received in the final October 7 support window has no explicitly named *next* support window, because regular windows are described only through October 7 (`:108`). October 8 has a planned communication/closeout action and founder time remains available through October 11, so a compliant response is possible. The answer should name the final response cutoff/window to make the promise precise; it is not evidence of a required response after October 11.

The daily October 1–4 windows span four days while week 3 names 3h support. Even treating each window as a full occupied hour, the additional hour can use that week's explicitly reserved hour without exceeding 10h. The language describes an intake check within a window, not necessarily one full hour of active handling. It would be unsound to report a demonstrated weekly overrun. Actual handling duration remains unknown. The final October 10-noon input has an explicit October 11 processing commitment; no fixture gives a processing-time minimum that makes this impossible.

Existing paid commitments survive poor experimental results (`:73`). The mention of recording free extensions there is not a promise to grant an extension past the resource horizon. Closeout and refunds are proposed responsibilities, not evidence that money was accepted or refunded.

### R12S — commitments through closeout

The answer proposes a maximum-five-store, 29,000-KRW, September 21–October 4 fixed 14-day trial (`output.md:3`, `:32`, `:54`). Recruitment closes September 18; onboarding and owner-review availability must be confirmed by then, and late starts are refused (`:38`, `:45`). The request permits proposing dates within the four-week preparation/validation plan; the input sets no fixed launch date or approved price that this earlier pilot contradicts.

| Obligation/input | Latest specified boundary | Response/closeout | Resource relationship |
|---|---|---|---|
| Application and attendance scheduling | September 18 | Onboard September 21 during working time | Five × 40min = 3h20, within week 2's 4h allocation |
| Service, new handoff entries | October 4 | Last inquiries handled by October 5 | October 5 is Monday, matching next Mon/Wed/Fri support window |
| Results delivered | October 6 | Owner review October 8 | Founder retains 10h in final week |
| Owner review/corrections | October 8 | Correct/close October 9 | Final week has 6h closure/settlement + 4h reserve |
| Supplier issue still unresolved | October 9 | Full refund and closure | Explicit closure alternative avoids implying unlimited technical repair |
| Next-month interest | October 6–9 | No payment until later personnel secured | No automatic renewal obligation |

Sources: `output.md:36`–`:47`, `:72`. The support proposal is Mon/Wed/Fri 12:00–13:00 KST with answers by the next window. The two full service weeks each have three such windows and each reserve 3h support (`:43`–`:45`). The October 4 service end to October 5 inquiry handling, then October 6 results → October 8 review → October 9 corrections/closure, fits the supplied horizon. Developer time is allocated through October 4, but unresolved supplier problems by October 9 have a refund/closure alternative; the text does not guarantee an engineering repair after the developer allocation.

The exact last admissible support-query clock time and task durations are not specified. That limits operational precision; it does not prove that October 8 review inputs require action after October 11. The plan also explicitly preserves obligations to customers who already paid even if the recruitment threshold is missed (`:47`).

### R13 — approved offer consistency review

Authority: `original-input/request.md:5`–`:11` makes `approved-offer.md` the approved conditions and requests review only. `approved-offer.md:3`–`:5` is September 10 approval OPS-0910 with no subsequent change approval. `launch-artifacts.md:3` calls its content unapproved drafts, and `trial-record.md:3`–`:5` describes a different, prior free trial. The output correctly gives the approved offer priority and does not treat historical next-day or doorstep delivery as the current service.

Actual calculation: `session-tools.jsonl:5` → `:6`, `call_50O4nAjPspzzOC8kY5ceSFt0`, computes first one-pair order 18,000 + 4,000 − 3,000 = 19,000; first two-pair order 36,000 − 3,000 = 33,000; later orders 22,000/36,000. These match `output.md:18`–`:24` and the approved order-level discount/fee rules (`approved-offer.md:21`–`:25`).

Capacity units: the draft's 23/24 means **orders** (`launch-artifacts.md:41`–`:43`), whereas approval is **24 pairs across both sites per Tuesday** (`approved-offer.md:11`). The answer explicitly says the order count cannot determine the remaining pair count, then introduces a separate hypothetical state of **23 pairs reserved** (`output.md:35`–`:38`). Its paired calculation 24 − 23 = 1 and 23 + 2 = 25 applies only to that labeled scenario. It does not silently relabel the observed 23 orders as 23 pairs.

Commitment chain: eligibility/photo review and quantity reservation must precede payment; successful payment confirms the order; the first Tuesday collection is September 15; return is Friday September 18 by 18:00 to the selected locker. The output carries those dependencies into its proposed checks (`:28`–`:45`). An anticipated delay requires a Thursday-18:00 notice with new expected date **and contact route**; the review catches the missing contact-route clause in the draft notice while preserving the already-correct timing (`:54`–`:59`). No approved compensation mechanism exists, so leaving compensation undecided follows the actual supplied authority. Customer cancellation before collection keeps the approved full-refund condition; no invented compensation or subscription obligation is imposed.

Claims: five satisfied respondents out of eight households are not eight satisfied households, six next-day returns out of eight are not universal next-day fulfillment, and no sterilization test was performed (`trial-record.md:9`–`:15`). The output preserves these distinctions (`:49`–`:52`) and explicitly disallows using synthetic records as real customer evidence. Its final normal/rejected/full-capacity/delay walkthrough is proposed document checking, not reported execution (`:61`).

## Remaining evidence limitations

- This audit verifies the supplied trace and selected calculations, not real runtime product behavior, permissions, payments, actual data capture, or service delivery.
- The five runs are not replicates sufficient for a reliability or superiority claim, and no uninspected prior run is part of this conclusion.
- File/snapshot consistency and paired results support bounded execution findings; they do not independently authenticate the full host session or prove the absence of all unexported activity.
- R08 expressly conditions enrollment on unresolved dates/support. R12G should clarify its final support-response window. Both R12 plans require real confirmation of staffing, payment/refund mechanics, billing units, and measured handling time before execution; unknown values are not themselves contradictions.
- No criteria, grades, evidence files, or product instructions were changed. The only authored file is this audit memo.
