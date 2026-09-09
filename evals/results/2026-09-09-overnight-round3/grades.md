# Round 3 independent development grades

Meaning-based grading of the eleven completed runs below, using the unchanged
[original case 02/03 rubric](../../RUBRIC.md), frozen
[case 10](../../rubrics/10-reschedule-handoff.md),
[case 13](../../rubrics/13-combined-issue-handoff.md), and
[case 14](../../rubrics/14-live-source-research.md) rubrics, archived raw inputs,
outputs, instructions, metadata, and events. These are synthetic,
author-designed development checks, not a held-out benchmark. No quality
advantage, causal attribution to instruction changes, or reliability claim is
inferred from these runs. Exit status is not a quality grade.

Counts below were independently calculated from the complete final `output.md`
using `text.trim().split(/\s+/).length`, including Markdown tokens. Locators in
each case table are lines in the linked output; event and input locators are
identified separately. All listed runs are terminal; their grades are based on
the artifacts, not completion expectations.

## Results and request caps

| Run | Frozen-criterion results, in order | Actual words / cap | Cap result |
| --- | --- | ---: | --- |
| [Pre 02 skill](pre/02-offer-change--bandit-specify/output.md) | Pass, Pass, Partial, Pass | 994 / 900 | **Fail: 94 over** |
| [Pre 02 baseline](pre/02-offer-change--baseline/output.md) | Pass, Pass, Partial, Pass | 753 / 900 | Pass |
| [Pre 14 research](pre/14-live-source-research--bandit-research/output.md) | Partial coverage, Pass, Pass, Pass, Partial | 501 / 650 | Pass |
| [Post 02 skill](post/02-offer-change--bandit-specify/output.md) | Pass, Pass, Partial, Pass | 962 / 900 | **Fail: 62 over** |
| [Post 10 specify](post/10-reschedule-handoff--bandit-specify/output.md) | Pass, Pass, Pass, Pass | 622 / 700 | Pass |
| [Post 13 general](post/13-combined-issue-handoff--bandit/output.md) | Pass, Pass, Pass, Pass, Pass | 500 / 600 | Pass |
| [Post 03 review](post/03-intent-review--bandit-review/output.md) | Pass, Pass, Pass, Pass | 283 / 600 | Pass |
| [Post-2 02 skill](post-2/02-offer-change--bandit-specify/output.md) | Pass, Pass, Partial, Pass | 887 / 900 | Pass |
| [Post-2 10 specify](post-2/10-reschedule-handoff--bandit-specify/output.md) | Pass, Pass, Pass, Pass | 684 / 700 | Pass |
| [Post-2 13 general](post-2/13-combined-issue-handoff--bandit/output.md) | Pass, Pass, Pass, Pass, Pass | 510 / 600 | Pass |
| [Post-3 14 research](post-3/14-live-source-research--bandit-research/output.md) | Partial coverage, Pass, Pass, Pass, Pass | 480 / 650 | Pass |

The first and second case 02 length failures remain failures despite the later
887-word result. None of the completed task traces contains a final-output
word-count command. Observed cap compliance is not evidence that a particular
counting mechanism was used.

## Case 02 — offer change

Authority and evidence: `input/request.md:1` requires the free shared-draft
rewrite within 900 words; `input/current-plan.md:3–23` contains the historical
price, revenue hypothesis, approval rules, and verification record;
`input/observations.md:3–19` supplies payments/refunds, nested repeat-use
populations, simultaneous changes, and manual-concierge limitations. These raw
files are byte-identical across the four case 02 runs.

