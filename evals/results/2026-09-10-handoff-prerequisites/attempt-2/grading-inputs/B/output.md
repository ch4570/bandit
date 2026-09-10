**Recommend an owner-and-claim callback queue for the two small desks, with a measurement report and controlled enrollment.** The strongest alternative is a manual handoff checklist using their existing Friday reviews: it costs less engineering effort but cannot establish whether persistent, visible ownership helps across shifts. Ship the queue provisionally; fall back to the checklist if essential ownership or completion behavior cannot fit.

SMS is the strongest automation alternative, but provider approval has no date and stored consent is incomplete. Reopen automation after those dependencies are resolved and the pilot identifies a remaining problem it could address.

**First customer group and intended outcome**

Enroll only the two consenting desks with 3–5 dispatchers, one time zone, and one shared phone number. Their simpler ownership model avoids the unstudied multi-branch case. Use existing branch permissions and named-desk enrollment.

The target outcome is that an incoming dispatcher can find outstanding promises, identify responsibility, and claim unowned work without losing it at handoff.

The September 9 evidence supports this hypothesis, not a proven effect: across four sampled desks, 31 late callbacks were attributed to handoff loss and 17 to missing ownership; five of eight interviewees wanted outstanding callbacks visible at shift start. These findings are not specific estimates for the two pilot desks. Their 91% populated owner field also means the queue must help with visibility of already-owned work.

**Retained scope and acceptance boundary**

| Retain | Observable acceptance outcome |
|---|---|
| Outstanding-callback queue using existing table/status components | A permitted dispatcher sees outstanding callbacks within existing branch access, with promised time and visible owner or “Unassigned.” Overdue status follows the desk’s time zone. |
| Explicit claim action | A dispatcher can claim an unassigned callback. Concurrent claims produce one owner; the unsuccessful claimant sees the current owner. No silent takeover or cross-branch movement occurs. |
| Connection to existing completion and correction paths | Dispatchers can reach the existing callback record, perform the callback, and record completion. Completed work leaves the outstanding queue. Existing authorized ownership corrections remain usable. |
| Missing-data and failure recovery | Missing contact details are visible; the item remains outstanding and can reach the existing correction process. Failed claims or saves never appear successful; refresh shows persisted state. An empty queue is distinguishable from a loading failure. |
| Controlled pilot and report | Customer success can stop enrollment or disable the feature through the existing flag without deleting callback records. Reporting uses existing server events and the reviewed call records. |

Completion, correction, and ownership-change paths are **dependencies to confirm**, not established implementation facts in the supplied notes. If they are missing, estimate the minimum repair before committing the slice; a queue that cannot reliably close or recover work is not a useful release.

**Capacity and delivery**

Capacity includes integration and fixes.

| Allocation | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue, owner and claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Combined estimate | 3.5 | 3 | 1.5 |
| Remaining capacity | 2.5 | 1 | 0.5 |

Method: add the two estimates and subtract from the available 6/4/2 days. **Arithmetic is not tool-verified because the task prohibits running code.** These are estimates, not a delivery commitment. Reserve the remainder for integration, essential recovery, and fixes; the detailed acceptance boundary above has not been separately estimated. QA and frontend headroom are particularly limited.

Ship by September 30 if the complete path fits. Do not assume the offered two-week pilot must finish by that date. Customer success must settle start/end dates and support coverage; the notes do not establish them. If a completed pilot is also required by September 30, feasibility remains unresolved.

**Deferred and excluded**

- **SMS reminders:** defer provider integration and consent handling. Only 116 of 240 reviewed records had auditable consent; missing consent does not permit texting.
- **Routing/escalation builder and multi-branch enrollment:** defer until ownership and time-zone rules are studied. No branch-ownership changes are authorized.
- **Weekly manager email:** defer; existing Friday reviews and the report provide a manual alternative. It adds engineering effort without completing the core journey.
- **Pricing, payments and contact enrichment:** excluded by the delivery constraints.
- **Homepage, video and booth work:** separate agency scope; neither campaign preference nor prospect interest demonstrates pilot demand. The pilot cannot substantiate “Every promise kept.”

**Learning and expansion decision**

Before activation, reconstruct a baseline for the two pilot desks from the manual review if desk-level records are available; otherwise label the comparison unavailable. Do not substitute the four-desk aggregate.

For the two-week pilot, report per desk:

- Callbacks completed more than 12 hours late **or still incomplete at that threshold**, divided by eligible promised callbacks.
- Outstanding unassigned callbacks at handoff, using ownership events where reconstructable and handoff notes otherwise.
- Failure causes from Friday reviews, including missing contact details and ownership confusion.

Allow each promise its full 12-hour observation window. Completion events do not prove queue usage, reminder viewing, or causation.

At the explicit expansion review, recommend adding only similar desks if both pilot desks find the queue useful, ownership remains reliable, and late-callback evidence improves without hidden unresolved work. Mixed results, low volume, or a missing baseline mean extend or revise the pilot. Permission leakage, lost records, or conflicting ownership mean disable and repair. Numeric success thresholds remain unset because pilot-desk baseline and volume are unknown; agree them before activation. No automatic expansion or business-validation claim follows from shipping.