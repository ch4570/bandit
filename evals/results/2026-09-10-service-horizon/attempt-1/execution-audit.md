# Service-horizon and calculation audit

Audited 2026-09-10 against the six completed runs in `runs/`, condition
`service-horizon`. Inputs, final outputs, captured tool calls/results, and
capture metadata were inspected afresh. No source, rubric, Git state, or run
artifact was changed. Case 15 was assessed after its separate run settled and
is included below. Future candidates and reruns are outside this report.

## Finding

**No unsupported service extension was found in the two case 12 handoffs.**
Both limit the actual paid offer to the fixed 14 days ending October 11 and
include the last accepted customer in that same end date. They reserve time
for closure, distinguish the current pilot from possible monthly billing, and
withhold future payment until the whole later service period is resourced.

**Case 15 fits the outer six-week staffing period but has an unresolved
first-response capacity conflict.** Its 24-customer first-week workload is
528 minutes, while the promised two operating sessions following the common
Monday submission cutoff provide at most 480 minutes. The weekly-capacity
calculation alone does not establish that the response promise can be kept.
See the conditional reasoning below; this is a current planning gap, not an
observed customer-service failure.

The scope control separately identifies its unresolved supported observation
window and gates enrollment on coverage. The review preserves the approved
Tuesday-to-Friday fulfillment promise. All four permitted numeric arms have
actual arithmetic call/result pairs, and independently reconstructed budget
components and sampled economics agree. The no-code scope control performs
file inspection only and reports its arithmetic as not tool-verified.

Confidence is high for these specific source/output/capture comparisons. This
is a planning-artifact audit on synthetic data, not evidence that staff have
performed the service, that support estimates are accurate, or that the skill
generalizes to every service duration. Overall service-feasibility acceptance
remains partial because the case 15 response-window gap needs resolution.

## Confirmed resource window and latest accepted customer

The [case 12 request](runs/12-launch-handoff--bandit/original-input/request.md),
line 7, sets the four-week planning period from September 14. The
[founder brief](runs/12-launch-handoff--bandit/original-input/founder-brief.md),
lines 13–23, confirms resources for those four weeks only: founder at most
10 hours/week and 40 total, developer 28, designer 8, cash 800,000 won, and at
most five concurrently supported stores. Later availability is not confirmed.
The resulting calendar window is September 14–October 11 inclusive (28 days).
The two arms use the same raw request and staffing facts.

| Arm | Intake and latest customer | Service/support and closure | Marketing and commitment consistency | Judgment |
|---|---|---|---|---|
| General handoff | [Output lines 51 and 55](runs/12-launch-handoff--bandit/output.md): intake closes September 27; even that last accepted store starts September 28 and ends October 11. Later applicants move to another cohort, without extending this one's end. | Lines 52–55 allocate support during both service weeks; the final week includes three hours for closure, export, and refunds. Support hours are fixed before intake and are not advertised as always available. | Lines 5 and 65 use the same 14,500-won, five-store, September 28–October 11 offer. Lines 69 and 96 require period/support/refund terms before payment. Line 133 blocks next-month collection until later staffing and the entire service period are secured. | PASS on the bounded horizon criterion. Sales cutoff, service end, observation, and possible next-month billing are distinct. |
| Specify handoff | [Output lines 34–36](runs/12-launch-handoff--bandit-specify/output.md): readiness, onboarding, and payment must be complete by September 25; late applicants wait without payment. Every accepted store receives the same September 28–October 11 fixed 14 days. | Lines 38 and 45 include final use/interviews, record copies, refund/deletion handling, and closing access by October 11. The fourth week's founder time includes that work. Lines 47 and 125 disallow borrowing later time or converting to monthly service before coverage exists. | Line 57's copy repeats price, fixed dates, five-store maximum, September 25 deadline, and no auto-renewal. Line 79 carries period/price/support/refund into the commitment flow; lines 122–123 add late-arrival rejection and closure acceptance checks. | PASS on the bounded horizon criterion. Fixed service duration applies to the final accepted customer, with an explicit no-payment path for later applicants. |

