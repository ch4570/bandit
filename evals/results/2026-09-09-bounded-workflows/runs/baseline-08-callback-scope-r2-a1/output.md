**RelayBoard callback pilot — scope handoff, 9 September 2026**

**Decision:** Ship an outstanding-callback queue with visible ownership and a claim action, plus a measurement report. Enroll only the two small desks that offered a two-week pilot, after confirming their participation. Require an explicit review before enrolling additional customers.

### First customer group and problem

Start with the two desks that each have 3–5 dispatchers, one time zone, and one shared phone number. They offer willing participants, shift-handoff notes, and an existing Friday review routine. Their owner field is already populated for 91% of callbacks.

Prioritize callbacks becoming lost or unowned across shifts. Across all four sampled desks, 62 of 240 promised callbacks were more than 12 hours late; 31 were attributed to handoff loss and 17 to missing ownership. Five of eight interviewed dispatchers wanted outstanding callbacks visible at shift start.

These findings support testing visibility and ownership. They do **not** establish that the queue will prevent those 48 delays, that the small desks share the aggregate late rate, or that customers will pay.

Defer the large multi-branch desks: temporary dual ownership and differing time zones need investigation. The prospect’s interest in an automation demo is neither a trial commitment nor purchase evidence.

### Shipped slice and acceptance boundaries

Use existing table and status components and existing branch permissions.

- Show outstanding promised callbacks within the dispatcher’s permitted scope, including promised time, current owner or “unassigned,” and available contact details. Put the earliest promised callbacks first.
- Make ownership visible before any claim action. Allow an unassigned callback to be claimed by the acting dispatcher.
- Preserve existing assignments. Do not silently transfer callbacks between dispatchers or branches. If simultaneous claims occur, retain one valid owner and refresh the unsuccessful claimant’s view.
- Reflect completion through the existing completion workflow; completed callbacks leave the outstanding queue. Do not introduce a separate closure workflow.
- Make absent contact details apparent using existing data. Keep those callbacks visible; this pilot does not solve contact-data collection.
- Restrict enrollment to named participating desks. Give customer success a documented way to stop enrollment and disable the pilot using the existing flag, without deleting callback records.

Release acceptance includes permission isolation, owner visibility, claim conflicts, completion updates, missing-contact cases, and flag disablement.

### Capacity and delivery

| Work | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue, owner, claim | 3 | 3 | 1 |
| Existing-event measurement report | 0.5 | 0 | 0.5 |
| **Committed total** | **3.5 / 6** | **3 / 4** | **1.5 / 2** |
| **Remaining for integration and fixes** | **2.5** | **1** | **0.5** |

Protect the remaining capacity; it is not another feature allocation. Confirm the acceptance details fit the queue estimate before implementation. QA has particularly little headroom.

Target release by **16 September**, followed by two weeks of observation through **30 September**. This is a scheduling target, not a proven delivery commitment. If release slips, ship the accepted slice by 30 September and move the expansion review until a full two-week pilot is observed.

### Explicit deferrals

- **Automatic SMS:** Too large alongside the queue; provider approval has no committed date. Only 116/240 records have auditable consent. No unconsented fallback is authorized.
- **Routing/escalation rules:** Exceed combined capacity and require unresolved multi-branch ownership behavior and new UI.
- **Weekly manager email:** Queue plus email already needs five frontend days against four available, before measurement. Use the pilot report in existing Friday reviews.
- **Also excluded:** ownership redesign, workflow builder, contact enrichment, pricing/payment changes, new providers, and an analytics warehouse.

Homepage copy, the video, and trade-show materials are separately owned and provide no evidence for this pilot’s scope.

### Learning and expansion decision

Before launch, establish a baseline **for the two participating desks**, using their records and handoff notes. Do not use the four-desk aggregate as their baseline.

Use existing completion and ownership-change events to report per desk:

- Promised-callback volume and share completed more than 12 hours late.
- Still-incomplete callbacks already past that threshold, reported separately.
- Unassigned outstanding callbacks and ownership changes.

Give baseline and pilot cohorts equal follow-up; label callbacks whose outcome is not yet observable. Use Friday notes to assess handoff loss, unclear ownership, and practical queue use. Events cannot establish who saw a reminder or prove adoption.

**Proposed expansion gate:** both desks show lower late-or-still-overdue shares than their own comparable baselines, report improved handoffs, and have no unresolved access, ownership, or record-integrity defects. Review counts and workload changes, not percentages alone. Mixed or sparse results mean extend observation or revise scope—not automatic enrollment.

A defensible numerical improvement threshold remains unresolved until desk-level baseline volumes are known. Agree it before pilot results are reviewed. Expansion should first target similar small desks; multi-branch rollout requires separate ownership discovery.