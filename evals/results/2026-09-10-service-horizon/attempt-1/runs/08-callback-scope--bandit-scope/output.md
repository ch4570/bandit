Recommend shipping an **outstanding-callback queue with visible ownership and a claim action**, plus a measurement report, for the **two volunteering small desks**. The strongest alternative is a manual shared callback list reviewed at each handoff: faster to try, but weaker at testing whether persistent in-product ownership helps. Reopen the build choice if essential ownership, completion, or recovery behavior exceeds capacity.

This is a proposed scope decision, not an approved requirement set or evidence of business validation.

**Why these customers and this slice**

The supplied synthetic study recorded 62 late callbacks: 31 attributed to shift handoff, 17 to missing ownership, and 14 to missing contact details. Five of eight interviewed dispatchers wanted outstanding callbacks visible at shift start. These findings support testing queue visibility and ownership; they do not establish that software prevents lateness.

The two small desks have 3–5 dispatchers, one time zone, one shared number, and an owner recorded for 91% of callbacks. They offered a two-week pilot and existing Friday reviews. The large desks introduce dual ownership, branch transfers, and time-zone questions outside the estimates. The prospect’s interest in an automation demo is weaker evidence than a volunteered pilot. Sources: `input/evidence.md`, `input/stakeholder-notes.md`.

**Capacity and release boundary**

Ship the useful slice by **2026-09-30**, subject to validating the estimates against the connected journey below.

| Allocation | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue, owner, claim | 3 | 3 | 1 |
| Existing-event measurement report | 0.5 | 0 | 0.5 |
| Total | 3.5 | 3 | 1.5 |
| Capacity remaining | 2.5 | 1 | 0.5 |
| Available capacity | 6 | 4 | 2 |

Method: add the two estimates by discipline; subtract from available capacity. Arithmetic is **not tool-verified**, respecting the request not to run code. Inputs: `input/delivery-constraints.md`. Remaining capacity covers uncertainty, integration, and fixes; it is not another feature allocation. No overlap between feature estimates is assumed.

Before building, engineering should confirm that the queue estimate covers safe claiming, existing completion access, and recovery. Frontend and QA headroom are particularly limited. If essential work does not fit, reduce presentation polish or use the manual alternative; do not remove ownership safety.

**Retained journey and acceptance outcomes**

At shift start, an authorized dispatcher opens outstanding callbacks for their existing branch, sees what is overdue and who owns it, claims an unowned item, calls using existing contact details, and records completion through the existing workflow.

- **Queue:** Reuse table/status components. Show promised time, owner or “unassigned,” and available contact details; put overdue items first. Completed items leave the outstanding view. An empty queue explicitly says there are no outstanding callbacks.
- **Ownership:** Display the owner before claim. Claim assigns an unowned callback to the acting dispatcher and persists across reloads. Concurrent claims must yield one owner; the other dispatcher sees the current owner rather than a false success.
- **Handoff and correction:** Keep existing owners. Resolve already-owned handoffs or mistaken claims through the existing authorized correction workflow, after confirming it exists and is usable. Do not silently overwrite owners or move branches. Missing correction support requires re-estimation.
- **Missing contact details:** Keep the callback visible and identify the missing information. Staff use the existing manual correction process; claiming does not imply the customer can be reached.
- **Failure and permissions:** Failed loads or saves show a retryable error without claiming success. Existing branch permissions apply throughout.
- **Pilot control:** Enroll only the two named, consenting desks. Customer success can stop enrollment and disable the existing feature flag without deleting callback records.

These are planned acceptance checks; implementation and tests have not been executed.

**Deferred choices**

| Choice | Why defer; what would reopen it |
|---|---|
| SMS reminders | Provider approval has no date; only 116/240 records have auditable consent. Reconsider after approval, consent-safe eligibility, demonstrated need, and separate capacity. |
| Routing/escalation builder | Adds substantial effort and unresolved branch ownership behavior. Reconsider after ownership research and recurring routing failures. |
| Weekly manager email | Existing Friday reviews plus the report provide pilot learning. Reconsider if managers demonstrably need recurring delivery; no new email vendor is available. |
| Large multi-branch enrollment | Ownership and time-zone semantics are unresolved and unestimated. Requires a separate decision. |

No new pricing, payment, enrichment, or branch ownership redesign. Trade-show printing and agency budget do not change engineering capacity. “Every promise kept” exceeds the evidence; keep pilot messaging to testing clearer callback visibility and ownership. Source: `input/homepage-refresh.md`.

**Learning and expansion decision**

Hypothesis: visibility and explicit ownership reduce handoff-related delay at these desks.

Use a comparable pre-pilot period for each selected desk, then two full pilot weeks. Report counts and rates separately by desk:

- Callbacks completed more than 12 hours late **or still incomplete after that threshold**, divided by callbacks whose promised time has matured sufficiently for classification.
- Ownership changes from existing server events.
- Handoff failures, missing-contact blockers, and queue use from shift notes and Friday reviews.

Allow the final callbacks to mature before closing measurement. Do not infer queue views or reminder exposure from ownership events.

Recommend limited expansion only if both desks show lower late-callback rates, notes corroborate useful repeated handoff use, and there are no unresolved permission, ownership, or data-loss failures. This is a proposed directional gate, not statistical proof. Low volume, missing baselines, or conflicting signals mean **inconclusive**; repeat or adjust the same pilot before expansion. Disable for consequential safety failures.

Customer success coordinates the explicit expansion review requested by management. Pilot start date and support coverage remain unresolved: shipping September 30 does not establish two weeks of supported observation. Confirm coverage before enrollment; otherwise move the pilot window.