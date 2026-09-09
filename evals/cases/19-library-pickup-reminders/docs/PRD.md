# HoldHarbor PRD v1 — single-branch hold pickup

Synthetic fixture. This library, readers, policies, and records are fictional.

## Purpose and adopted authority

The branch wants readers to collect ready holds and avoid unnecessary returns
to the shelf. Library manager Nora adopted these rules on 2026-08-01. They
remain authoritative unless the current request explicitly changes them.

- **D1:** A staff member's Ready scan starts a seven-day hold. Pickup by that
  deadline remains allowed. Seventy-two hours is an early-pickup measurement
  target, not the hold's expiry time.
- **D2:** The existing automatic email notice continues for every ready hold.
  SMS is optional and requires the reader's explicit consent and a confirmed
  phone number. A reader can withdraw consent. Neither phone ownership nor
  consent is a replacement for library-account authentication.
- **D3:** Texts contain a generic ready-hold notice and a sign-in link, never a
  book title or borrower details. Readers can see only their own hold details;
  signed-in branch staff can see and manage this branch's holds.

## Current behavior

- **R1:** Staff record Ready, Collected, Cancelled, or Expired on the hold.
  Collection requires the existing desk scan. Opening a notice or signing in
  does not mean the book was collected. A collected or cancelled hold must not
  receive a new reminder; expiry also ends reminder eligibility.
- **R2:** The v1 hold page shows the pickup deadline and current state using the
  existing account and hold services. It does not change the deadline.
- **R3:** During the pilot, staff manually composed an SMS after marking a hold
  ready and recorded delivery status in a private sheet. There is no automated
  SMS queue, retry handling, or reader-facing delivery status in the application.
  The provider supports submission and later status lookup by its message ID.
  Its behavior after a lost submission response has not been verified here.

## Original hypothesis and verification

- **H1:** Optional SMS might improve early pickup and reduce unclaimed holds.
  Neither benefit has an adopted numeric success threshold or causal estimate.
- **V1:** The supplied developer memo reports Ready-to-Collected and seven-day
  expiry checks executed and passed in v1 staging on 2026-08-02.
- **V2:** The same memo reports that email-link opening left collection state
  unchanged and another reader's hold details were denied, also passed in v1
  staging. These were application checks, not a production privacy audit.
- **V3:** Automated SMS queue, consent withdrawal while queued, duplicate
  submission, and uncertain provider response have not been implemented or tested.

The findings in [pilot notes](../pilot-notes.md) and the
[reader outcome export](../reader-outcomes.csv) are reported operational records,
not software acceptance results.
