**Recommend a branch-scoped callback queue for the two small desks**, with visible ownership, a claim action, and a measurement report. The strongest alternative is a manual handoff checklist using their existing Friday reviews: it costs less engineering effort, but does not provide a persistent shared view across shifts. Choose the queue to test that specific benefit. Reopen the choice if essential ownership or recovery behavior cannot fit capacity; use the manual pilot rather than ship an unreliable queue.

This is a proposed scope decision, not an approved requirement or delivery guarantee.

**First customer group and intended outcome**

Enroll only the two named, consenting desks with 3–5 dispatchers, one time zone, and one shared number. They have offered a two-week pilot and can supply handoff notes. Their simpler ownership model avoids an unstudied multi-branch redesign.

The intended outcome is straightforward: a dispatcher starting a shift can find outstanding callback promises, identify responsibility, claim an unowned callback, and record completion through the existing workflow.

The supplied synthetic evidence supports testing this hypothesis, not claiming effectiveness: in the four-desk review, shift handoffs and missing owners were prominent reasons for lateness; five interviewed dispatchers wanted an outstanding-callback view. Results were not reported separately for the small desks. Their already high owner-field coverage also means visibility across shifts may matter more than claiming alone. [Sources: `input/evidence.md`; `input/stakeholder-notes.md`.]

**Retained pilot scope**

| Retain | Required behavior and acceptance outcome |
|---|---|
| Outstanding-callback queue | Within existing branch permissions, show promised time, owner or “unassigned,” and available contact details. Make overdue items distinguishable without relying only on color. A shift starter can identify pending work. |
| Owner and claim | Display ownership before claiming. Claim an unassigned item as the acting dispatcher; do not silently replace an owner or move a callback between branches. Concurrent claims must resolve to one owner, with clear feedback to the unsuccessful claimant. |
| Durable handoff and completion | Ownership survives refresh and shift change. Reuse existing completion recording; completed work leaves the outstanding view. A failed update must not appear successful and must allow retry without losing the record. |
| Missing-contact exception | Keep the callback visible and identify missing details. The dispatcher uses the desk’s existing authorized correction process; missing data does not count as completion. |
| Controlled enrollment and exit | Customer success maintains the named enrollment list and can stop enrollment or disable the pilot through the existing flag. Disabling preserves callback records. |
| Measurement report | Use existing server events for completion and ownership changes, alongside desk handoff notes. No new frontend analytics or infrastructure. |

Engineering must confirm these necessary behaviors are covered by the queue estimate. They are acceptance boundaries, not independently estimated additions.

**Capacity and release boundary**

| Allocation | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue, owner, claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Selected total | 3.5 | 3 | 1.5 |
| Remaining within capacity | 2.5 | 1 | 0.5 |

Method: add the two selected estimates, then subtract from the supplied capacity of 6 backend, 4 frontend, and 2 QA days. Arithmetic is **not tool-verified**, because the request prohibits running code. These are source estimates, not validated commitments. Preserve the remaining capacity for integration, fixes, and uncovered essentials; QA is particularly tight. [Source: `input/delivery-constraints.md`.]

Ship by **2026-09-30**. A full two-week observation period may extend beyond release; pilot start timing is unresolved. Do not compress observation to imply validated results by month-end.

**Deferred and excluded**

- **SMS reminders:** provider approval has no committed date, and consent is stored for only some records. No consent-free fallback is authorized. Reconsider only after approval, consent handling, and evidence that reminders address the remaining problem.
- **Routing/escalation builder and large desks:** defer pending ownership and time-zone research and separately available capacity. Sales interest is not trial commitment.
- **Weekly manager email:** use the existing Friday review and pilot report. A new email feature adds effort without being necessary for the dispatcher journey.
- **Pricing, payment, enrichment, and branch ownership changes:** excluded by authorization.
- **Homepage, video, and trade-show work:** remain outside this slice. Agency resources do not increase engineering capacity, and campaign proposals provide no pilot evidence.

**Learning and expansion decision**

Before activation, establish a comparable baseline for each participating desk. Across two pilot weeks, report:

- Callbacks completed more than 12 hours late, plus still-open callbacks already beyond that threshold, divided by eligible promised callbacks whose threshold has elapsed.
- Ownership changes and unresolved callbacks, interpreted with handoff notes.
- At Friday reviews, staff-attributed handoff, ownership, and missing-contact failures.

Check timestamp completeness before interpreting results. Events cannot establish who saw the queue or prove causation.

Recommend expansion only after the managing director’s explicit review: both desks can complete the journey, no unresolved permission or ownership defects remain, lateness improves against their own baseline, and notes support fewer handoff failures without added burden. Low volume or conflicting results mean extend observation without expanding enrollment. Persistent missing-contact delays warrant investigating that bottleneck next.

No product code or tests were executed; acceptance checks and pilot outcomes remain unobserved.