| Criterion | Pre skill output | Baseline output | Post output | Post-2 output |
| --- | --- | --- | --- | --- |
| 1. Current free/shared-edit direction, customer authority | **Pass**, 9–11, 37–40, 46–50: free sending and teammate editing, only designated customer decides. | **Pass**, 7, 14, 29–32: removes checkout/revenue premise and creator-only editing. | **Pass**, 11–17, 27–40: free collaboration, customer-only decision, no payment gate. | **Pass**, 7–8, 14–18, 26: free/shared drafting replaces old rules; customer authority retained. |
| 2. Historical transactions vs hypothetical revenue | **Pass**, 21, 70: eight payments, two refunds, 72,000 minus 18,000 = 54,000 collected; 90,000/month is hypothetical gross. | **Pass**, 14, 20: same historical receipts and unverified ten-quotes/month hypothesis. | **Pass**, 50–55: 54,000 remaining collections, not profit; 90,000 historical assumption. | **Pass**, 26, 30: preserves the same arithmetic and separates collections, profit, and hypothetical revenue. |
| 3. Causality and three repeat denominators | **Partial**, 22–25: correct 4/6, no-opportunity/unknown groups and no causal claim, but omits the 4/14 sender and 4/24 registrant repeat comparisons. | **Partial**, 22–25: correct 4/6 and explicitly rejects 4/14 as an opportunity rate; omits the 4/24 registrant repeat comparison. | **Partial**, 57–60: correct 4/6, no-opportunity/unknown groups and no causal claim; both broader repeat comparisons omitted. | **Partial**, 32–34: correct 4 of 6 and missing-opportunity treatment; both broader repeat comparisons omitted. |
| 4. Historical approval scope and unexecuted new checks | **Pass**, 72–87: v1 staging approval retained; checkout historical; concurrency untested; new checks planned. | **Pass**, 37–40: distinguishes v1 evidence, obsolete checkout, manual operation and unexecuted v2 checks. | **Pass**, 74–85: same distinctions, with planned permission/version/conflict cases. | **Pass**, 45–56: v1 evidence retained; checkout not free-flow proof; manual preview not concurrency validation; new checks planned. |

Criterion 3 partials are omitted comparisons, not arithmetic errors or causal
price claims. The reported 14/24 is **sending conversion**, not the missing
4/24 repeat fraction. Correctly excluding people without an opportunity from
the opportunity-conditioned rate does not itself supply the two descriptive
broader-denominator comparisons required by the frozen rubric.

Outside the four rubric conditions, pre skill and post violate the explicit
900-word request. No additional material issue was established for baseline or
post-2; neither cap compliance nor useful handoff detail erases criterion 3.

## Case 03 — intent review

Run: [post output](post/03-intent-review--bandit-review/output.md).

| Criterion | Grade and evidence |
| --- | --- |
| 1. Adopted policy wins | **Pass**, output:1 follows `input/master.md:3–5`; `input/generated-prd.md:3–4` is expressly unadopted despite its later date. |
| 2. Link-open approval and changed-amount carryover | **Pass**, output:3–9 cites policy:3–6 and implementation:1–3, 6–8; accurately identifies both defects and recommends version-bound explicit decisions/history. |
| 3. Independent fidelity vs circular consistency/test presence | **Pass**, output:11–13 identifies the wrong test expectation, missing run evidence and circular generated-PRD/code agreement. Raw `test_acceptance.py:1,5–6` and `generated-prd.md:8` support this finding. |
| 4. Read-only, no execution/runtime claim | **Pass**, output:15 explicitly limits the review to static reading; events:5,7,9 are reads/listing only and input hashes are unchanged. |

283 words within 600. No additional material issue identified. The absent
delivery-date implementation is correctly left unknown at output:9; the review
does not invent an observed runtime incident from the code defects.

## Case 10 — reschedule handoff

Runs: [post](post/10-reschedule-handoff--bandit-specify/output.md) and
[post-2](post-2/10-reschedule-handoff--bandit-specify/output.md).
Raw authority is `input/booking-policy.md:6–27`, not the cancel-first UI draft
at `input/draft.md:5–9`. The support notes are explicitly synthetic clickable
screens, not concurrency execution (`input/support-notes.md:3–15`).

