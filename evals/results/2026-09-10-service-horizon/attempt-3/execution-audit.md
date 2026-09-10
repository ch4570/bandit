# Execution and service-horizon audit — round 3

Audit date: 2026-09-10. Scope: exactly the three settled synthetic runs named below. This is an audit of proposed plans and recorded calculation execution, not evidence that anyone sold, contacted customers, delivered consultations, or exercised operational controls.

All source citations below are relative to `/private/tmp/bandit-horizon.CtY2LG/round3/runs/`. `L12` means physical file line 12; JSONL citations identify the exported line and exact `call_id`. Only these runs' original fixtures, outputs, metadata, and execution records were used. No previous attempts, grades, issue/PR text, or repository skill files were opened. Mixed tool exports contain instruction-read commands and excerpts; those are not used as evaluative evidence. There are no qualitative/no-code control runs in this scope, and this audit makes no claim that a final-candidate control was executed.

## Findings at a glance

| Run | Calendar and latest-customer finding | Capacity finding | Calculation execution |
| --- | --- | --- | --- |
| `12-launch-handoff--bandit` | Sales end 9/25; all customers start 9/28; final request 10/9 noon, response and closeout 17:00. Explicit last-day exception prevents the ordinary next-weekday deadline from spilling past the funded period. | Weekly staffing and onboarding fit the proposed limits. Ordinary support-response capacity is not demonstrated for clustered demand; a separate two-hour closeout reservation is present but its component workloads are not estimated. No inevitable calendar overrun proved. | Matching completed calculator call/result; representative finance components reconcile. |
| `12-launch-handoff--bandit-specify` | No late entry after 9/25; all customers start 9/28; final request 10/11 16:00, response/refund/export/deletion and closure by 18:00, within week four. | Explicit final window is 5 stores × 20 minutes + 20 minutes spare = 120 minutes. This is a coherent proposed terminal allocation. Normal response-window handling remains an untested workload assumption, not demonstrated operations. | Matching completed calculator call/result; representative finance and staffing sums reconcile. |
| `15-supported-offer--bandit` | **Material internal contradiction:** eight Friday customers cannot use the promised clarification after their final Friday answer when clarifications close at the start of that answer window. Following the ordinary reply rule instead would require 11/9 service beyond the 11/8 contract. | Base and stress arithmetic is correct, but the cross-window time for promised clarifications is not reconciled. At the stated first-week +25% stress, every regular window's 220 customer minutes are already assigned. | Matching completed calculator call/result. Correct arithmetic does not resolve the omitted/unsplit follow-up workload or conflicting last-request rules. |

## 1. `12-launch-handoff--bandit`

### Confirmed resources and proposed lifecycle

The fixture confirms Gaon at at most 10 hours per week / 40 total, Doyoon 28 hours, Sora 8 hours, cash 800,000 won including a 100,000-won tool reservation, and at most five directly supported stores (`original-input/founder-brief.md` L13–23). Manual service is possible, with no continuous real-time support (`original-input/costs-and-delivery.md` L20–27). The request is planning only (`original-input/request.md` L19).

The output closes sales on Friday 9/25 and onboards on 9/26–27 (`output.md` L39), then provides the same fixed 9/28–10/9, 12-day offer to at most five stores (`output.md` L3, L32). The latest admitted customer therefore does not acquire a rolling 12-day period after the common end date. The period is explicitly distinct from a monthly subscription, and post-10/11 staffing must be secured before accepting later subscription payments (`output.md` L34, L76, L115).

Gaon's normal promise is weekday checking at 16:30–17:00 and an answer by the following weekday 17:00. Crucially, the same clause sets the **last intake to 10/9 noon and final response to 10/9 17:00**, reserves two hours of closeout that day, resolves undeliverable core failures through refunds, delivers record copies, and ends access at 17:00 (`output.md` L51). This is a specific terminal exception to the ordinary response rule. A last permitted request does not inherently create a Monday 10/12 obligation. No post-close new request or automatic renewal is promised.

### Capacity inside response windows

