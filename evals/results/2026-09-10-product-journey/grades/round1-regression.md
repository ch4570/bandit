# Independent anonymous regression grades

Evaluated only each answer's `input/` files, `criteria.md`, and `output.md`. Judgments concern observable meaning against the raw request and frozen criteria, without requiring particular headings or design choices. All listed acceptance dimensions are treated as mandatory. Line citations below are relative to this report's directory. Execution history was outside the permitted evidence; integrity judgments therefore cover the answer text, not an audit of tool use or filesystem changes.

## Answer A

**Overall: passed — all six mandatory dimensions passed.**

Actual SHA256 of `A/output.md`:

```text
f51a8e8038d0f9b511425aa3518b6645301fa387af394c51308bf2eb61245b1a
```

| Criterion | Judgment | Evidence and explanation |
| --- | --- | --- |
| Decisions remain distinguishable (`A/criteria.md:8–9`) | passed | `A/output.md:1,7–11` selects the two small desks and a queue/ownership pilot, explaining readiness and the handoff problem. `A/output.md:17–26,41–44` separates retained behavior, prerequisite checks, and deferrals with reasons. `A/output.md:60–62` requires explicit review before expansion and handles mixed results. This answers the separate choices requested in `A/input/request.md:3–12`. |
| Constraints are enforced (`A/criteria.md:10–12`) | passed | `A/output.md:30–39` correctly totals queue plus measurement at 3.5 backend, 3 frontend, and 1.5 QA days against 6/4/2; the source estimates are `A/input/delivery-constraints.md:3–17`. Additional safeguards are conditional on remaining capacity, with a manual fallback if essential gaps cannot fit (`A/output.md:26,39`). Alternative feature totals are correct (`A/output.md:41–43`), and the answer invents neither provider approval nor additional engineering capacity. |
| Evidence drives the handoff (`A/criteria.md:13–16`) | passed | `A/output.md:7–11` connects readiness, 31 handoff cases, 17 ownership cases, and five of eight requests for visibility to the choice. It explicitly rejects interpreting 48 of 62 cases as preventable delays, distinguishes prototype-free interviews, and treats prospect interest as weaker than offered pilots. These distinctions preserve `A/input/evidence.md:3–20` and `A/input/stakeholder-notes.md:3–13`. No invented confidence or validation score appears. |
| Relevant guardrails are explicit (`A/criteria.md:17–19`) | passed | `A/output.md:15,20–26` preserves branch access and assignments, restricts claims, handles concurrency, requires named consenting enrollment, and gives customer success a disabling flag that preserves records. `A/output.md:11,41–44` defers multi-branch redesign, respects both provider and consent restrictions, and excludes unauthorized pricing/payment/enrichment. These implement the boundaries in `A/input/delivery-constraints.md:19–26` and respond proportionately to the uncertainty in `A/input/evidence.md:17–20`. |
| Learning is observable (`A/criteria.md:20–22`) | passed | `A/output.md:50–58` combines existing events and partner notes, specifies comparable desk-level pre/post periods, counts overdue incomplete cases, and includes ownership/access failures, failed updates, backlog, and support effort. It conditions comparison on recoverable baselines and avoids substituting the pooled 62/240 figure. `A/output.md:60–62` describes provisional review conditions rather than proven effects. This uses the available records/events in `A/input/evidence.md:6–10,22–25` and partner review access in `A/input/stakeholder-notes.md:3–4`. |
| Delivery is usable (`A/criteria.md:23–25`) | passed | `A/output.md:24–26,50,60–62` assigns enrollment/feedback to customer success, prerequisites to backend and QA, reporting to backend, and expansion review to the managing director. The bounded pilot, prerequisite checks, unresolved baseline/start-date issues, and reasoned deferrals support handoff. `A/output.md:44` excludes the unrelated campaign and its separate budget, consistent with `A/input/homepage-refresh.md:7–9`. |

Feasibility contradictions: none found. The extra recovery and concurrency details do not have separately established estimates, but the answer explicitly gates them on the stated remaining capacity and offers a fallback; it does not claim an unconditional delivery commitment.

Unsupported validation claims: none found. The answer expressly limits preventability, pilot outcomes, willingness to pay, and business validation.

