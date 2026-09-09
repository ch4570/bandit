# HoldHarbor PRD — automated pickup SMS

Synthetic fixture: this library, readers, policies, and records are fictional.

## Purpose and decisions

Help readers collect ready holds while making SMS work visible. Nora’s adopted next-release decision replaces manual composition with a Ready-triggered automated queue. These rules, adopted August 1, 2026, remain authoritative:

- **D1:** Ready starts a seven-day hold; pickup through that deadline remains allowed. Seventy-two hours measures early pickup, never expiry.
- **D2:** Every ready hold retains automatic email. SMS requires explicit, withdrawable consent and a confirmed phone number. Neither replaces account authentication.
- **D3:** SMS contains a generic ready-hold notice and sign-in link, never titles or borrower details. Authenticated readers see only their own holds; authenticated branch staff manage only this branch’s holds.

**Proposed availability decision:** Continue with the original 50 readers rather than offer enrollment to all 250. This is a recommendation, not adopted policy; its adoption remains open before rollout. The requirements and checks below use this proposed boundary. Enrollment does not promise an immediate hold.

## Evidence and recommendation

The [September 9 pilot record](../pilot-notes.md) and [reader export](../reader-outcomes.csv) describe August 3–30 manual SMS alongside email. Fifty desk-recruited volunteers were not randomized. Outcomes concern each reader’s first ready hold only. All 30 index holds had mature seven-day outcomes reconciled against desk scans by August 30, 18:00 UTC.

Twenty of 50 readers had no ready hold: their pickup outcomes are inapplicable, not failures or missing observations. Among 30 opportunity readers, 18/30 collected within 72 hours and 23/30 before expiry; early collections are included in the latter count. Confirmed SMS delivery reached 14/30 opportunity readers, or 14/50 participants. Of those 14, 12 collected early and 13 before expiry; delivery does not prove reading. Four failed-delivery readers collected one early/two before expiry; seven without consent collected three/five; five with unconfirmed phones collected two/three.

The records describe manual operations, not automated-queue verification or causal improvement. All ready holds received email; no email-only comparison was assigned, and pickup motivation is unknown. The other 200 readers’ consent, phone readiness, and opportunities are unmeasured. The circulation lead favors expansion; the supervisor highlights unreachable readers and absent opportunities. Neither statement adopts policy.

Retaining 50 limits new enrollment exposure under 90 total staff minutes next week but does not establish sufficient capacity. **Proposed default:** reserve 30 minutes each for enrollment help, exceptions, and follow-up; record actual use. At budget exhaustion, pause new SMS enqueueing and enrollment assistance, retain visible pending work, and continue ordinary email/pickup. Review measured support demand, eligible opportunities, unresolved backlog, and implementation estimates before recommending expansion. H1—SMS improves early pickup/reduces unclaimed holds—remains unproven, without an adopted numeric threshold.

## Requirements and recovery

**R1–R2 retained:** Staff record Ready, Collected, Cancelled, or Expired. Only the existing desk scan records collection; opening notices/signing in never collects. The authenticated hold page shows current state and unchanged deadline.

**R3 replacement:** Each queue entry belongs to one hold’s Ready event and reader. Proposed default: one SMS per event, no scheduled follow-ups. Readers outside the cohort, without consent/confirmed phones, or without ready holds receive no queued SMS. Staff see exclusion reasons for ready holds.

Immediately before submission, recheck eligibility and hold state. Withdrawal, a changed/unconfirmed phone, collection, cancellation, or expiry suppresses unsent work with a visible reason. Submitted messages cannot be recalled; withdrawal blocks further submissions. Readers manage consent and phone confirmation through authenticated account access.

Staff see waiting, submitted/pending confirmation, delivered, failed, unresolved, or suppressed status, timestamps, and next action. Only provider confirmation establishes delivery. Repeated triggers or staff actions cannot duplicate submission for one event.

Lost submission responses become unresolved, never blindly resent. Reconcile through provider message-ID lookup when available; without a recoverable ID, retain uncertainty for staff attention and rely on email. Proposed default: staff may retry only definitive failures after eligibility recheck; no automatic retries.

## Delivery and observable checks

One developer has five days including verification/fixes; component estimates remain outstanding. Reuse existing services/provider/staff application. Defer mobile apps, other branches, marketing, and borrowing-policy changes.

V1–V2 remain reported passes in v1 staging, August 2: Ready-to-Collected, seven-day expiry, link-opening noncollection, and cross-reader denial. They remain evidence for v1, not a production privacy audit; integration needs rechecking. V3 automation remains unimplemented/unverified.

Planned acceptance: eligible Ready queues once despite repeated triggers; excluded readers retain email; withdrawal/terminal states suppress waiting messages; lost responses stay unresolved without resend; provider confirmation updates delivered status; failed-message retries recheck eligibility; unauthorized access is denied; deadline/desk collection behavior persists; cohort and budget pauses enforce the proposed boundary. No product tests were executed for this specification.