The weekly allocation is 10/10/10/10 founder hours, 6/14/6/2 development hours, and 4/4/0/0 design hours (`output.md` L36–43). Five 40-minute onboardings need 200 minutes; the week-two split is 180 + 200 + 120 + 100 = 600 minutes, matching the 10-hour cap (`output.md` L43; fixture `costs-and-delivery.md` L14).

The final two weeks each reserve 150 minutes of normal support; the last week also reserves a distinct 120-minute closeout within its 600-minute total (`output.md` L43, L51). These sums do not exceed confirmed resources. However, a store count and a monthly 30-minute support estimate are not a bound on arrivals before any particular reply deadline. For example, five 10-minute questions arriving after a normal checking window would require 50 minutes before the next weekday 17:00, whereas the next reserved normal window is 30 minutes. That is an illustrative permitted-demand scenario, not an observed workload or proof that those questions occur. The output does not allocate extra answer time for that clustering or state a per-request work limit. “Checking” could also be narrower than all answering work; the document does not locate that extra answering time.

The final noon cutoff leaves time for the two-hour closeout reservation before 17:00, but the plan does not break those two hours into support, copies, refunds, and access closure. Its refund fallback improves boundedness; actual processing times remain unverified. **Conclusion: explicit terminal horizon is coherent; full response-window capacity is conditional rather than established.**

### Recorded calculation evidence

The calculation claim at `output.md` L113 is supported by `session-tools.jsonl` **L5 → L6**, `call_id: call_xtYqBAw2hLGyiY6tRmEqev34`: completed `exec` call, matching `custom_tool_call_output`, and a separate numerical result object. The relevant fields include `models`, `setup`, `pilot`, `budget`, and `supportSensitivity`. The calculation is present even though a top-level command stdout event alone is not a complete record of its JavaScript result.

Representative reconciliation, using fixture `costs-and-delivery.md` L9–14:

- Monthly A contribution: `29,000 × .967 − 2,000 − (30/60 × 25,000) = 13,543`; five stores less 60,000 fixed cost give `7,715` (`output.md` L100–105; result `models[0].contribution`, `models[0].total5`).
- General-run model B includes **20,000** setup revenue: `5 × (19,000 × .967 − 2,000 − 12,500 + 20,000 × .967 − 40/60 × 25,000) − 60,000 = −27,268.333…`, rounded to `−27,268` (`output.md` L98–105; result `setup.firstB5`). This differs intentionally from the specify run's 29,000 setup proposal.
- The 12-day pilot conservatively keeps one full month of store/support costs: `5 × (14,500 × .967 − 2,000 − 12,500 − 40/60 × 25,000) − 60,000 = −145,725.833…`, rounded `−145,726` (`output.md` L109; result `pilot.total`).
- Cash assignments sum to `600,000`, leaving `200,000`; the 60,000 hosting cost is included in the tool reservation, not charged twice (`output.md` L111; result `budget`). These are calculations of proposals, not spending.

## 2. `12-launch-handoff--bandit-specify`

### Confirmed resources and proposed lifecycle

The four original fixtures are byte-identical to the corresponding general-run fixtures; their hashes are independently verified below. Resource evidence is `original-input/founder-brief.md` L13–23 and `original-input/costs-and-delivery.md` L9–14, L20–27.

The output offers a common **9/28–10/11 14-day** service, at most five stores, with sales/payment confirmation by 9/25 and onboarding 9/26–27. It explicitly refuses unprepared late joiners (`output.md` L31–35). This closes the latest-admission path without creating a later rolling service end.

Normal support windows are Monday/Wednesday/Friday 17:00–18:00, with answers by the next window. Sunday 10/11 adds a **16:00–18:00 terminal window**. Final intake is 16:00; response, refund handling, record delivery, access withdrawal, operational-copy deletion, and unresolved-item closeout are assigned by 18:00 (`output.md` L37–39). This Sunday exception is within the fourth funded week and precedes all unfunded future service. The wording does not promise a separate post-answer clarification entitlement that would restart the clock. The final-intake rule specifically closes the otherwise next-window path.

### Capacity inside response windows

