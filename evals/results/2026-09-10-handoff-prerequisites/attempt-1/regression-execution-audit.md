# Independent execution and claim audit

Scope: the five settled runs listed below. This audit used their `original-input/**`, `output.md`, `metadata.json`, `session-tools.jsonl`, and selected CLI events. `workspace/input/**` was read only to compute hashes. No skill text, grading criteria, previous diagnoses, product implementation, or tests were used as an assessment standard. No supplied product code or tests were executed; no external action was taken. Independent audit calculations are identified separately from calculations performed by the original agents.

Run abbreviations used in evidence references:

- **R05**: `runs/05-small-research--bandit-research/`
- **R08**: `runs/08-callback-scope--bandit-scope/`
- **L-general**: `runs/12-launch-handoff--bandit/`
- **L-specify**: `runs/12-launch-handoff--bandit-specify/`
- **R13**: `runs/13-offer-consistency-review--bandit-review/`

All references below are relative to `/private/tmp/bandit-prerequisites.4VHSx8/`. Line numbers are physical lines in the named file. For tool pairs, `7 → 8` means call on export line 7 and matching result on export line 8, joined by `call_id`.

## Findings

The preserved evidence supports the agents' limited execution claims. All 18 input-file occurrences match their original, workspace, and before/after metadata hashes. All five tool-export hashes match. Each of the 15 exported wrapper calls has a corresponding result. No captured action changed input files, ran supplied product code/tests, contacted customers, posted material, or made a payment. The metadata workspace snapshots contain no changed entries.

The principal remaining planning uncertainties are in L-general's final-week resource reconciliation and the timing of its final record-copy handoff. Neither proves the proposed service is impossible. The document does not specify the overlap needed to fit its offered support windows into the eight-hour support allocation, or a copy-delivery deadline preceding the last accepted closeout inquiry. L-specify explicitly schedules copy delivery before its error-report deadline. Both runs have viable stated paths for the latest eligible applicant, and both keep the purchased service within the four-week horizon.

Two actual execution/calculation errors in L-general were recovered before the final answer: a mistyped file name failed, followed by a successful read; an initial budget remainder used a different allocation total, followed by a correct recomputation. These are recorded below, without treating them as unrepaired final-output errors. The final published financial values checked here are arithmetically correct under the supplied assumptions.

### 1. L-general: final-week hours need reconciliation, not an assumed overload verdict

`output.md:39` allocates two hours to evaluation/settlement and eight to final inquiries, corrections, and closeout. `output.md:52` also offers recurring Monday/Wednesday/Friday 16–17 support. The special final-week windows at `output.md:53` yield:

| Date | Distinct offered window | Hours |
|---|---|---:|
| Monday 10/5 | 16–17 | 1 |
| Wednesday 10/7 | 16–17 | 1 |
| Friday 10/9 | 15–17, including the regular 16–17 window | 2 |
| Saturday 10/10 | 15–17 | 2 |
| Sunday 10/11 | 15–17 and 17–19 | 4 |
| Total | No double counting of Friday's overlap | 10 |

The raw founder constraint is at most ten working hours each week, forty overall (`original-input/founder-brief.md:17`). Ten offered availability hours are not proof of ten hours of active service work: evaluation might occur during idle portions, and response durations/customer demand are unknown. It would therefore be unsupported to declare twelve hours of unavoidable work or an impossible launch. The narrower defect is that the claimed eight-hour final support allocation and the ten-hour set of windows are not reconciled. A reviewable plan should state whether evaluation shares idle support windows, the priority when inquiries arrive, and what work the eight-hour allowance actually covers.

The original arithmetic calls verify the sum of the table's hour allocations; they do not calculate these calendar windows or demonstrate the required overlap. `output.md:41` should not be treated as a worked schedule proof.

### 2. L-general: final record-copy delivery is not placed before the closeout cutoff

`output.md:53` accepts access/closeout inquiries until 10/11 17:00 and processes them 17–19. `output.md:55` promises a record copy before the 10/11 end and then access termination, without a latest delivery time for that copy. A copy delivered after 17:00 would meet the stated delivery wording but give the customer no stated way to report a copy problem before the accepted-inquiry cutoff. This is an underspecified prerequisite, not evidence that the copy was actually delivered late or that the schedule cannot be made feasible.

