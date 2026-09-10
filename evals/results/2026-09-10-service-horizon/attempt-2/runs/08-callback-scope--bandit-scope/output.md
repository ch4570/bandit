**Recommend a callback queue with visible ownership and claim, plus the measurement report, for the two small desks already offering a two-week pilot.** This is a proposed scope decision. The strongest alternative is a manual shift-start callback list using existing records and handoff notes: faster to try, but less useful for learning whether persistent shared ownership improves handoffs. Reopen the choice if essential queue behavior exceeds capacity or cannot safely preserve ownership.

All supplied evidence is synthetic; it supports this planning exercise, not claims about real customers.

**Why this group and scope**

The September 9 review recorded 62 late callbacks among 240 promised callbacks: 31 attributed to shift handoff, 17 to missing ownership, and 14 to missing contact details. Five of eight interviewees requested outstanding callbacks at shift start. These findings motivate a queue; they do not prove it prevents delays.

The two small desks have 3–5 dispatchers each, one time zone, one shared number, and an owner recorded on 91% of callbacks. They offer an accessible pilot with simpler ownership. The large desks introduce unresolved dual ownership and branch time zones; the prospect’s interest in a demo is weaker evidence than an offered pilot. Sources: `input/evidence.md`, `input/stakeholder-notes.md`.

**Capacity and alternatives**

Engineer-days below use backend/frontend/QA order. Estimates are additive, from `input/delivery-constraints.md`.

| Option, including measurement | Estimated days | Decision |
|---|---:|---|
| Queue + report | 3.5 / 3 / 1.5 | Retain |
| SMS + report | 5.5 / 2 / 2.5 | Exceeds QA; provider approval and consent constrain delivery |
| Routing rules + report | 4.5 / 4 / 1.5 | Fits nominally, but consumes all frontend capacity and excludes ownership redesign |
| Manager email + report | 2.5 / 2 / 1.5 | Fits, but reports problems after the handoff rather than helping dispatchers act |

Capacity is **6 / 4 / 2**. Queue plus measurement leaves **2.5 / 1 / 0.5** for integration uncertainty and fixes, not another feature. Queue plus even the manager email and measurement would require **5.5 / 5 / 2.5**, exceeding frontend and QA capacity.

Calculation method: add each proposal’s estimate to report effort, **0.5 / 0 / 0.5**; subtract selected totals from capacity for remaining effort. Arithmetic is **not tool-verified**, respecting the request not to run code. Estimates remain provisional, not delivery commitments.

**Retained journey and acceptance boundaries**

An enrolled dispatcher starts a shift, sees outstanding callbacks within existing branch permissions, identifies responsibility, claims an unowned callback, completes the call through the existing workflow, and leaves accurate state for the next shift.

- Reuse table/status components. Show promised time, overdue status, owner or “Unassigned,” and available contact details. Prioritize overdue and earliest promises.
- Show ownership before claiming. Claim must persist one owner; concurrent claims must yield one winner and show the other dispatcher the current state. Do not silently overwrite an owner.
- Keep assigned callbacks visible. Use the existing authorized ownership-correction path for handoffs; confirming that path is a delivery prerequisite. If absent, estimate minimum correction behavior before committing.
- Reflect existing completion records so completed callbacks leave the outstanding queue after refresh. Do not introduce a separate completion system.
- Missing contact details remain visible as an obstacle; dispatchers resolve them manually through existing processes. Do not imply the queue solves this cause.
- Provide clear empty, loading, failed-load, and failed-claim states. Failed actions must not appear saved; allow retry or refresh.
- Restrict access to named participating desks under existing branch permissions. Customer success must be able to stop enrollment and disable the pilot through the existing flag without erasing records.

QA should demonstrate these outcomes, including concurrent claim, permission isolation, persistence across shifts, and disable/recovery. These are planned checks, not executed results.

**Explicit cuts**

Defer SMS until provider approval, auditable consent eligibility, and delivery capacity are established; never text records without consent. Defer routing/escalation and large-desk enrollment pending an ownership study and separate estimate. Defer manager email; use existing Friday reviews and the measurement report.

Exclude pricing, payments, enrichment, ownership redesign, and new providers or warehouses. Homepage copy, video styling, and Friday QR cards do not change pilot priority: another agency owns them, and sampled desks have not seen the campaign. “Every promise kept” is unsupported by this pilot.

**Learning, timing, and expansion**

Ship the gated slice by **September 30**, subject to fit confirmation. A full two-week pilot need not finish by that date. Pilot start and support coverage remain unresolved: customer success and engineering must confirm dates and coverage before making the two-week commitment.

Use each participating desk’s comparable pre-pilot records as baseline; the pooled four-desk result is not its baseline. Over two weeks, report per desk:

- Callbacks completed over 12 hours late, plus callbacks still incomplete after that threshold, divided by promises whose due time has passed by at least 12 hours.
- Raw eligible counts, ownership changes, and outstanding unowned cases from existing records/events.
- Friday handoff notes explaining misses, conflicts, workarounds, and whether dispatchers used the queue across shifts.

Do not infer reminder viewing from completion events.

At the managing director’s required review, recommend limited expansion to similar desks only if both desks use the queue across shifts, late-callback results improve against their own baselines, notes support the handoff hypothesis, and no material permission or ownership failures occur. Treat this as directional evidence, not causal proof. Mixed results or sparse volume mean inconclusive; investigate before expanding. Disable for unsafe ownership/access behavior. Large-branch rollout and willingness to pay remain separate, unanswered decisions.