The week-four support reservation is 3 × 60 + 120 = **300 minutes**, leaving another 300 of Gaon's 600 minutes for that week's other work. Week three reserves 180 minutes. Total planned staff allocations are 40/28/8 hours (`output.md` L43–51). Week-two 200 minutes onboarding + 180 sales/consent/payment + 220 preparation = 600 minutes, exactly the founder cap.

The terminal window explicitly allocates **5 × 20 + 20 = 120 minutes** (`output.md` L38); the listed closeout actions in L39 are assigned to that same window, not hidden in an unbudgeted later week. Under its proposed 20-minutes-per-store aggregate closeout assumption, the latest permitted requests and all listed closure work fit. No extra recurring consultation period is created by the ending or its acceptance criterion (`output.md` L135–136).

Normal windows still lack a request-volume/time bound. As a sensitivity example, all five stores using the fixture's 30-minute monthly support estimate in one deadline interval would be 150 minutes against a 60-minute window. The monthly estimate is not itself a promise that this clustering occurs, and the plan may spend remaining founder time or answer briefly; neither is made into a specific overflow schedule. Likewise, the 20-minute terminal per-store allowance has not been timed against combined copies, deletion, refund exceptions, and responses. **Conclusion: the terminal allocation is explicit and arithmetically consistent; there is no proven end-date contradiction, but ordinary deadline feasibility and actual closeout speed remain untested assumptions.**

### Recorded calculation evidence

The claim at `output.md` L119 has a matching completed calculator in `session-tools.jsonl` **L7 → L8**, `call_id: call_TstvfW6Bh36Zc39ePvydJWHm`. The result supplies `monthly`, `pilot`, `sensitivity`, `budget`, and `hours`.

- Repeated monthly A contribution `13,543` and five-store result `7,715` match the same components as above (`output.md` L111–119; result `monthly[0]`).
- This run's model B has **29,000** setup revenue. `3,873 − 16,666.666… + 29,000 × .967 = 15,249.333…` first-month contribution; five stores less 60,000 fixed cost give `16,246.666…`, rounded `16,247` (`output.md` L108–119; result `monthly[1].firstContribution`, `monthly[1].firstFive`).
- Pilot contribution `−17,145.166…` per store and five-store/fixed-cost total `−145,725.833…` match the reported rounded amounts (`output.md` L123; result `pilot`). This 14-day pilot also does not halve monthly support/storage costs.
- Budget `480,000` and staff hours `{gaon:40,doyoon:28,sora:8}` are returned by the completed call (`output.md` L49, L125; result `budget`, `hours`). The stated remaining `320,000` follows from the fixture's 800,000 cap.

## 3. `15-supported-offer--bandit`

### Confirmed resources and valid parts of the horizon

The founder has 12 preparation hours on 9/14–18 and then 90 minutes a week for settlements/intake management. The separate prepaid consultant contract runs **9/28–11/8**, Monday/Wednesday/Friday **18:00–22:00 including holidays**, for 72 total hours. Common records use one hour/week, leaving 660 customer minutes/week and 3,960 in total. No overtime, second consultant, or post-11/8 consultation is authorized (`original-input/operations.md` L7–12).

The output correctly distinguishes preparation, sales, and six-week paid operation (`output.md` L4, L46). It admits at most 24 people against the fixture's 32-intake ceiling, assigns eight people to each answer weekday, and keeps a fixed cohort start (`output.md` L48, L109, L119–120). The latest confirmed payer must pay by **9/25 18:00**, submit initial photos by **9/27 18:00**, and joins the common 9/28 start (`output.md` L61, L120). Their six-week entitlement is therefore not shifted beyond 11/8 just because they paid last.

There is a smaller admission ambiguity: intake is described as open through 9/25, with confirmation by the following day 18:00, while every payment link expires no later than 9/25 18:00 (`output.md` L109, L119–120). A late 9/25 applicant can lawfully reach the promised confirmation deadline after all payment links expire. This does not prove a late customer is accepted or force an overrun, but a precise final application/approval cutoff is missing.

### Proven contradiction: the final Friday clarification