Minimum clarification: place copy delivery and customer access verification before the 17:00 cutoff, then use the existing 17–19 recovery window for accepted defects. The ordinary inquiry/reply/correction path is already scheduled; it does not need to be invented again. L-specify's `output.md:45` gives the stronger explicit ordering: copy at noon, errors by 15:00, correction/final notice by 18:00.

## Execution boundaries and recorded errors

| Run | Original authorized work | Observed actions and matching final claim |
|---|---|---|
| R05 | Choose one customer group and one cheap validation method in at most 200 words; no external search/file creation needed (`original-input/request.md:1`). | File discovery/read only. Final proposes interviews, explicitly labels missing evidence, and contains 166 whitespace-delimited words. No arithmetic-verification claim. |
| R08 | Scope handoff from the supplied notes; do not edit, browse, contact, or run code (`original-input/request.md:9–13`). | File reads only; no arithmetic script or product execution. `output.md:38` explicitly says its arithmetic is not tool-verified because code execution was prohibited. Using the host's wrapper to read files is not evidence of executing a product or calculation program. |
| L-general | Korean plan/design handoff only; no original-file edits, customer contact, posting, payments, or actual experiments (`original-input/request.md:7–19`). | File reads plus two standalone arithmetic calls. `output.md:5` and `:97` distinguish proposal/planned verification from execution. No captured forbidden action. |
| L-specify | Same original request and fixtures as L-general, independently hash-matched. | File reads plus one standalone arithmetic call. `output.md:87`, `:117`, and `:126` state that tests/actions are proposed, not completed. No captured forbidden action. |
| R13 | Review consistency only; do not edit, contact, or perform applications/payments (`original-input/request.md:7–11`). | Reads and standalone Python arithmetic only. `output.md:63` says no product-code/test execution or external verification; that is consistent with the trace. Arithmetic was not prohibited by this request. |

All runs have metadata process exit code 0, `integrity_status: passed`, empty `violations`, and no snapshot errors. Metadata evidence: R05 `metadata.json:455`, R08 `:479`, L-general `:221`, L-specify/R13 `:475`. This audit independently rehashed input and export files; broader workspace immutability is supported by the recorded before/after snapshot comparison, not by a new unrestricted filesystem inspection.

Four CLI event streams contain an `item.type = error` notification at `events.jsonl:3`: R05, R08, L-specify, and R13. The message says skill descriptions were shortened to fit the context budget. These are host context-budget notices, not failed product execution, and the turns complete. No substantive finding here relies on the skill descriptions.

L-general has one actual failed shell read: `call_VHljPbrbTkwkC66B4NfIsMhr`, `session-tools.jsonl:3 → 4`, attempts `instructions/bandit/SILL.md` alongside the four inputs; that command exits 1. A second command in the same wrapper reads `instructions/bandit/SKILL.md` and exits 0. CLI events `:7` and `:9` confirm failure then success. The input material had been emitted before the typo error. The corrected read is sufficient evidence of recovery; the failed attempt must not be silently counted as a successful single command.

## Actual arithmetic calls and what they prove

CLI events are incomplete tool telemetry. In particular, L-general's two standalone arithmetic calls do not appear as shell command events, but their call/result records exist in the hash-verified session export. Absence from CLI stdout is not evidence of absent execution.

