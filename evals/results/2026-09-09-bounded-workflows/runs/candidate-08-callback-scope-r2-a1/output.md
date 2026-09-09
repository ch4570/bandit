Recommend a **shared callback queue with visible ownership and claim action for the two small desks**, plus a measurement report using existing events. This is a proposed, reversible pilot scope. The strongest alternative is a manual handoff checklist: it could test ownership discipline sooner, but would not test whether a persistent queue helps dispatchers recover outstanding promises. Reopen the choice if essential ownership or completion behavior cannot fit capacity.

All evidence below comes from the supplied synthetic artifacts; it does not establish real customer demand or business validation.

**First customer group and rationale**

Enroll only the two consenting desks with 3–5 dispatchers, one time zone, and one shared phone number. Customer success should record the named desks before enabling access. Their offered two-week pilot and existing Friday reviews provide a practical learning setting ([stakeholder-notes.md](input/stakeholder-notes.md)).

The four-desk review found 62 of 240 callbacks more than 12 hours late: 31 attributed to handoff loss, 17 to absent ownership, and 14 to missing contact details. Five of eight interviewees wanted outstanding callbacks visible at shift start. These observations support testing queue visibility and ownership; they do not show that software would prevent 48 late cases. The 91% owner completeness at small desks also means visibility, rather than claiming alone, must deliver value ([evidence.md](input/evidence.md), dated 2026-09-09).

Defer multi-branch desks. Temporary dual ownership and differing time zones require unresolved ownership rules. The large prospect’s interest in a demo is weaker enrollment evidence than an offered pilot.

**Retained journey and handoff boundary**

A dispatcher starts a shift, sees outstanding promises within existing branch permissions, identifies responsibility, makes the callback through the existing process, and sees its recorded completion remove it from the outstanding queue.

Retain these behaviors:

- Show promised time, current owner or “unassigned,” and available contact details. Make overdue promises recognizable using the desk’s time zone.
- Allow claiming an unassigned item. Concurrent claims must resolve to one persisted owner; the unsuccessful claimant sees the current owner rather than an apparent success.
- Keep assigned work visibly assigned. Do not silently take over work, transfer branches, or introduce routing rules.
- Reflect existing completion records. Refreshing or changing shifts must preserve ownership and the correct outstanding state.
- Keep items lacking contact details visible. Dispatchers use their existing manual process to obtain details; do not imply that these callbacks are ready or complete.
- Provide recovery from a mistaken claim through existing authorized ownership correction. Reuse existing completion and correction paths only after confirming they support the journey.
- Restrict enrollment to named desks. Customer success must be able to stop enrollment or disable the pilot through the existing flag without deleting callback records.

Acceptance checks are **planned, not executed**: authorized visibility, concurrent claims, persistent ownership, completion removal, mistaken-claim recovery, missing-contact handling, and flag disablement.

**Capacity and alternatives**

Capacity includes integration and fixes; estimates remain estimates ([delivery-constraints.md](input/delivery-constraints.md)).

| Scope | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue, owner, claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Selected total | **3.5** | **3** | **1.5** |
| Remaining capacity | **2.5** | **1** | **0.5** |

Protect the remainder for integration, recovery behavior, and fixes. Confirm whether the queue estimate covers those essentials before treating this as deliverable.

- **SMS:** defer. Provider approval has no date; only 116/240 records have auditable consent. SMS plus measurement alone exceeds QA capacity. Reconsider after approval, consent coverage, and a separate capacity decision.
- **Routing/escalation:** defer. It adds 4/4/1 days and depends on unresolved multi-branch ownership. Reconsider after an ownership study.
- **Weekly email:** defer. Adding it exceeds frontend and QA capacity. Use existing Friday reviews and the manual report; reconsider if managers repeatedly need asynchronous delivery.
- Exclude pricing, payments, enrichment, and marketing work. The homepage campaign supplies neither pilot evidence nor transferable engineering capacity.

**Learning and expansion**

Before enablement, reconstruct a desk-specific 14-day baseline; the pooled 62/240 rate is not the small desks’ baseline. During two pilot weeks, use promised times, completion events, ownership changes, and handoff notes to report:

- Callback counts and the share exceeding 12 hours late, including still-open promises already beyond that threshold.
- Handoff-loss, absent-owner, and missing-contact reasons from Friday reviews.
- Claim conflicts, incorrect ownership, dispatcher use at shift start, and added manual effort.

Compare equally mature cohorts and report each desk separately. Completion changes cannot establish reminder exposure or causality.

Expand only after the required explicit review: both desks regularly use the queue, handoff/ownership delays improve without increased unresolved work, and no consequential access or ownership failures remain. Mixed or sparse results justify extending observation, not wider enrollment. Improvement does not establish willingness to pay.

The unresolved timing decision is whether the two-week pilot must finish by September 30. That requires launch by September 16, which available estimates do not validate. Recommend shipping by September 30 and reviewing after two full pilot weeks; do not compress safety checks to manufacture an expansion result.