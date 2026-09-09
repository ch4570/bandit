# BorrowBox staff-approved pickup pilot

Version 0.3 — specification for the supplied 2026-09-10 decision. Synthetic planning artifact; implementation and acceptance checks have not been executed.

## Direction and authority

Help invited, already-verified members request tools and understand when staff have approved pickup. The [2026-09-10 board decision](../decisions-and-observations.md#current-pilot-decision-2026-09-10) supersedes instant confirmation, deposits, public signup, and automatic cancellation. [Operating facts](../current-constraints.md) govern access, hours, freshness, persistence, and recovery. This document specifies the complete pilot journey; proposed details below remain distinguishable from adopted policy.

Scope: 10 named pilot tool types, East and West depots, existing member accounts, one tool per submission, staff ledger review, staff-selected pickup windows, email, authoritative on-screen status, and operator follow-up. The morning CSV identifies eligible tool types and depot; its counts are indicative, never a reservation guarantee.

Exclude payments of every kind, real-time inventory integration, public registration or verification, SMS, unattended pickup, automatic tool locks, and automatic 48-hour cancellation. Newsletter, posters, and workshops are outside this journey. Future deposits and noncollection policy belong to Product/the board.

## People, records, and access

A member must be on the invitation list and verified in the existing member database to submit. Signing in alone confers neither eligibility nor access to someone else's requests. Members can read only their own requests; assigned depot operators can read and decide that depot's requests. Enforce these boundaries on direct links and actions as well as screens.

Each request belongs to one stable member ID, one depot, and one pilot tool type. Retain its identifier, submission time, response deadline, state, decision actor/time, and any pickup window or decline explanation. Inventory refreshes must preserve requests. Notification delivery has separate pending/sent/failed status and retry information; it never determines request state.

Proposed: snapshot tool/depot labels with the request so later catalog changes do not obscure history. “One at a time” means one tool per submission; no unsupported cap on outstanding requests is imposed.

## Journey and state rules

1. **Enter and choose.** Eligible members choose a depot and pilot tool. Explain that requests do not hold stock or promise a pickup slot. Display inventory freshness. If that depot's latest successful import is more than 24 hours old, block new requests with “Availability needs refreshing”; keep existing statuses readable. Proposed: missing successful imports also block requests. Failed imports do not reset freshness.
2. **Submit.** Recheck eligibility and freshness at submission. Persist one logical request before displaying **“Requested — awaiting staff approval.”** State becomes `Requested`; no stock reservation occurs. Show its ID, response deadline, and status page. A timed-out submission is an uncertain outcome: retry/reconcile the same submission without creating another request. A definite save failure shows failure and allows retry; never show a successful request without a stored record.
3. **Decide.** Assigned staff inspect the authoritative local ledger, then approve with a pickup window or decline with an explanation. Approval changes `Requested → Approved`; decline changes `Requested → Declined`. Members see the recorded result and, on approval, depot location, pickup instructions, and window. Proposed: require window start/end in Asia/Seoul within staffed hours and record the allocation in the ledger before releasing approval, coordinating competing requests so one unit is not promised twice. CSV counts cannot authorize approval.
4. **Withdraw.** The owner may change `Requested → Withdrawn`. Competing withdrawal and approval must produce exactly one final outcome: the first committed transition wins. The losing action receives the current state; an approval loser must release any provisional ledger allocation. Repeated decisions or withdrawals cannot duplicate effects. Approved requests direct members to depot staff by phone for cancellation.
5. **Fulfil and follow up.** Retain operator recording of collection and return (`Approved → Collected → Returned`). Staff handle approved cancellations by phone and record `Cancelled` with ledger release. Operators record uncollected items against the request; elapsed time alone neither cancels it nor creates a fee/refund. Proposed: flag “Uncollected” after the pickup window while retaining approval until staff resolve it under board guidance. No automatic reallocation or new penalty policy is implied.

## Timing and recovery

Both depots operate Tuesday–Saturday, 10:00–18:00 Asia/Seoul. Accept requests outside these hours when inventory is fresh. Approval or decline is due within two staffed hours of submission, counting only opening intervals; earlier decisions are allowed. For example, Tuesday 17:00 is due Wednesday 11:00; Saturday 17:00 is due Tuesday 11:00. Proposed: show overdue pending requests to operators for manual follow-up; expiry of the response deadline does not approve or decline them.

Email reports recorded staff decisions. Failure preserves the decision and pickup window; members can retrieve authoritative on-screen status. Operators see the failed notification and can retry delivery of that decision without deciding again.

## Planned acceptance checks

All checks below are planned, with no observed implementation outcome.

| Given / when | Observable result |
|---|---|
| Invited verified member submits a fresh-depot tool request | One stored request, exact awaiting-approval wording, deadline, and no promised slot or held stock. |
| Uninvited/unverified account submits; member opens another member's ID; wrong-depot operator decides | Each unauthorized action is denied without exposing protected request content or changing state. |
| Import age exceeds 24 hours at submission; import fails or refresh succeeds | Stale submission blocked; existing status readable; failure retains old timestamp; successful refresh preserves requests. Exactly 24 hours is not stale. |
| Submission saves but response times out; member retries | Same logical request and identifier recovered, with no duplicate. Failed save never displays success. |
| Staff check ledger and approve or decline | Correct persisted state and actor; approval requires a window and instructions; decline shows explanation. Competing requests cannot promise the same unit. |
| Owner withdraws while staff approve | One winning state; loser sees it; losing approval leaves no ledger allocation. |
| Decision email fails, then operator retries | Decision stays visible and unchanged; failed delivery is identifiable and retryable. |
| Request arrives Saturday 17:00 with fresh inventory | Deadline is Tuesday 11:00; no automatic decision when overdue. |
| Approved member seeks cancellation; pickup is missed; tool is collected/returned | Phone route shown; staff cancellation recorded; missed pickup flagged without automatic cancellation; collection/return recorded. |

## Evidence, learning, and remaining decisions

Historical record, preserved from [decisions and observations](../decisions-and-observations.md):

- **2026-08-14:** Seven of ten existing members expressed interest in confirmed slots during a staff-assisted paper exercise with manual availability checks. No unattended reservation, signup, or payment was tested.
- **2026-08-20:** Planning selected instant confirmation conditional on untested partner API and refundable-deposit integrations. Superseded by the 2026-09-10 decision.
- **2026-09-04:** Six observed West phone requests yielded four approvals and two declines because tools were out. Historical phone-service evidence, not app validation or measured improvement.

Review after two staffed weeks. Proposed measures: approvals/declines within deadline divided by requests whose deadlines elapsed; completed pickups divided by approvals with elapsed windows; notification failures; and observed request-versus-confirmation misunderstandings with observation counts. Report depot, period, denominators, and unresolved requests. No baseline, adoption target, conversion uplift, revenue result, or 20% pickup improvement is validated.

Before pilot operation, the pilot lead must supply the exact tool list, depot phone/location/instructions, and start date; operators must confirm the proposed ledger and follow-up procedure. These are unresolved operational details. Expansion requires the two-week review; future deposit amount and noncollection policy remain board/Product decisions.
