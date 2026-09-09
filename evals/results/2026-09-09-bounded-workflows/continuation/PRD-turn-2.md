# BorrowBox request-and-approval pilot — synthetic PRD

Replaces version 0.2 (2026-08-20). Planning authority: the 2026-09-10 board decision, amended by the user’s 2026-09-12 operating update. Launch is unverified.

## Purpose, authority, and scope

Help invited, already-verified members request tools and understand whether staff have approved pickup. Learn whether members and operators can complete this workflow without mistaking submission for confirmation.

Sources: [decisions and observations](../decisions-and-observations.md) and [operating facts](../current-constraints.md); the 2026-09-12 update supersedes depot scope and response duration. All evidence is synthetic.

The first pilot fortnight covers 10 named tool types at West only. Members choose one tool type per request; the depot is fixed to West. Operators check the local ledger, then approve with a staff-chosen pickup window or decline. Submission neither reserves stock nor promises a slot.

Excluded: deposits and all payment operations, automatic confirmation, live inventory integration, public registration or verification, SMS, unattended pickup, automated locks, and automatic 48-hour cancellation. Expansion waits for review after two staffed weeks.

## Actors and records

- Members use existing identity, stable member ID, verified status, and the invitation list. Only invited verified members may submit; members may read only their own requests. Request URLs grant no additional access.
- Operators may view and decide requests only for their assigned depot, including phone cancellation and collection records.
- Each request retains its member, tool type, depot, submission time, response deadline, current state, and attributable decision history. Approval records the operator and pickup-window start/end in Asia/Seoul. Notification delivery is separate from request state.
- West’s latest successful CSV import identifies its pilot catalogue and freshness. Availability counts are indicative; the local ledger determines approval.

**Proposed completion details:** prevent a second pending request by the same member until the first is decided or withdrawn, interpreting “one tool request at a time” conservatively. Eligibility loss blocks new submissions but preserves access to personal history. Product must settle these details before implementation relies on them.

## Member journey and freshness

Show West’s imported pilot tools, import timestamp, and a warning that availability requires staff checking. Never present counts as guaranteed stock or let members select a confirmed slot.

Display West as the sole pickup depot. East is unavailable and not selectable; reject East submissions from stale pages or direct requests without creating a request. At submission, recheck eligibility, West-only scope, and West’s import freshness. If the latest successful import is more than 24 hours old, block new West requests and explain that availability needs refreshing. Proposed fallback: also block when no successful import exists. Explain that members must await refresh; no alternate depot is available. Imports must preserve requests; stale data must not block reading status or resolving existing requests.

Persist one logical request before showing **“Requested — awaiting staff approval”**, West, and the four-staffed-hour response deadline. Repeated clicks or retries after timeout must recover the same request, not create another. If persistence is uncertain, show “Submission not yet confirmed” and a safe retry/status action; do not imply success or instruct creation of a new request.

Members can withdraw only while awaiting approval. Show authoritative status after actions and on reopening.

## Operator journey, states, and recovery

West’s assigned operators see its pending queue and deadlines. Before approval, the assigned operator checks the local ledger and records the allocation there so another approval cannot promise the same unavailable unit. Proposed operational safeguard: serialize checks and allocations per depot; an uncertain ledger update requires reconciliation before approval is shown.

Transitions are pending → approved, declined, or withdrawn. Approval requires a staff-chosen pickup window within staffed hours and displays depot pickup instructions. Decline displays a reason. Proposed window validation: require an end after its start and no already-ended window.

Withdrawal and staff decision compete for one transition: exactly one wins. The losing action changes nothing and receives the saved state. If approval wins, withdrawal explains that cancellation requires phoning the depot. Repeated or stale operator decisions cannot overwrite the winner.

After approval, members see phone cancellation instructions; no self-service cancellation is offered. Staff record a phone cancellation and reconcile the ledger allocation. Retain staff recording of collection and return. Operators record uncollected items after a missed window without automatically cancelling, releasing the allocation, or imposing a penalty. The board still owns noncollection policy.

Persist decisions independently of email delivery. Failed email leaves approval or decline intact and visible on screen. Operators see the affected notification, failure status, and retry action; retrying notification cannot repeat or reverse the decision.

## Service commitment and pilot operation

West operates Tuesday–Saturday, 10:00–18:00 Asia/Seoul. Accept requests outside those hours when freshness permits. Approval or decline is due within four staffed hours of submission, counting only those intervals; earlier responses are allowed. Show overdue requests to operators without automatically changing state.

Examples: Tuesday 17:30 submission is due Wednesday 13:30; Saturday 17:00 is due Tuesday 13:00. These deadlines promise a response, not approval.

Before launch, operators need the exact 10-tool mapping, West’s phone number and pickup instructions, named queue coverage, and a tested ledger coordination procedure. These operational details remain unresolved.

## Planned acceptance checks

Checks are planned, not executed.

1. Given an uninvited or unverified identity, submission is denied; another member’s request and an unassigned depot’s decision action remain inaccessible.
2. Given fresh West data, only West is selectable; East submissions are rejected. Successful submission shows the exact pending label without a slot or reservation promise. A timeout followed by retry yields one request and its saved status.
3. Given an import older than 24 hours, West rejects submission with no East fallback while existing status remains readable. A successful West refresh enables submission without deleting history. At exactly 24 hours, freshness alone does not block.
4. Given a pending request, ledger-backed approval shows the staff window; unavailable stock produces decline with a reason. Competing allocations cannot approve the same unavailable unit.
5. Given concurrent withdrawal and approval, one terminal pending-state transition wins and both parties see it; the loser gets an actionable explanation.
6. Given failed approval email, the member still sees approval and the operator can retry only the notification.
7. Given the service-time examples above, deadlines match; overdue requests stay pending and visible. Phone cancellation updates history and ledger; noncollection never triggers automatic cancellation.

## Evidence, superseded plans, and review

- **2026-08-14:** Seven of ten existing members in a staff-assisted paper exercise wanted a confirmed pickup slot. Staff checked availability manually. No unattended flow, signup, or payment was tested. Historical preference evidence only.
- **2026-08-20:** Planning selected instant confirmation conditional on untested inventory and refundable-deposit integrations. Superseded by the 2026-09-10 decision, along with 40-tool public checkout, five-second confirmation, and automatic cancellation/refunds.
- **2026-09-04:** Of six observed West phone requests, four were approved and two declined because tools were out. This describes phone service, not app success or baseline improvement.
- **2026-09-10:** Adopted staff approval without deposits for invited verified members, initially at East and West with a two-staffed-hour response commitment. Depot scope and response duration are superseded; other decisions stand.
- **2026-09-12:** User reports East cannot staff the first fortnight; adopt West-only requests and four staffed hours for responses. No new workflow results were supplied.

At West’s two-staffed-week review, report submitted requests, decisions within deadline/decisions due, withdrawals, uncollected approvals, notification failures, and observed request-versus-confirmation misunderstandings with participant denominators. Collect member and operator completion observations. Proposed measurement plan; no validated adoption threshold, revenue result, or conversion uplift exists. The old 20% pickup aspiration had no baseline or demonstrated effect. Future deposits and noncollection policy remain board decisions; evidence from this pilot must inform expansion.
