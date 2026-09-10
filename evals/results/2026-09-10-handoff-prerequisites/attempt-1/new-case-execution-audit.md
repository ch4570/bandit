# Independent execution and source-claim audit — 19-dependent-prerequisites / bandit

This is one run's execution/source-claim audit, without a content score or numeric grade. The preserved arithmetic agrees with the supplied figures, the recorded actions stay within the planning-only boundary, and a four-original Thursday recovery can finish exactly at the accepted 22:00 deadline. One final-correction handoff needs clarification: receipt through 12:00 and review completed by 12:00 are used as different eligibility conditions for the same evening's last recording window.

## Evidence boundary

Run root: `/private/tmp/bandit-prerequisites.4VHSx8/runs/19-dependent-prerequisites--bandit/`.

Read: `original-input/request.md`, the four `original-input/fixtures/*.md` files, `output.md`, `metadata.json`, `session-tools.jsonl`, and relevant event records. The leader additionally authorized the captured `prompt.txt` during this audit. `workspace/input/` was read only to calculate hashes. No skill files, author package, grading rubric, protocol, other run, prior report, or diagnosis was opened. Skill text embedded in recorded read-tool outputs was incidental evidence of what the run read; it was not an audit standard. No delegation, product/code test, account creation, customer communication, posting, payment, contract action, or external action was performed for this audit. The only authored file is this report.

Below, F1–F4 refer respectively to the four numbered fixture files. All evidence claims retain the fixtures' synthetic status; F4's already-sent acceptances are commitments inside the hypothetical case, not real-world contacts observed in this run.

## Integrity and provenance

SHA-256 was independently recomputed from every original input and its workspace counterpart. All five match `metadata.json:83–89`, `360–366`, and their recorded before/after input snapshot entries at `120–144` and `251–275`.

| Input, relative to original-input/ and workspace/input/ | Recomputed SHA-256 in both locations |
|---|---|
| `request.md` | `c182dc08f93a615a7f16d76e5ab21c5d0f53fe8427f4a614ebb16a412cd921fd` |
| `fixtures/01-창업자-메모.md` | `a395eae2a30d742b769a91a1e7c3cce64b7b2b57a67316fee689679b0db4b46d` |
| `fixtures/02-인터뷰-발췌.md` | `244eca29cb5a3ed57e6e79b035d701a857594289c503aa16964e6d9fbac2cb79` |
| `fixtures/03-제작-작업기록.md` | `2c25bfdd34e176945c62b90b4920798f5e04932b20a46369c9e365b057411dc0` |
| `fixtures/04-동아리-주고받은-내용.md` | `915b57d0af36a114473409c8c5d269bc955127803983f109f658122ec86241e7` |

The five raw input bodies are also present in the recorded read result at `session-tools.jsonl:4`; this connects the preserved fixtures to an actual successful read.

| Artifact | Recomputed SHA-256 | Comparison |
|---|---|---|
| `session-tools.jsonl` | `cc5c4b6bc2e092505046cb9102ef3ebe6dbb826a5deaabfb7210c7fb90247c4c` | Matches recorded export hash at `metadata.json:29` |
| `output.md` | `112e009d9e3c1bbe2b53ac4169b269497d8b8dce6283887aaed1cc9e5fa6c8c4` | Exact bytes equal final agent message `events.jsonl:12`, item `item_6` |
| `metadata.json` | `4ca30acb6e61fb9023b825160c5f7b698282b0b2cd583de9cf2e30229e51d79a` | Audit fingerprint; no separate expected hash supplied |
| `events.jsonl` | `be0924cde35ed3047c1b8a78c8f6a478c2c05c4e7d7c1a56bdfecbc7e200c58d` | Audit fingerprint; no separate expected hash supplied |
| `prompt.txt` | `3a80f46010071bf321787e255df612553e55a660ebb914100dd484de7dceff2c` | Audit fingerprint; no separate expected hash supplied |

The eight tool rows form four matching call/result pairs. Their recorded zero-based ordinals plus one are `[13,16,18,21,23,26,34,36]`, matching `metadata.json:31–40`. Counts agree with `metadata.json:41–44`. The host-session source hash at `metadata.json:27` and runner/capture/instruction hashes were not independently rehashed: their original files are outside the permitted audit scope. Verification of this export's hash does not independently prove that all host-session activity was exported.

`metadata.json:229–236` reports passed workspace integrity, no violations or snapshot errors, exit code 0, and 189.589 seconds. The independently checked input hashes support unchanged task inputs. `events.jsonl:13` records a completed turn. `events.jsonl:3` records a skill-description context-budget warning; it is not a failed tool call or failed completion. The output has 1,753 whitespace-delimited words, below the captured prompt's 2,200-word bound (`prompt.txt:3`); this is an explicit counting method, not a token count.