The offer includes six weekly checks, **one bundled question and one short clarification about the answer in every round** (`output.md` L38). Normal answers arrive by the assigned Monday/Wednesday/Friday 22:00. Clarifications are accepted **after the answer, until the next operating day 18:00**, and answered that day by 22:00 (`output.md` L62).

The same plan makes the last photo submission Sunday **11/1 18:00**, the final clarification cutoff Friday **11/6 18:00**, and all consultation/summary dispatch Friday **11/6 22:00** (`output.md` L64). At the 24-person cap, eight customers have Friday answers (`output.md` L48).

| Last-week group | Normal final answer deadline | Ordinary clarification deadline/response | Relationship to contract and final cutoff |
| --- | --- | --- | --- |
| Monday group | 11/2 22:00 | 11/4 18:00 / 22:00 | Fits. |
| Wednesday group | 11/4 22:00 | 11/6 18:00 / 22:00 | Fits. |
| **Friday group** | **11/6 22:00** | **11/9 18:00 / 22:00** | **Past the 11/8 contract; also incompatible with the absolute 11/6 18:00 clarification cutoff.** |

The consultant starts work on that final Friday at 18:00. The last clarification cutoff is therefore already reached before the Friday answer can ordinarily be delivered and read. Moving every last Friday answer early enough to support a later clarification is not in the plan; changing the ordinary deadline after sale is not an existing exception. Even an instantaneous answer exactly at 18:00 would provide no usable post-answer clarification interval.

This proves an **internal promise conflict**, not that post-contract service actually took place. Enforcing the absolute cutoff withholds the included final clarification from the Friday group. Enforcing the ordinary entitlement creates an unfunded 11/9 answer obligation. Merely stating “no new consultation after 11/8” (`output.md` L65) does not reconcile those alternatives. A remedy would have to change the final-round answer schedule or the advertised final-round entitlement before sale, and then recheck capacity.

### Actual-window capacity is not established by the 62-minute total

The fixture estimates an initial 15-minute review, **six** weekly photo-check/answer blocks of seven minutes including week one, and five minutes closing (`original-input/operations.md` L18). Thus `15 + 6 × 7 + 5 = 62` minutes/person, and `24 × 62 = 1,488`. First week is `24 × 22 = 528`; final week is `24 × 12 = 288`. These component calculations are correct (`output.md` L50–57).

The output assigns 220 customer minutes and 20 common-record minutes to each four-hour session. Eight first-week customers consume 176 minutes at base time or **220 minutes at +25%**, exactly filling the claimed stressed customer window (`output.md` L57). However, first-week Wednesday must also accommodate Monday customers' permitted clarifications, and Friday must accommodate Wednesday clarifications. Friday clarifications roll into next Monday, which also has that week's regular cohort work. The capacity object in the actual calculator contains no separate clarification term or allocation across those answer windows.

Two interpretations remain unresolved:

- If the seven-minute weekly estimate covers the original photo answer only, the new included clarification needs additional time. At base estimates, a first-week Wednesday/Friday window has 44 minutes spare, or 5.5 minutes per prior-day customer if all eight clarify. At the stated +25% stress it has **zero** spare minutes: even eight one-minute follow-ups would require 228 customer minutes against 220. This is a conditional stress counterexample, not a measurement of clarification duration.
- If the author intended those clarifications to be included in the seven minutes, that component must be split and moved to the next operating day; the calculation that assigns all `8 × 22 × 1.25` minutes to each group's initial answer session does not demonstrate the resulting deadline schedule. No split, timing observation, or carryover calculation is provided.

Consequently the 2,472 unused whole-period minutes are real within the simplified model, but cannot establish that the promised replies fit their deadlines. The output itself correctly warns against using that total to enlarge enrollment; the same caution is necessary for its 24-person stressed-capacity claim. Baseline overload is **not proved**, because the clarification work duration and inclusion in seven minutes are unknown. The documented +25% robustness claim does **not** cover the full promised service as scheduled.

