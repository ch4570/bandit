# Independent execution and claim audit

Audited the four settled runs below against their frozen task inputs and recorded execution. No numeric grading. No product code/tests or external actions were executed for this audit. Only this report was written.

Paths below are relative to `/private/tmp/bandit-batchcaps.AF24cq/runs/`. `05`, `08`, `12`, and `13` abbreviate `05-small-research--bandit-research`, `08-callback-scope--bandit-scope`, `12-launch-handoff--bandit-specify`, and `13-offer-consistency-review--bandit-review`. `input/file:Lx` means the frozen `original-input/file`, not current product source. Line spans identify all relevant evidence; JSONL line numbers are physical export lines.

## Findings and limits

- All 14 frozen input files match the recorded before/after hashes and the corresponding `workspace/input` files. All four tool-export hashes match metadata. Every recorded call has exactly one paired result. Recorded workspace snapshots are identical before/after; all shell commands completed successfully.
- No forbidden write, external contact, browsing, supplied-product execution, test execution, or subagent use appears in the captured calls. Run 08 also respects its stronger prohibition on running code: it only reads files and explicitly disclaims tool verification of arithmetic.
- Run 12 and run 13 really executed arithmetic in the orchestration tool, with paired numeric results. CLI command-event output omits those computations; this is not evidence of absent execution. Some run 12 count totals are literal supplied values in the calculation call, so that call does not independently sum those totals. Independent recomputation confirms them.
- No incorrect reported arithmetic was found. Run 12 has a narrower launch handoff ambiguity: a Wednesday October 14 onboarding can accept prerequisite information during Monday October 12's support window, after the proposed common service start. The paid-access/start-date rule for that accepted path is not explicit. Its final same-window closeout promise also has unresolved workload and overflow timing. Neither gap proves that the proposed work is impossible: future staffing is an explicit prepayment gate, and the onboarding reserve itself fits.
- Run 13 consistently treats the artifacts as drafts and the checks as proposed, unexecuted checks. Its capacity example is a reachable hypothetical, not an assertion about live bookings.

The audit uses the raw requests as its standard, not skill text incidentally included in recorded tool results. No current skill/source files, criteria, grades, protocol documents, other run results, prior diagnoses, or issue records were consulted. Full host-session files were outside scope; their source hashes cannot be independently authenticated here. Export hashes and call/result consistency authenticate the supplied exports against metadata, not completeness of every possible host action.

## Integrity and execution evidence

SHA-256 was recomputed from file bytes. For each input, the frozen file, `workspace/input` file, `metadata.input_sha256`, and `metadata.input_after_sha256` agree.

| Run | Frozen inputs checked | Tool-export SHA-256 | Relevant metadata lines |
|---|---:|---|---|
| 05 | 1 | `b7edeb7ab6a6d243a960df65b2ad60f81e33452aaeb75ecbdae5423e83be32ff` | export L29; input L77; integrity L453–458; after input L785 |
| 08 | 5 | `0c5db7fd028531c08c8f61297ca9dc9d2dc32fec5ed1124d10c197ab6d5b37e7` | export L29; input L79; integrity L479–484; after input L831 |
| 12 | 4 | `534b154c36e7c164b9a6a571c251b15acaf24986bead34787c8f2d4f3221fb61` | export L29; input L81; integrity L475–480; after input L822 |
| 13 | 4 | `71fe28a38a0223891482ccaec673c509ad64cda95d442ef74baac26c042acaf6` | export L29; input L81; integrity L475–480; after input L822 |

Input hashes:

