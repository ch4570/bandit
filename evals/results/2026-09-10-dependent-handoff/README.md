# Accepted customer paths and dependent handoffs — 2026-09-10

This continues Issue 18 / Draft PR22 on `fix/issue-18-service-horizon` after
`7afdd224097eb6852639f81ff51c57506e5b2e98`. It is unreleased development work,
not a deployed service, customer experiment or comparative benchmark.

**Not an overall clean result. Keep Issue18 and PR22 incomplete.** The second
candidate respects the no-code boundary and improves the main service chains,
but retains an accepted-customer enrollment/recovery gap and narrower deadline
ambiguities. High scores and passing package checks do not erase those findings.

## What changed and how it was tested

The shared timing rule traces dependent interactions backwards from staffed
completion and forwards through usable customer response time. After the first
execution, it explicitly includes accepted late/recovery paths and stated
customer availability, and checks their remaining response-window capacity.
Confirmed later resources remain usable even after preparation ends. No
particular offer, price, weekday, duration or refund policy is prescribed.

A fresh no-code violation also prompted a permission clarification in the shared
calculation contract: a prohibition on code includes arithmetic code, not just
product code. A permitted non-code calculator or an explicitly unverified check
remains possible. The instruction does not require overriding the user's scope.

Canonical references remain under `skills/bandit/`; specialist copies come from
the existing sync script. Entrypoints, five-skill inventory, installation,
version and dependencies are unchanged. The runner's sole code change adds
case16 to its local-only inventory. English/Korean usage guidance is aligned.

The [protocol](protocol.md) records each change before its execution. Each
candidate has seven fresh CLI tasks with the same raw inputs, arms, output caps,
timeout and host-default model/effort. Executing agents receive no criteria,
diagnosis, previous output or desired answer. Independent graders receive only
raw inputs, output and unchanged criteria. Separate audits inspect paired tool
events, hashes, actual resource dates and ordered interactions.

Case16's four synthetic raw files and separate meaning-based criteria were
independently authored and frozen at `2026-09-10T06:36:04Z`, before its first
execution, without inspecting the candidate or earlier cases. It concerns a
craft seller's product-information cards, with separate operator/designer
windows and customer review before revision. Its rubric allows justified
alternatives or deferral. That first execution is targeted transfer evidence;
later executions are public development regressions, not hidden benchmarks.

## Preserve both findings and grading corrections

| Attempt | Original conditions, cases05/08/12/13 | Case15, separate weighted rubric | Case16, separate weighted rubric | Separate audit |
|---|---|---|---|---|
| 1 — dependent chain | 31 pass / 0 partial / 0 fail | Original 97/100; adjudicated 87/100 with critical operational-promise finding | 97/100; clean, no critical finding | Actual no-code breach in case08; unusable included follow-ups for accepted case15 paths |
| 2 — permissions and accepted paths | 30 pass / 1 partial / 0 fail | 94/100; no frozen critical finding, but material enrollment/recovery gap | 98/100; clean, no critical finding | No-code boundary respected; five permitted arithmetic calls confirmed; conditional timing/allocation gaps remain |

The first case15 grade missed an ordinary-week late-photo branch. Its Friday
answer arrives after Friday noon's post-answer-question cutoff. The final-week
exception repairs that late-input branch only in the final week. The plan also
calls weekend-only customer F suitable, although that customer's next chance to
read the Wednesday answer comes after the Friday question cutoff, especially
after the last staffed session in the final week. These are contradictions in
the proposed offer, not observed customer harm. The original 97/100 report is
unchanged; the [separate adjudication](attempt-1/supported-offer-adjudication.md)
records the revised 87/100 and its source-located critical finding.

The first audit additionally describes 528 first-week work minutes versus at
most 480 Wednesday/Friday minutes when all usable inputs arrive late. The
adjudication qualifies that counterexample: earlier application photos might
permit Monday prework. The output does not establish those dependencies or
rework time. This is a conditional capacity risk, not a proven unavoidable
overload or an extra critical failure. Neither interpretation is erased.

Case08's calculation is correct and actually executed, but the raw request
forbids running code. This is an authorization regression, not fabricated tool
execution. It does not reverse the earlier correction that absent CLI stdout
events cannot prove non-execution. Content quality, permission compliance,
calculation execution and business feasibility are separate judgments.

Case16's first result orders inputs → initial production → usable customer
review → later revision/export → final delivery inside the confirmed windows.
Five first-stage orders use 175 of 180 designer minutes; spare second-stage time
does not increase the first-stage limit. Its narrow five-minute buffer and
unmeasured work in the operator reserve remain assumptions to test. Its 80-point
clean threshold belongs to its own frozen rubric; case15 has no passing cutoff.
Do not combine these scores or convert them into a general success rate.