Late photos are moved to the next operating round with regular submissions prioritized, and missing rounds can be refunded (`output.md` L63, L127). After the final Friday there is no contracted next round. The refund route can bound undelivered late work, but the latest allowed late-photo/clarification interaction and final refund trigger should be stated; it cannot cure the included final clarification conflict above.

### Administrative closeout is assigned, but its capacity is conditional

The founder owns post-contract payment/refund/privacy administration (`output.md` L65), promises refunds within seven days of requests (`output.md` L127), and deletes photos/lifestyle material on 11/8 (`output.md` L129). The fixture's weekly 90-minute administrative allowance has no stated end date, so a refund deadline after 11/8 is **not by itself an unauthorized consultant-extension contradiction**. It is a separate identified owner/resource path.

The 90-minute allocation is `32 + 20 + 15 + 23 = 90` for intake, payments/refunds, comments, and status/metrics (`output.md` L125). That is an allocation, not a timed demonstration of 24 possible refund cases, final deletion, and retained-record administration. Stopping new intake cannot shed obligations already owed to admitted customers. No inevitable administrative overload is proved because durations and arrival counts are unmeasured; overflow handling for already-admitted customers remains unspecified.

### Recorded calculation evidence

The claim at `output.md` L91 is supported by `session-tools.jsonl` **L7 → L8**, `call_id: call_kYhzngqngG2GOl8KxGDU0jyI`, a completed JavaScript calculation with matching numerical result. Fields `offers`, `scenarios`, `capacity`, `alternative32`, and `stress` are present. No command stdout event is needed to infer this completed calculation; the exported result directly records it.

- `89,000 × (1 − .033 − .05) − 1,000 = 80,613` contribution per initial payer (`output.md` L71–73; fixture `operations.md` L28–30; result `offers[2].contribution`). Full initial payment is the fee/refund basis, and refunded customers retain their store/send cost.
- At 24 payers: initial receipts `2,136,000`, fee `70,488`, refund assumption `106,800`, customer cost `24,000`, contribution `1,934,712`; subtract consultant `72 × 15,000 = 1,080,000`, tools `30,000`, and preparation labor `12 × 20,000 = 240,000` to obtain `584,712` (`output.md` L75–91; result `scenarios[3]`).
- `ceil(1,110,000 / 80,613) = 14` cash break-even; `ceil(1,350,000 / 80,613) = 17` including preparation labor. These match the recorded results; remaining operational-management labor is explicitly omitted (`output.md` L83–85).
- The calculator returns first-week base/stress `528/660`, per-session base/stress `176/220`, full-period workload `1,488`, available `3,960`, and unused `2,472` (`result.capacity`; `output.md` L52–57). This validates the stated arithmetic, with the clarification inclusion/scheduling limitation above.

## 4. Recorded execution and integrity limits

All three metadata files report `process_exit_code: 0`, `exit_code: 0`, integrity `passed`, and no integrity violations. Evidence: general-run `metadata.json` L10, L217–223; specify `metadata.json` L10, L477–483; supported-offer `metadata.json` L10, L219–225. Their terminal `turn.completed` records are respectively `events.jsonl` L13, L15, and L13.

All three `events.jsonl` files have a nonfatal `item.completed` error record at L3 saying skill descriptions were shortened to fit context. It is not a failed calculator result or a failed terminal turn. It is disclosed here rather than describing the event streams as error-free.

The exports contain respectively 3/3, 4/4, and 4/4 calls/results, with empty export error arrays (`metadata.json` session-tools block L12–44 for the general run, L12–46 for the other two). The recorded calls are fixture/instruction reads and in-process numerical calculations; the numerical evidence used above comes from matching completed call/results. The metadata explicitly warns that CLI JSON events are not a complete tool trace (each `metadata.json` L16), so absence from command stdout was not treated as absence of execution.

Input hashes below match the frozen metadata. The recorded before/after input hashes also agree. This supports preservation of the audited fixture files in these runs; it is not a universal safety guarantee or evidence of real customer operations. The outputs themselves label the work as proposals and planned checks: general `output.md` L5, L92; specify L6, L129; supported offer L6, L142.

