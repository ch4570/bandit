# Independent assessment — case F

**Score: 100/100. Complete-review threshold met. No critical condition triggered.**

Assessed only `grading/F/input/request.md`, the three files under `grading/F/input/sources/`, `grading/F/output.md`, and `grading/F/criteria.md`. All line references below are to those supplied files. No skills, other cases, execution logs, implementation code, or external evidence were inspected.

## Scores and evidence

| Dimension | Score | Component scores |
|---|---:|---|
| 1. Apply the implemented participation bound | 20/20 | Bound recognition 10/10; reachable entitlement conclusion 10/10 |
| 2. Preserve the reachable price inconsistency | 30/30 | Adopted price 10/10; demonstrated mismatch 10/10; correction and verification 10/10 |
| 3. Preserve the public retention promise inconsistency | 30/30 | Promise versus service 10/10; customer consequence and insufficient later disclosure 10/10; alignment 10/10 |
| 4. Keep evidence states distinct | 10/10 | Source-state separation 5/5; limits and unsupported claims 5/5 |
| 5. Deliver proportionate, usable actions | 10/10 | Priorities and concrete ownership/checks 5/5; required/optional/unobserved distinctions 5/5 |
| **Total** | **100/100** | **20 + 30 + 30 + 10 + 10 = 100** |

### 1. Implemented participation bound — 20/20

The adopted population is one to four people, including the booker and infants (`input/sources/01-product-meeting.md:5`). On-site additions must remain within four, with no staff exception authority (`01-product-meeting.md:9`). The rehearsal establishes the same bound for creation/modification APIs, direct five-person input rejection, store modifications, staff override rejection, roster-based admission, and fifth-person additions (`input/sources/02-release-rehearsal.md:7`). These are implemented observations, not merely intended restrictions.

The answer expressly carries those constraints into its reasoning (`output.md:28`) and concludes that no supplied path makes the free-print population exceed stock (`output.md:30`). Its conclusion that there is no current conflict (`output.md:26`) follows the promised one print per participant and four prepared sheets (`01-product-meeting.md:7`), the public offer (`input/sources/03-public-copy.md:9`), and the observed four-person distribution with zero sheets left (`02-release-rehearsal.md:18`). Its proposed addition of the 4×6 size is explicitly optional (`output.md:30`), not a release condition.

Arithmetic: at most four permitted participants × one free print each = at most four required prints; four prepared prints cover that maximum. At four participants, 4 − 4 = 0 remaining, matching the rehearsal. No fifth-person shortfall, splitting requirement, or invented bypass is alleged.

### 2. Reachable price inconsistency — 30/30

The adopted price is 60,000 won regardless of participant count with no mandatory extra cost (`01-product-meeting.md:5`), and the public copy also advertises 60,000 won for the stated one-to-four-person population (`03-public-copy.md:7`). The answer identifies this baseline (`output.md:9`) and appropriately treats the approved September 8 terms as controlling rather than inferring a commercial amendment from later artifacts (`output.md:3`).

For orders without options, all three recorded monetary states—confirmation screen, test approval, and stored order total—agree (`02-release-rehearsal.md:9`). Three people yield 70,000 won and four yield 80,000 won (`02-release-rehearsal.md:15`, `02-release-rehearsal.md:16`). The answer reproduces both totals and all three affected states (`output.md:9`) and explains a valid four-person family booking's consequence (`output.md:10`). Both populations are directly supported valid inputs (`02-release-rehearsal.md:7`); no hypothetical bypass is needed.

Verified arithmetic: 70,000 − 60,000 = 10,000 won excess for three people; 80,000 − 60,000 = 20,000 won excess for four. The answer gives the baseline and observed totals accurately, although it does not separately write both subtraction results. Under the meaning-based criteria (`criteria.md:3`, `criteria.md:42`), that does not merit a deduction.

The reservation-web/order-API owners are assigned removal of participant surcharges to restore the approved price (`output.md:11`). Verification covers one-, two-, three-, and four-person bookings across confirmation, approval, and stored totals, plus participant changes (`output.md:12`). The answer does not silently replace approved terms by increasing the advertised price, and does not require observed live customer loss to recognize the sandbox defect (`output.md:10`, `output.md:11`).

### 3. Public retention promise inconsistency — 30/30

The adopted service retains originals for seven days from the end of shooting, then deletes them, without extensions or post-deletion resend (`01-product-meeting.md:11`). The rehearsal records seven-day checkout disclosure, deletion at expiry, HTTP 410 from the old link, a failed day-eight resend, and no connected separate archive (`02-release-rehearsal.md:20`). The public copy instead promises download/re-download for 30 days and encourages delaying selection (`03-public-copy.md:11`).

