# BorrowBox pickup-request pilot PRD

Rewritten against the supplied 2026-09-10 decision. All material is synthetic. This is a planning specification; implementation and acceptance checks have not been executed.

## Purpose, authority, and scope

Help invited, already-verified members and depot staff complete a request-and-approval journey without mistaking a request for a confirmation. The [2026-09-10 board decision](../decisions-and-observations.md) supersedes the instant-reservation plan. [Operating constraints](../current-constraints.md) govern access, hours, inventory, and recovery.

Include 10 named pilot tool types, East and West depots, one tool per submission, staff decisions, pickup windows, pending withdrawal, status tracking, and notification recovery. Use existing member records, invitations, request storage, morning inventory CSV, local ledgers, and email adapter.

Exclude public registration, member verification, payments/deposits/refunds, real-time inventory, automatic confirmation, SMS, unattended pickup, and automatic 48-hour cancellation. Staff retain collection/return recording. Newsletter signup and repair-fair branding are separate work; the existing green palette remains usable ([calendar](../brand-calendar.md)).

## Actors and records

- **Member:** existing stable member ID, invited and verified; may submit and read only their own requests and withdraw their own pending requests. Signing in or possessing a request link grants no access to someone else’s request.
- **Depot operator:** may view, decide, and maintain fulfillment records only for their assigned depot. Staff use the local ledger before approval or decline.
- **Request:** belongs to one member and depot and identifies one pilot tool type. Record submission time, response deadline, current state, decision actor/time, pickup window when approved, and notification status. Preserve transitions and withdrawal/cancellation details.
- **Inventory import:** identifies pilot tools by depot and last successful import time. Counts are indicative, never a reservation promise. Refreshing inventory preserves requests and their history.

Proposed defaults below are draft product choices, not additional board policy. “One at a time” means one tool per submission; no additional concurrent-request limit is inferred.

## Member journey and availability

1. Sign in through existing access. Check invitation and verified status before accepting a request; ineligible users receive an explanation without signup or verification controls.
2. Choose East or West and one of its pilot tools. Show inventory freshness and explain that staff must check availability; no confirmed slot is offered here.
3. Accept requests outside staffed hours. If the depot’s latest successful import is more than 24 hours old, block new submissions and explain that availability needs refreshing. **Proposed recovery:** also block when no successful import exists. Check freshness again at submission; exactly 24 hours old remains eligible.
4. After durable recording, show **“Requested — awaiting staff approval”**, request reference, response deadline, and status access. State explicitly that this does not reserve stock or promise a pickup slot.
5. A timeout means the outcome is uncertain. Offer retry/status recovery using the same logical submission; retries return its existing result without creating another request. Do not display success before recording succeeds.

Existing request status remains readable during stale inventory and notification failures.

## Staff decisions, deadlines, and recovery

The response commitment is approval or decline within two staffed hours. Count only Tuesday–Saturday, 10:00–18:00 **Asia/Seoul**; staff may respond earlier. For example, Saturday 17:00 submission is due Tuesday 11:00; Sunday submission is due Tuesday 12:00. Show deadlines to members and operators. **Proposed default:** highlight overdue pending requests for operators; missing a deadline never auto-approves or declines.

| Transition | Permission, outcome, and recovery |
| --- | --- |
| Requested → Approved | Assigned operator checks the authoritative local ledger and supplies a pickup window. Show approval, depot pickup instructions, and window on screen; enqueue decision email. |
| Requested → Declined | Assigned operator checks the ledger and records a member-readable reason. Show the decision and email it. Member may make a fresh request when eligible. |
| Requested → Withdrawn | Owning member withdraws before a staff decision; show withdrawal to both parties. |
| Approved → Cancelled | Depot staff record cancellation arranged by phone. Member status supplies the depot phone contact; no member self-cancellation control after approval. |

**Proposed consistency rule:** the first durably recorded approval, decline, or withdrawal wins. Competing or repeated actions cannot replace it; show the losing actor the current result. Operators must coordinate ledger allocation before approving competing requests for the same stock; a stale CSV cannot justify approval. If recording fails or is uncertain, reconcile the request and ledger before promising pickup.

**Proposed fulfillment model:** retain approval history and separately record awaiting collection, collected, returned, or uncollected. Operators record uncollected items manually; no automatic expiry, fee, refund, or inferred noncollection deadline applies.

Email delivery is separate from the request decision. Failure preserves approval/decline and authoritative on-screen status. Operators see the failed notification and can retry delivery without repeating the decision or creating a request.

## Planned acceptance scenarios

These are unexecuted checks for the pilot build using synthetic invited/uninvited members, both depot roles, fresh/stale imports, and simulated storage/email failures.

1. Given an invited verified member and fresh depot data, submitting one tool records one request and the exact pending message; no stock reservation, payment, or pickup promise occurs. Ineligible submission is rejected.
2. Given another member’s request or another depot’s operator, reading or changing it is denied; the owner and assigned operator retain permitted access.
3. Given an import aged over 24 hours, submission is blocked with a refresh explanation while existing status remains readable. A successful refresh permits eligible submissions without deleting history.
4. Given a timed-out recorded submission, retry returns the same reference and state. Given no recorded request, recovery creates at most one logical request.
5. Given the Saturday/Sunday examples above, deadlines match the stated Tuesday times; overdue requests remain pending and visible.
6. Given ledger-verified availability, approval requires a pickup window and displays pickup instructions. Unavailable stock produces a reasoned decline; competing requests cannot receive the same unavailable allocation.
7. Given simultaneous withdrawal and approval, exactly one transition persists and the losing action displays it. After approval, the member is directed to phone cancellation; staff cancellation is reflected in status.
8. Given email failure after approval, approval remains readable and operators can retry the failed notification. Collection, return, and uncollected recording never trigger automatic cancellation or money movement.

## Evidence, learning, and remaining decisions

Historical evidence remains limited to its original conditions:

- **2026-08-14:** seven of ten existing members in a staff-assisted paper exercise wanted a confirmed pickup slot; staff manually checked availability. No unattended flow, signup, or payment was tested. Historical preference evidence only.
- **2026-08-20:** planning group selected instant confirmation conditional on an untested partner inventory API and refundable-deposit integration. Superseded by the supplied **2026-09-10** pilot decision, including the former 40-tool/public-signup direction.
- **2026-09-04:** six observed West phone requests produced four approvals and two declines because tools were out. Phone-service evidence only; neither an app test nor measured improvement.

Review after two staffed weeks. Proposed measures: eligible submissions, approvals/declines/withdrawals, staffed response times and overdue counts, notification failures, and observed member/staff confusion between requested and approved. Report denominators, observation period, and limitations. The old 20% weekly-pickup aspiration had no baseline; no adoption, uplift, or revenue result is validated.

Before operating, identify the 10 tool names through the import, supply depot phone/pickup details, assign operator coverage, and settle proposed ledger coordination and fulfillment defaults. Start date and quantitative expansion thresholds remain open. Review evidence before expanding tools, public signup, or unattended pickup. Future deposit amount and noncollection policy remain board decisions, outside this pilot’s implementation scope.
