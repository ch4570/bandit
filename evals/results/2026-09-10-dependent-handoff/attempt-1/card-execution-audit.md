# Dependent card handoff: execution and constraint audit

Audited one settled synthetic run: `runs/16-dependent-handoff--bandit`, dated 2026-09-10. Verdict within this bounded audit: **the proposed dependency order and capacity are consistent with the supplied constraints; the claimed JavaScript calculation has an actual completed call and matching result. No true contradiction was found in the checked claims.** Operational assumptions remain unresolved, particularly the work covered by the operator's reserve.

This is not a full content rubric or evidence of real customer activity. File/line citations below are relative to `/private/tmp/bandit-interactions.ezd9Vq/runs/16-dependent-handoff--bandit/`. Sources were the four `original-input` files, `output.md`, `metadata.json`, `session-tools.jsonl`, and selected CLI event fields. Workspace input bytes were also hashed. No repository skill file, prior run, grading report/criteria, or Issue/PR text was opened. The raw tool export contains recorded instruction-file reads; embedded instruction prose was not used as an audit criterion.

## Dependency order and confirmed resources

The fixture separates preparation (150 operator minutes, September 14–18) from order operations (240 minutes, September 21–October 2), and prohibits transferring those budgets. Designer availability consists only of September 24 and September 30, 18:00–21:00, 180 minutes each, with no transfer of unused time (`original-input/operations.md:3`, `:5`, `:9`, `:10`). The output preserves these boundaries (`output.md:34`, `:39`, `:43`, `:52`, `:53`). Its listed preparation checks are explicitly planned, not completed customer design or usability work (`output.md:109`, `:117`).

| Ordered handoff | Output commitment | Constraint check |
| --- | --- | --- |
| Customer supplies facts and photos; operator checks eligibility/completeness and confirms payment | Apply by September 23 noon; complete materials/payment by 18:00 (`output.md:37`, `:38`, `:83`, `:87`) | Proposed intake buffers precede the first design window. Unsupported facts and excluded work are not promised (`:22`, `:24`). |
| Operator passes confirmed inputs to designer; designer creates initial cards/previews | September 24, 18:00–21:00; previews sent by operator by 21:30 (`output.md:39`, `:40`, `:105`, `:107`) | Initial design stays inside the first confirmed window. Sending already-generated previews is operator work, not extra designer time. |
| Customer reviews the received draft; operator consolidates the final response | September 25–27 evenings, response deadline September 28 noon; operator consolidates that afternoon (`output.md:41`, `:42`, `:93`) | A/B can each spend about 10 minutes in the evening, starting the day after draft arrival through September 28 noon, and cannot preapprove (`original-input/research.md:14`). These evenings provide a real post-draft opportunity. Viewing is not approval; the last response bundle is used. |
| Designer applies that response and exports final files | September 30, 18:00–21:00 (`output.md:43`) | Uses the second confirmed window after feedback exists. No extra customer approval round is promised (`output.md:93`). |
| Operator checks/delivers final files and handles access issues | By October 1 noon; support through October 2 (`output.md:44`, `:45`, `:99`) | Within the confirmed operator period. Customer printing follows delivery; the recorded print submission deadline is October 5 noon (`original-input/operations.md:27`; `output.md:46`). |

The **latest confirmed window for starting this full review-and-revision offer is September 24**, not September 30. Starting the initial draft on September 30 would leave both the A/B response deadline and the last designer window behind it. The output explicitly rejects September 30 starts (`output.md:30`) and does not use the second window's spare time to add first-stage customers. September 23 is a proposed intake cutoff, not a source-established uniquely latest intake time. No alternative path for a late new customer is promised.

Recruitment repeats the price, capacity, actual post-draft response period, and delivery date (`output.md:63`, `:64`, `:66`, `:71`). Nonresponse is not automatic approval: cancellation/refund is disclosed (`:73`, `:101`). Missing the September 24 work cannot be repaired by assuming unbooked design time; the output's contingency requires a usable confirmation opportunity or refund (`:55`).

