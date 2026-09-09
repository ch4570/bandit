# HoldHarbor PRD — automated pickup SMS

Synthetic fixture: all people, policies, and records are fictional. This specification replaces manual SMS composition and private-sheet tracking with an automated, staff-visible queue.

## Authority and availability

Nora’s August 1 rules remain adopted: **D1**, Ready starts a seven-day hold; pickup through its deadline is allowed; 72 hours measures early pickup, not expiry. **D2**, ordinary automatic email continues for every ready hold; SMS requires explicit, withdrawable consent and a confirmed number. Neither replaces account authentication. **D3**, SMS contains only a generic ready-hold notice and sign-in link; authenticated readers see only their holds; authenticated branch staff manage this branch’s holds.

Queue automation is adopted; availability is undecided. **Recommendation (proposed): continue with the original 50 readers**, rather than offer enrollment to all 250. Enrollment need not await a ready hold and does not promise one. Pilot participation alone does not establish SMS consent. Requirements and rollout below use this proposed boundary pending Nora’s decision; no expansion has occurred or been announced.

## Evidence and rationale

[September 9 pilot notes](../pilot-notes.md) and [reader export](../reader-outcomes.csv) describe August 3–30 manual SMS plus ordinary email. Fifty desk-recruited readers were nonrandomly selected. Thirty had index ready holds; 20 had no opportunity, so their NA pickups are neither failures nor missing outcomes. All 30 outcomes were mature and desk-reconciled by August 30, 18:00 UTC; later holds are excluded.

Among 30 opportunities, 18 had consent and confirmed phones; 14 received SMS: 14/18 eligible deliveries (77.8%), 14/30 opportunities (46.7%), 14/50 participants (28%). Early/eventual pickups were 12/14 and 13/14 delivered; 1/4 and 2/4 failed-delivery; 3/7 and 5/7 no-consent; 2/5 and 3/5 unconfirmed-phone. Overall, 18/30 (60%) collected within 72 hours and 23/30 (76.7%) by expiry; seven did not. Eventual totals include early pickups.

Delivery does not establish reading. Universal email, nonrandom groups, and no assigned comparison prevent causal SMS attribution. H1—better early pickup and fewer unclaimed holds—remains unresolved, without an adopted numeric threshold. The circulation lead favors expansion; the supervisor highlights missed opportunities and reachability. Neither statement adopts policy. The other 200 readers’ consent, phone readiness, and demand are unknown. These data support bounded operational learning, not extrapolation to 250.

## Current requirements and recovery

**R1–R2 retained:** staff record Ready, Collected, Cancelled, or Expired through existing services; collection requires the desk scan. Notice opening/sign-in never collects. The reader page shows authoritative state and deadline, without extending it. Use the service’s deadline/timezone, including its deadline boundary.

**R3 replacement; proposed operational defaults:** one automatic SMS per eligible hold’s Ready event, with no recurring reminders or historical backfill. Enrollment/preferences belong to the authenticated reader; staff may assist but cannot infer consent. Readers outside the proposed cohort cannot enroll for this release. Readers without ready holds generate no message. Missing consent/confirmation suppresses SMS; email continues. Later eligibility applies to future Ready events.

A queue record belongs to one hold and records eligibility, timestamps, provider ID when available, status, and attention reason. Staff see waiting, submitted/pending, delivered, failed, unresolved, or suppressed/cancelled. Reader-facing delivery tracking is deferred.

Recheck eligibility and hold state before submission: withdrawal, invalidated confirmation, collection, cancellation, or expiry cancels waiting work. Already submitted messages cannot be recalled; withdrawal blocks subsequent submissions. Repeated Ready events or staff actions must not duplicate a send.

A known provider ID permits status lookup. Confirmed delivery ends work. Definitive failure shows its reason; staff may retry only after correction and eligibility recheck. A lost submission response or uncertain delivery becomes unresolved: no blind resend. Staff reconcile via provider lookup when possible; otherwise retain uncertainty and rely on email. Provider behavior after lost responses remains unverified.

## Rollout and planned checks

One developer has five days including fixes and verification; component estimates remain unknown. Reuse existing services/provider/staff app. Defer new apps, branches, marketing, and borrowing-policy changes.

Proposed next-week support budget: 30 minutes enrollment, 45 exceptions, 15 follow-up; log actual minutes. Stop enrollment at its cap; pause new SMS submissions when exception capacity is exhausted, preserving queue visibility and email. No additional staff pool exists. Review unresolved cases and workload before considering broader availability; 50 readers is not a capacity guarantee. Measure enrollment assistance, eligible submissions, delivery exceptions, and support minutes next week; follow index pickups through seven days. Propose expansion only with resolved exceptions and a measured workload forecast fitting 90 minutes; otherwise retain or reduce enrollment. Nora decides availability.

Acceptance scenarios, all planned/unexecuted: eligible Ready creates one queue item; duplicate triggers create none; ineligible/outside-cohort/no-hold readers receive none; withdrawal or terminal hold state cancels waiting sends; lost responses cannot trigger duplicate retries; staff can distinguish delivery outcomes; unauthorized hold access fails; link opening leaves collection unchanged; seven-day collection/expiry remains intact.

V1–V2 retain reported August 2 v1-staging passes for lifecycle, link, and access checks; regression needs recheck. V3 queue checks remain unimplemented/untested. Operational records are not software passes.