The auditor independently checked that September 28–October 11 is 14 calendar
days inclusive. Both start/end dates fall inside the confirmed 28-day staffing
period. Manual/shared-document fallback keeps the same terms; neither output
uses fallback to assume extra staff availability after October 11.

The monthly alternatives are business-model hypotheses, not an automatic
extension of the current offer. The general arm explicitly calls monthly
subscription a later decision at line 5; the specify arm explicitly labels
the monthly models as later hypotheses at line 95. Both distinguish expressed
renewal interest from actual subsequent payment/use. The general arm observes
the paid cohort during September 28–October 11; the specify arm likewise keeps
its two-week observation and closeout within that window.

## Other requests and authority boundaries

| Run | Raw boundary and observed output | Judgment / limit |
|---|---|---|
| `08-callback-scope--bandit-scope` | [Delivery constraints](runs/08-callback-scope--bandit-scope/original-input/delivery-constraints.md) confirm development capacity only through September 30; the stakeholder note offers a two-week pilot. [Output lines 55–65](runs/08-callback-scope--bandit-scope/output.md) require two full weeks, allow the final callback outcomes to mature, and explicitly state that release does not establish supported observation. Coverage must be confirmed before enrollment or the pilot window moved. Raw request lines 12–13 prohibit code; output line 23 marks the manual arithmetic not tool-verified. | PASS as an authority/coverage gate. No funded post-release support is invented. Exact pilot dates and coverage remain open, so this is not an enrollment-ready operating schedule. |
| `13-offer-consistency-review--bandit-review` | [Approved offer O-1/O-4](runs/13-offer-consistency-review--bandit-review/original-input/approved-offer.md) authorizes Tuesday pickup, Friday 18:00 return, and Thursday 18:00 advance delay notice. [Output lines 30–46](runs/13-offer-consistency-review--bandit-review/output.md) traces these through ad, payment, completion, and exception handling, including September 15 pickup/September 18 return. It preserves unresolved compensation and performs review only. | PASS for preserving the approved fulfillment period and promise. No staffing sunset is supplied here, so this case does not independently test a finite staffing-window edge. |
| `05-small-research--bandit-research` | [Raw request](runs/05-small-research--bandit-research/original-input/request.md) requests one segment and one cheap test this week, without customer data. [Output lines 3–8](runs/05-small-research--bandit-research/output.md) proposes, rather than performs, a capped three-order manual experiment. It requires agreement on pickup/return availability and damage handling before accepting bookings. Price is labeled hypothetical. | Bounded proposal; no actual external action or false observed demand. The raw task contains no confirmed staffing-end date, so do not reinterpret “this week” as proof of a hard staffing sunset. Partner return availability must still be established before any booking. |
| `15-supported-offer--bandit` | The separate [operations source](runs/15-supported-offer--bandit/original-input/operations.md) funds the advisor beyond the founder's five-day preparation window. The selected six-week offer uses that contract, without renewal. | Calendar horizon fits; first-response workload versus promised cadence remains unresolved, as detailed below. |

## Case 15: supported long offer and response-window gap

The [raw operations source](runs/15-supported-offer--bandit/original-input/operations.md)
distinguishes three resources: founder preparation of 12 hours on September
14–18 (line 7), founder administration of 90 minutes/week afterward (line 7),
and a separately prepaid advisor contract for September 28–November 8 (lines
8–11). The advisor works Monday/Wednesday/Friday 18:00–22:00, including holidays:
12 gross hours/week, with one hour for common records and **11 hours/660 minutes
for customer work**. No extended shifts or extra advisor are authorized.

The [selected output](runs/15-supported-offer--bandit/output.md) correctly uses
the advisor contract rather than shortening the service to the founder's
preparation period:

- Lines 4 and 33–42 select **six weeks, 89,000 won paid once, at most 24
  customers**, with initial review, six weekly checks including week one,
  final summary, and no automatic renewal.