## Separate capacity and representative economics

Source task times are operator 12 + 8 + 4 = 24 minutes/order, designer 35 minutes initially and 15 + 5 = 20 minutes later, plus 48 operator minutes per trial (`original-input/operations.md:18` through `:25`). Independent audit-side recomputation produced:

| Budget | Calculation | Result and interpretation |
| --- | --- | --- |
| First designer window | `floor(180 / 35)` | 5 orders; 175 minutes used; 5 spare. Binding constraint. |
| Second designer window | `floor(180 / 20)` | Capacity 9 for this stage alone; 5 actual orders use 100 minutes; 80 spare. Does not raise first-stage capacity. |
| Operator order period | `floor((240 - 48) / 24)` | Baseline capacity 8; 5 orders use 168 minutes, leaving 72 minutes. |
| Preparation | `150 / 60 × 20,000` | Separate time value of ₩50,000; no use as order/design capacity. |

These agree with `output.md:50`, `:51`, `:52`, `:53` and the run's returned calculation. Pooling the 360 designer minutes into complete 55-minute orders would incorrectly allow 6; this output avoids that error.

The fixture fixes two designer windows at ₩120,000 total, a one-time ₩10,000 template charge, 3% payment fee, and operator time valued at ₩20,000/hour (`original-input/economics.md:3`, `:5`). At 5 orders × proposed ₩40,000, independently recalculated revenue is ₩200,000; fees ₩6,000; fixed cash costs ₩130,000; cash balance ₩64,000. Baseline order-operation time is 168 minutes = ₩56,000, leaving ₩8,000 before first-time preparation; after another ₩50,000 preparation value the result is −₩42,000. The output agrees (`output.md:123` through `:133`). All four returned scenario rows (0, 2, 4, 5) also matched independent recomputation.

Calculated break-even order counts are 4 for cash, 5 with baseline recurring operator time, and 7 including first preparation; 7 exceeds the feasible 5 (`output.md:137`). These are arithmetic scenarios at the proposed price, not purchase or repeatability evidence. The no-sales row includes both the fixed cash obligation and the explicitly assumed executed preparation/operation process (`output.md:130`, `:135`, `:139`).

## Actual calculation execution evidence

The export contains three completed `exec` calls, each paired with a result by exact call ID:

| Call ID | Call/result evidence | Bounded meaning |
| --- | --- | --- |
| `call_ClBJpQQFfevnArDc2L6Jpf77` | `session-tools.jsonl:1` / `:2` | Local source read/listing; not a calculation or external operation. |
| `call_XDRSiF29Cw7TRphS6aDoB9E6` | `session-tools.jsonl:3` / `:4` | Local source reads; not a calculation or external operation. |
| `call_FQMkawpWxDWsTqx1MQRqfWbT` | `session-tools.jsonl:5` / `:6` | Actual JavaScript arithmetic call/result supporting the execution claim at `output.md:135`. |

The calculation call at line 5 is marked `status: "completed"`, timestamp `2026-09-10T06:38:12.514Z`, ordinal 26. After a source-read call it executes `const rows=[0,2,4,5].map(...)` using `cash:n*38800-130000`, `opsMinutes:48+24*n`, and the corresponding recurring/first economic formulas. Its `text(...)` call also calculates stage capacities and break-even values.

The response at line 6 has the **same call ID**, timestamp `2026-09-10T06:38:12.740Z`, ordinal 29. `payload.output[0].text` says `Script completed`. `payload.output[2].text` contains the actual returned arithmetic JSON, including:

```json
{"n":5,"revenue":200000,"fee":6000,"cash":64000,"opsMinutes":168,"recurringEconomic":8000,"firstEconomic":-42000}
```

That same result returns `capacity:{first:5,second:9,operator:8}`, `breakEven:{cash:4,recurring:5,first:7}`, and full-case designer times 175/100, operator 168, preparation 150. The auditor recomputed the values in a separate read-only Node call; this cross-check is additional evidence, not a substitute for execution in the original run.