| Run | Call ID and export lines | Actual computation/result | Limit |
|---|---|---|---|
| L-general | `call_PtUKBJjF5cdrXvEFkewbIqnj`, `7 → 8` (recorded source lines 33 → 35) | Price/fee/margin calculations, first-period onboarding, five-store economics, break-even counts, evidence ratios, support sensitivity, budget sum, and five-store labor minutes. Result includes A monthly 13,543; A first −3,123.6667; A five first −75,618.3333; B monthly 3,873; setup net 19,340; B five first −27,268.3333; budget 520,000. | Its `remaining` expression is `800000-620000`, returning 180,000 despite its separate allocation sum being 520,000. This was an actual inconsistent intermediate calculation. |
| L-general | `call_NCMeIkz4xYk4iRwBXOqSnsfu`, `9 → 10` (source 39 → 41) | Recomputes allocation 520,000 and remainder 280,000 from the same terms; B first contribution 6,546.3333; five-store cash margin 70,215; founder hours 40; developer 28; designer 8. | Corrects the earlier remainder; final `output.md:114` uses the corrected value. The hour sums check allocation totals only, not the actual work calendar. |
| L-specify | `call_y21KwQV4e2jGSceFdn6ldp1V`, `5 → 6` (source 29 → 32) | Calculates price/fee/margins for 29,000, 19,000, and 39,000, break-even 5/16, cash 70,215, budget 800,000, evidence ratios, and 15/30/60-minute support sensitivity. Using 39,000 for B's first combined setup/month payment is arithmetically equivalent under the fixture's purely proportional 3.3% fee. | `founderHours:[10,10,10,10]` is a literal array, not a derivation or sum. This call does not calculate developer/designer totals or service calendar dates. |
| R13 | `call_Nal4g0CkFpweYO7NzTTh6QsV`, `5 → 6` (source 34 → 38) | Runs standalone `python3 -c` arithmetic; paired shell result exits 0 and returns first-one 19,000, first-two 33,000, repeat-one 22,000, repeat-two 36,000, remaining-if-23-pairs 1, and 23-pairs-plus-two 25. | This verifies arithmetic, not implemented pricing/capacity behavior. Its conditional variable names correctly use pairs, not the draft's existing 23 orders. |

R05 and R08 have no standalone arithmetic calls in their complete exported call/result sets. Neither falsely claims they do. The audit independently checked R08's retained totals (3.5 backend, 3 frontend, 1.5 QA), remaining capacities (2.5/1/0.5), and weekly-email add-on (5.5/5/2.5), confirming that the add-on exceeds frontend and QA capacity. The input's separate feature-estimate rule is respected (`R08/original-input/delivery-constraints.md:3–17`; `output.md:31–42`).

Independent arithmetic and calendar checks confirm the following final claims:

- Free-use opportunities: 14+12+16 = 42; memos 11+5+12 = 28; reads 8+2+10 = 20; manual reminders 5+4+7 = 16. Thus 28/42 = 66.7%, 20/42 = 47.6%, 20/28 = 71.4%. Both launch runs retain the correct denominators and do not infer an effect from absent reminder cross-tabs or a missing baseline (`research-records.md:20–32`).
- Monthly support costs 0.5 × 25,000 = 12,500; onboarding costs 40/60 × 25,000 = 16,666.6667. A gives monthly 13,543 and first −3,123.6667 per store; B gives monthly 3,873 and first 6,546.3333 after the fee-adjusted setup charge. Five-store first totals after fixed 60,000 are −75,618.3333 and −27,268.3333. Final rounding is correct. The arithmetic retains full monthly cost assumptions for the shorter pilot, rather than treating a shorter offer as measured savings.
- A's and B's recurring fixed-cost break-even counts are 5 and 16; the latter exceeds the supplied five-store simultaneous-support limit. The comparison is under unverified supplied estimates, not evidence of profitable operation or demand. Both runs say so.
- The inclusive planning period 9/14–10/11 has 28 days. L-general's 9/21–10/11 offer has 21 days; L-specify's 9/28–10/11 offer has 14 days. Those are feasible distinct proposed schedules, not an inconsistency between runs. Weekdays used in the review and final-week windows are correct: 9/15 is Tuesday, 9/18 Friday, 10/9 Friday, 10/10 Saturday, and 10/11 Sunday. These date checks were performed by the auditor, not shown as original-agent calendar calls.

## Latest eligible customer and recovery-path traces

### L-general

The raw fixtures grant forty founder hours, twenty-eight developer hours, eight designer hours, and at most five directly supported stores; they do not prohibit weekend work or prescribe fixed founder office hours (`founder-brief.md:15–23`). The plan itself proposes the specific response windows. Weekend milestones therefore are not an independent contradiction.

