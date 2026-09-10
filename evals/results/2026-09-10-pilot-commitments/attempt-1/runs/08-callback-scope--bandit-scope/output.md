Recommend a **named-desk pilot of the callback queue with visible ownership and claim**, plus measurement from existing server events. Start with the two small desks that offered to participate. The strongest alternative is a manual shared callback list reviewed at shift changes: quicker to try, but weaker at testing whether persistent, integrated ownership helps. Reopen the build choice if safe claiming or the complete callback journey exceeds capacity.

This is a scope recommendation, not an approved requirement set. All customer evidence supplied is synthetic; it supports this exercise’s decisions, not claims about real customers.

**Why this group and problem**

The two desks each have 3–5 dispatchers, one time zone, one shared number, and owner fields populated for 91% of callbacks. They offer an accessible pilot with fewer ownership ambiguities. Larger desks have temporary dual owners, multiple branch time zones, and no ownership study; the large prospect offered demo interest, not trial commitment. [Sources: input/evidence.md; input/stakeholder-notes.md]

Across the four-desk, 14-day review, 31 late callbacks were attributed to shift handoff and 17 to missing owners. Five of eight interviewees wanted outstanding callbacks visible at shift start. These observations motivate the queue hypothesis; they do not establish prevention or small-desk-specific benefit. Missing contact details caused another 14 late cases and remain a limitation.

**Retained pilot journey**

A dispatcher starts a shift, sees outstanding callbacks within existing branch permissions, identifies responsibility, claims an unowned item, makes the callback through the existing workflow, and records completion.

| Retain | Observable acceptance outcome |
|---|---|
| Queue using existing table/status components | Outstanding records show promised time, owner or “unassigned,” and missing contact details; completed records leave the outstanding view after refresh. |
| Visible owner before claiming | Claiming an unassigned item persists one owner. Concurrent claims cannot silently overwrite ownership; the losing dispatcher sees the current owner and can refresh. |
| Safe handoff and correction | Already-owned work identifies whom to coordinate with. Use the existing authorized assignment process for corrections; no automatic reassignment or cross-branch movement. Confirm that process exists before enrollment. |
| Ordinary recovery | Empty queue is distinguishable from loading/error. Failed claims show failure and permit retry without claiming success. Missing contact details trigger the desk’s existing manual follow-up, never enrichment or texting. |
| Controlled availability | Only named, consenting desks enroll. Customer success can halt enrollment or disable the pilot through the existing flag without deleting callback records. |
| Measurement | Existing completion and ownership events support the report; shift-handoff notes supply context and usage evidence. No reminder-view metric is implied. |

Engineering must confirm existing callback capture, assignment correction, and completion are usable from this journey. If a dependency is missing, re-estimate the connected slice rather than ship an unusable queue.

**Capacity and alternatives**

Engineer-days below use input/delivery-constraints.md. Arithmetic is **not tool-verified**, respecting the request’s prohibition on running code.

| Allocation | Backend | Frontend | QA |
|---|---:|---:|---:|
| Available | 6 | 4 | 2 |
| Queue + measurement: feature + report | 3 + 0.5 = 3.5 | 3 + 0 = 3 | 1 + 0.5 = 1.5 |
| Remaining | 2.5 | 1 | 0.5 |

Keep the remainder for integration, recovery behaviors, permission checks, and fixes. Estimates are provisional; safe claiming and existing-workflow integration are the main scope uncertainties.

- **Weekly manager email:** defer. Adding it requires 5 frontend and 2.5 QA days including measurement, exceeding capacity. Use Friday reviews and the pilot report manually. Reconsider if managers demonstrate recurring action from the report.
- **SMS reminders:** defer. Alone with measurement, QA needs 2.5 days; provider approval is undated, and only 116 of 240 records have auditable consent. Reconsider after approval, a consent-compliant eligible population, and fresh capacity estimates.
- **Self-service routing/escalation:** defer. Multi-branch ownership is unresolved; custom UI adds complexity. Reconsider after an ownership study and a committed eligible pilot.
- **Exclude:** payments, pricing changes, enrichment, new providers, ownership redesign, and public enrollment.

Homepage headlines, video styling, and QR-card deadlines do not change this scope or provide transferable engineering capacity. “Every promise kept” is unsupported by this pilot. [Source: input/homepage-refresh.md]

**Delivery and learning**

Ship by September 30, 2026, subject to confirming the above dependencies. **Pilot dates and post-release support coverage remain unresolved:** a two-week trial may extend beyond release. Customer success should confirm participating desk names, dates, and support coverage before enrollment. Do not compress observation to claim success by the release deadline.

For each desk, compare a comparable pre-pilot period with two pilot weeks:

- Primary outcome: callbacks completed over 12 hours late **or still incomplete at that boundary**, divided by promised callbacks whose boundary has elapsed. Report counts and rates; exclude immature cases.
- Diagnostic outcomes: handoff-related and unowned late cases from Friday reviews; ownership changes and completions from server events.
- Practical value: handoff notes showing whether dispatchers actually use the queue, plus duplicate work, confusing ownership, and manual effort.

Obtain desk-specific baseline counts; the four-desk aggregate is not their baseline. Usage and causal improvement remain unobserved.

**Expansion decision**

At the managing director’s required review, recommend a small expansion to similar desks only if both desks show improved late-callback outcomes against their own baselines, repeated shift-handoff use, manageable support effort, and no unresolved permission or ownership failures. These are proposed directional gates, not statistical proof.

Mixed results, low volume, or missing baseline data mean inconclusive: adjust or extend only with confirmed coverage. Permission failures or harmful ownership confusion mean disable and return to existing handoffs; customer success coordinates outstanding callbacks. Multi-branch expansion and willingness to pay remain separate, unresolved decisions.