Recommend a queue-and-ownership pilot for the two consenting small desks, with a measurement report and feature-flag rollback. Ship by **2026-09-30**; assess two weeks of live use before enrolling anyone else. The strongest alternative is a structured manual handoff using their existing notes: cheaper and immediately available, but less able to test whether persistent shared visibility helps. Prefer the queue unless essential ownership safeguards exceed capacity.

This is a recommended scope handoff. All supplied customer evidence is synthetic; it supports decisions within this exercise, not claims about real customers.

**First customer group and rationale**

Choose the two desks with 3–5 dispatchers, one time zone, and one shared number. They have offered a two-week pilot, already review late callbacks on Fridays, and have owners populated for 91% of callbacks ([stakeholder notes](input/stakeholder-notes.md), [evidence](input/evidence.md)).

The September 9 review recorded 62 of 240 callbacks more than 12 hours late: 31 attributed to handoff loss, 17 to missing ownership, and 14 to missing contact details. Thus, 48 of 62 late cases concern the queue’s intended problem; this is **not** an estimate of preventable delays. Five of eight interviewees requested outstanding-callback visibility, without seeing a prototype.

Defer multi-branch desks: temporary dual ownership and different time zones make their core workflow materially different. The large prospect’s interest in a demo does not outweigh two offered pilots.

**Retained journey and acceptance boundaries**

At shift start, an authorized dispatcher opens outstanding callbacks within existing branch permissions, sees what needs attention, establishes responsibility, calls through the existing process, and records completion.

| Retain | Observable acceptance outcome |
|---|---|
| Shared outstanding queue using existing table/status components | Show promised time, lateness, current owner or “unassigned,” and available contact details; prioritize overdue items. Empty results are distinguishable from loading or failure. |
| Claim unassigned callbacks | Owner is visible before action. Concurrent claims leave one persisted owner; the unsuccessful claimant sees the current owner. Failed saves never display false success. |
| Preserve existing assignments and branch access | Existing owners remain assigned. No silent reassignment or branch movement; unauthorized callbacks are inaccessible. Wrong-owner cases use the existing authorized correction process, if available. |
| Completion through the existing workflow | Confirmed completion removes the callback from outstanding work and remains recorded after refresh. Failed completion remains visible for retry. |
| Missing-contact recovery | Clearly identify absent contact details and keep the callback outstanding with a named owner. Staff resolve details through their existing process; no enrichment service or new collection workflow. |
| Controlled participation and rollback | Named consenting desks only. Customer success can stop enrollment or disable the pilot using the existing flag without deleting records; desks resume their handoff notes. |

Before enrollment, backend and QA must confirm existing callback capture, completion, and authorized ownership correction support this journey. Their usability is an assumption, not established by the notes. If a necessary gap cannot fit the remaining capacity, use the manual alternative rather than release a disconnected queue.

**Capacity and alternatives**

Estimates from [delivery constraints](input/delivery-constraints.md), in engineer-days:

| Work | Backend | Frontend | QA |
|---|---:|---:|---:|
| Queue, owner, claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Total / available | 3.5 / 6 | 3 / 4 | 1.5 / 2 |
| Remaining for integration, safeguards, fixes | 2.5 | 1 | 0.5 |

This fits nominally; it is not a delivery commitment. QA headroom is especially tight. Validate that retained recovery and permission behavior fits these estimates before adding breadth.

- **SMS reminders:** defer. With reporting, 5.5 backend, 2 frontend, and 2.5 QA days already exceed QA capacity. Provider approval has no date; only 116/240 records have auditable SMS consent. No consent bypass is allowed. Reconsider after approval, consent eligibility, and a funded estimate.
- **Routing/escalation rules:** defer. They introduce new UI and unresolved multi-branch ownership; combined with the queue and report they require 7.5/7/2.5 days. Reconsider after studying branch transfers.
- **Weekly manager email:** use existing Friday reviews and the report manually. Adding email to the selected slice requires 5.5/5/2.5 days, exceeding frontend and QA capacity. Reconsider if managers repeatedly need unattended delivery.
- Exclude pricing, payment, enrichment, and ownership redesign. The separate homepage/trade-show work supplies neither engineering capacity nor pilot evidence. “Every promise kept” is unsupported.

**Learning and expansion decision**

Hypothesis: shared visibility and explicit ownership reduce handoff-related delays in these small desks.

Customer success should use supplied handoff notes and existing Friday reviews; backend provides the scoped report from completion and ownership events. No new analytics warehouse or reminder-view tracking.

For each desk, compare a comparable pre-pilot 14-day period with two live weeks:

- **Primary:** callbacks completed over 12 hours late **or still incomplete at that point**, divided by all promised callbacks whose 12-hour follow-up window has elapsed. Report counts and rates; exclude immature cases.
- **Supporting:** unassigned outstanding callbacks at shift handoff; ownership changes; manually categorized late-case reasons; shifts where staff report using the queue divided by observed shifts.
- **Guardrails:** conflicting ownership, access incidents, failed updates, missing-contact backlog, and manual support effort.

The pooled 62/240 baseline cannot substitute for desk-specific baselines. Confirm their recoverability; missing data makes comparison inconclusive.

Recommend limited expansion only after the managing director’s explicit review: both desks repeatedly use the queue, both show lower late-callback rates with supporting handoff evidence, and no unresolved ownership or access failures remain. These are provisional decision criteria, not statistical proof. Mixed results or insufficient volume mean hold enrollment and investigate; consequential correctness failures mean disable.

Exact improvement targets and live-start dates remain unresolved. A September 30 release may place the two-week review in October. No observed pilot outcome, willingness to pay, or business validation is established.