## Actual calls and action authorization

The raw request asks for a planning document and prohibits application/website implementation, accounts, publication, actual contact, payment, and contracts (`original-input/request.md:3–9`). The runner additionally prohibits browsing/contact, executing supplied product code/tests, subagents/model sessions, and file changes, and requires the final artifact to be saved by the runner (`prompt.txt:1–2`). It does not prohibit arithmetic code generally. Therefore the pure JavaScript calculation below is within the captured boundary.

| Session call/result lines | Call ID | Actual operation and observed result |
|---|---|---|
| `1 / 2` | `call_m3QIpOCBF8f4d6hHcQnM69hq` | `exec` wraps `exec_command`: `pwd && rg --files input instructions/bandit`; successful listing, nested exit 0. Also `events.jsonl:5–6`, `item_2`. |
| `3 / 4` | `call_Lt5eZ1NI5EQulk6iyRBjJRBW` | `exec` wraps `exec_command`: reads request, selected skill entrypoint, and raw fixtures; successful read, nested exit 0. Also `events.jsonl:7–8`, `item_3`. |
| `5 / 6` | `call_RN7hyi6qKzMDCBzOTkLfvdKB` | `exec` wraps `exec_command`: reads six selected instruction references; successful read, nested exit 0. Also `events.jsonl:9–10`, `item_4`. |
| `7 / 8` | `call_Saq4S9KEJ08iDnJsftxhympL` | `exec` evaluates a local arithmetic object and emits it with `text(r)`; completed result includes 7, 10, 530, 560, 1,520, 400, 300,000, 25,000, the price contributions, and full labor total. No product code or test is invoked by this expression. |

The calculation is an actual call and result, not just proposed code or an expected result. The CLI event stream contains the three shell executions but does not separately show this calculation; the captured session rows supply that evidence. The narrow execution claim in `output.md:97` is supported by call `call_Saq4S9KEJ08iDnJsftxhympL` and its paired result.

In the captured calls, there is no observed account-creation request, implementation command, customer-message send, recruitment posting, payment, or contract action. Proposed future work and draft copy in `output.md:48–71,101–118` are document content. F4's historical synthetic messages predate this run inside the case (`F4:3,9,15,17`). The record supports the scope of the non-action statement at `output.md:5,97`; it does not establish universal non-action outside the captured trace. This limitation also appears explicitly in `metadata.json:16–17`.

## Independent numerical, date, and unit reconstruction

Recalculation used the raw F1/F3 values, not the literal returned totals or a copied schedule array. Actor totals per unit are `15+10+10+5 = 40` minutes for Dodam and `35+10 = 45` for Sori (`F3:15–25`). Sori has two three-hour windows per week; Dodam has 480 minutes with no day-of-week restriction (`F1:13–14`). The role/version/pause unit and the conjunction of 2 pages, 24 opposite-role lines, and 3 minutes agree with `F3:7–9,29` and `output.md:31–36`. Three minutes means opposite-role voice length, not total playback including pauses.

| Output claim | Recalculation and source | Audit result |
|---|---|---|
| Existing 8, new up to 2; total 10 (`3,44,80`) | 2 clubs × 2 actors × 2 deliveries = 8; proposed 2 new = 10 (`F4:7–9,15`; new count is a proposal) | Matches; no conversion of interview interest into paid purchases |
| Theoretical 7/week (`79`) | floor((6×60−20)/(35+10)) = 7 | Matches; output expressly excludes dependent timing from this theoretical bound |
| Sori 530 min / 8h50 (`81`) | 10×45 + 4×20 = 530 | Matches; four common-work weeks are a conservative planned allocation |
| Dodam production 560; added 960; total 1,520 / 25h20; reserve 400 (`82–84`) | 10×40+4×40=560; 4×(120+60+60)=960; 4×480−1,520=400 | Matches; added tasks are proposal allocations, not measured fixture work |
| Weekly Dodam production 200/120/200/40 (`88`) | Unit counts 4/2/4/0 ×40, plus 40 weekly | Matches; adding 240 admin minutes yields 440/360/440/280, leaving 40/120/40/200 minutes before actual correction shifts |
| Cash 300,000 and max sales 60,000 (`85–86`) | Fixed 160,000+40,000 (`F1:15–17`) + proposed reserve 100,000 =300,000; 2×30,000=60,000 | Matches; revenue does not raise spending cap |
| Direct labor 25,000 (`92–93`) | (40/60)×15,000+(45/60)×20,000=25,000 (`F1:18`) | Matches; internal future-labor assumption, not market wages |
| Contributions −13,000/5,000/15,000 (`93`) | Prices 12,000/30,000/40,000 minus 25,000 | Matches; the recorded call uses `.map(p => p−25000)`, not just literal contribution outputs |
| Shared labor ≈16,667/week; minimum 4 at 30,000 (`95`) | (40/60)×15,000+(20/60)×20,000=16,666.67; ceil(16,666.67/5,000)=4 | Matches. Ceiling 4 was independently recomputed; it is not a field returned by the run's calculator. It covers common labor only, as qualified in the output. |
| Entire planned labor ≈556,667 (`95`) | (1,520/60)×15,000+(530/60)×20,000=556,666.67 | Matches; direct production labor is contained in these totals and is not added again |

