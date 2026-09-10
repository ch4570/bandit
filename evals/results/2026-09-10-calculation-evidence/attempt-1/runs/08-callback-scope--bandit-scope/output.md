Recommend a **branch-local outstanding-callback queue with visible ownership and claim, plus a pilot measurement report**, for the two small desks that offered to participate. Ship by September 30, 2026, then observe two weeks of use. The strongest alternative is a structured manual shift-handoff list: quicker to trial, but it does not test whether persistent shared visibility improves handoffs. Choose the queue provisionally; revert to the manual approach if safe ownership handling cannot fit the release capacity.

All evidence below comes from the supplied synthetic artifacts. It supports a pilot decision, not claims about real customers or validated demand.

**First customer group and rationale**

Enroll only the two willing desks with 3–5 dispatchers, one time zone and one shared number. Customer success names participating desks and coordinates their existing Friday reviews.

The September 9 evidence records 31 late callbacks attributed to shift handoff and 17 to missing ownership; five of eight interviewees wanted outstanding callbacks visible at shift start. This makes visibility and ownership a reasonable hypothesis. However, these small desks already populate ownership for 91% of callbacks: the pilot must test handoff continuity, not assume that adding owners solves the problem.

Defer the large multi-branch desks. Temporary dual ownership and differing time zones introduce unresolved rules outside the estimates. A prospect’s interest in an automation demo is weaker evidence of readiness than the small desks’ offered pilot.

**Retained journey and acceptance boundary**

A dispatcher starts a shift, sees outstanding callbacks within existing branch permissions, identifies what is due, checks ownership, claims eligible unowned work, contacts the customer and records completion through the existing workflow.

Retain:

- A queue using existing table/status components, showing promised time, current owner and available contact details; clearly distinguish overdue and unowned items.
- Owner visibility before claim. A successful claim persists and becomes visible to colleagues. Concurrent claims must not silently overwrite ownership; the unsuccessful claimant sees the current owner and can refresh.
- Existing completion handling: completed callbacks leave the outstanding view. Failed saves remain visibly unresolved and offer retry.
- Empty and unavailable states that distinguish “no outstanding callbacks” from failed loading.
- Missing-contact visibility and a manual handoff to the desk’s existing process for finding details. Such callbacks remain outstanding; no enrichment is added.
- Existing branch access controls, named pilot enrollment and customer-success control to stop enrollment or disable the feature. Disabling retains callback records.

Already-owned callbacks remain with their owner. Shift staff coordinate through their current handoff process; no automatic reassignment, cross-branch transfer or new routing policy is included.

Engineering must confirm that existing completion and ownership-correction workflows support this journey. If they do not, re-estimate the affected scope before treating delivery as feasible.

**Capacity and alternatives**

Estimates from `input/delivery-constraints.md`, in engineer-days:

| Allocation | Backend | Frontend | QA |
|---|---:|---:|---:|
| Available, including integration/fixes | 6 | 4 | 2 |
| Queue and claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Selected total | 3.5 | 3 | 1.5 |
| Remaining headroom | 2.5 | 1 | 0.5 |

Arithmetic check executed using calculator-style JavaScript: queue + report returned `[3.5,3,1.5]`; capacity − total returned `[2.5,1,0.5]`, ordered backend/frontend/QA. No product code or tests were executed. These are estimates, not a delivery commitment; preserve headroom for integration and fixes.

Adding any other proposal exceeds at least one role’s capacity:

| Deferred proposal | Total with selected scope: backend/frontend/QA | Reason and reopening condition |
|---|---|---|
| Weekly manager email | 5.5 / 5 / 2.5 | Exceeds frontend and QA. Use existing Friday reviews; reconsider if managers repeatedly need distribution beyond them. |
| Automatic SMS | 8.5 / 5 / 3.5 | Exceeds all roles; provider approval has no date, and only 116/240 records have auditable consent. Reconsider after approval, consent-safe eligibility and evidence that messaging addresses remaining delays. |
| Self-service routing/escalation | 7.5 / 7 / 2.5 | Exceeds all roles and requires unresolved ownership rules/new UI. Reconsider after studying multi-branch handoffs. |

These additive totals were also returned by the arithmetic check. Deferred work has no assigned second team or implied delivery date.

**Learning and expansion decision**

Hypothesis: a persistent queue with visible ownership reduces callbacks completed more than 12 hours after the promised time, particularly handoff-related delays.

Use existing server events and the funded report to compare each pilot desk’s two-week baseline with its two-week pilot:

- Primary measure: callbacks still incomplete 12 hours after promised time ÷ all promised callbacks whose 12-hour observation window has elapsed. Include unresolved cases, avoiding a completed-only denominator.
- Report raw counts and rates separately by desk, alongside ownership changes.
- Use Friday reviews and shift-handoff notes to classify remaining delays, record confusing claims and understand whether dispatchers actually use the queue. Events cannot establish who saw a reminder or queue.

The pooled 62 late cases among 240 callbacks are context, not the small desks’ baseline. Customer success must establish desk-specific comparable counts.

Recommend expansion only after the managing director’s required review: both desks show a consistent directional improvement, notes support better handoffs, and there are no unresolved access, ownership-loss or record-loss defects. Expand initially to similarly simple desks.

Mixed results, sparse eligible callbacks or changed workloads are **inconclusive**: extend observation or revise the slice. Disable for consequential permission or ownership failures.

A defensible numerical improvement threshold remains unresolved; establish it with desk-specific baseline volumes before enrollment. Willingness to pay also remains unknown. No pricing change is proposed. Homepage copy, video and trade-show materials do not determine this scope; “Every promise kept” exceeds what this pilot can substantiate.

Acceptance checks and pilot outcomes are planned, not verified.