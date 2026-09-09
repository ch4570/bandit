# BorrowBox staffed pickup pilot — PRD

Rewritten against the supplied **2026-09-10 pilot decision**; this is a specification, not evidence of implementation or launch. All inputs are synthetic.

## Direction and authority

Invited, already-verified members request tools from East or West; depot staff decide after checking the local ledger. The goal is to learn whether members and operators can complete this workflow without confusing a request with confirmation.

[Current decisions](../decisions-and-observations.md#current-pilot-decision-2026-09-10) replace the 2026-08-20 instant-reservation plan. [Operating facts](../current-constraints.md) govern hours, eligibility, freshness, access, and recovery. The [calendar](../brand-calendar.md) adds no pilot requirements: newsletter membership grants no eligibility, and poster exchange supplies no inventory or member data.

Scope: 10 named pilot tool types, two depots, existing sign-in, request submission/status, operator decisions, email notification, and pickup tracking. Exclude deposits and all payment operations, real-time inventory promises, public registration/verification, SMS, unattended pickup, and automatic confirmation or noncollection cancellation.

## Actors and records

- Members must have both verified status in the existing database and pilot invitation eligibility to submit. No account creation or verification occurs here. Members read only their own requests.
- Operators read and decide only requests belonging to their assigned depot. Signing in or possessing a request link does not authorize access.
- A request belongs to one stable member ID and identifies one tool type and depot. Record submission time, status, staff decision/actor/time, and any staff-selected pickup window. Notification status is separate.
- The daily 08:00 inventory CSV identifies pilot types by depot; counts are indicative and may be stale. The local ledger governs approval. Submission creates no stock hold and promises no pickup slot.

**Proposed defaults:** Each submission covers one tool type; “one at a time” does not impose an undocumented global limit on outstanding requests. Submitted tool/depot cannot be edited: withdraw while pending and submit anew. Pickup windows use Asia/Seoul and fall within staffed hours. These choices keep the pilot simple and require product confirmation before implementation.

## Member journey and availability

1. Sign in through the existing member service. Explain ineligibility without offering signup. Show eligible members the depot and imported pilot tool choices, latest successful import time, and a notice that staff must check availability.
2. Before accepting a new request, check that depot's latest successful import is no more than 24 hours old. Older data blocks submission with “Availability needs refreshing”; existing status remains readable. **Proposed:** no successful import also blocks submission. An import failure does not advance freshness; refreshing preserves requests.
3. Persist the request, then display **“Requested — awaiting staff approval”**, its reference, and the response deadline. A request is never labeled confirmed merely because submission succeeded.
4. On timeout, show that receipt is uncertain and offer safe retry/status lookup. Repeating the same submission recovers the same logical request and reference, including any subsequent decision; an explicit new submission is distinct.
5. The member can reopen status to see pending, approved with pickup details, declined, or withdrawn. Approved status supplies depot, pickup window, and the depot's phone contact for cancellation.

## Decisions, deadlines, and recovery

Requests are accepted outside staffed hours. Approval or decline is due within **two staffed hours**, counting only Tuesday–Saturday, 10:00–18:00 Asia/Seoul. For example, Saturday 17:00 is due Tuesday 11:00. Staff may respond earlier. Show due/overdue requests to operators; overdue remains pending, with a delay notice to the member, never auto-approved or auto-declined.

| Transition | Authority, result, and recovery |
|---|---|
| Pending → approved | Assigned operator checks the authoritative ledger and chooses a pickup window. Record approval and show pickup instructions. **Proposed:** record the allocation in the ledger before completing approval; competing requests cannot receive the same unavailable unit. If ledger allocation cannot be established, keep pending and show the operator a recoverable error. |
| Pending → declined | Assigned operator checks the ledger; record and show the decline. **Proposed:** require a member-readable reason so the member can choose another tool/depot or try later. |
| Pending → withdrawn | Owning member withdraws; show withdrawal and remove from the decision queue. |
| Withdrawal races approval | Exactly one transition wins. If approval wins, withdrawal reports approved status and phone cancellation instructions. If withdrawal wins, approval reports withdrawn and must not leave a ledger allocation for it. |
| Approved → staff cancellation | Member phones the depot; no member self-service cancellation. **Proposed:** operator records cancellation and reconciles any ledger allocation. |

Repeated or stale decisions must return the recorded outcome rather than overwrite it. Failed decision saves must not display success; retries recover any persisted result and operators reconcile uncertain ledger allocations before reassignment.

Retain the requirement for staff to mark collection and return. Operators record uncollected items without automatically cancelling, releasing stock, charging, or refunding. The longer-term noncollection policy remains unresolved.

After a recorded decision, attempt email notification. On failure, preserve the decision and authoritative on-screen status; show operators which notification failed and allow retry without creating another decision. Email delivery is not a prerequisite for approval.

## Planned acceptance scenarios

These checks are **planned; outcomes unobserved**. No product code or tests were run.

- Given invited verified membership and fresh depot data, submission persists one request and displays the exact awaiting-approval message; no stock reservation or pickup promise appears.
- Given missing invitation or verification, submission is denied. Another member's request and another depot's operator queue remain inaccessible even through direct links.
- Given an import exactly 24 hours old, freshness alone permits submission; beyond 24 hours, submission is blocked. Existing requests remain readable after failure and refresh.
- Given a saved submission whose response timed out, retry returns its original reference and current status with no duplicate request.
- Given a Saturday 17:00 request, the deadline is Tuesday 11:00; passing it leaves the request pending and visibly overdue.
- Given available ledger stock, approval records a staffed pickup window and instructions. Given unavailable stock, decline shows its reason. Competing approvals cannot allocate the same unit.
- Given concurrent withdrawal and approval, one wins and both parties see the resulting state; no orphan allocation remains.
- Given a saved approval and failed email, approval remains readable and the operator can retry notification. Phone cancellation, collection, return, and uncollected recording produce their stated outcomes; elapsed 48 hours triggers no cancellation.

## Evidence, learning, and handoff

**Historical only:** On 2026-08-14, seven of ten existing members in a staff-assisted paper exercise wanted a confirmed pickup slot; staff checked availability manually. No unattended flow, signup, or payment was tested. On 2026-08-20, planners selected instant confirmation conditional on untested inventory/deposit integrations; that decision is superseded. On 2026-09-04, six observed West phone requests yielded four approvals and two declines because tools were out. This supports the relevance of availability checks, not app success or measured improvement.

Review after two staffed weeks. **Proposed measurement:** report submitted requests, decision outcomes, decisions within deadline/submissions due, withdrawal conflicts, notification failures, and observed request-versus-confirmation misunderstandings with participant counts. Record conditions and denominators; no uplift, revenue, or adoption claim is established. The former 20% weekly-pickup aspiration had no baseline and is not a current target.

Before implementation, resolve proposed defaults and confirm actual tool names, depot phone contacts, and ledger allocation/reconciliation procedure. Product owns unresolved future deposit and noncollection policies. Review pilot evidence before expanding tools, public signup, or unattended pickup.