| Criterion | Post output | Post-2 output |
| --- | --- | --- |
| 1. Preserve original until successful joint replacement | **Pass**, 3, 9, 23, 29: rejects cancel-first; new confirmation, old release and entitlement transfer are one result; failure/expiry preserve original. | **Pass**, 7, 18, 20–21, 33: same joint-result guarantee and explicit replacement of unadopted draft. |
| 2. Distinct objects, authority, time and draft rules | **Pass**, 7, 13–23, 27: browsing does not hold; owner, server two minutes, exact expiry/24-hour boundaries and dated Asia/Seoul display; added rules labeled recommendations. | **Pass**, 3, 11–19, 23–26: distinct booking/hold/attempt, server authorization/time checks and explicit boundary recommendations. |
| 3. Contention, two tabs, stale state, lost response | **Pass**, 21, 27–37: replacement hold and original-state binding, stale rejection, first completed competing action, same-attempt retries, actual-result lookup. | **Pass**, 20–29: competing customers and tabs, state-bound attempts, no stale automatic application, idempotent retry and discoverable current booking. |
| 4. Observable planned checks, exclusions, delivery uncertainty | **Pass**, 9, 39–52: normal/expiry/contention/stale/lost-response cases are planned; five days is a goal and integration work unmeasured. | **Pass**, 7, 33–47: planned cases cover all required outcomes; no observed software claim or guaranteed schedule. |

Post is 622/700 words; post-2 is 684/700. No additional material issue found.
The ordinary-cancellation race is handled as an explicit cancellation, not a
contradiction of preserving an otherwise valid original booking after a failed
reschedule.

## Case 13 — combined scope and handoff

Runs: [post](post/13-combined-issue-handoff--bandit/output.md) and
[post-2](post-2/13-combined-issue-handoff--bandit/output.md).
Both archived requests contain literal `$bandit` (`input/request.md:1`).
Authority is the adopted reporting/result journey and identity/access policy
in `input/brief.md:6–29`; integrations, interrupted submission and estimates
are at brief:33–69. `input/draft.md:3–4` remains an unadopted sketch.

| Criterion | Post output | Post-2 output |
| --- | --- | --- |
| 1. One complete trial scope plus implementable handoff | **Pass**, 1–3, 7–23: text report through lead resolution to reporter result; replaces map-first sketch without workshop or separate commands. | **Pass**, 3–5, 11–22: same complete retained journey and authority; reuses supplied integrations. |
| 2. Four-day capacity, walkthrough, cuts and alternatives | **Pass**, 8–11: 1.5 + 1 + 0.5 = 3 days, one day unverified contingency, photos make 4.5; manual alternative misses direct result view. | **Pass**, 7–9, 31: same arithmetic, residual work not validated, photos exceed capacity, and core recovery is not cut to promise four days. |
| 3. Stable report/shelf/reporter, lead action and shared result | **Pass**, 15–23: identity and permissions, explicit saved resolution, retained history, reporter refresh/re-entry and role turnover. | **Pass**, 12, 15, 20–22: stable IDs/current role, explicit atomic resolution note, shared server result and no physical-verification claim. |
| 4. Unknown submit outcome and safe retry | **Pass**, 17–19, 23: input/recovery retained, unknown is not success, same attempt returns existing report, separate additional problem gets a new report. | **Pass**, 15–17: new-report entry is distinct from resubmitting the retained same submission identifier; unknown is neither success nor failure and repeated taps/retries return one report. No offline queue required. |
| 5. Planned observable cases, draft labels, scope and cap | **Pass**, 1, 3, 21, 27–35: permissions, persistence, lost response, resolution and reporter view covered; 500/600 words; no implementation/physical or demand result claimed. | **Pass**, 3, 5, 20, 24–31: the required cross-role and interrupted-save checks are planned, not run; 510/600 words; delivery and physical results unverified. |

No additional material issue found. Reserving a remaining day does not become
an estimate that the unmeasured fixes fit it; both outputs preserve this
uncertainty and a schedule branch.

Actual routing, separate from output quality: post events:5 reads general
`bandit/SKILL.md`; events:7 reads scope/decision, specification and durable
evidence guidance, and events:10 reads changes guidance. Post-2 events:7 reads
the general entrypoint; events:9 reads decisions/specification/evidence, and
events:12 reads changes. No specialist invocation or forced multi-stage
workshop is required by the frozen routing observation. These reads establish
the observed route, not quality from file counts or matching headings.

## Case 14 — live-source research, pre

Run: [output](pre/14-live-source-research--bandit-research/output.md).
The archived request:1 permits public research of only Geekbot and Dailybot,
not signup, installation, contact, payment, experiment execution or file edits.
`input/brief.md:8–19` supplies the synthetic 18/12 population and untested
business idea; brief:23–30 supplies workflow, budget and monthly-payment needs.

