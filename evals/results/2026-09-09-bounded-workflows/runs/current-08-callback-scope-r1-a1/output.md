**Recommend a callback queue pilot for the two small desks**, with visible ownership, safe claiming, and a report using existing server events. This is a proposed scope decision, not an approved requirement. The strongest alternative is a manual handoff checklist using their existing Friday reviews: cheaper and useful for learning, but it would not deliver the requested shipped improvement or test whether a persistent queue helps.

The trade-off is deliberate: test ownership and handoff visibility for willing participants while deferring automation and multi-branch complexity. Reopen scope if the complete queue cannot fit capacity, desk participation falls through, or ownership conflicts appear within these desks.

**First customer group and rationale**

Enroll only the two consenting desks with 3–5 dispatchers each, one time zone, and one shared phone number. Customer success should confirm named participants and the two-week pilot dates before enabling access.

The supplied synthetic evidence, recorded September 9, covers four desks and is a convenience sample. Of 62 callbacks more than 12 hours late, 31 were attributed to handoff loss and 17 to missing ownership. Five of eight interviewed dispatchers wanted outstanding callbacks visible at shift start. These findings support testing a queue; they do not prove it will prevent delays. The reason counts are not broken down by desk, and the small desks already have 91% owner coverage, so their improvement opportunity remains uncertain.

Defer the large multi-branch desks and prospect. Temporary dual ownership, branch time zones, and unstudied transfer behavior introduce dependencies outside the estimates. Interest in a demo is not a trial commitment.

**Retained pilot journey**

A dispatcher starting a shift can:

- Open outstanding promised callbacks within existing branch permissions, showing promised time, current owner or “unassigned,” and available contact details. Order by promised time so overdue work is apparent.
- Claim an unassigned callback. Show ownership before claiming; concurrent claims must leave one owner and tell the unsuccessful claimant the current state. Do not silently replace an owner or move a callback between branches.
- Use the existing callback and completion process. Completed callbacks leave the outstanding queue; reopening the queue reflects saved ownership and completion.
- Identify callbacks missing usable contact details and keep them visible as unresolved. Use existing manual correction or escalation procedures; never imply that claiming an item resolved its contact problem.

For an owned callback whose dispatcher is unavailable, retain the existing authorized handoff procedure. Confirm that procedure and contact correction are usable before release; if they are absent, price the minimum recovery behavior within the remaining capacity before committing to the slice.

Customer success controls named-desk enrollment and can stop enrollment or disable the pilot through the existing feature flag without deleting callback records.

Acceptance checks should cover branch isolation, visible ownership, competing claims, persistence across shifts, completion removal, missing-contact handling, and disablement with records preserved. These checks are planned; no product code or tests were executed.

**Capacity and delivery boundary**

| Work | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue, owner, claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Total | 3.5 | 3 | 1.5 |
| Remaining capacity | 2.5 | 1 | 0.5 |

The envelope is 6 backend, 4 frontend, and 2 QA days, including integration and fixes, through September 30. Preserve the remainder for those needs and confirmation of the connected journey above. Estimates are provisional: validate that concurrency, permissions, recovery, and flag controls are included. QA has only half a day remaining.

No additional proposed feature fits alongside this slice across all disciplines. A two-week pilot completed by September 30 would need to start by September 16; staffing and elapsed delivery time are unvalidated. Ship within the release window if feasible, but schedule the expansion review after two full pilot weeks if activation is later.

**Deferred and excluded**

- **SMS:** provider approval has no date; only 116/240 reviewed records have auditable consent. Reconsider after approval, consent-safe coverage, and evidence of residual reminder need.
- **Routing/escalation builder:** exceeds the frontend envelope alongside the queue and depends on unresolved multi-branch ownership.
- **Manager email:** exceeds the combined frontend estimate; use the pilot report during existing Friday reviews.
- Exclude pricing, payments, contact enrichment, branch-ownership changes, and marketing work. Campaign materials provide no evidence about callback outcomes.

**Learning and expansion decision**

Use existing events to report each desk’s callback volume, completions, ownership changes, and proportion completed more than 12 hours after promise. Report unresolved overdue callbacks separately; do not count recent pending callbacks as successes. Establish comparable desk-level baseline figures from their handoff notes where possible.

At Friday reviews, collect specific saved or missed handoffs, ownership confusion, contact blockers, and whether dispatchers actually use the queue. Events cannot establish who saw it.

Recommend expansion only after the managing director’s explicit review: reliable permission and ownership behavior, manageable support burden, continued desk participation, and directional improvement supported by concrete handoff examples. Small samples cannot establish causality. A numerical success threshold remains unresolved because desk-level baseline volumes and acceptable improvement are missing; agree it before interpreting results. Any multi-branch expansion additionally requires ownership and time-zone discovery plus fresh estimates.