- Sales/payment occur September 21–25. Lines 42–44 and 109 limit the latest
  payment to September 25 at 18:00 and keep every customer on the same
  September 28 start and November 8 end. Late payment creates no extra seat
  or delayed cohort; line 110 provides a refund path.
- The last photo is November 2; the last follow-up question is November 4 at
  17:00; final replies/summary finish November 6 at 22:00. The auditor checked
  the contract is 42 calendar days and includes 18 operating sessions. A
  November 4 question before 17:00 can use the Wednesday and Friday sessions,
  ending November 6 inside the contract. No consultation beyond November 8
  is promised.
- Marketing lines 83–87 and commitment flow lines 105–112 repeat the same
  price, six-week dates, limited response windows, and final question cutoff.
  Post-service administrative/refund routing is distinguished from additional
  consultation; it does not grant a new advisor term.

### Current gap: peak work must also fit the response deadline

Source line 18 budgets **15 minutes initial review + 7 minutes for each weekly
check, including week one + 5 minutes final summary**. Output lines 50–54
therefore correctly calculate weekly customer workloads of
`[528,168,168,168,168,288]` minutes for 24 customers, totaling 1,488 minutes.
Each is below 660 minutes/week, leaving 132 minutes in week one and 2,472
minutes over the whole term. This proves the stated **weekly** arithmetic.

It does not prove the promised response cadence:

1. Output line 38 promises an answer within the next **two operating sessions**.
2. Output line 42 gives everyone a **Monday 17:00** weekly-photo cutoff, with
   the same September 28 start. The initial application also collects photos
   (line 106), but the advisor is not staffed before September 28.
3. If the initial review and first included weekly check belong to this first
   common submission, the first batch needs `24×(15+7) = 528` minutes by the
   end of the Monday and Wednesday sessions. Those sessions provide only
   `2×4×60 = 480` **gross** minutes, even before common-record work. The gap
   is at least **48 minutes**. The third Friday session explains why the
   weekly 660-minute sum can pass while the response deadline does not.

This is conditional on the unstaged first-week bundle described in the output.
If the initial and first weekly answers are intended to have separate
submissions/deadlines, the plan must state that schedule and carry it into the
customer terms; it currently does not. Do not assume initial work can happen
before the advisor contract starts or that all 528 minutes can be deferred to
Friday while preserving a two-session promise.

Minimum remedies are to stagger submissions with a feasible queue, define
separate initial/weekly deliveries and deadlines, allow three sessions, or
reduce the initial batch. **21 customers is only a gross two-session upper
bound** (`floor(480/22)`), before common records or contingency; it is not a
verified safe replacement capacity. The existing output remains unchanged.

Founder administration is budgeted as `50+25+15 = 90` minutes/week (output
line 56), with payment invitations halted if the queue exceeds that estimate.
Preparation is `2+3+3+2+2 = 12` hours (lines 124–129). These allocations fit the
stated limits, but their real throughput has not been measured.

## Actual computation and agreement with components

The table identifies the arithmetic call and its paired result in each
`session-tools.jsonl`. Rows and source lines are one-based. Each pair has
matching `call_id`, completed `exec` status, and a `Script completed` result
with JSON values. These are direct JavaScript calculations, not inferred from
prose or stdout command counts.