```text
05 request.md                8c380f53238d35842c21d0efce097cff4cf69f5a16326cbafb554e83e4f2cda1
08 delivery-constraints.md   ea9cc442b72a71c395048a047ce97e8dc476be15678a5df1f4b3544a5c8f4ff1
08 evidence.md               e2109014472dbc8e6491e56b8909ce5553dfa6f368c5e23ef64e534420477d18
08 homepage-refresh.md       dceb3cdeea0b3f266128ffc8d23b327148ed4d11dd613ab37548b31c397e4a43
08 request.md                2adc6540b5630ff06638c182d98a0fd7279617f221e6b95d885a8cba081c27f5
08 stakeholder-notes.md      a272879966fa60b22d0753ca452d07523d3923f64133bc523113c1b4128eb462
12 costs-and-delivery.md     16f36d1314d151bfbb0e8939a0454a817a868a922678b944e8636da313e5fcd5
12 founder-brief.md          9fe09a2be550d96900b6bfe2b15935a055c597069bfbfa64a22681c4a6e12453
12 request.md                a4011d3ad4a61ef0e6dbcbececf1249314c2890a1a9bf7e52e4f655923f692dd
12 research-records.md       ec4e2d2dddde09cfef4753cba6501a0493a59542f166bc8eaca22a320d937e34
13 approved-offer.md         73ce7d1792c57651ed3efa6918bd227571e1d912e91bdbd6936feb2ca4273df5
13 launch-artifacts.md       02c98402a274368f8a8bbc462e1decc59b4b3b5fb6b42501715fd16307580f51
13 request.md                cafe99eea88d8722c6b740e3b45020473ba601cc08548ec0f43702bd800afe2c
13 trial-record.md           11cfc4ef8a66f5703dc6118b268bbc60dda754b420c5508cedb574c948508848
```

All four `prompt.txt:L2` restrict activity to the task inputs and installed snapshot, prohibit other repositories/evaluations/sessions, browsing/contact, product code/tests, subagents, and file changes. The captured commands access only permitted input/snapshot paths. Snapshot-content reads are recorded as execution facts; their instructional content was not used as an audit standard.

| Run | `session-tools.jsonl` call/result lines | Call ID | Observed action |
|---|---|---|---|
| 05 | L1 / L2 | `call_Vic6JVpHlD6kW0PBumfCNsa7` | List input, read request and snapshot references; shell exit 0 |
| 08 | L1 / L2 | `call_nTllNPswWmnHezwNGj4xHfWk` | List input and read snapshot; shell exit 0 |
| 08 | L3 / L4 | `call_5h0L0uwY6kV5BIdDqFA2szaX` | Read all five raw inputs; shell exit 0 |
| 12 | L1 / L2 | `call_sRVXkhEa0DWr6K81f6W4EplV` | List input and read snapshot references; shell exit 0 |
| 12 | L3 / L4 | `call_y8LwUih5SZegD10rrwj76qBI` | Read all four raw inputs; shell exit 0 |
| 12 | L5 / L6 | `call_Jdej7fYdzO2bn45lbyn8hB2o` | Snapshot-reference read, then actual JS model/rate/budget calculations with returned numbers |
| 13 | L1 / L2 | `call_gKvq3txbXSbrEObFI0LzWNEs` | Read request, list input/snapshot files; shell exit 0 |
| 13 | L3 / L4 | `call_aunBHBLPfVP5BWxciyu2JW5p` | Read snapshot and numbered raw artifacts; shell exit 0 |
| 13 | L5 / L6 | `call_7g09jL5WUr0DthNRGwHijDVx` | Actual JS price, undercharge and capacity calculations with returned numbers |

The numeric expressions in run 12 and run 13 execute inside `exec` rather than a shell command. In 12, `events.jsonl:L9–10` shows only the accompanying reference-read shell command; the arithmetic is present in the full tool export L5–6. In 13, CLI events L5–8 contain the two reads and there is no separate calculator command event, but the full export L5–6 records the arithmetic. Both calculation-verification claims therefore have execution evidence.

All four CLI event files have a nonfatal context-budget notice at L3: skill descriptions were shortened. It is not a failed task/tool call or a finding about answer quality. Completed turns are recorded at 05 L8, 08 L10, 12 L13, and 13 L10. Whitespace-delimited final-output counts are respectively 180, 917, 1,609, and 865; 05 meets its raw 200-word limit, and the others meet prompt limits of 1,000/1,800/1,400. Korean word counts are reported with this explicit counting convention.

## Run 05: small research

The sole raw request asks for one customer segment and one cheapest validation method this week, with no interview/customer evidence, no search or file creation, and a 200-word limit (`input/request.md:L1`). Output L3 chooses local single-person employed households with a recent laundry-shop visit. L5 proposes five ten-minute phone interviews through acquaintances/referrals. L13 labels its 3-of-5 criterion provisional, provides a hold outcome for fewer than five completions, and L15 explicitly rejects friendly answers as paid demand. Those are proposals, not invented customer observations. There is no claimed calculation execution, and none is necessary to support the recommended small exploratory action. No material execution or claim error found in this run.

