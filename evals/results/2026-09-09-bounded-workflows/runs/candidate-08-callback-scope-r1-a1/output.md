**Recommend a pilot for the two small, single-time-zone desks: an outstanding-callback queue with visible ownership and a claim action, plus measurement using existing server events.** This is a proposed scope decision, not an approved requirement. The strongest alternative is a manual shared handoff list using their existing Friday reviews: cheaper and useful for learning, but it would not deliver the requested shipped improvement or test ownership within RelayBoard. Reopen this choice if reliable claiming cannot fit the available capacity.

All supporting evidence is synthetic and supplied for this task; it does not validate market demand.

**First customers and intended outcome**

Enroll only the two named desks that agree to participate, each with 3–5 dispatchers, one time zone, and one shared number. Customer success should confirm their identities and participation before enabling the existing feature flag.

These desks have offered a two-week pilot and can provide handoff notes. Their owner fields are populated for 91% of callbacks, making existing ownership a practical starting point. The multi-branch desks have unresolved dual-owner and time-zone behavior. The large prospect expressed interest in a demo but committed to neither a trial nor purchase. ([Stakeholder notes](input/stakeholder-notes.md), [evidence](input/evidence.md))

The intended outcome: a dispatcher starting a shift can find outstanding promises, see responsibility, take an unowned callback, and complete it through the existing workflow without losing it at handoff.

**Retained scope and observable boundaries**

| Keep | Rule and acceptance outcome |
|---|---|
| Outstanding queue | Show incomplete promised callbacks within existing branch permissions, with promised time and current owner visible before claiming. Completed callbacks leave the outstanding view. Reopening the queue reflects saved state. |
| Claim unowned work | An authorized dispatcher can claim an unowned callback. Concurrent claims must produce one authoritative owner; the unsuccessful claimant sees the current owner. An unsuccessful save must not appear successful. |
| Existing ownership | Preserve populated owners. No automatic transfers, branch changes, or new routing rules. Handle mistaken claims through an existing authorized correction path; confirm that path exists before release. |
| Contact and completion | Make existing contact details accessible and missing details apparent. Staff resolve missing information through their current process; a claim does not mean the callback is complete. Preserve the existing completion workflow. |
| Controlled participation | Customer success can stop enrollment or disable the pilot using the existing flag without deleting callback records. Verify that access remains branch-restricted. |
| Measurement | Produce a report from existing completion and ownership events; supplement it with the desks’ handoff notes and Friday reviews. No new analytics warehouse or notification provider. |

These are proposed acceptance checks, **not executed verification**. Confirm queue display, durable ownership, concurrent claims, correction, access, completion, and disablement within the feature estimate.

**Capacity and delivery boundary**

Queue plus measurement totals **3.5 backend, 3 frontend, and 1.5 QA engineer-days**, against **6 / 4 / 2** available. That leaves **2.5 backend, 1 frontend, and 0.5 QA days** for uncertainty within the release window ending September 30. These are estimates, not a delivery commitment. ([Delivery constraints](input/delivery-constraints.md))

The main estimate risk is whether the quoted queue includes safe concurrent claiming and ownership correction. Resolve that narrowly before committing delivery; cut optional presentation first. Do not ship misleading ownership to preserve the date.

Ship by September 30; run the offered two-week pilot from actual enablement. A full pilot readout by September 30 requires starting by September 16, which the notes do not establish as feasible.

**Deferred choices and trade-offs**

- **SMS:** defer. It targets reminders rather than directly repairing handoff ownership; provider approval has no date, and only 116/240 records have stored consent. Queue plus SMS would require 8 backend, 5 frontend, and 3 QA days before measurement. Reconsider only with provider approval, consent-compliant targeting, and evidence that reminders address remaining delays.
- **Routing/escalation:** defer until multi-branch ownership is studied and redesigned with explicit authority. Queue plus routing already exceeds backend and frontend capacity.
- **Weekly manager email:** use Friday reviews and the pilot report manually. Adding email to the selected scope requires 5 frontend and 2.5 QA days, exceeding capacity. Revisit if managers repeatedly use the report and delivery automation has demonstrated value.
- Exclude pricing, payments, contact enrichment, and branch-ownership changes. Marketing and trade-show work have separate ownership and provide no callback-pilot evidence.

**Learning and expansion decision**

The pooled baseline is **62/240 callbacks more than 12 hours late (25.8%)**; 48 late cases were attributed to handoff loss or absent ownership. These are reported reasons, not proven preventable delays.

Compare each pilot desk’s late-callback share with its own preceding comparable period, reporting counts, volumes, unresolved callbacks, and completed ownership changes. Do not treat unfinished callbacks as on-time or infer reminder views from unavailable data. Use notes to assess handoff losses, duplicate work, missing contact details, and actual queue use.

Recommend expansion only after the managing director’s explicit review finds repeated use, directionally fewer late/handoff failures, and no unresolved ownership or access defects. Flat or worse results warrant diagnosis, not broader enrollment. A numeric success threshold remains unresolved: desk-specific baselines and volumes are missing. Agree it before enablement; two weeks can support a next experiment, not establish causality or willingness to pay.