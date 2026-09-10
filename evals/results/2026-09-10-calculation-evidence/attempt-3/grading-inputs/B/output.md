**Recommend an owner-visible callback queue and a measurement report for the two small desks that offered a pilot.** The strongest alternative is a structured manual handoff list: it could test the ownership hypothesis sooner, but would not deliver the requested shipped improvement. The queue sacrifices notification and routing breadth to test whether shared visibility helps across shifts. Reopen this choice if safe claiming exceeds capacity or participating desks cannot use it in their normal handoffs.

This is a proposed scope decision. The supplied evidence is synthetic; it supports this planning exercise, not claims about real customers.

**First customer group and rationale**

Enroll only the two consenting desks with 3–5 dispatchers, one time zone, and one shared number. Customer success should record their names before enabling the existing flag.

The September 9 evidence reports 31 handoff-related and 17 owner-related cases among 62 callbacks completed more than 12 hours late. Five of eight interviewed dispatchers wanted outstanding callbacks visible at shift start. These findings support a visibility-and-ownership hypothesis, but do not establish that software will reduce delays. The small desks already have owners on 91% of callbacks, so this slice must help people find existing responsibilities as well as claim unowned work.

Defer the large desks: temporary dual ownership and branch time zones introduce unresolved behavior beyond these estimates. The prospect’s interest in a demo is weaker enrollment evidence than the small desks’ offered trial.  
Sources: `input/evidence.md`, `input/stakeholder-notes.md`.

**Retained pilot journey**

At shift start, an authorized dispatcher opens the outstanding queue, sees promised time, current owner or “unassigned,” and whether contact details are missing. Reuse the existing table and status components.

- Show only callbacks allowed by existing branch permissions. Do not move callbacks between branches.
- Allow claiming an unassigned item. Show the current owner before any action; prevent a stale or simultaneous claim from overwriting another owner. On conflict, refresh the item and explain who owns it.
- Keep assigned callbacks visible across shifts. Ownership transfer remains a manual coordination step using existing authorized behavior; verify that this supports handoffs before release. Do not silently equate “claim” with reassignment.
- Use the existing callback and completion workflow. Persist successful changes; completed callbacks leave the outstanding queue.
- Keep callbacks with missing contact details visible. Dispatchers resolve details through their existing process; no enrichment is included.
- Distinguish an empty queue from loading or failed retrieval. Failed claims must not appear successful; allow retry after refresh.
- Give customer success control to stop enrollment or disable the flag without deleting records. Desks then resume their existing handoff notes.

Acceptance checks should cover next-shift visibility, concurrent claims, forbidden branch access, completion persistence, missing details, retrieval failure, and flag rollback. These checks are **planned, not executed**.

**Capacity and alternatives**

Capacity through September 30 is **6 backend, 4 frontend, and 2 QA engineer-days**, including integration and fixes.

| Scope | Backend | Frontend | QA |
|---|---:|---:|---:|
| Queue, owner, claim | 3 | 3 | 1 |
| Existing-event measurement report | 0.5 | 0 | 0.5 |
| Proposed total | 3.5 | 3 | 1.5 |
| Remaining capacity | 2.5 | 1 | 0.5 |

Method: add the two estimate rows, then subtract each discipline’s total from its capacity. These derived figures are **not tool-verified**, because the task prohibits running code. Estimates come from `input/delivery-constraints.md`; they are not delivery commitments.

Preserve remaining capacity for integration and fixes, especially the narrow QA allowance. Engineering must confirm that permissions, claim conflicts, recovery, and flag controls fit the queue estimate. If they do not, revise the release plan rather than removing essential ownership safeguards.

- **SMS:** defer. Provider approval has no date, and only 116 of 240 records have auditable consent. Reconsider after approval, a consent-safe design, and evidence that reminders address the remaining problem.
- **Routing/escalation:** defer pending a multi-branch ownership study and revised estimates.
- **Manager email:** defer; adding it to the selected scope exceeds frontend and QA capacity. Use the report in existing Friday reviews without a new email provider.
- **Homepage, video, QR cards:** outside this decision. Their timing and agency budget do not change product capacity. Do not adopt “Every promise kept” as a pilot outcome guarantee.

**Learning and expansion decision**

Run the offered two-week pilot after readiness checks. Its start date is unresolved: a September 30 release does not itself guarantee two weeks of observation by that deadline.

Customer success should obtain each participating desk’s preceding 14-day handoff notes and review them with its Friday reviewers. Do not treat the pooled four-desk results as these desks’ baseline.

The report should measure, separately by desk:

- Callbacks completed over 12 hours late **or still incomplete after that threshold**, divided by callbacks whose promised time has passed by at least 12 hours.
- Ownership changes and callback completions from existing server events.
- Handoff-related misses, unresolved ownership, and operational burden from manual notes.

Apply the same definitions to baseline and pilot; report counts, denominators, and missing data. Reminder exposure cannot be measured with current data.

Proposed expansion gate: after explicit managing-director review, add a small cohort of similar desks only if both desks use the queue across shifts, lateness improves against comparable baselines, and no material access or ownership failures emerge. Sparse records, inconsistent notes, or conflicting desk results mean **inconclusive**, not success. Disable for material safety failures; revise the slice if normal handoffs remain unsupported. No numeric improvement target or willingness-to-pay conclusion is supported yet.