# Commercial execution and claim audit

Audit date: 2026-09-10. Scope: exactly the three settled runs below. No material mismatch was found between their commercial conclusions and the supplied evidence, or between their claimed arithmetic execution and the captured tool results. This is an independent, bounded audit, not a product test or a broader quality benchmark.

## Evidence scope and notation

All paths below are relative to `/private/tmp/bandit-reachability.MFPOwH/runs/`:

| Alias | Run directory |
|---|---|
| R | `13-offer-consistency-review--bandit-review` |
| G | `13-offer-consistency-review--bandit` |
| P | `18-review-reachability--bandit-review` |

`R/output.md:34`, for example, means line 34 of that run's output. Fixture citations for case 13 apply identically to R and G: their four original inputs are byte-identical. `O`, `L`, and `T` below abbreviate `original-input/approved-offer.md`, `original-input/launch-artifacts.md`, and `original-input/trial-record.md`. For P, `M`, `H`, and `C` abbreviate `original-input/sources/01-product-meeting.md`, `02-release-rehearsal.md`, and `03-public-copy.md`.

I read the complete original inputs and output of each run, metadata, captured session-tool records, and selected CLI events needed to reconcile execution and completion. Workspace input copies were read only to hash them. I did not open skills, grading criteria/reports, prior outputs, issues, or a protocol. Skill text embedded in captured read results was not an audit standard. The standards here are the original requests, their explicitly approved conditions, and their evidence states.

## Integrity and execution evidence

For every input, six values agree: independently computed original-input SHA-256, independently computed current workspace/input SHA-256, metadata `input_sha256`, metadata `input_after_sha256`, and the input entries in metadata's before/after workspace snapshots. This covers 12 original/copy pairs, including all nested P source documents. The hashes are:

| Runs | Input relative path | SHA-256 |
|---|---|---|
| R, G | `approved-offer.md` | `73ce7d1792c57651ed3efa6918bd227571e1d912e91bdbd6936feb2ca4273df5` |
| R, G | `launch-artifacts.md` | `02c98402a274368f8a8bbc462e1decc59b4b3b5fb6b42501715fd16307580f51` |
| R, G | `request.md` | `cafe99eea88d8722c6b740e3b45020473ba601cc08548ec0f43702bd800afe2c` |
| R, G | `trial-record.md` | `11cfc4ef8a66f5703dc6118b268bbc60dda754b420c5508cedb574c948508848` |
| P | `request.md` | `0218b873d1932b16b638bf7e7db99ef0688b4de3b5718ced0d17e50e620cc2ca` |
| P | `sources/01-product-meeting.md` | `b28b62ac901a22776df16b84f396ae67583cd38912fb5a141e8e84700a084f3f` |
| P | `sources/02-release-rehearsal.md` | `a4c4beea7dbcb1d6c415d5e063825d1158fdc1aeaa0b957bddd2ab48d55a1d05` |
| P | `sources/03-public-copy.md` | `8961c9787d3a92879068834e08d8467fe8e35c78331e8076794294c8e7650f35` |

Metadata anchors: R `metadata.json:81`, `:136`, `:483`, `:822`; G `:83`, `:105`, `:227`, `:341`; P `:79`, `:134`, `:485`, `:828`. I also compared all recorded before/after workspace entries: zero differences in each run. Their recorded integrity checks passed with empty violations and snapshot errors: R `:475–480`, G `:219–224`, P `:477–482`. This is snapshot evidence, not proof against a hypothetical temporary edit restored between snapshots.

The exported session-tool files independently hash to the values recorded at each run's `metadata.json:29`:

| Run | `session-tools.jsonl` SHA-256 | Paired calls/results |
|---|---|---:|
| R | `862c7c01f1e62bf5d4e40c83429a495573bca41188706e769b7d70f141021bff` | 3 / 3 |
| G | `233a72bbe3424799de4dc01c0854fd2cb45cd916508c03b66d4a6b9f4bbd1173` | 4 / 4 |
| P | `62e9658240c83c43427e27cb1dc0b310bec441355747d0cb307927b57ae74e38` | 2 / 2 |

Every captured call has one result with the same call ID and a completed-script marker. The following records positively establish fixture reading and calculation; I also verified that each entire raw fixture occurs in its paired read result, removing `nl` line prefixes where necessary:

| Run | Session-tool lines | Call ID | Positive evidence |
|---|---|---|---|
| R | 1–2 | `call_OhntfiBQsmQ8qhXlUz7Uw1Lg` | Complete request read and file discovery. |
| R | 3–4 | `call_nVVlYlPtu3T7pIwr1OCuXdn2` | Complete approved offer, launch drafts, and trial record returned by the source-read branch; command exited 0. |
| R | 5–6 | `call_nR9Osb2nbfgX0cPPhti8DvOl` | Executed JavaScript arithmetic returns first totals 19,000 and 33,000; draft differences 4,000 and 3,000; 23 existing pairs plus 2 equals 25, exceeding 24 by 1. |
| G | 1–2 | `call_Xi8HT1SH1AAdqs3jjpkIsnnR` | Working directory and file discovery. |
| G | 3–4 | `call_Lrmu21yvUn3QJVA4ebPu1lX9` | Complete request and all three source documents returned; command exited 0. |
| G | 5–6 | `call_UUOEg9oOHn3JumQDIuPrtC9D` | An instruction-reference read completed; its prose was excluded from audit judgment. |
| G | 7–8 | `call_Y4Q2OIfPhgozzjzYFUPXm3VJ` | Executed JavaScript arithmetic returns regular totals 22,000 and 36,000; first totals 19,000 and 33,000; differences 4,000 and 3,000; remaining capacity 1 and proposed total 25. |
| P | 1–2 | `call_GQl83utfbBOw23k9EwwkdEji` | Working directory and file discovery. |
| P | 3–4 | `call_XBFJjYGCVQuhWxMqraIodpqo` | Complete request and all three source documents returned; command exited 0. |

R's arithmetic assertion at `output.md:34` and G's assertion at `output.md:40` are therefore supported by actual paired execution, not just proposed commands. Their CLI streams only expose the shell reads, not these JavaScript-only calculations: R `events.jsonl:5–10`; G `:4–9`. The omission is not evidence of non-execution. P makes no claim to have run calculations or product tests.

All three processes exited 0 (`metadata.json:10`). Terminal completion is present at R/G `events.jsonl:12` and P `:10`. R and P `events.jsonl:3` contain a skill-description context-budget warning; these are not failed product tests or a failed terminal turn. No product request, charge, external message, or evidence edit appears in the captured tools; the recorded sandbox is read-only and web search/multi-agent execution are disabled. This conclusion is limited to the supplied traces and snapshots, without treating CLI coverage as exhaustive.

## Case 13: independent commercial trace

The governing source is O:5, which explicitly denies any superseding approval. L:3 says the launch materials are unapproved drafts, not implemented behavior or execution results. T:3–5 describes a synthetic, free, differently operated trial. Both outputs preserve these states (R/G `output.md:3`); neither substitutes trial practice or draft wording for the approved paid offer.

### Pricing and capacity

The complete allowed quantity set is one or two pairs (O:11; L:37). Approved price is `18,000 × pairs + shipping − discount`, with 4,000 shipping for one pair, waived shipping for two, and a first-order discount of 3,000 once per order (O:21–23). No other coupons, subscription, or minimum term are provided. Independent recomputation gives:

| Pairs | Regular approved total | First approved total | Draft first total | Draft below approved by |
|---:|---:|---:|---:|---:|
| 1 | 22,000 | 19,000 | 15,000 | 4,000 |
| 2 | 36,000 | 33,000 | 30,000 | 3,000 |

L:45–47 supports both draft totals: one pair omits shipping; two pairs doubles the order discount. AD-1's unconditional free collection/return alongside “15,000 from” (L:11) cannot be repaired solely by correcting the checkout. LP-1 also omits the one-pair shipping amount (L:23). R `output.md:28–34` and G `:28–40` correctly require the advertisement, price card, checkout, and related confirmation amounts to agree. Their customer consequences are conditional design risks; no real undercharge, additional bill, or customer loss is established.

The capacity counterexample is reachable within the draft's permitted choices: 23 existing one-pair orders consume 23 pairs, the next valid two-pair order passes `23 orders < 24`, and the resulting 25 pairs exceed the shared 24-pair limit (O:11; L:41–43). More generally, 23 valid orders represent 23–46 pairs; choosing the lower bound already proves the conflict, so the finding does not need an invented third pair or hidden booking path. R `output.md:21–26` and G `:21–26` use the valid lower-bound counterexample and require shared pair accounting plus prepayment reservation. Concurrent booking safeguards are proposed verification criteria, not a claim that a race was executed or observed.

The phrase “two or more pairs receive free shipping” (L:23) has no differing charge outcome for the supplied one/two-pair selection set: the only qualifying quantity is two. R `output.md:36` and G `:64` correctly make narrowing that phrase to “two-pair order” optional. This is a bounded document inference; L:3 prevents treating the draft selector as independently tested API enforcement. The limited quantity condition also does not excuse the advertisement's genuinely unconditional shipping promise.