1. The last eligible store provides owner approval, employee count, shifts, on-shift access, and onboarding availability by Friday 9/18 noon (`output.md:49`). Missing material is requested by 15:00 and can arrive by Saturday 9/19 noon (`:50`). A customer unable to attend the stipulated times is excluded. The 9/17 feasibility decision and disclosed manual fallback precede payment (`:32`, `:41`).
2. That store can be explained/onboarded Saturday afternoon, use one of the two Sunday-morning supplementation slots, then receive the Sunday 15–17 first-result/access check and pay by 18:00 (`:50–51`). Five forty-minute onboardings total 200 minutes, within the four-hour onboarding allocation. Durations for recruitment, individualized amendments, and supplementation are not known; this establishes a feasible ordering, not actual demonstrated throughput for five customers with every possible defect.
3. Service begins 9/21 and ends 10/11. It includes the record space, next-shift read acknowledgment, owner date view, onboarding, and restricted support (`:30`). Web and manual alternatives are conditional on fulfilling the same offered functions/access isolation and being disclosed before payment (`:32`). No customers are automatically enrolled beyond five, and no late intake is accepted.
4. A latest ordinary query accepted Friday 10/9 noon has a reply 15–17; its correction request is accepted Saturday noon and handled 15–17; its follow-up is accepted Sunday noon and handled 15–17 (`:53`). The final access/closeout branch accepts requests until Sunday 17:00 and has 17–19 handling. This explicitly handles the last accepted ordinary reply/correction/follow-up chain inside the four weeks. It does not promise an unlimited additional feedback cycle after every final answer.
5. Pre-start cancellation/non-provision receives a full refund; post-start cancellation uses remaining service days/21, with provision through the refund date; repeated failures/overload trigger manual recovery or a refund for unprovided time (`:54`). Already-paid obligations survive a weak experiment result (`:71`). These are policy proposals, not actual refunds. They leave time-to-repair and workload unmeasured.
6. Record copy and access termination are promised by the final date; sales of further support/renewal are barred without separately secured staff (`:55`). The missing copy-before-inquiry-cutoff dependency and hour-reconciliation issue are the qualified findings above. No later paid month is silently assumed to be staffed.

### L-specify

1. The provision method, final payment amount/method, and participation times are to be settled by 9/24 (`output.md:41`, `:58`, `:126`). The latest completed application/material correction is Friday 9/25 18:00, followed by eligibility/payment by Sunday 9/27 18:00 (`:43`). These dates give a prospective customer time to receive the final method and conditions before payment; the document does not claim that any payment setup has actually been implemented.
2. On-shift onboarding is booked before payment; stores without a person available for final checking/support are excluded (`:43–45`). Onboarding starts the week of 9/28, with four founder hours allocated. Five forty-minute sessions total 3h20, so a latest fifth customer can fit a booked start-day schedule. The plan's phrase “14-day service” does not imply 24-hour emergency service: restricted support is included in the offer (`:54`). Actual customer shifts and bookings remain prospective.
3. Paid delivery runs 9/28–10/11, fourteen inclusive days, and contains the same core record/read/owner-view journey and an end-of-service copy (`:30`, `:54`). The monthly alternatives explicitly do not create commitments after 10/11 (`:95`, `:97`). Manual provision is gated on access separation/read semantics and disclosed before payment (`:41`).
4. A last ordinary inquiry arrives Friday 10/9 noon, is answered 16–17, and may generate a follow-up accepted Saturday noon and handled Saturday 16–17. The copy is delivered Sunday noon; errors are accepted until 15:00; fixes and final guidance finish by 18:00 (`:45`). The copy precedes its error-report deadline. There is no need to substitute L-general's different 21-day schedule when assessing this chain.
5. When capacity is exceeded, new intake stops; existing stores are informed. If the promised service cannot be recovered, the proposed fallback is a full refund and record copy (`:47`). Already accepted obligations survive failed experiment criteria. Before-start cancellation/non-provision is also covered (`:43`). The exact effort for individual export/repair/refund cases is unknown; no raw input proves that all reserve time will be exhausted.
6. The table assigns final-week support 3h, copy/closeout 3h, analysis 2h, and recovery 2h (`:39`). The recurring weekday windows consume three offered hours; the Saturday follow-up can use the closeout/recovery allocations. Copy-processing duration is not given, so a feasible allocation exists but capacity under arbitrary simultaneous defects is not proven. No required original-agent script actually derives these calendar tasks from the literal founder-hour array.