## Run 08: callback scope

The request expressly says not to run code (`input/request.md:L9–13`). Both recorded calls are reads. Output L36 correctly says the arithmetic was not tool-verified. Audit recomputation from `input/delivery-constraints.md:L3–16` gives:

```text
queue + report = (3,3,1) + (0.5,0,0.5) = (3.5,3,1.5) engineer-days
remaining     = (6,4,2) - (3.5,3,1.5)   = (2.5,1,0.5) engineer-days
```

These match output L29–36. The output does not treat that arithmetic as proof of full-slice feasibility: L23 and L36 require estimates for missing completion/correction/recovery behavior before commitment, and L1 permits a manual-checklist fallback. This matters because raw evidence L22–25 establishes fields/events, not an implemented correction UI or reliable claim concurrency. The accepted journey includes seeing ownership, claiming, completing and removing an item, missing-contact correction, save/claim failure recovery, empty/error distinctions, and nondestructive disablement (output L17–23). These are visibly proposed acceptance requirements, not assertions that the existing system already supports them.

The two small desks are the volunteered pilot population, not the large prospect (`input/stakeholder-notes.md:L3–7`; output L7). Aggregate late-case evidence remains separate from small-desk effects (raw `evidence.md:L6–20`; output L11, L50). Consent is limited to 116 of 240 records and there is no approved provider or consent-free fallback (`delivery-constraints.md:L19–21`; output L3, L42). The plan retains branch permissions, excludes unauthorized pricing/contact enrichment/ownership redesign, and does not borrow the agency's budget.

The shipping deadline is September 30; the two-week pilot's exact dates are absent from raw input. Output L38 preserves that distinction and leaves completion-by-September-30 unresolved. Output L54 includes callbacks still incomplete after their 12-hour threshold, avoiding a completion-only success denominator; L58 requires the full observation window. Expansion remains a separate review with a desk-specific baseline/threshold gate (L50–60). No demonstrably impossible release promise or numeric error found; full-path estimation and pilot dates remain stated preconditions.

## Run 12: launch handoff

### Calculations and evidence claims

Raw `research-records.md:L26–30` recomputes to 42 opportunities, 28 memo-containing opportunities, 20 read-marked opportunities, and 16 founder-reminded opportunities. The rates are 28/42 = 66.6667%, 20/42 = 47.6190%, and 20/28 = 71.4286%; output L19 reports correctly rounded values and keeps the two read denominators distinct. The tool call L5 actually divides those totals, but its `counts` object merely prints literal 42/28/20/16. It does not sum the raw rows; the audit separately performed those sums. Four independent shops, six interviewees, three free-use shops, zero paid customers, missing reminder cross-tabs, and absent before/after outcome evidence are preserved by output L13–21 against raw L3–7, L20–32.

Raw `costs-and-delivery.md:L9–16` uses VAT-exclusive won, monthly fixed cost 60,000, per-shop storage/notifications 2,000, 3.3% fee, 30 monthly support minutes at 25,000/hour, and one-time 40-minute onboarding. These imply support 12,500/month and onboarding 16,666.6667. Recomputed model values match output L100–109 and the paired result for `call_Jdej7fYdzO2bn45lbyn8hB2o`:

| Value | A: monthly 29,000 | B: initial 30,000 + monthly 19,000 |
|---|---:|---:|
| Recurring payment fee | 957 | 627 |
| Recurring contribution/shop/month | 13,543 | 3,873 |
| Five-shop recurring result after 60,000 fixed cost | 7,715 | −40,635 |
| First-month five-shop result including onboarding and setup-fee net | −75,618.3333 | 21,081.6667 |
| Arithmetic recurring break-even shop count | 5 | 16 |

B's setup net is 30,000 × 0.967 = 29,010 **per shop**, as the actual expression multiplies the complete per-shop result by five. Rounding the final totals gives the printed −75,618 and 21,082. B's 16-shop result is an extrapolation of assumptions specified for at most five shops; output L107 explicitly says it exceeds the support cap rather than presenting it as a viable current plan. The unknown acquisition/maintenance costs remain excluded and disclosed (L111).