### Eligibility, location, timing, and evidence claims

| Material issue | Full source trace and reachability | Output assessment |
|---|---|---|
| Unsupported collection area/location | O:9 allows only registered lockers in Solbit A/B and excludes doorstep and nationwide service. L:7 promises nationwide doorstep collection; L:33 opens an outside-complex doorstep-address path. T:5's earlier doorstep pickup was a free trial, not an amendment. | R:7–12 and G:7–12 correctly require both public copy and the unsupported application path to change. This is a supplied draft-path conflict, not proof of a live outside-area payment. |
| Eligibility assessed after payment | O:15 excludes suede, leather, electronics, and badly deformed shoes. O:25 requires eligibility and capacity confirmation before final price/return acknowledgment and payment. L:35 explicitly advances excluded materials; L:49 says photo review follows payment, with refund on rejection. | R:14–19 and G:14–19 correctly identify a route to paying before known eligibility, include all supplied exclusion categories, and require a prepayment check. “Staff will contact you” is no working rejection gate. Refund afterward does not fulfill “do not charge.” |
| Return promises disagree | O:29 defines Tuesday pickup and Friday 18:00 return to the selected locker; O:11 identifies the first Tuesday as September 15. L:9 promises tomorrow; L:55 promises within 24 hours of collection; L:25 already agrees with Friday. T:10–11 records six next-day and two two-day returns under different trial conditions. | R:38–43 and G:42–47 correctly align AD-1, prepayment UX, and confirmation to September 15 → September 18 at 18:00 while preserving correct LP copy. They do not assert the paid pilot has already returned shoes late. A correct later screen alone would not repair the advertisement. |
| Satisfaction and sterilization | T:12–15 records five respondents out of eight households, all five satisfied, no paid repurchase offered, and no sterilization test. O:17 offers ordinary washing/drying without a sterilization guarantee. L:9 claims all trial customers satisfied and 99.9% sterilization. | R:47–52 and G:49–54 correctly reject extending 5/5 respondent satisfaction to 8/8 participants and reject the unsupported performance claim. They preserve the free/small/referred trial's evidence limits and do not infer paid demand. R does not repeat the 6/8 return count, but its governing return conclusion is independently supported. |
| Delay/cancellation policy | O:31 requires new estimated date and contact path by Thursday 18:00, with compensation unapproved. O:33 defines before-pickup refund, after-pickup change-of-mind rejection, and individual review for operator interruptions. L:61–65 agrees on cancellation, date notice, and leaving compensation undecided, but omits contact from the delay description. | R:54–58 and G:56–66 preserve matching terms and unresolved compensation, and treat contact/exception disclosure as smaller completion work. These are document omissions, not evidence that a delay notification actually failed. G additionally leaves undefined reservation-release and photo-review details as questions rather than inventing deadlines or policy. |

The outputs' release-blocking findings are therefore substantive contradictions with reachable draft paths. Their optional quantity wording and unresolved compensation treatment are proportionate. Public expectations are repaired alongside downstream screens, rather than using a narrow checkout gate to excuse incompatible advertising.

## Case 18: independent commercial trace

M:3–11 establishes the approved product. H:5 explicitly places its observations in RC2, a test-payment environment, and a clock-controlled storage environment. C is the public copy applied to RC2. These evidence states support conclusions about recorded rehearsal behavior while providing no actual-card-charge or actual-customer-loss evidence. P `output.md:3`, `:9–10`, and `:34–40` preserves that distinction.

### Real pricing conflict within allowed participants

All one-to-four-person bookings, including the booker and infants, should cost 60,000 with no mandatory extra fee (M:5; C:7). H:7 makes three/four-person bookings valid, and H:9–16 records option-free totals consistently across the confirmation screen, test payment approval, and stored order:

| Participants | Approved/public total | Recorded test total | Difference |
|---:|---:|---:|---:|
| 1 | 60,000 | 60,000 | 0 |
| 2 | 60,000 | 60,000 | 0 |
| 3 | 60,000 | 70,000 | +10,000 |
| 4 | 60,000 | 80,000 | +20,000 |

P `output.md:7–12` correctly selects the reachable four-person example, preserves the fact that test approval and storage also differ, and does not reduce the finding to a display problem or an untested concern. Optional additional prints cannot explain these charges: they were not selected, and M:7/C:9 expressly makes them optional. Removing participant surcharges implements the approved flat price; merely raising the public price to the broken implementation would require a new product decision. The proposed all-quantity and changed-participant checks are future checks, not falsely claimed executions. Actual card charges remain explicitly unconfirmed (H:22; output:10,38).

