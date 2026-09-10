# Attempt 3: captured calculation execution audit

Archive note: local link destinations are relocated for this export. The
[original report bytes](execution-audit.raw.md) remain unchanged.

Audited 2026-09-10. Scope: the five settled runs under `captured/`, condition
`numeric-evidence-captured`. “Attempt 3” names this development round; each
metadata record has `attempt: 1` within its own condition. Only this audit
report was written. Task outputs, captured tool records, source instructions,
and grading criteria were not changed.

## Bounded verdict

**PASS for the original Issue 16 monetary sum, fee, and period-calculation
execution criterion in the three permitted numeric arms.** Each arm has an
actual completed arithmetic call paired with its returned result. The two
handoffs calculate their final budget allocations from the component amounts,
and the review calculates prices and capacity from approved rules. Independent
recomputation agrees with the inspected monetary results and their final
rounding. This judgment uses `session-tools.jsonl`, not missing or present
stdout command events alone.

Case 08 correctly respects its explicit prohibition on running code: its
captured calls only inspect files, and its output marks arithmetic as not
tool-verified. Case 05 stays qualitative, with no arithmetic call or execution
claim. These are separate controls, not cases that should be forced to run a
calculator.

**Confidence: high for the specific recorded calls and checked figures.** This
is one fresh run per arm on synthetic fixtures, not a reliability estimate or
proof of general superiority. Broader numerical coverage is partial: the
specify arm's founder-hour total and remaining hours are literal fields in the
tool input, not computed sums. They are correct on independent recomputation,
but their mere presence in a returned object is not proof of tool calculation.
That caveat does not negate its executed monetary checks; it prevents a claim
that every resource total was derived by the tool.

## Authority, inputs, and candidate identity

The auditor inspected every captured raw tool call and its paired result,
each final output, metadata, and the relevant cost/approved-offer sources.
All raw input hashes, full instruction hash maps, and prompt bytes match the
corresponding `round2/` run. No instructions changed between the second and
third rounds. Previously read raw requests therefore retain their exact
meaning and authority here.

- [Case 12 request](runs/12-launch-handoff--bandit/original-input/request.md),
  lines 15 and 19, requests cost-based business-model planning while prohibiting
  edits to originals and real customer contact, publishing, charging, or
  experiments. Standalone arithmetic is permitted. The specify request is
  identical.
- [Case 13 request](runs/13-offer-consistency-review--bandit-review/original-input/request.md),
  lines 7–11, requests price/offer review without artifact changes or external
  actions. Standalone price and capacity arithmetic is permitted.
- [Case 08 request](runs/08-callback-scope--bandit-scope/original-input/request.md),
  lines 12–13, explicitly says not to “run code.” Its no-code constraint takes
  precedence over the skill's calculation guidance.
- [Case 05 request](runs/05-small-research--bandit-research/original-input/request.md)
  requests one segment and one cheap validation method within 200 words. No
  consequential derived total is needed.

## Exact execution pairs

The export rows below are one-based. Source lines come from each run's
`session_tools.exported_source_lines`. Every listed computational call has
`name: exec`, `status: completed`, a matching `call_id` in its output, and a
`Script completed` result followed by the returned JSON.

| Permitted arm | Captured call/result | Exact call ID | Arithmetic observed |
|---|---|---|---|
| General handoff | [session-tools.jsonl](runs/12-launch-handoff--bandit/session-tools.jsonl), rows **7/8**, source lines **32/34** | `call_ie11XDTaKNX8RDkr8FfACj1I` | Usage ratios; monthly fees, contribution, first month, five-store results and break-even; 14-day pilot economics; support sensitivity; component budget sum/remainder; role-hour totals. |
| Specify handoff | [session-tools.jsonl](runs/12-launch-handoff--bandit-specify/session-tools.jsonl), rows **5/6**, source lines **29/31** | `call_xveIuLrjvItnIcNTBbCr98CY` | Monthly fees/contribution, setup/onboarding, five-store economics, break-even, 60-minute support sensitivity; component budget sum/remainder; service hours and historical ratios. Founder `sum`/`remaining` fields are literals. |
| Offer review | [session-tools.jsonl](runs/13-offer-consistency-review--bandit-review/session-tools.jsonl), rows **5/6**, source lines **24/26** | `call_M8bfmNkZQctAcY3NMmBcwF7i` | One-/two-pair ordinary and first-order prices, differences from the draft, remaining capacity, excess capacity, and maximum pairs under an incorrect order-count rule. |