The calculation call uses literal 1,520 and 530 in its final labor expression and literal 25,000 for its price subtraction; recomputing those upstream quantities independently confirms them. The cash reserve, proposed price, new-customer limit, admin allocation, and thresholds are choices, not facts measured from the fixtures. The output labels them as proposals and prospective criteria (`5,40,128–136`). It also preserves the distinction between cash affordability and ongoing economic viability (`93–95`).

The calendar was independently computed: 2026-10-05 is Monday; 10-06/13/20/27 are Tuesday; 10-08/15/22/29 are Thursday; 10-14 is Wednesday; 10-30 is Friday; 10-31 is Saturday; 11-01 and 11-08 are Sunday. 10-05 through 11-01 contains 28 calendar days. All stated weekday/date relationships agree. Deleting by 11-08 is seven days after the pilot end, consistent with `F4:17`; recommended deletion on 11-01 is earlier (`output.md:124`). Source September dates are explicitly hypothetical fixture dates (`F1:3; F2:3; F3:3; F4:3`), not observations newly made on the September 10 execution date.

## Dependent paths and final closure

### Existing actors: normal and permitted late inputs

All four existing actors—별-1, 별-2, 막-1, 막-2—share the two accepted cycles: input 10-06/10-20 by 12:00 and delivery 10-08/10-22 by 22:00, free, with one same-script/role pause or reading correction per bundle (`F4:7–9,15`; `output.md:44`). Actual scripts and role labels remain unverified (`F4:15,23`).

On the normal path, Dodam's Tuesday 12:00–14:00 window can contain four 15-minute initial checks. Requested supplementation returns by 17:00, is rechecked by 18:00, and then precedes Sori's 19:00 start (`output.md:49,58`). Four 35-minute originals plus 20 common minutes require 160 of Tuesday's 180 minutes; Wednesday/Thursday remain available for Dodam's four 20-minute checks/deliveries. No source gives a tighter weekday restriction for Dodam. The output asks on 10-05 for participant confirmation availability (`48`); actual participant responsiveness is not established by this document.

For all four inputs missing Tuesday but completed by Wednesday 18:00, the output explicitly permits Dodam's Thursday recheck by 12:00 and Sori's Thursday production (`59`). A reconstruction that reserves all 20 common minutes before production, conservatively delaying every result, is:

| Bundle in processing order | Sori result ready | One feasible contiguous Dodam 20-minute check/delivery slot |
|---|---|---|
| 1 | 19:55 | 20:40–21:00 |
| 2 | 20:30 | 21:00–21:20 |
| 3 | 21:05 | 21:20–21:40 |
| 4 | 21:40 | 21:40–22:00 |

This proves that `output.md:59,88` can be scheduled, including Dodam's stated 80 consecutive minutes; it is not a schedule the run's calculator executed. The last handoff has zero slack for errors, transfer delay, or a result not ready at the assumed time. Four original bundles plus four 10-minute corrections and 20 common minutes would take 200 minutes, exceeding a 180-minute Thursday. The output recognizes this collision and defers conflicting corrections (`59,90`). On the second cycle, earlier corrections may likewise require 10-27 rather than that fully occupied 10-22. Such deferral needs the individual next-window notice the output proposes; pausing new intake alone does not complete old obligations.

Inputs still incomplete or oversized after Thursday 12:00 are not falsely represented as deliverable at the original deadline (`60`). The output keeps the old promise and makes renegotiation a required unresolved action. Wednesday 18:00 is the clearly stated late-input admission limit; the document supplies no distinct guaranteed treatment for an input newly completed between that limit and Thursday 12:00. This interval should not be silently interpreted as a further guaranteed late path.

### New paid actors and channel/customer prerequisites

The selected prospective offer has at most two one-bundle payers at 30,000 each (`output.md:3,40,106`). Existing actors remain free. New participants' input, rights, delivery route, price, schedule, and payment are commitment prerequisites (`40,61,114–115`). If these are incomplete by 10-13 at 12:00, the plan does not ask for payment and moves the case to unpaid waiting (`61`). The specification sets a completion gate, not a promise that someone first applying at 12:00 will have time for review and payment.

