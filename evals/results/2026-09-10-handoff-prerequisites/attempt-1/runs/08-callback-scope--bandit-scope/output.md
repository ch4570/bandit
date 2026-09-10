**Recommend an owner-visible callback queue for the two small, single-time-zone desks**, with a measurement report and controlled enrollment. This is a proposed scope decision, not an approved requirement.

The strongest alternative is a manual shift-handoff checklist using their existing Friday reviews. It requires less engineering and could test the handoff hypothesis, but would not provide persistent shared visibility between shifts. Use it if the complete queue cannot fit the release window. Reopen the scope if ownership behavior proves more complex than the estimates allow or the pilot shows no useful improvement.

### First customer group and intended outcome

Enroll only the two named desks with 3–5 dispatchers, one time zone, and one shared phone number, after confirming participation. They have offered a two-week pilot and handoff notes; their owner field is populated for 91% of callbacks. Preserve existing branch access and ownership boundaries.

The intended outcome is simple: **a dispatcher starting a shift can find outstanding promises, see responsibility, claim an unowned callback, and record completion through the existing workflow.**

The supplied synthetic evidence supports this hypothesis, not a proven effect. Across four desks, 31 late callbacks were attributed to handoff loss and 17 to missing ownership; five of eight interviewed dispatchers requested visibility at shift start. Those findings are not a baseline specific to the two selected desks.  
Sources: `input/evidence.md`, `input/stakeholder-notes.md`.

### Retained pilot scope

| Retain | Boundary and acceptance outcome |
|---|---|
| Outstanding-callback queue | Show authorized branch records, promised time, visible owner or “Unassigned,” and whether overdue. Completed callbacks leave the outstanding view after saved completion. Reuse existing table/status components. |
| Claim action | A dispatcher can claim an unassigned callback. Show ownership before acting; simultaneous claims must not silently overwrite an owner. A losing claimant sees the current owner and can refresh. |
| Durable handoff | Ownership remains visible across shifts and reloads. Retain the existing authorized ownership-change workflow; do not introduce automatic reassignment or branch transfers. |
| Missing contact and failure recovery | Make absent contact details apparent without enrichment. Keep the callback outstanding while staff resolve details through their existing process. Failed loads or claims show a clear retry state and never imply a successful save. |
| Enrollment and rollback | Customer success controls the named pilot cohort and can stop enrollment or disable the feature with the existing flag. Disabling preserves records; desks resume their existing manual process. |
| Measurement report | Use existing completion and ownership events plus supplied handoff notes. No new analytics warehouse, reminder-view tracking, or frontend reporting dashboard. |

Before commitment, engineering must confirm that existing completion, contact correction, and ownership-change workflows support this journey. These are dependencies, not evidence of working implementation. If essential recovery behavior exceeds the allowance, reduce optional presentation or use the manual fallback; do not ship misleading ownership.

### Capacity and deferred work

From `input/delivery-constraints.md`:

| Allocation | Backend days | Frontend days | QA days |
|---|---:|---:|---:|
| Queue with owner and claim | 3 | 3 | 1 |
| Measurement report | 0.5 | 0 | 0.5 |
| Proposed total | 3.5 | 3 | 1.5 |
| Remaining against 6 / 4 / 2 | 2.5 | 1 | 0.5 |

Calculation: add each discipline’s queue and report estimates, then subtract from its available capacity. **Arithmetic is not tool-verified because the task prohibits running code.** Remaining capacity is contingency for uncovered dependencies, integration, and fixes—not another feature commitment. QA is particularly constrained. Estimates remain provisional.

- **SMS reminders: defer.** Provider approval has no date; only 116 of 240 reviewed records have auditable consent. No consent-free fallback is authorized. Reconsider only with approval, consent enforcement, capacity, and evidence that reminders address the remaining problem.
- **Routing/escalation rules and multi-branch enrollment: defer.** Conflicting owners and branch time zones require discovery and ownership design outside these estimates.
- **Weekly manager email: defer.** Existing Friday reviews and the pilot report provide a manual alternative; the email would exceed available frontend and QA capacity when added.
- **Pricing, payments, enrichment, campaign changes: excluded.** Homepage copy, video, and trade-show materials neither establish demand nor change engineering capacity.

### Release, learning, and expansion gate

The release deadline is **2026-09-30**. A full two-week observation period may extend beyond it. Customer success must confirm pilot dates and operational coverage; do not compress the observation window to imply learning is complete at release.

Before activation, capture a comparable two-week baseline for each selected desk. For baseline and pilot, report callbacks completed more than 12 hours late—or still outstanding beyond that point—divided by promises whose 12-hour assessment point has elapsed. Show counts and denominators by desk. Supplement this with ownership changes and Friday notes identifying handoff loss, missing owners, and missing contact details. Existing events cannot establish who viewed a reminder or prove causation.

**Proposed expansion gate:** after two weeks, compare each desk with its baseline. Expand only after explicit review if late-callback rates improve in both desks, handoff notes support practical benefit, and there are no unresolved permission, ownership, or data-loss failures. Sparse or conflicting results mean extend or revise the pilot, not declare success.

The minimum worthwhile improvement remains unresolved: these notes cannot justify a numerical threshold. Agree it with participating desks before activation. Successful results would support another small-desk cohort—not multi-branch readiness, paid demand, or the promise “Every promise kept.”