## Review findings versus implementation evidence

R13 correctly uses the operations approval as authoritative and identifies the launch documents as unapproved drafts (`output.md:3`; `original-input/launch-artifacts.md:3`; `approved-offer.md:5`). Wording such as “can proceed to payment” describes the behavior specified by a draft, not a reproduced deployed-system defect. The proposed acceptance checks are not evidence that they were executed.

The material proposed corrections are grounded in the raw approval:

- Region/collection: only the two approved compounds' registered lockers, versus national/doorstep advertising and the “other” address branch (`output.md:7–12`; approval `:9`).
- Return deadline: Tuesday collection to Friday 18:00, versus next-day/24-hour claims; the first September 15/18 dates are calendar-correct (`output.md:14–19`; approval `:29`).
- Price and unit: one order-level 3,000 discount and one-order 4,000 transport fee, waived for two pairs; all four displayed totals are correct and the VAT-inclusive basis is preserved (`output.md:21–34`; approval `:21–25`).
- Capacity: twenty-four actual pairs across both compounds, not twenty-four orders. The review's twenty-three-single-pair-orders example is explicitly conditional and correctly yields twenty-five pairs when two are added. It does not pretend the draft's twenty-three orders are known to contain only twenty-three pairs (`output.md:36–41`; draft `:41–43`). It includes the no-available-slot exit.
- Payment prerequisites: material/state verification and capacity reservation occur before charging/confirmation, with pending/ineligible paths unable to charge (`output.md:43–48`; approval `:15`, `:25`). This is a requested draft repair, not a successful payment integration test.
- Evidence claims: five satisfaction respondents out of eight households do not mean all eight were satisfied; six of eight returned the following day do not support universal next-day delivery; no sterilization test supports 99.9% (`output.md:17`, `:50–55`; trial `:9–15`). Synthetic evidence remains labeled.
- Matching parts are retained. “Two or more pairs free transport” is only optionally narrowed because the current draft already caps orders at two. Missing approval of delay compensation is treated as an unresolved decision, not an invented defect requiring a new guarantee; the missing inquiry channel in the delay notice is correctly added (`output.md:59–61`).

The callback scope similarly labels existing completion/contact-correction/ownership-change paths as dependencies to confirm, not working implementation (`R08/output.md:25`). It includes lost-claim recovery, missing contacts, load failures, controlled enrollment, record-preserving disablement, and a manual fallback. Its baseline distinguishes the selected desks from the four-desk convenience sample, uses matured promised-time denominators including outstanding late records, and leaves the worthwhile improvement threshold unresolved (`:47–53`). No actual queue performance or business validation follows from this plan.

## Integrity evidence

Each hash below was recomputed from the allowed files. Every input hash matches `metadata.input_sha256`, `metadata.input_after_sha256`, the original file, and its workspace input counterpart. The two launch runs' four fixtures match one another as well.

| Run(s) | Input file | SHA-256 |
|---|---|---|
| R05 | request.md | `8c380f53238d35842c21d0efce097cff4cf69f5a16326cbafb554e83e4f2cda1` |
| R08 | delivery-constraints.md | `ea9cc442b72a71c395048a047ce97e8dc476be15678a5df1f4b3544a5c8f4ff1` |
| R08 | evidence.md | `e2109014472dbc8e6491e56b8909ce5553dfa6f368c5e23ef64e534420477d18` |
| R08 | homepage-refresh.md | `dceb3cdeea0b3f266128ffc8d23b327148ed4d11dd613ab37548b31c397e4a43` |
| R08 | request.md | `2adc6540b5630ff06638c182d98a0fd7279617f221e6b95d885a8cba081c27f5` |
| R08 | stakeholder-notes.md | `a272879966fa60b22d0753ca452d07523d3923f64133bc523113c1b4128eb462` |
| Both launch runs | costs-and-delivery.md | `16f36d1314d151bfbb0e8939a0454a817a868a922678b944e8636da313e5fcd5` |
| Both launch runs | founder-brief.md | `9fe09a2be550d96900b6bfe2b15935a055c597069bfbfa64a22681c4a6e12453` |
| Both launch runs | request.md | `a4011d3ad4a61ef0e6dbcbececf1249314c2890a1a9bf7e52e4f655923f692dd` |
| Both launch runs | research-records.md | `ec4e2d2dddde09cfef4753cba6501a0493a59542f166bc8eaca22a320d937e34` |
| R13 | approved-offer.md | `73ce7d1792c57651ed3efa6918bd227571e1d912e91bdbd6936feb2ca4273df5` |
| R13 | launch-artifacts.md | `02c98402a274368f8a8bbc462e1decc59b4b3b5fb6b42501715fd16307580f51` |
| R13 | request.md | `cafe99eea88d8722c6b740e3b45020473ba601cc08548ec0f43702bd800afe2c` |
| R13 | trial-record.md | `11cfc4ef8a66f5703dc6118b268bbc60dda754b420c5508cedb574c948508848` |