Attempt 2's case15 provides a weekend after the final result and a later staffed
reply, preserving the included final question without adding unconfirmed staff.
But it expressly accepts weekend-only customers while recruitment/payment end
Friday after Monday/Tuesday announcements. Its Tuesday/Wednesday correction
deadlines also leave those customers' recovery path unresolved. These are
material journey gaps, even though its frozen critical definitions did not
establish a new critical finding. Keep them under the unfinished Issue18 work.

Its late-input workload qualification is narrower than a raw staffing overload:
the peak 464 modeled minutes can fit the remaining 480 Wednesday/Friday minutes
if common records happen Monday, but not the output's fixed 220 customer minutes
per day (440 total). The plan must reconcile its own allocation or narrow that
path. Recovery merely ending by November 6 does not supply all preceding customer
response steps; the stated refund fallback limits the promise but does not prove
full delayed delivery. Case12 general also leaves its last ordinary inquiry's
next-support-day reply ambiguous; its weekend closeout explicitly covers errors
and non-delivery. These findings are not observed service failures.

The original-condition partial is C/J12-5: adding total recruitment labor to
per-store cash acquisition cost omits the paid-store denominator. Displayed
offer, budget and effort totals still reproduce. Preserve the dimensional
finding with the cost/commitment follow-up in Issue20; do not quietly alter the
original rubric. Case16's remaining deduction concerns unconverted applicant
work drawing on the same finite operating reserve, not a proven baseline
accepted-order overload.

## Evidence

- Attempt 1: [content grade](attempt-1/content-grade.md),
  [case15 original grade](attempt-1/supported-offer-grade.md),
  [case15 adjudication](attempt-1/supported-offer-adjudication.md),
  [case16 grade](attempt-1/card-content-grade.md),
  [six-run audit](attempt-1/execution-audit.md),
  [case16 audit](attempt-1/card-execution-audit.md),
  [run index](attempt-1/execution-summary.json).
- Attempt 2: [content grade](attempt-2/content-grade.md),
  [case15 grade](attempt-2/supported-offer-grade.md),
  [case16 grade](attempt-2/card-content-grade.md),
  [seven-run audit](attempt-2/execution-audit.md),
  [run index](attempt-2/execution-summary.json).

Reports are copied byte-for-byte. Their historical temporary path roots and
`A/`–`G/` locators map to each attempt's `grading-inputs/`; audit run paths map
to that attempt's `runs/`. Each run retains exact prompt/output, stdout events,
stderr, metadata, before/after inputs and supported raw tool calls/results.
Instruction snapshots and runner/helper snapshots bind the tested candidate.
No general host messages or reasoning are exported. Tool content can include
task material; these fixtures are synthetic, not private customer records.

## Verification and limits

All 14 processes/runner exits are zero, input-integrity checks passed, and the
requested session-tool exports were captured. The second attempt's audit hashes
all seven exports and 26 original/workspace input pairs. It confirms five actual
arithmetic call/result pairs; research and no-code scope have only read/list
calls. JavaScript orchestration of read-only file tools is distinguished from
executing an arithmetic program. Some budget/workload inputs remain literals in
the calculation rather than recomputed subexpressions; independent recomputation
agrees, but the execution evidence is not overstated.

Final candidate checks: sync; Node/Python structure/reference validation;
Node79/Python213 tests; Python compilation; scoped whitespace checks; and an npm
archive with all 45 skill files byte-identical to source. Historical inventories
of 159, 434 and 443 files match their retained hashes. Instruction snapshots,
outputs, input copies and criteria also match each new run's recorded hashes.
The [inventory](evidence-sha256.json) binds this result directory. ZIP packaging
metadata is recorded separately in the PR so it does not hash itself here.

Supplemental SkillEvaluator0.2.1 Tier1 passed for all five skills, retaining its
nonblocking advisories. SkillSpector2.3.5 `--no-llm` reports risk score zero but
one pre-filter finding per skill, not zero raw findings. The detailed canonical
scan has zero remaining issues after its own heuristic filtering and explicitly
marks analysis incomplete. No suppression baseline was supplied. Raw scanner
reports stay outside the repository at the run's temporary report directory;
this is not a full security-tier or prompt-injection-resistance claim.

Static/package checks are not skill-quality benchmarks. No real campaign,
payment, service load, rendered UI, customer validation, scheduled paid model
evaluation, merge or release has occurred. This offline task does not resolve
the earlier live-research currency/source-payload limits. Cost-period and
accepted-customer recovery work remains in Issue20; review reachability remains
in Issue21. The historical service-horizon results remain byte-unchanged.