These are pure JavaScript tool calls rather than nested shell calculations.
The preserved input contains the expressions and the preserved output contains
their results. They establish actual execution despite the known stdout
exporter's omission of this call form.

### Claims matched to the recorded results

- General [output line 114](runs/12-launch-handoff--bandit/output.md) says
  formulas, usage rates, budget, and hour totals were checked. Its monetary
  table at lines 98–112 and budget at line 50 match the corresponding returned
  fields, including `480000 / 320000` allocation/remainder and the recurring
  contribution values `13543 / 3873`.
- Specify [output line 105](runs/12-launch-handoff--bandit-specify/output.md)
  gives formulas and pre-rounding first-month values. The raw result is
  `-75618.33333333331 / 16246.666666666686`, consistent with its two-decimal
  citation and whole-won table. Its line-113 budget matches returned
  `500000 / 300000`. Its line-125 distinction between arithmetic and unexecuted
  product checks is supported for the recorded calculations.
- Review [output lines 19 and 27](runs/13-offer-consistency-review--bandit-review/output.md)
  claims returned prices/differences and capacity calculations. The result
  contains exactly ordinary prices `22000 / 36000`, first prices
  `19000 / 33000`, shortfalls `4000 / 3000`, and capacity results `1, 25, 48`.

## Independent component and formula check

The auditor wrote and executed separate arithmetic from the visible output
components and the supplied cost rules. Captured tool source was inspected,
not evaluated as a substitute for independent reconstruction. Fifty numerical
comparisons against recorded result fields passed within `1e-7` tolerance;
whole-won output values were also compared with the recorded results' rounding.
The fifty comparisons are a bounded consistency check, not fifty independent
behavioral test cases.

### Budget components, rather than asserted totals

| Arm | Final-output components in won | Same components evaluated in the actual tool input | Independent sum and remainder |
|---|---|---|---|
| General, output line 50 | `100000 + 100000 + 120000 + 40000 + 10000 + 10000 + 100000` | Yes. The call explicitly adds those seven values and subtracts their sum from `800000`. | **480000 allocated; 320000 unallocated**. Both match the returned result and final output. |
| Specify, output line 113 | `100000 + 100000 + 120000 + 30000 + 10000 + 10000 + 130000` | Yes. The call includes matching named allocation fields and explicitly evaluates the same addition and remainder expression. | **500000 allocated; 300000 unallocated**. Both match the returned result and final output. |

The monthly fixed `60000` cost remains inside each `100000` tool reservation,
as the cost source states; it is not an additional eighth cash allocation.
Including that fixed cost in the economic-result calculation is a different
accounting view and does not duplicate it in the cash-budget sum.

### Economics and period conversions

The [cost source](runs/12-launch-handoff--bandit/original-input/costs-and-delivery.md),
lines 9–14, supplies monthly fixed cost `60000`, monthly per-store cost `2000`,
fee rate `0.033`, support `30` minutes, hourly cost `25000`, and initial
onboarding `40` minutes. Both handoffs use those same inputs. Proposed monthly
prices are `29000` and `19000`; the alternative setup fee is `29000` in both
captured handoffs.