| Arm | Exact pair | Inputs/results reconciled with output |
|---|---|---|
| General | [Rows 7/8](runs/12-launch-handoff--bandit/session-tools.jsonl), source lines 32/34; `call_bDj3mejgi1SGkVkES3udCxEw` | Budget components at output line 57 are `100000+100000+120000+30000+10000+10000+100000`. The actual call evaluates that sum and `800000−sum`, returning **470000/330000**. It also evaluates usage rates, fees, recurring/first-month results, support sensitivity, pilot revenue/fee/loss, and role-hour sums. |
| Specify | [Rows 7/8](runs/12-launch-handoff--bandit-specify/session-tools.jsonl), source lines 33/35; `call_rxtn3Hc3p1QFPArK5NVw0vLc` | Output line 109's components are `100000+100000+120000+50000+10000+10000+200000`. The same component multiset is evaluated in the call, returning **590000/210000**. It calculates all three role-hour totals and five-store onboarding/support time, as well as economics. |
| Review | [Rows 5/6](runs/13-offer-consistency-review--bandit-review/session-tools.jsonl), source lines 27/29; `call_Au4GvH8d9b57kej222sfEltm` | Approved first-order components return **19000/33000** won, draft shortfalls **4000/3000**, and `23+2 = 25` pairs. These agree with output lines 16 and 28. Ordinary-order prices are also directly available from the approved source; do not overclaim that every cited source number was computed. |
| Six-week offer | [Rows 7/8](runs/15-supported-offer--bandit/session-tools.jsonl), source lines 34/36; `call_Ljc3vMiRdj7KFAF82WGwol90` | Executes per-customer workload, weekly and total capacity, three demand scenarios, alternatives, sunk/preparation-cost views, refund sensitivity, break-even, and refund-unit total. The call/result pair is real; its correct weekly arithmetic does not validate the separate two-session response promise. |

The auditor independently reconstructed 27 selected component/formula
comparisons for the initial five runs and 40 more for case 15; all agreed
within `1e-7`. These are arithmetic consistency comparisons, not independent
behavioral trials. Examples:

- Both monthly-model comparisons use `price×.967−2000−25000×.5`, returning
  `13543/3873` contribution and `7715/−40635` after fixed cost for five stores.
- The general alternative has a **29000**-won setup fee and returns a five-store
  first-month result of `16246.666…`; the specify alternative deliberately uses
  **20000**, returning `−27268.333…`. The different outputs reflect different
  labeled offers, not inconsistent arithmetic.
- The general pilot applies full monthly storage/support as a conservative
  scenario and returns `−145725.833…` won. The specify pilot explicitly assumes
  half the monthly storage/support and returns `−109475.833…`. Its half-month
  treatment is a labeled cost assumption, not measured cost or an exact calendar
  proration. The printed whole-won results agree with rounding.
- General role totals are computed as `10×4`, `4+16+6+2`, `4+3+1`; specify
  totals are `10+10+10+10`, `8+14+4+2`, `5+3`. Both return **40/28/8** and
  match their schedule components. The fixed 60000-won hosting charge is inside
  the cash tool reservation in both plans, rather than added twice.
- Case 15 source components give advisor cost `72×15000 = 1080000`, prepaid
  tools `30000`, and preparation labor `12×20000 = 240000`: prepaid cash cost
  **1110000** and preparation-inclusive cost **1350000**. The call uses those
  correct totals; the auditor independently derived them from source components.
  `89000×(1−.033−.05)−1000 = 80613` won per paying customer. For 8/16/24
  customers, new net cash is **644904/1289808/1934712** and preparation-inclusive
  result is **−705096/−60192/584712**, agreeing with output lines 64–66.
- Case 15's break-even counts are **14** for prepaid cash recovery and **17**
  including preparation labor. A 20% refund scenario requires **21**, with
  **264312** won preparation-inclusive result at 24 customers. Fee is charged
  on initial payment and per-customer cost remains for refunded customers,
  matching the source. The 5% refund scenario is explicitly separate from the
  proposed customer refund policy. Its components `15000+6×11500+5000 = 89000`
  are actually summed by the call. Marketing allocation is **0 of 90000**;
  prepaid sunk cost and new net cash are not conflated with full cohort profit.

### D / case 12 specify: storage assumption provenance

The [cost source, line 10](runs/12-launch-handoff--bandit-specify/original-input/costs-and-delivery.md)
states **2000 won per active store per month**, as a temporary estimate. It
does not establish metered daily billing or a provider rule that a 14-day
service costs 1000 won. Output line 107 explicitly introduces half the monthly
storage/support as an assumption, and the code evaluates `s/2` and `l/2`.
Thus execution and arithmetic are verified; actual half-month billing is not.

Keeping the full monthly storage amount while retaining the half-support
assumption would add **5000 won** for five stores and change the pilot result
from `−109475.833…` to `−114475.833…` (about **−114476 won**). This is a content
and input-provenance limitation, not an arithmetic execution failure. The
reported pilot result must remain conditional until the cost basis is checked;
tool execution is not empirical billing validation.