The proposed cash buckets sum to 800,000. The 60,000 monthly hosting cost is inside the 100,000 tool reservation, not added twice (raw costs L9; output L113). The four preparation weeks sum to founder 40, developer 28, designer 8 hours; the founder's six work buckets also sum to 40 (output L39–45; raw founder L17–21). These are planned allocations, not validated estimates for every new UX rule.

### Calendar, latest prerequisite, accepted service and closeout

Calendar recomputation: September 14, 2026 is Monday; October 11 is Sunday; that inclusive preparation period is exactly 28 days. October 12 is Monday, October 14 Wednesday, November 11 Wednesday, and November 13 Friday. The candidate October 12–November 11 service period is 31 inclusive calendar dates, consistent with a month-long proposal rather than a second four-week period.

The raw staffing authority is only four weeks (`founder-brief.md:L13–23`). Output L5, L41, L117 and L132 explicitly require later staffing/tool confirmation before payment or firm reservation, with an October 4 decision and delay on failure. Thus service past October 11 is an unresolved resource decision, not an unconditional promise funded by the original 40 hours. The input itself asks for four weeks of preparation and sets no fixed launch date (`request.md:L7`; `founder-brief.md:L9`). Deferring actual paid delivery subject to confirmation does not contradict a raw fixed delivery deadline.

| Accepted/exception path | Evidence and consequence |
|---|---|
| Conditional application | Output L58 and L68–70: application is not payment/confirmed reservation; confirmed resources and terms precede payment. Over-cap applications wait with no charge (L86, L132). |
| Onboarding | L119 separately reserves four hours October 12–14. Five shops × 40 minutes = 200 minutes, leaving 40 minutes in that reserve. It is incorrect to squeeze this batch into a single one-hour support window: the output expressly allocates separate onboarding time. |
| Latest onboarding prerequisite | L119 requires access data by the support window before each appointment. For an October 14 appointment before that day's 18:00 support window, the preceding proposed M/W/F window is October 12, 18–19 KST; appointment times are not fixed. Therefore data can be timely under this allowed scheduling case yet arrive after the common October 12 candidate service start (L5). The handoff does not explicitly state whether usable paid access begins on October 12, after that appointment, or with a corresponding shift/proration. “No late new starts” does not resolve this scheduled October 14 case. This is a supported start-date/entitlement ambiguity, not a proven capacity violation. |
| Missing prerequisite or delayed development | L119 postpones payment and start together if access information is missing; L47 requires a functionally adequate manual fallback and renewed consent before payment when delivery changes. The exact moved end date is not specified, and late starts are separately excluded; this needs one consistent calendar rule before acceptance. |
| Service support | L119 proposes M/W/F 18–19 KST and first response by the next support window. There are 14 windows October 12–November 11, plus the November 13 recovery window: 15 scheduled hours total. |
| Latest ordinary inquiry | L121 accepts inquiries through November 11 at 18:00 and promises a first response in that day's 18–19 window. Additional confirmation is accepted through November 13 at 18:00, to finish in that day's window. The follow-up window exists; the plan does not simply drop obligations when enrollment ends. |
| Overflow/termination | L121 assigns the founder either additional response time or direct termination/refund guidance; L123 preserves in-period support despite nonrenewal, supplies record copies, ends access, and gates retention/deletion terms before payment. These are real recovery provisions, but the volume/duration that can be completed in the last one-hour window and the timing/resources for overflow handling remain unbounded. |

No numerical impossibility follows from those last-window uncertainties. Raw 30 minutes/shop/month is an estimate of total recurring support, not a per-ticket upper bound or proof that all five shops will send a 30-minute request at once. Conversely, it cannot prove that a one-hour final window always suffices. If ten founder hours/week were separately renewed, one feasible allocation for the explicitly scheduled work is seven hours in October 12–18 (four onboarding plus three support), then three support hours in each following week through November 13. That totals 19 reserved hours and does not itself exceed ten in any week. Interviews, monitoring, copies, refunds and other closeout work would still need allocation, and renewal is not evidenced in the raw staffing. This conditional allocation shows why “impossible” would overstate the evidence.