CLI events record successful shell-read completions at `events.jsonl:6`, `:8`, `:11`, but do not expose this JavaScript calculation as a distinct shell command. That absence does **not** mean it was unexecuted: the paired raw session rows supply affirmative evidence. The capture warning explicitly states the limitation (`metadata.json:16`, `:17`). The final CLI agent message at `events.jsonl:12` matches `output.md` after whitespace trimming, and the turn completes at `:13`. The diagnostic at `events.jsonl:3` only reports shortened skill descriptions; it is not a calculation failure.

## Integrity and scope

Recomputed SHA-256 of `session-tools.jsonl` equals `metadata.json:29`:

`2c0286d96c120d3731e17f5364640e9b93b4f0a51ad5e1ef23eba671c5f82d05`

All four original input hashes equal their current workspace input hashes and both metadata input manifests (`metadata.json:81` through `:85`, `:339` through `:343`):

| File | Verified SHA-256 |
| --- | --- |
| economics.md | `7f50a6dcc7b6a2a16dce37caefca463747e183fa74291720199344b31717f22e` |
| operations.md | `e3b1fc177f74d04a6a04af70b31facfd2022ab1423371ea013ad65ca38e3e3a5` |
| request.md | `f758032be79595a2373a566a7418fdee4ed1c04f2288db2ec8a8b77841721954` |
| research.md | `3ae661fd19859ac784dddc906ccf674ee92f4416c578d17fdb5c101b69cbe78a` |

Current `output.md` hash is `d8a798cf89811f1613dd6eeb364688db1841e292f434e1e6d88a52a0a64f30da`. The metadata's recorded before/after workspace snapshots are identical and report integrity passed with no violations (`metadata.json:217`, `:218`). Only actual input files and the tool export were independently hash-verified; this audit did not reopen instruction files to validate their hashes.

The export has six records, three calls and three results, matching `metadata.json:39` through `:43`. Metadata maps these to source-session lines 13, 16, 18, 21, 27, 30, out of 38 source lines (`:28`, `:31` through `:37`); export ordinals are consistently those line numbers minus one. Thread IDs agree between `metadata.json:26` and `events.jsonl:1`. The original retained host session and capture module are outside the assigned run, so their metadata hashes were **not independently authenticated**. Hash agreement establishes consistency with these local manifests, not externally authenticated provenance.

The fixture explicitly marks people, trades, and figures as synthetic and prohibits real contact/search (`original-input/request.md:3`). The captured actions are source reads and calculation; no captured command performs customer contact, payment, design delivery, printing, or other external business operation. The output itself calls its checks planned and acknowledges missing demand evidence. This audit establishes a calculated proposal on synthetic inputs, not completed service work or validated demand.

## True contradictions versus unresolved assumptions

**True contradictions:** none found in the audited dependency order, confirmed-window placement, separate capacities, representative cost/time components, or calculation-execution claim.

**Unresolved assumptions:**

- The first designer window has only 5 spare minutes. The proposal fits the rehearsal measurement but does not establish tolerance for rework or delay (`output.md:50`, `:55`). No alternate designer availability is confirmed.
- The 72-minute operator reserve includes required preview sending, reminders, final-file checking, and possible exceptions; their actual duration is unmeasured (`output.md:52`). The ₩8,000 recurring surplus assumes only baseline 168 minutes. Another 24 minutes eliminates it, as the output states (`:137`); using all 240 minutes yields a recurring balance of −₩16,000. The output discloses this uncertainty, so it is not a proven arithmetic omission, but neither is the ₩8,000 a fully measured end-to-end margin.
- Only A/B have observed review-window availability. The broader offer filters new applicants for the same schedule (`output.md:66`, `:83`), but availability, 10-minute task sufficiency, and 5 paying customers remain unverified (`original-input/research.md:3`, `:14`).
- Refund-fee return, taxes, extra cash expenses, printer pricing/receipt timing, next-month designer supply, and post-market analysis time are not proven. The output identifies the applicable limits (`output.md:99`, `:101`, `:135`, `:147`, `:149`); no external operation was inferred to resolve them.
