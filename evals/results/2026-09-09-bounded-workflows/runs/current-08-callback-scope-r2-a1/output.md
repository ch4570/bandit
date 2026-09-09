**Recommend a shared callback queue plus a pilot measurement report for the two small desks**, with enrollment limited to named, consenting participants. The strongest alternative is a manual shift-handoff checklist using their existing Friday reviews: it costs less engineering effort but does not provide persistent, shared ownership visibility. Choose the queue to test that benefit; return to the manual approach if essential recovery behaviors exceed capacity.

This is a proposed scope decision, not an approved requirement or evidence of business validation. Reopen it if ownership cannot be handled safely, delivery estimates grow beyond capacity, or the pilot shows no useful improvement.

**First customers and rationale**

Start with the two desks that each have 3–5 dispatchers, one time zone, one shared number, and an offered two-week pilot. Their 91% owner-field coverage makes ownership gaps manageable without assuming every callback is assigned.

The supplied synthetic 14-day review found 62 of 240 promised callbacks more than 12 hours late. Of those, 31 were attributed to shift handoff and 17 to absent ownership. Five of eight interviewees requested an outstanding-callback view. These findings support testing visibility and ownership, but do not establish that a queue prevents delays. The figures cover all four desks; they are not a baseline specifically for the two pilot desks. [input/evidence.md; input/stakeholder-notes.md]

Exclude the multi-branch desks initially: temporary dual ownership and different time zones require unresolved ownership work. The large prospect’s interest in a demo is weaker recruitment evidence than an offered trial.

**Retained pilot journey**

| Situation | Proposed behavior and acceptance outcome |
| --- | --- |
| Dispatcher starts a shift | Show outstanding callbacks within existing branch permissions, with promised time, current owner or “unassigned,” and available contact details. Overdue and unassigned items must be identifiable. Completing a callback through the existing workflow removes it from the outstanding view; refreshing preserves server state. |
| Dispatcher claims an unassigned callback | Show ownership before claiming. A successful claim persists and becomes visible to colleagues. Concurrent claims must produce one owner; the unsuccessful claimant sees the current owner. A failed save must not appear successful. |
| Callback already has an owner | Preserve that assignment. No automatic takeover, cross-branch movement, routing, or new reassignment workflow. Customer success and each desk must identify the existing authorized handoff/correction procedure before launch; inability to resolve stale ownership reopens scope. |
| Contact details are missing | Keep the callback visible with a missing-contact indication. Staff use their existing process to obtain/correct details; no enrichment or automatic closure. This remains a known limitation on achievable improvement. |
| Pilot must stop | Customer success can stop enrollment and disable the pilot using the existing feature flag without deleting callback records. |

These are required outcomes to confirm against the queue estimate, not separately estimated commitments. Reuse existing table/status components and completion behavior. [input/delivery-constraints.md; input/stakeholder-notes.md]

**Capacity and delivery boundary**

Queue plus report totals **3.5 backend, 3 frontend, and 1.5 QA days**, against **6/4/2 available**. Remaining capacity is **2.5 backend, 1 frontend, and 0.5 QA days** for uncovered integration, recovery, and fixes; it is not interchangeable across disciplines. QA is particularly constrained.

Ship by **September 30, 2026**, conditional on confirming the essential behaviors above fit. Do not promise a completed two-week evaluation by that date: that requires pilot activation by September 16. Otherwise, ship within the release window and complete evaluation afterward. Readiness for a September 16 start is unresolved. [input/delivery-constraints.md]

Defer:

- **SMS reminders:** queue plus SMS already exceeds every capacity limit; provider approval is undated and only 116/240 records have stored consent. Revisit after consent coverage, approval, and incremental benefit are established.
- **Routing/escalation:** exceeds frontend capacity alongside the queue and depends on unresolved multi-branch ownership. Revisit after studying that workflow.
- **Weekly manager email:** queue plus email needs five frontend days before measurement. Use the report in existing Friday reviews; revisit if recurring managerial action warrants automation.

Homepage copy, video, and trade-show work do not inform this pilot’s scope or supply engineering capacity. [input/homepage-refresh.md]

**Learning and expansion decision**

Use the additional report effort to compare each pilot desk’s preceding 14 days with its two-week pilot: eligible promised callbacks, completion delay, callbacks over 12 hours late, and ownership changes. Count still-open callbacks once they pass that threshold; allow newer promises to mature before comparison. Reconcile records and use handoff notes/Friday reviews to identify missed items, stale owners, missing contacts, and whether staff actually used the queue. Server events cannot establish reminder viewing.

The managing director’s explicit review precedes further enrollment. Recommend expansion first to similarly simple desks only if both desks show a directionally lower late-callback rate, staff report useful handoffs and want to continue, and no unresolved access, ownership, or record-loss defects remain. Mixed or sparse results justify extending observation, not claiming success. This uncontrolled convenience sample cannot establish causality, multi-branch readiness, or willingness to pay.

All acceptance checks and pilot measurements are **planned; outcomes remain unobserved**. No product code or tests were executed.