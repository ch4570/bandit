# BorrowBox staffed pickup requests — PRD

Version 0.3. Synthetic specification reflecting the supplied pilot decision dated **2026-09-10**; replaces the 2026-08-20 instant-reservation plan. Requirements and acceptance checks below are specified, not implementation or launch evidence.

## Direction and evidence

Authority: [decisions and observations](../decisions-and-observations.md), “Current pilot decision, 2026-09-10,” and [operating constraints](../current-constraints.md). The board adopted staff approval because the partner API is unavailable and removed deposits. The pilot serves invited, already-verified members, with 10 named tool types at East and West. Its learning goal is whether members and staff complete the workflow without mistaking a request for confirmation.

Historical record (synthetic; preserved under original conditions):

- **2026-08-14:** Seven of ten existing members in a staff-assisted paper exercise wanted to choose a confirmed pickup slot. Staff checked availability manually. No unattended reservation, signup, or payment flow was tested. This does not validate the new workflow.
- **2026-08-20:** The planning group selected instant confirmation conditional on a partner inventory API and refundable-deposit integration; neither was tested. The v0.2 plan included public signup, 40 types, same-day slot selection, sub-five-second confirmation, and automatic 48-hour cancellation/refunds. These requirements are superseded. Its 20% weekly-pickup aspiration had no baseline or established effect size and is retired.
- **2026-09-04:** Of six observed West phone requests, staff approved four and declined two because tools were already out. This describes the phone service, not an app test or measured improvement.

## Scope and access

Use the existing member database’s stable IDs, verified status, and pilot invitation list to permit submission. No account creation or verification. Members read only their own requests; signing in or possessing another request’s URL grants no access. Operators read and decide only their assigned depot’s requests. Enforce these boundaries on every read and action.

Each submission concerns one tool type and one depot; no basket. The CSV supplies the pilot catalog and depot associations, not guaranteed availability. Staff use the authoritative local ledger before deciding. Existing green styling is usable; poster, newsletter, and workshop work in [the calendar](../brand-calendar.md) adds no pilot dependency.

Exclude payments, authorizations, refunds, real-time inventory, SMS, public registration, automatic confirmation, and unattended pickup/tool-lock control.

## Journey, records, and decisions

A request records its stable identifier, member ID, tool type, depot, submission time, response deadline, status, and attributable decision history. Approval also records the staff-selected pickup window and location. Notification delivery is tracked separately from the request decision.

1. Eligible members choose a catalog tool and depot. Explain that availability is indicative and staff approval is required; members do not select a promised pickup slot.
2. Persist the request before showing **“Requested — awaiting staff approval”**, its identifier, status link, and response deadline. Submission neither reserves stock nor promises pickup. A timeout means the outcome is uncertain: offer safe retry/status recovery. Repeating the same submission must recover one logical request, even after a lost response.
3. Operators see their depot’s pending queue and deadlines, check the local ledger, then approve with a pickup window or decline. Display the recorded outcome to the member and attempt email notification. Proposed operating detail: require a short decline reason so the member understands the outcome.
4. Members revisit authoritative on-screen status. Approved status includes window, depot location, and staff phone contact for cancellation. Pending requests offer withdrawal. Approval is never inferred from email delivery or elapsed time.

| Current state | Actor/action | Result and recovery |
|---|---|---|
| Awaiting approval | Owner withdraws | Withdrawn; no approval may subsequently replace it. |
| Awaiting approval | Assigned operator approves/declines | Approved with window, or Declined; recorded decision remains visible. |
| Approved | Member seeks cancellation | Direct to depot staff by phone; no member cancellation action. Staff record the resolved cancellation. |
| Approved | Staff handle pickup | Retain collection/return recording from v0.2. Record uncollected items without automatic cancellation or expiry. |

Withdrawal and decision compete for one transition: the first committed action wins; the loser receives the actual current state and an explanation. Repeated/stale operator actions cannot overwrite it. Proposed operating detail: ledger allocation accompanies approval to avoid promising the same unit twice; software does not claim a live external stock lock.

## Operating limits and recovery

Both depots staff **Tuesday–Saturday, 10:00–18:00 Asia/Seoul**. Accept requests outside these hours. Approval or decline is due within **two staffed hours**, counting only these intervals from submission. Show overdue pending requests to operators; a missed deadline never auto-approves or declines.

CSV export occurs daily at 08:00. If the latest successful import is **more than 24 hours old**, block new requests for that depot and explain that availability needs refreshing. With no successful import, also block. Failed imports do not advance freshness. Keep existing statuses readable; successful refresh restores submissions without erasing requests. Recheck freshness at submission.

Email failure preserves the staff decision and on-screen status. Operators see the affected notification, failure, and retry action. Retry delivery without creating another request or decision. A failed request save must not appear successful; provide retry without duplication.

## Planned acceptance checks

All checks are **planned; outcomes unobserved**. No supplied product code or tests were executed.

- Given invited verified membership and fresh depot data, submitting one tool persists one pending request with the exact awaiting-approval label, deadline, and no reserved stock or pickup promise.
- Given an uninvited/unverified member, submission is denied; given another member’s identifier or another depot’s operator, unauthorized reads/actions reveal no request details and make no change.
- Given a submission timeout after persistence, retry returns the same request; given save failure before persistence, no success appears and retry can create exactly one request.
- Given Saturday 17:00 submission, the deadline is Tuesday 11:00; given Sunday submission, it is Tuesday 12:00.
- Given import age exactly 24 hours, freshness alone does not block; beyond 24 hours or without an import, submission blocks while status remains readable. Failed refresh preserves the block; successful refresh preserves requests.
- Given ledger review, approval requires a window and displays pickup instructions; decline displays its outcome. Email failure leaves either decision intact and exposes operator retry.
- Given simultaneous withdrawal and approval, exactly one wins and both actors see the resulting state; repeated decisions cannot replace it.
- Given approval, member cancellation routes to phone; an uncollected item remains recorded without 48-hour auto-cancellation or refund.

## Pilot review and unresolved details

Review after two staffed weeks before expansion. Proposed measurements: recorded submissions, approvals/declines/withdrawals, staffed-time response compliance, notification retries, and observed request-versus-confirmation misunderstandings. Report counts and denominators; no observations means no conclusion. No adoption, conversion, revenue, or uplift target is validated.

Before launch, the pilot owner must supply the exact 10 tool names, invitation list, depot phone/location details, and start date; operations must confirm ledger allocation and pickup-window practice. Product retains future deposit amount and noncollection policy decisions. Neither is delegated to engineering nor blocks this payment-free pilot.