Integrity: no unauthorized execution or edits are claimed in the answer. Actual tool-use compliance cannot be established from the permitted files alone.

## Answer B

**Overall: passed — all six mandatory criteria passed.**

Actual SHA256 of `B/output.md`:

```text
e43aaf841c45911ed236df7e2eeeced51f6c7dd6383248f812c93a726628ac01
```

| Criterion | Judgment | Evidence and explanation |
| --- | --- | --- |
| Scope and authority (`B/criteria.md:5`) | passed | `B/output.md:1,26–30,42–50` provides an assessment and one proposed test, explicitly stating that it is unexecuted and no outcomes exist. The activity details serve feasibility rather than becoming a product specification or broad research program. `B/output.md:14` excludes the room notice from evidence. This respects the requested scope in `B/input/request.md:5–7`; actual execution history remains outside this review. |
| Evidence provenance and denominators (`B/criteria.md:7`) | passed | `B/output.md:9–12` keeps five of eight volunteers, three of those five, nine incidents across five of twelve nights, six timed searches, and three untimed incidents distinct. It retains the poll denominator of 31, identifies self-selection/mixed roles and unknown views, avoids cross-tabulation, and acknowledges the two-person overlap rather than pooling samples. This preserves the evidence units in `B/input/field-notes.md:5,12,14`; the omitted 240-member group size and duration range do not distort the judgment. |
| Uncertainty and opportunity judgment (`B/criteria.md:9`) | passed | `B/output.md:9–24` distinguishes reported naming confusion from rushed-return explanations, recognizes that both can matter, and notes that logged incidents lack causal attribution. It selects wording comprehension because it is observable in the allowed tabletop slot while rushed returns are poorly reproduced there. This connects uncertainty directly to the learning objective, grounded in `B/input/field-notes.md:5–14` and `B/input/decision-and-capacity.md:3,9–11`. |
| One feasible, falsifiable next test (`B/criteria.md:11`) | passed | `B/output.md:28–40` proposes one offline interpretation comparison using the six retired props, copied shelf list, removable paper materials, two facilitators, existing opted-in adults, two preparation hours, and £20. Six two-minute task sets fit the proposed fifteen minutes with a limited transition allowance; the full allocation fits twenty minutes plus five-minute wrap-up. Consent, anonymous handwritten notes, production-stock separation, and rehearsal stopping constraints are explicit. `B/output.md:36,40,44–48` specifies comparison, order/task balancing, observable outcomes, disconfirming outcomes, and reduced-attendance/contamination handling. These fit `B/input/decision-and-capacity.md:7–11` without adding recruitment, software, or sessions. |
| No fabricated demand or commercial proof (`B/criteria.md:13`) | passed | `B/output.md:1,12–16,22,30,50` treats poll answers as stated interest, rejects Dev's universal price/delay claims, identifies untested purchase/maintenance assumptions, and labels outcomes as nonexistent. The proposed threshold is explicitly prospective (`B/output.md:44–48`), not a fabricated measurement. This preserves `B/input/decision-and-capacity.md:5,11` and the no-price/no-prototype evidence in `B/input/field-notes.md:12`. |
| Actionable, bounded answer (`B/criteria.md:15`) | passed | `B/output.md:1,20–24,44–50` provides a clear immediate choice, explains why this uncertainty is testable now, and connects improvement, ceiling performance, no improvement, or weak evidence to distinct next decisions. Fewer than two completed unfamiliar-participant comparisons or compromised evidence prevents a development commitment. Even favorable results justify only further local validation, with explicit limits on real searches, performance nights, adoption, and payment. This answers the one-afternoon/two-weekend decision in `B/input/decision-and-capacity.md:3,7,11` and `B/input/request.md:5`. |

Feasibility contradictions: none found. Individual turns and the two-hour preparation budget are tight but plausible for the permitted small paper exercise; the answer includes a buffer, an enforced stop, and incomplete-task reporting. Destination/task imbalance and answer-key ambiguity are appropriately classified as inconclusive rather than hidden.

Unsupported validation claims: none found. Success is limited to description comprehension in this exercise and does not purport to demonstrate demand, commercial viability, or real performance benefits.

Integrity: no unauthorized execution or edits are claimed in the answer. Actual tool-use compliance cannot be established from the permitted files alone.