## 5. SHA-256 provenance

Hashes were recomputed from the audited files. For the two launch runs, each individual original input has the same bytes/hash in both runs; hashes below apply independently to each run's own `original-input/` directory. Metadata input-hash locations are general L81–86, specify L83–88, and supported-offer L83–88. Export hashes match each metadata file's `session_tools.export_sha256` at L29. Output hashes are audit-computed because they are not supplied as an output hash in these metadata records.

| Launch original input (both runs) | SHA-256 |
| --- | --- |
| `costs-and-delivery.md` | `16f36d1314d151bfbb0e8939a0454a817a868a922678b944e8636da313e5fcd5` |
| `founder-brief.md` | `9fe09a2be550d96900b6bfe2b15935a055c597069bfbfa64a22681c4a6e12453` |
| `request.md` | `a4011d3ad4a61ef0e6dbcbececf1249314c2890a1a9bf7e52e4f655923f692dd` |
| `research-records.md` | `ec4e2d2dddde09cfef4753cba6501a0493a59542f166bc8eaca22a320d937e34` |

| Supported-offer original input | SHA-256 |
| --- | --- |
| `channels-and-alternatives.md` | `0d2bcd7080ae7d1af1a09ef6338f8ecb71ea22abf457ac5103f9b6ab95ffdb21` |
| `customer-notes.md` | `44cc27e33a683ad7c6f71c33607278183c7b8b2c2e49e119c7a4604b76afd4b6` |
| `operations.md` | `8f9532f21045919ffee120432efc5fa9823db291569f00d45382b876cc594fa9` |
| `request.md` | `cb2b6fba4ceee5375b134d4ca9a7c3b8fea273a0500c983507d5b267e863db11` |

| Run / file | SHA-256 |
| --- | --- |
| `12-launch-handoff--bandit/output.md` | `d8f2f6253c596b4c2ec70dbb000db2d130244ac38174fa0cecee992f0ee2df82` |
| `12-launch-handoff--bandit/session-tools.jsonl` | `ae8ef0d57a3c299fce136d8ec79ce73a58303795537f652b3d821e9f4acc635e` |
| `12-launch-handoff--bandit/events.jsonl` | `e357fdec6c081b0d3f7f826176c88b85dd999a569538a1bfa78054ceabac665e` |
| `12-launch-handoff--bandit/metadata.json` | `b73e7299fbd7d9304d05a698c443314399609de0c1d67bf84ecf5517111f8f3c` |
| `12-launch-handoff--bandit-specify/output.md` | `9da4cd5171a9d212f81a9f61b57ad6c39f4c0f7072e6151fdd83b7d5f09e54fd` |
| `12-launch-handoff--bandit-specify/session-tools.jsonl` | `861a07d3be1a1953bd0e7c323d00f11ed88066ab9577a4916f98fd5c5a55e885` |
| `12-launch-handoff--bandit-specify/events.jsonl` | `d236f13691845bc49a8fdcb734fbcf82b72d23733ee5b9f6b36486817096087a` |
| `12-launch-handoff--bandit-specify/metadata.json` | `14b821a2958c6fe4bbe9534f388eee36dd637c8bbaf18088870c92fda19563f5` |
| `15-supported-offer--bandit/output.md` | `12e76a34b72f3212170e89faa6b2abd66022a5a55059ec4d470792b0d75ba7b1` |
| `15-supported-offer--bandit/session-tools.jsonl` | `151bd6ffbbbe565ce09fd46c6b542f1192992e0dbe957f593b65b2b2c283b6df` |
| `15-supported-offer--bandit/events.jsonl` | `40230fcb611275be212f69f6b0afb747ea8256fc6b129de818cebd821bb2eba9` |
| `15-supported-offer--bandit/metadata.json` | `a130d7de28a14edd164c4e4dffe6cfeb3e46aa09ef8f52bb75cd13cf51a99ce8` |

The scope supports one concrete final-round promise contradiction and several explicitly conditional capacity gaps. It does not establish observed overload, customer harm, comparative skill quality, or safety outside these three synthetic executions.