Input metadata locations: R05/R08 `metadata.json:79`; L-general `:85`; L-specify/R13 `:81`. After-hash locations: R05 `:787`; R08 `:831`; L-general `:343`; L-specify/R13 `:822`.

| Run | Recomputed `session-tools.jsonl` SHA-256 | Calls/results |
|---|---|---:|
| R05 | `2a9c166ba13c53b7e055036e1750e446b748ae6e6ebdb1083ccedf071bf1de24` | 2 / 2 |
| R08 | `96b69d4d3a0cc77581eeeed1936a540f75abf5f68f6ea088f34140b9fe8660ae` | 2 / 2 |
| L-general | `e8e5cdede78215ad20c659361fd7ab60bed48e3996f1d480ac675f05b77f4392` | 5 / 5 |
| L-specify | `7c8a29e96a0eae0c1168979c40bffb6153dd64e8b924426aa566d79480ff5914` | 3 / 3 |
| R13 | `ae33d32e4f7a852ce81434283f65e9dd2ca9fb2aeccf25a362f90528f9bc4ef8` | 3 / 3 |

Every export hash is stored at its run's `metadata.json:29`. Export record counts and source-line ordinals also match metadata. All fifteen call IDs are paired in the following ledger:

| Run | Call ID | Call → result export lines |
|---|---|---|
| R05 | `call_zXBsxHFN5fvH4cKRz6Hte7jm` | 1 → 2 |
| R05 | `call_Ipxl88ReIKZE5Zcx5zF3x7GN` | 3 → 4 |
| R08 | `call_OAtbw9YiosY1iVuUIzAHdveo` | 1 → 2 |
| R08 | `call_jfkxU5DA7g525wTujZDmeFo7` | 3 → 4 |
| L-general | `call_NzCwOmEHQp4V7oNfO7GM3fob` | 1 → 2 |
| L-general | `call_VHljPbrbTkwkC66B4NfIsMhr` | 3 → 4 |
| L-general | `call_XJdfTorjGDREwqqdpjZUDKQA` | 5 → 6 |
| L-general | `call_PtUKBJjF5cdrXvEFkewbIqnj` | 7 → 8 |
| L-general | `call_NCMeIkz4xYk4iRwBXOqSnsfu` | 9 → 10 |
| L-specify | `call_VkLf6aBs1AVxw7KgbxvybCaD` | 1 → 2 |
| L-specify | `call_BdWPjf2TwJyfVRnY7Z00OpuO` | 3 → 4 |
| L-specify | `call_y21KwQV4e2jGSceFdn6ldp1V` | 5 → 6 |
| R13 | `call_eTDqtcrwYIAuzcRQp4Jc2rMp` | 1 → 2 |
| R13 | `call_Q7mm8ylNSlsgQR0EQFrCtzUg` | 3 → 4 |
| R13 | `call_Nal4g0CkFpweYO7NzTTh6QsV` | 5 → 6 |

The metadata also records hashes of original host sessions, the exporter module, and instructions. Those source files are outside the permitted inspection scope and were not independently rehashed. Matching the export validates this preserved trace against its recorded digest; it does not independently certify exporter implementation or every possible uncaptured side effect. No numerical quality grade is assigned.