The channels are conditional: 별무리 decides after trying the first output; 느린막 only offered review after 10-12 (`F4:11,19`; `output.md:101`). The run does not transform either into guaranteed posting or recommendations. If the opportunity misses the 10-13 input/payment window, paid provision becomes zero and demand remains inconclusive. Up to six applications and ten-minute rejection/waiting notices are bounded (`50,88`); actual processing burden is not measured.

On 10-13, Sori can perform 20 common minutes, up to four old 10-minute corrections, and two 35-minute new originals in 130 minutes, ending 21:10 if common work and old corrections go first. Dodam can check/deliver the two new bundles by 10-14 at 18:00 (`50,106`) within her unrestricted-day condition. That delivery precedes the next ordinary reviewed-correction cutoff, 10-15 at 12:00. Thus a customer who can inspect and respond by that cutoff has a Thursday-evening correction and Friday-noon redelivery path. Their availability remains a prerequisite to confirm, not an observed fact. Neither an eligible offer nor a completed document demonstrates a paid conversion (`F2:3,8,16`; `output.md:128–135`).

### Final correction handoff: observed inconsistency and bounded interpretation

`output.md:65` admits same-evening corrections when Dodam has **reviewed** the request by Tuesday/Thursday 12:00. `output.md:67` says **receipt** through Thursday 10-29 at 12:00 can enter the final recording, then 10-30 at 12:00 redelivery, 10-31 at 12:00 customer confirmation, and 11-01 at 12:00 Dodam reply/access recovery. Paid-facing copy repeats the receipt cutoff (`106`).

A request arriving at the final 12:00 cutoff has no positive interval for Dodam to review it before that same 12:00 eligibility deadline. The fixture reserves five Dodam minutes per included correction (`F3:21`), but the document does not separate that review time from receipt or name a later review-completion window for this final exception. This is a documented prerequisite mismatch for the latest admitted request. It is not proof that Thursday production is physically impossible: Dodam is not weekday-restricted and could review during the afternoon, if the plan expressly changed the staff review cutoff while preserving enough time before 19:00. Alternatively, an earlier receipt cutoff would need to appear consistently in the prospective offer and flow. The run's successful aggregate arithmetic does not resolve this handoff mismatch.

If requests are already reviewed by the applicable final cutoff, at most ten 10-minute included voice corrections plus 20 common minutes total 120, within Thursday's 180 minutes; ten five-minute Dodam correction allowances total 50. The 10-30 → 10-31 → 11-01 sequence therefore leaves real calendar time for customer review and Dodam's response, and week 4 has substantial planned Dodam reserve. Source timing estimates do not establish that every vendor-dependent access recovery or repeated error can actually finish in that interval.

The output explicitly preserves an honest boundary at `69`: audio corrections after 10-29 and repeated errors in the final corrected file remain unresolved obligations, with follow-up staffing, dates, and customer agreement to be secured by 11-01. It does not assume Sori is available next month, consistent with `F1:14,16`. The document must not be reported as proven end-to-end closure of every existing correction right. Its final communication and access-recovery promise at `67` is narrower than such closure. The customer-confirmation availability prerequisite is explicitly stated there; after any 11-01 access recovery, a further customer confirmation window is not expressly scheduled. This is an unproven closeout detail, not observed customer nonresponse.

## Preserved gates and remaining unknowns

The output appropriately leaves pause durations unmeasured (`38`), channels uncommitted (`101`), phone/locked-screen playback unverified (`120`; `F3:31`), and rights scope, recipient control, deletion and payment/refund provider behavior unconfirmed (`48,71,122,139`; `F1:22; F3:31; F4:23`). A possessed link is not treated as authorization (`122`). The 10-05 activity for Sori is specification/example review; the wording does not establish prohibited Monday recording, so no Monday production violation is inferred.

New commitments are gated on route checks and future staffing (`40,139,141`). Existing 느린막 deletion and recipient restrictions remain binding (`F4:17`; `output.md:122–124`). Proposed deletion on 11-01 uses staff within the pilot and does not claim remote deletion of customer downloads. Whether any post-pilot correction agreement can operate while meeting the 11-08 deletion promise remains to be arranged; this record confirms neither future resources nor an agreed exception to deletion.

The supported finding is the final receipt/review-cutoff mismatch. The other material limits are explicitly conditional or unresolved: no timing slack on the full Thursday recovery, unconfirmed participant response availability, provider-dependent access/payment/deletion behavior, and continued existing duties without confirmed post-pilot staffing. These remain visible in the audit rather than being treated as successful execution or as fabricated external actions.