### Free prints: no supported shortage counterexample

M:5–9 gives one free 4×6 print to each participant and supplies four sheets per booking. Both booker and infants count. Staff have no authority to exceed four, and on-site additions must stay within four. Crucially, H:7 records enforcement as well as intent:

- Web choices are one through four; create and modify APIs count everyone and reject direct five-person input with 422 without saving it.
- Store edits use the same check; a staff attempt to change the cap returns 403.
- Only registered participants can check in; adding a fifth participant to a four-person booking was rejected in both web and store screens.
- H:18 records one free print per checked-in person and a four-person visit in which all four received one, leaving zero free sheets.

For every allowed participant count `n ∈ {1,2,3,4}`, required free sheets are `n ≤ 4`, and remaining sheets are respectively 3, 2, 1, 0. M:7 disallows converting leftovers into additional free prints or cash. C:7 explicitly bounds the public offer to one-to-four including infants/booker, and C:9 promises a print to everyone who participated. No supplied route adds a fifth participant or requires more than four free sheets. An assumed staff exception, unregistered fifth participant, or free conversion would contradict the supplied permission/flow constraints.

P `output.md:26–30` therefore correctly rejects a serious free-print defect using the whole recorded chain, rather than relying only on meeting intent or a web selector. Adding “4×6” to the copy is optional clarity: the omission supplies no competing print-size promise or reachable shortfall. This is scoped to the provided RC2 rehearsal; it is not a claim to have inspected production access control or independently rerun check-in.

### Real retention promise conflict, despite the seven-day checkout notice

M:11 approves delivery of the download link at session end, seven-day retention from that time, deletion at expiry, and neither extension nor resend after deletion. H:20 records the seven-day final-screen notice, actual object deletion after clock advancement past seven days, a 410 from the original link, unsuccessful store resend on day eight, and no connected separate original archive. C:11 instead promises download at any time for 30 days and encourages postponement.

Day eight is inside the public promise and beyond the recorded availability: it is a concrete, permitted customer wait, not a hypothetical bypass or staff exception. The supplied test already records the failed recovery route. The extra 23 promised days are unsupported; nothing supplied permits assuming a backup or extension. The seven-day checkout notice does not by itself repair misleading public copy that invites waiting.

P `output.md:14–22` correctly treats this as a required public-copy correction, preserves the deletion/410/resend/absent-archive observations, and supplies a seven-day replacement with the correct start event and no false recovery promise. Its day-eight customer example is a plausible consequence grounded in the rehearsal, not a claim that an actual customer lost photos. P does not demote the known retention conflict into a mere request to check whether it exists.

P `output.md:34–42` separately lists actual card charges, on-site additional-print payment/receipts, and manual outage recovery as unconfirmed, matching H:22. It does not use unspecified outage recovery to undo the confirmed normal retention expiry. These are future confirmation needs, not fabricated defects or new executed tests.

## Findings and limits

1. **No material execution overclaim identified.** Both case-13 tool-calculation assertions have matching executed expressions and returned numbers. P attributes implementation conclusions to the supplied rehearsal and expressly disclaims its own product/test execution. All complete source fixtures were available in paired tool-read results.
2. **No material commercial false positive or omission identified in this scope.** Both laundry outputs find the permitted-quantity price and capacity counterexamples, eligibility/timing/public-promise contradictions, and unsupported evidence claims. The photo output finds the reachable price and retention conflicts while rejecting an unsupported free-print shortage through quantity, permission, check-in, and distribution evidence.
3. **Evidence strength is preserved.** Case 13 is a document/design audit; case 18 includes supplied, synthetic rehearsal observations of test approvals, stored totals, deletion, and resend failure. Neither permits claiming real charges, actual customer loss, production enforcement, or a new executed rehearsal. None was added in this audit.
4. **Optional clarity stays proportionate.** The one/two-pair wording and missing print dimensions are optional; unapproved compensation and untested operational details remain unresolved. Draft rules are not presented as newly tested enforcement, and correct checkout details do not excuse independently misleading public promises.

This audit independently performed file hashing, trace/result reconciliation, and arithmetic only. It did not rerun products, charge cards, change evidence, contact anyone, or inspect code. Current input hashes and recorded workspace snapshots support unchanged inputs; they cannot prove every possible external or transient action absent from all logs. No numerical score or inference about other runs, broader skill superiority, or real-world business validation is made.
