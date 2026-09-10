Recommend a **shared outstanding-callback queue with visible ownership and claim**, plus measurement, for the **two small desks that offered a two-week pilot**. The strongest alternative is a structured manual shift-handoff checklist using their existing Friday reviews: it avoids engineering work and could test ownership discipline, but cannot establish whether a persistent queue improves handoffs. Choose the queue to deliver a usable product slice by September 30; reopen that choice if safe ownership handling exceeds capacity or dispatchers cannot use it reliably.

This is a recommended scope handoff, not an approved requirement set or validated business case. All supplied customer evidence is synthetic.

**Audience and evidence**

Enroll only those two named, consenting desks: each has 3–5 dispatchers, one time zone, and one shared phone number. Customer success coordinates participation; existing branch permissions remain binding.

The September 9 evidence supports testing visibility and ownership: among 62 late callbacks across four desks, 31 were attributed to shift handoff and 17 to missing ownership; five of eight interviewees wanted outstanding callbacks visible at shift start. However, these totals are not specific to the small desks, whose owner fields were already populated for 91% of callbacks. A populated field may still fail to establish responsibility, but that is a hypothesis to test. The convenience sample and interviews do not prove effectiveness or demand.

Defer large multi-branch desks. Their temporary dual ownership and differing time zones introduce unstudied semantics. The prospect’s interest in a demo provides no trial or purchase commitment.  
Sources: `input/evidence.md`, `input/stakeholder-notes.md`.

**Retained journey and acceptance boundaries**

At shift start, an authorized dispatcher opens outstanding callbacks for their permitted branch, sees responsibility, takes an unowned callback, performs the callback through existing working practices, and records completion.

- Reuse existing table/status components. Show promised time, overdue status, owner or “Unassigned,” and available contact details. Prioritize overdue items.
- Claim applies to unassigned callbacks. Show the current owner before action; never silently replace an owner or move a callback between branches.
- Concurrent claims must produce one saved owner. A losing claimant sees the current owner; failed saves remain visibly unsuccessful and can be retried.
- Retain existing completion and authorized correction/handoff paths. Confirm these support ordinary ownership mistakes and shift changes; otherwise include their minimum safe recovery within the estimate before committing delivery.
- Missing contact information stays visible and outstanding. Staff resolve it through existing procedures; no enrichment or invented contact data.
- Include clear empty, loading, and retryable failure states. An error must not appear as an empty queue.
- Customer success can stop enrollment or disable the pilot through the existing flag without deleting callback records.

Planned acceptance checks cover the complete journey across a shift change, concurrent claims, failed saves, missing contacts, branch access, and disabling/re-enabling with records preserved. These checks have **not been executed**.

**Capacity and alternatives**

Engineer-days below include the separate measurement report using existing events.

| Option | Backend | Frontend | QA | Decision |
|---|---:|---:|---:|---|
| Available | 6 | 4 | 2 | Hard ceiling |
| Queue + measurement | 3.5 | 3 | 1.5 | Retain |
| Remaining capacity | 2.5 | 1 | 0.5 | Hold for uncertainty |
| Queue + measurement + weekly email | 5.5 | 5 | 2.5 | Exceeds frontend and QA |
| SMS + measurement | 5.5 | 2 | 2.5 | Exceeds QA; provider blocked |
| Routing + measurement | 4.5 | 4 | 1.5 | Fits estimates, weaker first-pilot fit |

Calculation check: componentwise addition of feature and measurement estimates, then subtraction from capacity, returned the values above through a calculation tool. Inputs: `input/delivery-constraints.md`. No product code or tests were run.

These are estimates, not delivery commitments. Confirm that permission, claim-conflict, recovery, and flag behavior fit the queue estimate; do not treat backend headroom as interchangeable with scarce QA time.

Defer SMS until provider approval has a date, stored consent can be enforced, and capacity exists. Only 116 of 240 reviewed records had auditable consent; unauthorized texting is not a fallback. Defer routing until multi-branch ownership is understood. Handle manager reporting through existing Friday reviews and the pilot report; reconsider email if repeated manual reporting becomes burdensome. No new vendors, warehouse, pricing, payments, or ownership redesign.

**Learning and expansion decision**

Hypothesis: persistent visibility and clear responsibility reduce handoff-related delay at these small desks.

Before activation, customer success assembles each participating desk’s preceding 14-day baseline. During the two-week pilot:

- Report callbacks completed more than 12 hours after promise **or still incomplete at that point**, divided by all promised callbacks whose 12-hour deadline has elapsed. Report counts and rates separately by desk; allow late-window records to mature.
- Use existing completion and ownership-change events, plus handoff notes, to distinguish ownership problems, missing contacts, and other causes.
- At Friday reviews, record whether dispatchers used the queue at handoff, found unclear responsibility, or reverted to manual work. Existing events cannot prove someone viewed the queue.

Recommend limited expansion to similar desks only after both desks show a directional improvement, staff report useful handoffs, and no unresolved access, ownership, or data-loss defects remain. This is a proposed decision rule, not statistical proof. Mixed results or too few eligible callbacks are inconclusive; investigate before expanding. Disable for consequential ownership/access failures.

Unresolved: baseline performance for these two desks and the minimum worthwhile improvement are unknown. Set that threshold before seeing pilot outcomes. Also confirm activation and support dates: September 30 is the shipping deadline, not evidence that a full two-week observation can finish by then. The managing director’s explicit review remains required before further enrollment.

Homepage headlines and trade-show materials do not determine this scope. Avoid promising “Every promise kept”; this pilot cannot guarantee it.