**RelayBoard callback pilot — scope handoff**

**Decision.** Ship an outstanding-callback queue with visible ownership and a claim action for the two volunteer desks with 3–5 dispatchers, one time zone, and one shared phone number each. Enroll only those named desks after confirming participation. Include a measurement report using existing server events. Require an explicit review before expanding enrollment.

This tests whether making unfinished promises and ownership visible improves shift handoffs. It does not establish market demand, willingness to pay, or that software will prevent delays.

**Why this group and problem**

The manual review found 62 of 240 callbacks were more than 12 hours late (25.8%). Staff attributed 48 of those 62 cases to shift handoff or missing ownership. Five of eight interviewed dispatchers wanted outstanding callbacks visible at shift start. These are useful signals, but come from a small convenience sample and retrospective attribution.

The small desks offer a committed two-week pilot, handoff notes, and an existing Friday review. Their owner field is already populated for 91% of callbacks, making visibility worth testing alongside claiming unowned work.

Defer multi-branch desks. Temporary dual ownership and different time zones create unresolved semantics that the estimates exclude. The large prospect’s interest in a demo is not a trial commitment.

**Shipped slice**

Reuse existing table and status components:

- Show incomplete promised callbacks within existing branch access permissions, ordered by promised time, with overdue items distinguishable.
- Show promised time, assigned dispatcher or “Unassigned,” and available contact details. Make missing details visible; keep those callbacks in the queue.
- Show ownership before any claim action. Allow an authorized dispatcher to claim an unassigned callback for themselves.
- Prevent concurrent claims from silently overwriting ownership; refresh and show the current owner when a claim conflicts.
- Reflect existing completion and ownership changes. Completed callbacks leave the outstanding queue while their records remain intact.
- Restrict access through named-desk enrollment and the existing feature flag. Give customer success operational control to stop enrollment or disable the pilot without deleting records.

The queue supports existing callback work. It does not introduce reassignment, branch transfers, or a new callback-completion workflow.

**Capacity and tradeoffs**

| Committed work | Backend | Frontend | QA |
|---|---:|---:|---:|
| Queue, owner, claim | 3 days | 3 days | 1 day |
| Measurement report | 0.5 day | 0 | 0.5 day |
| Total | 3.5 days | 3 days | 1.5 days |
| Capacity remaining | 2.5 days | 1 day | 0.5 day |

Retain the remaining capacity for integration, fixes, and release uncertainty. Confirm that claim conflict handling and enrollment controls fit the queue estimate before implementation.

Defer all other proposals:

- **SMS:** provider approval has no committed date; only 116/240 records have auditable consent. Queue plus SMS also exceeds every engineering/QA budget. Never text without stored consent.
- **Routing/escalation:** exceeds frontend capacity when combined with the queue and depends on unresolved multi-branch ownership.
- **Weekly manager email:** queue plus email requires five frontend days before measurement, exceeding four available. Use the pilot report and existing Friday reviews instead.
- **Pricing, payments, contact enrichment:** outside authorization. Missing contact details remain an acknowledged source of delay.
- **Homepage and trade-show work:** separately owned and provides no evidence for this scope or additional engineering capacity.

**Delivery and learning**

Target readiness by September 16 and a two-week pilot September 17–30. Verify scheduling feasibility immediately; the estimates describe effort, not elapsed delivery time. If readiness slips, ship safely by September 30 and finish the observation period afterward. Do not substitute a shortened pilot for two weeks of evidence.

Before enabling, verify branch permissions, owner visibility, concurrent claims, overdue display, completion updates, and flag disablement.

Use the report to compare each pilot desk’s baseline and pilot **share of callbacks completed more than 12 hours late or still incomplete after that threshold**. Assign cohorts by promised time and allow every record to mature past 12 hours. Report counts, denominators, incomplete cases, and each desk separately. First check baseline timestamp completeness and desk-level availability; the pooled 25.8% is context, not a valid desk-specific benchmark.

Existing events establish completion and ownership changes, not queue views. Use handoff notes and Friday reviews to assess actual use, missed work, ownership confusion, and missing-contact blockers.

**Expansion gate**

Propose expansion only if both desks show usable adoption, fewer handoff/ownership failures, and directional improvement in late-callback rates without access or ownership incidents. Treat this as a decision signal, not causal proof. Disable for access breaches or ownership corruption; iterate if use is low or results are mixed.

A defensible numerical improvement threshold remains unresolved until desk baselines and volumes are known. Agree it before enabling. Multi-branch expansion additionally requires a separate ownership study and estimate.