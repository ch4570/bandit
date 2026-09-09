# BorrowBox staff-approved pickup pilot

Current specification: reflects the pilot decision dated 2026-09-10. Supersedes the 2026-08-20 instant-reservation plan. This is a specification, not evidence of launch or validated results.

## Purpose and evidence

Learn whether invited, already-verified members and depot staff can complete a request-and-approval workflow without mistaking a request for confirmation.

- **2026-08-14 observation:** Seven of ten existing members in a staff-assisted paper exercise wanted to choose a confirmed pickup slot. Staff checked availability manually. No unattended reservation, signup, or payment flow was tested.
- **2026-08-20 decision, superseded:** The planning group selected instant confirmation conditional on a partner inventory API and refundable-deposit integration. Neither integration was tested.
- **2026-09-04 observation:** Of six observed West phone requests, staff approved four and declined two because tools were already out. This describes the phone service, not app testing or improvement over a baseline.
- **2026-09-10 current decision:** The partner API is unavailable for this pilot; the board removed deposits. Use staff approval, no automatic confirmation, and invited verified members only. Review after two staffed weeks before expansion.

## Scope and operating model

Pilot scope is 10 named tool types across East and West, with one tool per request. Members choose a depot, not a confirmed pickup slot. Submission neither reserves stock nor promises a pickup window. Only staff approval supplies a staff-chosen pickup window.

Both depots operate Tuesday–Saturday, 10:00–18:00 Asia/Seoul. Requests are accepted outside these hours when inventory freshness permits. Staff must approve or decline within two staffed hours of receipt; only opening intervals count, and earlier responses are allowed. Display the calculated response deadline. A Saturday 17:00 request is due Tuesday 11:00; a Sunday request is due Tuesday 12:00. An overdue request stays pending and is visibly overdue to operators; it does not auto-confirm or auto-decline.

Exclude public signup, account verification, payments of any kind, live inventory promises, SMS, unattended pickup, automatic lock control, and automatic 48-hour cancellation. Retire the former 40-tool, same-day instant-confirmation scope and 20% pickup-growth aspiration as current requirements. The existing green palette is usable. Newsletter signup, posters, and repair-fair planning are outside this pilot; partner data sharing is unavailable.

## Member and operator experience

1. Authenticate using the existing member database. Allow submission only for an invited member whose existing status is verified; provide an eligibility explanation otherwise. Do not create or verify accounts.
2. Show the pilot tool types by depot from the latest successful CSV import, its timestamp, and a warning that availability requires staff checking. Do not present stale counts as guaranteed stock.
3. Submit one selected tool and depot. Persist the request with member ID, receipt time, and response deadline; show **“Requested — awaiting staff approval”**, a stable request reference, and status access. Explain that no stock or slot is reserved.
4. The assigned depot operator sees pending requests and deadlines, checks the authoritative local ledger, then approves with a pickup window and depot instructions or declines with a member-readable reason. Do not allow approval without a pickup window or ledger-check acknowledgement.
5. Members see their own current status. Approval shows its pickup window and location; decline shows its reason. Pending requests offer withdrawal. Approved requests explain that cancellation requires calling depot staff during staffed hours; provide the depot phone contact.
6. Operators handle approved cancellations by phone and record the outcome. Record collection or noncollection against an approval; noncollection does not automatically cancel it or impose a penalty. Inventory and physical handoff remain staff-managed.

## State, reliability, and access acceptance

The decision states are **Requested**, **Approved**, **Declined**, **Withdrawn**, and **Cancelled by staff**. Collection/noncollection is a separate operational record. Store decision time and actor; keep notification delivery separate from the decision.

| Given / when | Required observable outcome |
|---|---|
| Eligible member submits a valid tool/depot request | Exactly one Requested record appears with the required awaiting-approval text; no reservation or pickup-window promise appears. |
| Submission times out and the member retries the same attempt | A stable submission identifier returns the same logical request, even if the original write succeeded. Show uncertainty and safe retry until status is recovered; never falsely claim failure or create a duplicate. |
| Latest successful depot import is over 24 hours old, or none exists | Block new submissions at that depot, including attempts from an already-open form, and explain that availability needs refreshing. Exactly 24 hours is not “over 24.” Other fresh depots remain usable. |
| A CSV refresh succeeds or fails | Success updates catalog freshness without erasing requests. Failure retains the previous successful timestamp; existing statuses remain readable. The export is produced daily at 08:00; freshness uses successful import time. |
| Assigned operator approves after checking the ledger | Persist Approved and its staff-chosen window; show them to the member. A decline instead persists Declined and its reason. |
| Pending member withdrawal races with operator approval | Commit only one transition atomically. The losing action receives the actual final state and an explanation; an approval winner directs cancellation to the phone route. Repeated actions cannot overwrite the outcome. |
| Decision email fails | Preserve the decision and authoritative on-screen status. Show operators which notification failed and offer retry of that notification without re-deciding the request. |
| Another member requests a request URL, or an operator accesses another depot | Deny reading or changing the record through both interface and server access checks. Signing in alone grants neither permission. |
| Member tries to withdraw an already-decided request | Reject the transition and show current status; approved cancellation remains staff-by-phone. |

## Pilot readiness and learning

Before launch, configure the invitation list, 10 named tool types, depot assignments, phone contacts, imports, and operator coverage. Verify the acceptance conditions with synthetic cases, including the weekend deadline, timeout retry, failed email, and concurrent decisions. These are required checks, not completed test results.

During two staffed weeks, record submissions, approvals, declines, withdrawals, collection/noncollection, overdue decisions, import blocks, and notification failures/retries. Report timely decisions divided by all requests requiring a staff decision, excluding withdrawals, alongside counts and unresolved overdue requests. Observe members explaining their status after submission and approval; record correct interpretations out of observed participants and any request/confirmation confusion. Gather staff completion difficulties and ledger-check issues.

At review, use these observations to decide whether to revise, continue, or expand. No adoption target, conversion uplift, revenue result, or numeric success threshold has been validated.

## Unresolved decisions

Confirm the exact tool names, invitation membership, phone contacts, pilot start/review dates, and review owner before launch. Product/board retain future deposit amount and noncollection policy decisions. Public signup, expanded inventory, and unattended pickup require a post-pilot decision; they are not implicit follow-on commitments.