| Independently reconstructed quantity | Result | Actual computation coverage |
|---|---:|---|
| Onboarding `40/60 × 25000` | `16666.666…` won | Evaluated in both calls. |
| Recurring support `30/60 × 25000` | `12500` won | General uses this correct intermediate as `labor=12500`; specify evaluates `.5*25000`. |
| Monthly fees `29000×.033`, `19000×.033` | `957 / 627` won | Evaluated in both calls. |
| Recurring contribution `price×.967−2000−12500` | `13543 / 3873` won | Evaluated in both calls. |
| First contribution: add setup net of fee, subtract onboarding | `−3123.666… / 15249.333…` won | Evaluated in both calls; final values round to `−3124 / 15249`. |
| Five-store recurring contribution less fixed cost | `7715 / −40635` won | Evaluated in both calls. |
| Five-store first month less fixed cost | `−75618.333… / 16246.666…` won | Evaluated in both calls; final values round to `−75618 / 16247`. |
| `ceil(60000 / contribution)` | `5 / 16` stores | Evaluated in both calls, then compared with five-store capacity in the outputs. |
| General support sensitivity at `15/30/60` minutes | `38965 / 7715 / −54785` won for five stores | Explicit minute-to-hour conversion evaluated in the call. |
| Specify support at `60` minutes | `1043 / −8627` won per store | Evaluated in the call and matched in output line 109. |
| General 14-day pilot with full monthly delivery/support assumptions | `107.5` won cash; `−145725.833…` won including labor | Evaluated in the call; output line 112 rounds to `108 / −145726` and labels the conservative monthly-cost treatment. |

The 14-day pilot is a separately proposed offer with full monthly cost
assumptions explicitly applied. The audit does not treat it as an observed
month-to-day conversion or validate those business assumptions.

### Review components and units

[Approved offer O-3](runs/13-offer-consistency-review--bandit-review/original-input/approved-offer.md)
sets `18000` won per pair, `4000` per one-pair order with a two-pair waiver, and
one `3000` discount per first order. O-1 sets capacity at `24` pairs, not orders.
The recorded call implements those exact conditions:

- Ordinary prices: `18000×1+4000 = 22000`; `18000×2+0 = 36000`.
- First-order prices: subtract `3000` once, producing `19000 / 33000`.
- Against draft `15000 / 30000`, shortfalls are `4000 / 3000`.
- Remaining capacity `24−23 = 1`, adding two pairs produces `23+2 = 25`, and
  incorrectly allowing 24 two-pair orders produces `24×2 = 48` pairs.

All agree with the raw tool result and the final table/scenarios. The final
review also correctly leaves the actual pair count of the draft's 23 orders
unknown rather than treating that order count as a measured pair count.

## Controls and broader coverage caveat

| Control | Complete captured pairs inspected | Observed result |
|---|---|---|
| Qualitative case 05 | [session-tools.jsonl](runs/05-small-research--bandit-research/session-tools.jsonl), rows 1/2 and 3/4; source lines 14/17 and 19/22 | Both `exec` bodies only call shell file inspection (`cat`, `rg`). No task arithmetic or calculation-execution claim. The final answer remains a short segment/interview recommendation. |
| No-code case 08 | [session-tools.jsonl](runs/08-callback-scope--bandit-scope/session-tools.jsonl), rows 1/2 and 3/4; source lines 14/17 and 19/22 | Both `exec` bodies only wrap file inspection. No arithmetic/product computation is present. [Output line 39](runs/08-callback-scope--bandit-scope/output.md) explicitly labels derived capacity figures not tool-verified because code is prohibited. |

The specify calculation input includes
`hours: {founder: [9,10,10,9], sum: 38, remaining: 2, ...}`. The `sum` and
`remaining` numbers are literals, not expressions evaluated from the array.
Its developer and designer schedule totals are also not derived in that
arithmetic call. Independent addition confirms `9+10+10+9 = 38`, `40−38 = 2`,
`4+16+8 = 28` developer hours, and `4+4 = 8` designer hours. This establishes
their correctness in the audit, not original tool derivation. In contrast,
`5*(40/60+.5)` actually computes the service hours and returns `5.8333…`,
matching five hours fifty minutes. Track exhaustive capacity-total coverage
separately from the original monetary/fee/period criterion.

## Capture integrity and final-helper re-extraction

All five original captures report `status: captured`, no capture errors, process
exit `0`, and workspace integrity `passed`. The auditor independently verified:

- Every exported call has exactly one matching result and vice versa: **14
  call/result pairs, 28 records** total. Three pairs contain arithmetic; eleven
  contain file-inspection orchestration.
- Export byte hashes match each original metadata record; record and call/result
  counts agree, and each raw row's ordinal maps to its recorded source line.
- All five prompt and input hashes and full instruction maps match round 2.

The run's runner hash is
`6a92e06596c0fe63e922e720f3ff737ff2ea08142382f57bdc936c44e6988e3f`.
The original capture-helper hash is
`45a252983a30514530f349da524d6948bac31facaf96b085aec07b70e0a99659`.

Afterward, the leader fixed header reads to use unbuffered I/O so source-body
bytes cannot be prefetched before session binding. The auditor inspected the
[final-helper re-extraction receipt](../attempt-3/reextraction-check.json)
and compared its entries against all original metadata and current export
hashes. All five have the same thread, source hash, source-line mapping, and
byte-identical tool export, with final capture status `captured` and no errors.
The final helper hash recorded there is
`5f7885c0e7f55bced0eb806a0c9ef7789a1560028fba93bcb61e5b8bc39c2d18`.
No model task or grading input was rerun or changed for that re-extraction.
Collector safety regression tests are the leader's separate verification scope;
this audit verifies the receipt's consistency with the inspected artifacts.

## Readiness and limits

The original bounded monetary execution criterion now has affirmative evidence:
actual computation, recorded results, output reconciliation, and independent
component checking. It can be accepted for these runs. An additional skill
rewrite is not justified merely by the earlier flattened stdout trace.

Do not expand that acceptance into a claim of exhaustive verification of every
number, market validation, universal tool compliance, or full PR readiness.
The literal-hour caveat remains, business assumptions are synthetic, and other
PR checks are outside this report. Earlier ephemeral execution results remain
inconclusive; this new evidence does not retroactively prove their calls. The
earlier independently confirmed incorrect budget also remains historical
failure evidence.

## Evidence fingerprints

| Run | Source session SHA-256 | Captured export SHA-256 | Output SHA-256 |
|---|---|---|---|
| `05-small-research--bandit-research` | `3685215fb07e66979614ade2a8001aa2f5e7c1cebd5e65bbfc7ff161ce977216` | `fc7dac0082cfc8254c7a694e59c7aa4867b3b39c6582da5a1e32974956510492` | `457d680e1c7bd09a09a0f765a839821feaa3aa5b3b7621314116dbda49148899` |
| `08-callback-scope--bandit-scope` | `01f65907a1d119fd45f7e79590dce3c91ccdabd0ce74553d43ed7681a9b2e86e` | `3790f55e6d4cc1ac5e3ab12cb007d4f7611fd4255c3a6d6dea56846cfbd9748e` | `300c22ddd9b1fc1216dc7856143fdc0b2c146f94d0b5d341e5c2feede0202375` |
| `12-launch-handoff--bandit` | `c5df18a737c43b9700abec3e32b5b8a3f194faf6ae4ef3d34e726cdfb6a61dd0` | `695b9f172602101f5603da96b9fd1e31f9b07b1984c41f86478ea83fb1b3dfeb` | `e20a0de3b80b1271f8e7ba6a566c3a1f6464356ec6c682024bf0c5e1871c4daa` |
| `12-launch-handoff--bandit-specify` | `858e6898efb0a334deccb1a3c65fccc575665967cb892cf08218f1397c69a473` | `0022b0cf9dc4f53a779b33be40ce6b5849d8694a82811f82cfc14321d1fbf592` | `b169fd0ad7785b44a3e0e903f1454be63a7b67946efc26445658ae25b8d9fef4` |
| `13-offer-consistency-review--bandit-review` | `4dd1c9fe222932d52e73aaf339e25274551c5e8179ab4ec9ad851eb0d41ac2ee` | `5995a4fabe2eca8f7820e7396577206b5ed2352afe8877e11573357db507ed81` | `fd4d3329f63881e7b31f997f952d6b7365c2258d61aa086f35a8bccf6cb0d0e7` |
