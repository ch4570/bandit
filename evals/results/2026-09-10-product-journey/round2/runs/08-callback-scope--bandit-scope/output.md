**Recommend a callback queue with visible ownership and a claim action for the two small desks that offered a pilot.** Include a measurement report using existing server events. The strongest alternative is a manual shift-handoff checklist: it could test the ownership hypothesis sooner, but would not provide a persistent shared view or meet the request for a shipped improvement.

This is a recommendation, not an approved requirement. Reopen it if essential recovery behavior exceeds capacity, either desk declines participation, or ownership conflicts appear within these desks.

**First customer group and outcome**

Enroll only the two consenting desks with 3–5 dispatchers each, one time zone, and one shared number. Customer success should record the named desks and participants. Exclude multi-branch desks initially: temporary dual ownership and differing time zones require investigation and work outside the estimates.

The intended outcome is that a dispatcher starting a shift can find outstanding promises, identify responsibility, and complete or hand off a callback without losing it.

The supplied synthetic evidence supports testing this outcome, not claiming it works. Of 62 callbacks more than 12 hours late, 31 were attributed to handoff loss and 17 to missing ownership. Five of eight interviewed dispatchers requested an outstanding-callback view. These are attributed reasons and preferences from a convenience sample; they do not establish preventable delays or market demand. [Sources: `input/evidence.md`; `input/stakeholder-notes.md`.]

**Retained pilot scope**

| Retain | Boundary and acceptance outcome |
|---|---|
| Outstanding-callback queue | Use existing callback records, promised times, owners and completion state. Show incomplete callbacks within existing branch permissions, ordered by promised time. Distinguish overdue, unassigned and missing-contact cases. |
| Visible owner and claim | Show the current owner before any action. A dispatcher may claim an unassigned callback. Simultaneous claims must resolve to one owner; the unsuccessful claimant sees the current owner. No silent takeover or branch movement. |
| Connected completion and handoff | Reach the existing callback detail and completion workflow from the queue. Completion removes the item from outstanding work after refresh. Keep an existing owner visible across shifts; reassignment uses the existing authorized process. |
| Recovery | Missing contact details leave an item outstanding and visibly blocked; staff obtain details through their existing process. Save/load failures must not look like success. Retry or refresh must preserve confirmed state. No enrichment is added. |
| Pilot control and measurement | Restrict access to named enrolled desks. Customer success can stop enrollment or disable the pilot through the existing flag without deleting records. Produce the event-based report. |

These are required outcomes within the proposed slice, not separately validated estimates. Confirm that existing detail, correction and reassignment paths support them before committing delivery; otherwise narrow enrollment or use the manual fallback rather than omit essential recovery.

**Capacity and release boundary**

Using the supplied additive estimates:

| Allocation | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue, owner and claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Total | **3.5** | **3** | **1.5** |
| Remaining from 6 / 4 / 2 | **2.5** | **1** | **0.5** |

Reserve the remainder for integration, recovery and fixes; it is not capacity for another proposed feature. Frontend and QA are the tight constraints. Engineering and QA should check essential behavior against these estimates first. Release by **2026-09-30** remains a target, not a verified commitment. Run the offered two-week pilot after readiness; the evidence does not establish that both release and the full observation period fit before September 30. [Source: `input/delivery-constraints.md`.]

**Deferred and excluded**

- **SMS reminders:** defer. Provider approval has no committed date, only 116 of 240 records have auditable consent, and queue plus SMS exceeds every capacity limit. Never text without stored consent. Reconsider only after approval, consent eligibility and incremental benefit are established.
- **Routing/escalation rules:** defer. They exceed combined capacity and introduce unresolved multi-branch ownership behavior.
- **Weekly manager email:** defer. Queue plus email exceeds frontend capacity even before reporting. Use the measurement report in the desks’ existing Friday review.
- Exclude payment, pricing changes, enrichment, branch-ownership changes and new providers. Homepage, video and trade-show work supplies no evidence for this pilot and no transferable engineering capacity.

**Learning and expansion decision**

Hypothesis: shared visibility and explicit ownership reduce lost callback promises.

Before launch, establish a comparable baseline for these same two desks from available records and handoff notes; do not use the pooled four-desk result as their baseline. Over the two-week pilot, measure:

- Callbacks completed over 12 hours after promise, plus still-incomplete callbacks beyond that threshold, divided by all promises with sufficient follow-up.
- Unassigned callbacks at shift handoff, using ownership events where reconstructable and staff notes otherwise.
- Lost handoffs, blocked contact details, ownership conflicts and added dispatcher effort in Friday reviews.

Keep desk-level counts and denominators alongside rates. Existing events cannot prove someone viewed a reminder or used the queue; improvement cannot establish causality.

After two weeks, customer success, operations and engineering should explicitly review expansion. Recommend a small next cohort of similarly simple desks only if both desks show a favorable late-callback trend, staff describe useful handoffs, essential recovery works, and no permission or ownership defects remain. Sparse or incomparable data means extend observation, not declare success. Stop or disable for consequential access or ownership failures.

An expansion-size commitment remains unresolved: support capacity is unspecified. Multi-branch expansion and willingness to pay also remain unvalidated. All acceptance checks and pilot measurements above are planned; none has been executed.