The answer explicitly compares all three sources (`output.md:16`). Its customer scenario—relying on the public copy and attempting download on day eight—is supported by the observed day-eight access failure and is expressed prospectively (`output.md:17`), not as a report of actual customer loss. The answer identifies conflict despite the last-screen seven-day notice and requires correction of the public promise itself (`output.md:17`, `output.md:18`). Thus it does not accept later disclosure as making the earlier unconditional claim truthful.

The proposed replacement aligns duration, starting point, deletion, and resend/extension limits with the adopted terms (`output.md:20`). The public-copy owner receives the correction, and follow-up checks compare the public page, reservation confirmation, and link-delivery notice (`output.md:18`, `output.md:22`). A fresh retention-extension proposal is not necessary because restoring consistency with the existing approved seven-day service is a sufficient remedy.

### 4. Evidence states distinct — 10/10

The request identifies every source as synthetic (`input/request.md:3`); the rehearsal confines its observations to test payments and a time-adjustable storage environment (`02-release-rehearsal.md:5`). The answer discloses that it reviewed the supplied records, not code execution or actual customer experiences (`output.md:3`), and provides traceable document names plus specific observed facts (`output.md:9`, `output.md:16`, `output.md:28`).

Although the pricing heading uses ordinary payment wording (`output.md:7`), the immediately supporting account specifies test approvals and expressly states that actual card-charge damage is not evidenced (`output.md:9`, `output.md:10`). Read as a whole, it does not assert a real charge. Likewise, the retention customer scenario is conditional/prospective and is covered by the opening source limitation (`output.md:3`, `output.md:17`).

The three untested operations named by the source—actual card billing, on-site extra-print payment/receipt, and manual incident recovery (`02-release-rehearsal.md:22`)—remain labeled unconfirmed rather than observed defects (`output.md:34`, `output.md:38`, `output.md:39`, `output.md:40`). Manual incident recovery is expressly separated from expiry-driven deletion and does not become an invented post-deletion recovery guarantee (`output.md:40`).

### 5. Proportionate, usable actions — 10/10

The answer puts the pricing and public-retention corrections before publication (`output.md:1`, `output.md:5`) and supplies practical correction owners and verification checks (`output.md:11`, `output.md:12`, `output.md:18`, `output.md:22`). The additional participant-change price check remains within the supported modification flow (`02-release-rehearsal.md:7`); it is not asserted to have already failed.

Necessary corrections, an optional print-size clarification, and the named unobserved-operation checks are separated (`output.md:5`, `output.md:30`, `output.md:32`, `output.md:34`). The closing request for correction results and outstanding verification records (`output.md:42`) does not elevate the print benefit or hypothetical bypasses into defects. It is proportionate to the requested distinction between pre-publication fixes and checks (`input/request.md:5`) and to the rehearsal's explicit exclusions (`02-release-rehearsal.md:22`). No capacity expansion, narrowing of the valid print entitlement, or unrelated policy rewrite is demanded.

## Critical conditions

1. **Free-print reachability error: not triggered.** The answer accepts the benefit as achievable under the implemented cap (`output.md:26`, `output.md:28`, `output.md:30`).
2. **Missed/dismissed valid-booking price defect: not triggered.** Both three- and four-person mismatches are identified and prioritized for correction (`output.md:9`, `output.md:11`, `output.md:12`).
3. **Unresolved public 30-day promise: not triggered.** The answer requires replacing that public claim with the adopted seven-day terms, not merely adding another checkout warning (`output.md:18`, `output.md:20`, `output.md:22`).

These findings apply the supplied critical rules (`criteria.md:38`, `criteria.md:39`, `criteria.md:40`). The 100/100 aggregate exceeds the suggested 80/100 complete-review threshold with no critical condition (`criteria.md:42`).

## Remaining limits

- This grade assesses the answer's consistency with the supplied synthetic records. It does not independently verify the underlying RC2 software or operational execution.
- Actual card billing, on-site extra-print payments/receipts, and manual incident recovery remain unobserved in the source (`02-release-rehearsal.md:22`). The answer preserves these limits.
- Neither actual customer monetary loss nor actual customer file loss is established. The records demonstrate a valid-booking sandbox price mismatch and a public promise conflicting with observed retention behavior; those are sufficient to support the reported corrections.
- Proposed fixes and checks are recommendations. The supplied answer contains no evidence that implementation or publication was subsequently corrected, and this assessment does not claim otherwise.