The 05 and 08 exports contain only file-inspection wrappers, respectively two
and three paired calls. Neither contains task arithmetic or an execution claim
contradicting the no-code boundary. No writes, product execution, external
contact, or child sessions are present in the inspected tool inputs.

## Integrity, confidence, and remaining gaps

All six runs are terminal with process exit `0`, metadata integrity `passed`,
and `session_tools.status: captured` without capture errors. Independently
verified: export hashes match metadata; all 20 calls have matching results
(40 rows); saved request hashes match recorded input hashes. The capture helper
is `5f7885c0e7f55bced0eb806a0c9ef7789a1560028fba93bcb61e5b8bc39c2d18` and
runner hash is `0cfd4c25a1b16bc24eee73fdcc96877e5b0486de64b6bd6e29ff903333e9fe55`.
Terminal/integrity statuses are not the basis for the behavioral findings.

The case 12 outer service horizons and the case 15 outer advisor term fit the
confirmed resources, but **the case 15 first-response capacity promise remains
a current gap**. It must not be erased because the weekly totals and final
service dates fit. The remaining concrete limits are:

- Case 15 needs a stated schedule or changed limit that makes the first
  528-minute batch compatible with the two-session response promise. Without
  separate staging, the available gross window is only 480 minutes. No current
  output was repaired or rerun in this audit.

- Actual closure, refunds, record delivery, and support effort are planned
  acceptance work, not observed execution. Both case 12 plans require these
  tasks inside the final staffed week; their estimates still need operational
  confirmation before real sales.
- Scope 08 cannot enroll yet on these documents alone because pilot dates and
  support coverage remain explicitly unresolved.
- Review 13 and research 05 contain no confirmed staffing-sunset fixture, so
  they cannot establish general coverage of the latest-customer boundary.
- D's half-month storage cost is labeled but lacks source-confirmed billing
  proration; keep the resulting economics conditional.

All six runs have now been assessed. **Do not mark overall service-feasibility
readiness as passed on this set.** Arithmetic execution is positively recorded,
and the outer calendar constraints are handled, but the case 15 response-window
gap remains unresolved. Later candidates must retain these original findings
and be evaluated separately.

## Evidence fingerprints

| Run | Output SHA-256 | Captured tool export SHA-256 |
|---|---|---|
| `05-small-research--bandit-research` | `9c1907e55cc960ba039f92ad7d4db76524aba6241004b209165dcbd8aea661e6` | `ab31c08143559c5f70f89847bb857a0d6f1745fcd373a989461ae957b8310d75` |
| `08-callback-scope--bandit-scope` | `41ac340864cd328c7e0466593512b7718ebb6e34a109abdf99600a4b8d75fce3` | `7a01d71d038f6ffcb2c9d639ce5d4380a7fd12c39f34d52794073a546b390427` |
| `12-launch-handoff--bandit` | `190551ba4156a7d63e2e28a13f811b31be27aa2f1c221072d459ca38d57610ea` | `65544bee5832af708f1db1b1e586e3a8dce503b4ae615d0e807531957917cbc2` |
| `12-launch-handoff--bandit-specify` | `c753a721e12b01e69b3b19ccf8a0467b1d70fa4fa7485cf4bdc2dc1b60d80b3f` | `629088c422aaf16ac08f5847010e6493bb530adf487a94599345291490d49bc1` |
| `13-offer-consistency-review--bandit-review` | `529f8ab7cb1a717d8f6cff89e3455145b29d7e29c132b55c9a84dade4ac0ba66` | `af5a68547b4fc95490fea19e5cfef8bbeaaf1730a84d7c4750ad071bed1025e9` |
| `15-supported-offer--bandit` | `d1333680b64e05c9595f0ae09cb198413cdeb4e08f7b2adda460f9c64b6ccf3a` | `7e610b5f71fc195cacf04d91095512def3f0c20598f53f46b9761023b379690a` |
