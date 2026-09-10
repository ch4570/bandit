Recommend a **named, two-desk pilot of the callback queue with visible ownership and claiming, plus measurement using existing events**. The strongest alternative is a manual shared handoff list: faster to start, but less useful for learning whether persistent in-product ownership helps. Choose the queue provisionally; revert to the manual approach if safe claiming and recovery exceed capacity. Reopen expansion only after the managing director’s explicit review.

**First customer group and rationale**

Start with the two willing small desks: each has 3–5 dispatchers, one time zone, and one shared number. Customer success should record their names and participation agreement before enabling access. Their existing Friday reviews and offered handoff notes make learning practical. The multi-branch prospect has expressed demo interest, not trial or purchase commitment.

The supplied evidence is synthetic and describes a four-desk convenience sample dated 2026-09-09. Of 62 late callbacks, staff attributed 31 to handoff loss, 17 to missing ownership, and 14 to missing contact details. Five of eight interviewees wanted outstanding callbacks visible at shift start. This supports testing the queue, not claiming it prevents delays. The small desks’ 91% populated owner field also suggests that visibility across shifts matters alongside assigning owners. Segment-specific late-callback counts remain unknown. [Sources: input/evidence.md; input/stakeholder-notes.md.]

**Retained pilot journey**

A dispatcher starts a shift, sees outstanding promises within existing branch permissions, identifies responsibility, claims an unowned callback, completes the callback through the existing process, and leaves saved state for the next shift.

Recommended scope and acceptance boundaries:

- Reuse table/status components. Show promised time, current owner or “Unassigned,” and available contact details; make overdue items easy to find. An empty queue must be distinguishable from a loading or retrieval failure.
- Show ownership before claiming. An authorized claim must persist and leave one owner. If two dispatchers claim simultaneously, the unsuccessful claimant sees the saved owner; a failed save must not appear successful.
- Preserve existing completion behavior. Completed callbacks leave the outstanding queue after saved completion; failed updates remain recoverable without losing the record.
- Keep callbacks with missing contact details visible. Dispatchers use their existing manual process to obtain details and retain responsibility; no enrichment or new contact-data workflow.
- Keep branch access and ownership boundaries intact. Do not automatically reassign owned callbacks or transfer them between branches. Use existing authorized correction paths for mistaken claims; confirming that such a path exists is a release dependency.
- Customer success controls named enrollment and can disable the pilot through the existing feature flag without erasing records. On disablement or service failure, desks resume their handoff notes.

These are proposed acceptance checks, not executed verification. Engineering must confirm that permissions, claim conflicts, correction, and flag controls fit the supplied estimate.

**Capacity and alternatives**

Engineer-days below use backend/frontend/QA order:

| Scope | Required days | Decision |
|---|---:|---|
| Queue + measurement | 3.5 / 3 / 1.5 | Recommend |
| Available capacity | 6 / 4 / 2 | Fixed ceiling |
| Remaining capacity | 2.5 / 1 / 0.5 | Integration uncertainty and fixes |
| Queue + email + measurement | 5.5 / 5 / 2.5 | Exceeds frontend and QA |
| SMS + measurement | 5.5 / 2 / 2.5 | Exceeds QA; provider blocked |
| Routing + measurement | 4.5 / 4 / 1.5 | Fits nominally, but lacks ownership-redesign coverage |

Arithmetic: add each feature estimate and the report’s 0.5 backend/0.5 QA days; subtract the selected total from capacity. **Not tool-verified because the request prohibits running code.** Estimates are not delivery commitments. [Source: input/delivery-constraints.md.]

Defer automatic SMS: provider approval has no date, only 116 of 240 records have auditable consent, and texting without consent is prohibited. Revisit only with approval, consent-safe eligibility, sufficient capacity, and evidence that messaging addresses the remaining problem.

Defer routing/escalation until multi-branch ownership and time-zone behavior are studied and separately estimated. Defer weekly email: existing Friday reviews provide a manual substitute; revisit if managers demonstrate a recurring reporting need after queue use. No new provider, warehouse, pricing, payment, or ownership redesign.

**Timing, learning, and expansion**

Ship the safe slice by **2026-09-30**, conditional on estimate confirmation. The offered two-week pilot is an observation period, not automatically contained within the build window. Exact activation dates and support coverage remain unresolved: do not promise a full two-week result by September 30 or assume later staffing.

Customer success should use existing notes to establish a comparable 14-day baseline for the same two desks, then review a full 14-day pilot using:

- **Primary outcome:** callbacks completed more than 12 hours late, plus still-incomplete callbacks past that threshold, divided by all promised callbacks due in the window. Allow the final 12-hour threshold to mature.
- **Supporting evidence:** ownership changes and completion events, plus handoff notes identifying lost promises, unowned work, missing details, and whether dispatchers actually used the queue. Events alone do not prove viewing.
- Report counts and rates separately by desk, missing records, workload changes, and Friday feedback.

Proposed expansion gate: both desks show fewer handoff/ownership failures and improved late-callback outcomes without access violations, conflicting ownership, or unacceptable support effort. Flat, mixed, sparse, or incomplete evidence means revise or extend only with confirmed capacity; serious safety failures mean disable. No numerical improvement threshold is supported yet.

Expand first to comparable small desks after the required review. This pilot cannot establish paid demand or multi-branch readiness. The homepage campaign is separate and supplies no pilot evidence; “Every promise kept” is not a supported outcome claim.