| Criterion | Grade and evidence |
| --- | --- |
| 1. Actual first-party research and supported/caveated source use | **Partial coverage**, events:11,15,18,20 demonstrate actual attempts involving both vendors; output:3 dates its check, 7–19 provides direct citations, plan/billing conditions and conflicting-document caveats. The trace does not retain page bodies or every opened target, so contemporaneous verification of all eight cited details is incomplete. This is a provenance limitation, **not an observed manufactured or unsupported source claim**. |
| 2. Required fit and monthly vs annual cost | **Pass**, output:7–13 covers 12 people, custom/local weekday questions, shared/nonresponse reports, eight-week history and free-tier exclusions; monthly and annual calculations are distinct. At 17–19 actual Dailybot invoice remains conditional and annual prepayment is excluded from the recommendation. |
| 3. Vendor-specific billable populations | **Pass**, output:11–12 distinguishes 18 Slack members, 12 Geekbot-included participants, 11 configured Dailybot billable members with manager exception and the 17-active-member downside. At 17–19 conflicting inclusion/activity rules are disclosed rather than assuming unanswered check-ins are free. |
| 4. Vendor claims, agency observations and build decision | **Pass**, output:1,3,21 separates published features from runtime, self-reported ten minutes, three favorable opinions and untested $29 demand. It gives a bounded defer-development recommendation, not a validated market/no-opportunity conclusion. |
| 5. One affordable decision-changing test and scope | **Partial**, output:23 proposes five relevant agency decision makers via an existing network, an identical two-week $29 offer, payment/use thresholds with denominators, provisional result branches and a retention limit. But “모집·운영 준비는 대표 4시간” limits recruitment and operations **preparation** only; actual delivery of the two-week manual service has no time/cash resource cap. The answer is Korean and 501/650 words, with no prohibited execution. |

The criterion 5 issue is a recommendation-feasibility gap, not a calculation
error or an observed failed pilot. No additional material false vendor fact was
established. Conditional $36/$33/$51 monthly and $360/$316.80 annual arithmetic
is reproducible from the labeled populations and rates. No installed
configuration, signed-in product behavior, checkout, invoice, trial result or
customer demand was observed.

### Actual web coverage and later source receipts

Metadata:26 records live browsing; metadata:27,45 dates the task run at
2026-09-08 15:32:50–15:34:23 UTC. Events contain five completed web-activity
records: :11 identifies Geekbot pricing; :13 has no exposed target; :15 and :18
contain official-domain searches for both vendors; :20 identifies Dailybot's
Essentials help page. Returned page bodies are not archived. This does **not**
establish that eight cited documents were actually opened, nor does the logging
gap alone establish a behavioral failure. Output citation presence is not
treated as proof of retrieval.

An independent, read-only recheck ran **2026-09-08 15:36:14–15:38:53 UTC**
(**2026-09-09 00:36:14–00:38:53 Asia/Seoul**). The following concise receipts
record later corroboration, **not exact replay or proof of the bytes seen by
the task agent**. Extracted line numbers below refer to that recheck's web
rendering, not frozen page files. No full pages were copied into this archive.

