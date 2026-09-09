# BorrowBox staff-approved pickup pilot

Version 0.3 — specification reflecting the 2026-09-10 decision, replacing the 2026-08-20 instant-reservation plan.

## Purpose and scope

Learn whether invited members and depot staff can complete a request-and-approval workflow without mistaking a request for a confirmation. Pilot scope: 10 named tool types identified by the inventory CSV, East and West depots, and invited members already verified in the existing member database. Members choose a depot and submit one tool request at a time; submission neither reserves stock nor promises a pickup slot.

No public registration or account verification, deposits or other payment operations, live inventory, SMS, or unattended/automated pickup are included. Existing green styling is usable. Newsletter signup, repair-fair posters, and lending-library collaboration are outside this workflow; newsletter membership does not confer pilot eligibility.

## Evidence and decision history

- **2026-08-14 observation:** Seven of ten existing members in a staff-assisted paper exercise wanted to choose a confirmed pickup slot. Staff manually checked availability. No unattended reservation flow, signup flow, or payment was tested.
- **2026-08-20 decision, superseded:** The planning group selected instant confirmation conditional on a partner inventory API and refundable-deposit integration. Neither integration was tested.
- **2026-09-04 observation:** In six phone requests at West, staff approved four and declined two because tools were already out. This describes the phone service, not app performance or improvement over a baseline.
- **2026-09-10 current decision:** With the partner API unavailable and deposits removed by the board, use staff approval for invited, verified members. Review after two staffed weeks before expansion.

The former 40-tool public launch, member-selected slots, instant confirmation, minute-by-minute inventory updates, five-second confirmation promise, self-service cancellation after approval, and automatic 48-hour cancellation/refund are superseded. The former 20% pickup-growth aspiration is not a validated target. No adoption, conversion, or revenue result has been validated.

## Member and operator workflow

1. Sign in using the existing member system. Require both verified status and inclusion on the pilot invitation list to submit; offer no new-account flow.
2. Choose East or West and one of its listed pilot tools. Explain that imported counts may be stale and staff will check availability. Show the depot's last successful import time.
3. Submit. Once stored, display **“Requested — awaiting staff approval”**, a request identifier, depot, tool, and response deadline. Do not show a confirmed pickup window or reservation language.
4. Assigned depot staff review pending requests and check the authoritative local ledger before deciding. Approval requires a staff-chosen pickup window; decline displays its outcome and reason. Persist the decision before attempting email.
5. The member reads authoritative on-screen status. Approval shows the pickup window, location, and instructions; decline makes clear that pickup is not approved.
6. A member may withdraw a pending request. After approval, direct cancellation requests to depot staff by phone. Staff record the resulting cancellation when handled. Operators record collection and uncollected items; elapsed time alone never cancels a request.

Both depots operate Tuesday–Saturday, 10:00–18:00 Asia/Seoul. Accept eligible requests outside these hours. Approval or decline is due within two staffed hours from submission, counting only opening intervals; earlier responses are allowed. For example, Saturday 17:00 submission is due Tuesday 11:00. Show the deadline to members and operators and flag overdue pending requests without automatically deciding them.

## State, access, and reliability requirements

A stored request begins **Requested** and transitions to **Approved**, **Declined**, or **Withdrawn**. Approval carries its pickup window. Staff-handled cancellation and collection/uncollected records follow approval; uncollected is an operational record, not an automatic cancellation. Retain request identifiers, member/depot/tool, timestamps, actor, and decision history. Track notification delivery separately from request status.

Members can read only their own requests and withdraw only their own pending requests. Operators can view and decide requests only for their assigned depot. Enforce these rules on every data read and action, including direct identifier access.

Import the daily 08:00 CSV. If the latest successful import for a depot is more than 24 hours old, block new submissions for that depot and explain that availability needs refreshing. Treat no successful import as unavailable. Keep existing statuses readable, and preserve requests across imports. Imported counts never replace the ledger check.

## Observable acceptance conditions

| Situation/action | Required result |
| --- | --- |
| Uninvited or unverified member submits | Reject without creating a request; explain eligibility. |
| Eligible submission with fresh depot data | Store one request and show the exact awaiting-approval message, identifier, and staffed-hours deadline. |
| Import age exceeds 24 hours at submission | Block that depot even if the page was loaded earlier; retain readable existing statuses. A successful refresh restores eligibility without deleting requests. |
| Submission times out and the member retries the same attempt | Return the same logical request and identifier if already stored; otherwise create at most one. Do not report success without a stored request. |
| Operator approves after checking ledger | Store approval and required window; member sees approved pickup instructions. Missing window or wrong-depot operator cannot approve. |
| Ledger shows requested tool unavailable | Operator can decline with a reason; no pickup confirmation appears. |
| Withdrawal races with approval | Commit only one pending-state transition. The losing action receives the resulting status and explanation; approval cannot overwrite withdrawal or vice versa. |
| Decision email fails | Preserve the decision and on-screen status. Operator sees the failed notification and can retry without repeating or changing the decision. |
| Member requests another member's record | Deny access without revealing its contents. |
| Approved member attempts withdrawal, or item remains uncollected for 48 hours | Provide phone cancellation guidance for the former; record noncollection for the latter. Neither triggers automatic cancellation or payment activity. |

## Pilot readiness, learning, and unresolved questions

Before opening, verify the 10-tool catalog, invitation list, depot operator assignments, successful imports, depot phone numbers/locations, and staffing coverage. Walk through the acceptance conditions with design, engineering, and operators.

During the pilot, record submission outcomes, approval/decline/withdrawal outcomes, staffed-hours response times and overdue requests, retry/notification failures, and uncollected items. Observe members explaining whether submission guarantees pickup; record confusion and staff difficulty completing decisions. These are learning measures, with no invented success threshold or causal uplift claim.

Review after two staffed weeks, reporting denominators, observed problems, and limitations. Decide whether to revise or continue before expanding tools, public signup, or unattended pickup. Pilot start/review dates, future deposits, and long-term noncollection policy remain unresolved. Deposit amount and noncollection policy belong to product/board decisions, not engineering defaults.
