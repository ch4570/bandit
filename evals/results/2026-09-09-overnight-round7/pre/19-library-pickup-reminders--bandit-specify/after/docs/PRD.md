# HoldHarbor PRD — automated pickup SMS

Synthetic fixture: all people, policies, and records are fictional. This replaces v1’s manual-text plan; implementation and release verification remain outstanding.

## Direction and boundary

Nora adopted automation tied to Ready on September 9, 2026. Preserve August 1 decisions D1–D3: Ready starts a seven-day hold, pickup remains allowed through its deadline, and 72 hours measures early pickup only. Automatic email continues for every ready hold. SMS requires explicit, withdrawable consent and a confirmed number; neither substitutes for account authentication. Texts contain only a generic notice and sign-in link, never titles or borrower details. Readers access only their own holds; authenticated branch staff manage this branch’s holds.

**Recommended, not adopted:** offer next-release enrollment only to the original 50 readers. The other 200 retain existing email and pickup services. Consent is still required within the 50. Branch-wide availability remains an open decision for Nora; the following rollout and checks use this proposed boundary.

Reuse account/hold services, provider, and staff application. One developer has five days including verification/fixes; no estimates establish feasibility yet. Exclude mobile apps, other branches, marketing, and borrowing-policy changes.

## Evidence and recommendation

[September 9 pilot notes](../pilot-notes.md) and [reader export](../reader-outcomes.csv) describe August 3–30, desk-recruited, nonrandom readers. Calculated reader-level results:

- Opportunity: 30/50 had an index ready hold; 20/50 had none, so their pickup outcomes are inapplicable, not failures.
- Reach: 14/30 opportunity readers received confirmed SMS (46.7%); 14/18 consented, confirmed-phone attempts delivered (77.8%). Four failed; seven lacked consent; five had unconfirmed phones.
- Pickup: delivered readers collected 12/14 within 72 hours (85.7%), 13/14 before expiry (92.9%). Overall, 18/30 collected early (60%), 23/30 before expiry (76.7%); seven remained uncollected. Early pickups are included in deadline pickups.
- Failed-delivery, no-consent, and unconfirmed-phone groups respectively collected 1/4, 3/7, 2/5 early and 2/4, 5/7, 3/5 before expiry.

All index deadlines passed by August 30, 18:00 UTC; desk scans were reconciled without missing outcomes. Later holds are excluded. Delivery does not prove reading. Everyone with a ready index hold also received email; no randomized email-only comparison or attribution exists. H1 (SMS improves early pickup/reduces unclaimed holds) remains unresolved. Prompt delivered-group pickup supports continued observation, not causal benefit.

The circulation lead favors expansion; the supervisor highlights absent opportunities and reach failures. Neither changes policy. The 200 others’ consent, phone readiness, and hold opportunities are unknown. Offering 250 is five times the enrollment population, not demonstrably five times workload. These uncertainties and limited support favor continuation.

## Required journey and queue

R1: Staff Ready creates at most one logical SMS notice per hold’s Ready episode when cohort, consent, phone, and active-hold conditions qualify. Repeated events cannot duplicate it. Proposed default: no retroactive SMS after later enrollment; explain that eligibility applies at the next Ready event. No ready hold means no queue entry.

R2: Readers authenticate to manage consent and confirm their number through existing services. Withdrawal prevents queued submission. The hold page retains current state and deadline. Only the desk scan records Collected; opening links/signing in never does.

R3: Staff see waiting, delivered, failed, unresolved, and suppressed notices, with timestamps, reason, and next action. Recheck eligibility immediately before submission; collection, cancellation, expiry, withdrawal, or lost phone confirmation suppresses unsent work. Already submitted texts cannot be recalled.

R4: Track provider message ID and status; acceptance alone is unresolved pending delivery confirmation. Lost submission responses remain unresolved, never automatically retried. Lookup known IDs; staff reconcile uncertainty before any resend. Permit one staff retry only after confirmed non-delivery and renewed eligibility checks. Preserve attempts; concurrent actions cannot duplicate submission. Late statuses update delivery history without reopening holds or authorizing another text. Email remains the fallback.

## Rollout and planned checks

Proposed next-week 90-minute support cap: 20 enrollment, 50 exceptions, 20 follow-up; these are budgets, not measured estimates. Log actual minutes; stop enrollment when its allocation runs out, pause new SMS submissions when exception capacity is exhausted, and preserve email. No additional staff pool exists.

Before release, estimate the complete journey against five days; defer activation if essential controls cannot fit. Planned checks: eligible Ready queues once; outsiders/unconfirmed/nonconsenting readers cannot queue; withdrawal/terminal states suppress waiting work; duplicate events/retries and lost responses produce no duplicate texts; staff see failures and recovery; ownership, generic content, desk collection, and deadline rules hold.

V1–V2 remain reported passes in v1 staging, August 2: collection/expiry, link non-collection, and cross-reader denial. They are historical scoped evidence, not new-release passes or a production privacy audit. V3 automation checks remain unexecuted. V1 used manual SMS and a private delivery sheet, without queues, retries, or reader delivery status; lost-response provider behavior remains unverified.

Reconsider expansion after measured support usage, enrollment/reach counts, and fully matured first-hold outcomes; no opportunities means inconclusive pickup evidence. Expansion requires a capacity estimate within 90 minutes and resolved queue safety checks, not a claimed pickup lift.