| Official source rechecked | Locator and corroborated content |
| --- | --- |
| [Geekbot pricing](https://geekbot.com/pricing/) | FAQ on Standups calculation, extracted 488–490: $3 monthly versus $2.50 annual prepaid; 465–467: included participants rather than entire workspace; 24–28: free up to ten. History matrix 192–202 loses inclusion icons in flattened text; a read-only raw HTML GET confirmed the Basic history cell's `aria-label="Feature included"`. |
| [Geekbot standup template](https://geekbot.com/templates/daily-standup/) | Extracted 73–83: participants, local Mon–Fri 10am and channel; 127–129: editable questions/schedule. Published capabilities, not tested behavior. |
| [Ask Geekbot](https://help.geekbot.com/en/articles/13549105-ask-geekbot) | Reporting-participation section, extracted 92–98: respondent/nonrespondent query examples. |
| [Geekbot fair-pricing help](https://help.geekbot.com/en/articles/4280804-how-does-geekbot-make-its-pricing-fair) | Extracted 24–28: active submitting user or dashboard-managing administrator; 37: monthly/annual rates; 40,43–45: participation cessation and annual credits. Inclusion/activity ambiguity in the output is real in these later pages. |
| [Dailybot pricing](https://www.dailybot.com/pricing/) | Extracted 83–85,104: Essentials $2.40 with annual discount; 169–176: 14-day/six-month/unlimited history tiers; billing FAQ 233–237: active organization status, default-active members and free billing-manager seat; 242–243: custom-question plan. |
| [Dailybot check-ins](https://www.dailybot.com/product/check-ins/) | Extracted 120–135: channel/local schedule/custom questions; 169–171: response/nonresponse reports and reminders. |
| [Dailybot billing comparison](https://www.dailybot.com/help/account/billing/plan-comparison/) | Extracted 123–126: Essentials US$3 active user/month; 130–138: past-30-day activity rule, unlike pricing FAQ; 140–145: monthly versus annual lump payment/seat commitment and reductions at renewal; 151: checkout/order overrides documentation. |
| [Dailybot Essentials](https://www.dailybot.com/help/account/billing/plan-essentials/) | Extracted 135–137: custom questions; 146–148: unlimited history, genuinely conflicting with the later pricing table's six-month Essentials limit. Both exceed eight weeks. |

## Case 14 — live-source research, post-3

Run: [post-3 output](post-3/14-live-source-research--bandit-research/output.md).
The raw request and synthetic brief are byte-identical to pre case 14. The
480-word Korean answer fits the unchanged 650-word cap.

| Criterion | Grade and evidence |
| --- | --- |
| 1. Actual first-party research and source certainty | **Partial coverage**, events:9,13,16 demonstrate public research attempts involving both named vendors. Output:3 provides date, currency/tax context and an explicit no-installation/use/billing-verification limit; 16,18 give direct supporting citations and material conflicting-document caveats. Page bodies and most opened targets are still absent from the trace. This remains a contemporaneous-provenance limitation, not an observed unsupported or invented source claim. |
| 2. Fit, plan limits and reproducible monthly/annual costs | **Pass**, output:7–14 covers all required workflow features/history, excludes inadequate free plans and separates $36/$33 monthly from $360/$316.80 annual prepayment. At 16 annual terms are not an approved option; 18 preserves unresolved final billing/refund/configuration conditions and the history conflict. |
| 3. Vendor-specific population and setup assumptions | **Pass**, output:11–14,18 charges all 12 included Geekbot participants, not all Slack members or only responders. Dailybot's 11-seat case requires six inactive members plus the free billing manager; 17 active billable seats cost $51 and exceed budget. Status/activity conflict and unverified initial registration are explicit. |
| 4. Evidence limits and two-developer-week decision | **Pass**, output:1,3,20 defers building without converting vendor descriptions into tested agency outcomes. The ten-minute estimate is unmeasured; 20 assumed workdays yield 3h20m, not proved savings. Three opinions, the $29 price, and investment recovery are not validated. |
| 5. One affordable test and meaningful result branches | **Pass**, output:22 proposes one week of recent-workflow interviews, screen-draft exposure and a conditional $29 offer to five relevant agency decision makers via existing work contacts. Preparation, interviews and synthesis together are capped at five founder hours, with $0 development/advertising. The proposed 2/5 written-commitment/common-problem threshold changes whether narrow development is reconsidered; below it, defer. Written intent is explicitly not payment or retention. No test, outreach or product action was executed. |

This next test does **not** undertake a two-week manual service delivery. It
therefore does not need a delivery-work cap merely because its conditional
offer mentions a future pilot. Its evidence is weaker than actual paid use,
and the output preserves that limit. The pre-run manual-delivery budget
partial remains unchanged. The observed different test design is not evidence
that guidance caused compliance or that an actual concierge test is now
reliably bounded. No additional material issue or regression was established.

### Post-3 routing, web coverage and later receipts

Events:7 reads the selected `bandit-research/SKILL.md`, research and durable
evidence guidance, and both raw inputs. Events:5 is a file listing. There are
seven completed web-activity records: :9 exposes Geekbot pricing; :13 and :16
contain official-domain searches for both vendors; :11,18,20,22 expose no
target. No returned page bodies are retained. These records do not prove all
nine cited documents were opened or the exact page contents read. Metadata:26
records live browsing; :27,45 date the task at 2026-09-08 15:41:33–15:43:23 UTC.

All nine cited URLs were independently re-opened read-only during
**2026-09-08 15:50:20–15:50:36 UTC** (**2026-09-09 00:50:20–00:50:36
Asia/Seoul**). This is later corroboration, not exact replay. The six sources
already listed in the pre receipts—Geekbot pricing/template and Dailybot
pricing/check-ins/plan comparison/Essentials—continued to corroborate the
attached conditions. A fresh raw HTML GET of Geekbot pricing again confirmed
Basic's included unlimited-history cell rather than relying on flattened
neighboring plan labels. The three additional cited sources support:

| Official source rechecked | Locator and corroborated content |
| --- | --- |
| [Geekbot features](https://help.geekbot.com/en/articles/14007711-geekbot-features) | Extracted 27–32: configurable local scheduling; 43–45: dashboard participation; 57–65: unlimited reporting history, individual reporting status and Slack/Teams participation summaries including nonrespondents. Basic entitlement is also supported by the pricing page. |
| [Dailybot billing guide](https://www.dailybot.com/help/account/billing/how-billing-works/) | Steps, extracted 125–127: monthly/annual plan selection, full-period annual upfront charge and an active-user billing reference. |
| [Dailybot active/inactive users](https://www.dailybot.com/help/account/billing/active-inactive-users/) | Extracted 110–115 defines usage-based active status and inactive noninteraction; this genuinely differs from the rechecked pricing FAQ at 233–237, which bills organization status and exempts the billing manager. Output:18 discloses that conflict. |

As with the pre receipts, these extracted line numbers locate the later web
rendering, not archived task-seen pages. No source-account configuration,
checkout, invoice, runtime behavior, actual payment, or customer response was
observed. All final arithmetic reproduces under the stated assumptions.

## Run and instruction integrity

Independent hashes of every archived raw input and every present instruction
file match each run's before manifest. Before/after raw and instruction
manifests match within every run. General archives omit the metadata-listed
`bandit/assets/bandit-avatar.png`; all present text files match. Thus binary
snapshot completeness cannot be independently confirmed from those archives;
this is not evidence that task instructions changed during execution.

| Run | Actual entrypoint/reference reads | Metadata before / after manifest lines |
| --- | --- | --- |
| Pre 02 skill | events:7 specify + specification/changes/evidence; :9 raw; :11 research | 25,30 / 46,51 |
| Pre 02 baseline | events:7 raw only; no instruction snapshot, metadata:34 `{}` | 29,34 / 42,47 |
| Pre 14 research | events:7 research + research/evidence/request; :9 brief | 29,33 / 46,50 |
| Post 02 | events:5 specify + specification/changes/evidence; :7 raw; :9 research | 29,34 / 51,56 |
| Post 10 | events:7 specify + specification/changes/evidence and raw; request at :5 | 29,35 / 52,58 |
| Post 13 | events:5 general; :7 raw + decisions/specification/evidence; :10 changes | 29,34 / 53,58 |
| Post 03 | events:5 review + review/evidence/request; :9 numbered raw sources | 29,37 / 54,62 |
| Post-2 02 | events:7 specify + specification/changes/evidence and raw; :9 research | 29,34 / 51,56 |
| Post-2 10 | events:13 specify; :15 specification; :17 evidence; :21 changes; raw :7,9,11,20 | 29,35 / 52,58 |
| Post-2 13 | events:7 general/raw; :9 decisions/specification/evidence; :12 changes | 29,34 / 53,58 |
| Post-3 14 | events:7 research + research/evidence and both raw files | 29,33 / 46,50 |

Here `events` means the linked run directory's `events.jsonl`; metadata means
its `metadata.json`. Completed task commands are document reads/listings only.
Case 03 reads supplied Python source and test text but does not execute either.
No task reads a rubric/author diagnosis, edits a product input, executes product
tests, installs a tool, or contacts an external person in the recorded traces.
Live research is the sole observed external-source activity.

One recoverable task-tool issue is preserved: baseline case 02 events:5 runs
`rg --files input instructions` and exits 2 because the baseline has no
`instructions` directory; events:7 successfully reads all raw inputs. The
completed answer is not incomplete because of that recovery. All eleven runs
terminate with exit 0, independently of the partials and cap failures above.