The unit economics above correctly reproduce the raw active-support estimate of 2.5 hours/month for five shops. The 15 reserved support windows do not by themselves establish 15 hours of exclusive active labor; whether their availability cost or closeout work changes that assumption is unverified. Output L111 appropriately requires actual time measurement, but its displayed margin should not be described as demonstrated economics for the complete schedule.

The UX covers employee/owner separation, explicit reading distinct from completion, version changes and stale reads, denied/revoked access, save failure, no records versus unread records, and a manual fallback (output L78–96, L127–132). It labels checks unexecuted (L125). No product-test or deployment claim is supported or made. The actual payment/refund mechanism, retention period and later staffing remain explicitly undecided (L134).

## Run 13: consistency review

The raw task names the approved operating offer as authority and labels the launch artifacts unapproved drafts (`input/request.md:L5–11`; `launch-artifacts.md:L3`; `approved-offer.md:L5`). Output L1–3 preserves that distinction. Its proposed checks are not presented as observed implementation failures; L78 explicitly says implementation and paid operations are not verified.

The separate calculation call `call_7g09jL5WUr0DthNRGwHijDVx` at export L5–6 evaluates expressions, not just literal answers:

```text
first one-pair order = 18,000 + 4,000 - 3,000 = 19,000
first two-pair order = 18,000 × 2 - 3,000     = 33,000
shortfalls versus draft                     = 4,000 and 3,000
illustrative capacity                       = 23 pairs + 2 pairs = 25 > 24
```

These support output L29–34 and L56. Regular-order totals independently recompute to 22,000/36,000 as printed at L40. The approved unit is actual pairs, combined across two sites, with 1–2 pairs/order (`approved-offer.md:L11`); draft L41–43 instead counts orders. Output L56 explicitly conditions its counterexample on all existing 23 orders being one pair and states this is not the live reservation state. It does not infer exact occupied pairs from the order count. L58–60 repairs both unit and capacity-before-charge, offers another round or exit without payment, and includes concurrent-last-slot checks.

The review's other principal discrepancies are supported by the raw artifacts:

| Review evidence | Raw conflict and preserved boundary |
|---|---|
| Output L5–13 | National/doorstep AD and “other” address path (`launch-artifacts.md:L7, L33`) conflict with the two registered-locker sites (`approved-offer.md:L9`). Old doorstep trial conditions remain historical (`trial-record.md:L5`). |
| L15–23 | Tomorrow/24-hour promises (draft L9, L55) conflict with Friday 18:00 return (approved L29). Calendar recomputation confirms the September 15, 2026 Tuesday round returns by Friday September 18. The review adds the correct date before payment and in confirmation rather than relying on correct LP text alone. |
| L25–40 | Draft L11, L45–47 omit the one-pair transport fee or double the order-level discount; approved L21–25 establishes the correct totals, fee unit, tax inclusion and prepayment terms. |
| L42–50 | Draft L35, L49 accepts excluded material and delays photo screening until after charge; approved L15 and L25 requires screening first. Review keeps screening timing unpromised and requires waiting/ineligible cases not to pay. |
| L62–70 | Trial L12–15 records 5 respondents out of 8 households, all 5 satisfied, no germicidal test and no paid repurchase. The review rejects “all customers” and 99.9% claims without inventing dissatisfied nonrespondents or paid demand. |
| L74–76 | Correct locker/return/one-off/quantity/cancellation terms remain; “two pairs or more free” has no reachable pricing conflict under the two-pair maximum. Delay contact-route omission is repaired; unapproved compensation remains open (approved L31–33; draft L61–65). |

The final review follows a complete commercial path through valid eligibility, pair capacity, final price and return promise before charge, confirmation, insufficient capacity/invalid intake, late return, cancellation and unresolved operator stoppage. It does not redesign the business or claim to have exercised any of those flows. No material arithmetic, evidence-status, or permission error found in this run.

## Audit boundary

These conclusions apply to these four settled outputs and their captured tools. They are not a benchmark of the current skills, an implementation/test result, proof of actual customer demand, or proof that unresolved launch staffing has been secured. The launch date/entitlement ambiguity and final-window workload specification remain the concrete limitations to carry into the handoff; the evidence does not support calling the overall promise numerically impossible.
