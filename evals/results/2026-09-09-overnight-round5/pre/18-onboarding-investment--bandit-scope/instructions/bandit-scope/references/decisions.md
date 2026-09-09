# Decide scope and priorities

Name the decision, deadline, available capacity, and constraints already chosen
by the user. Use existing evidence before gathering more. Recommend a reversible
choice when delegated, making its assumptions and tradeoffs visible.

## Choose a complete value path

Define the actor's starting situation and the outcome worth returning for. Keep
the smallest connected journey that produces that outcome under ordinary use.
Include a dependency, state, permission, or recovery behavior when omitting it
would make that journey fail or mislead the user about the result.

Cut optional breadth before breaking the core path. A two-week MVP may omit
multiple integrations or automatic reminders while retaining unambiguous
ownership, saved state, and correction of a consequential input. Decide these
from the domain; neither a fixed feature count nor a generic CRUD checklist
determines the MVP.

Compare a few plausible alternatives, including a manual/prototype alternative
when it could answer the business question sooner. Explain what is kept,
deferred, and excluded; why; the dependency; and what would reopen the choice.
Separate a required constraint from a preference you are recommending.

## Use estimates at their supported resolution

Estimate in comparable units and expose unknowns. If engineering capacity is
unknown, give a provisional scope with assumptions or a range; do not promise a
delivery date as validated. Identify the riskiest dependency and a way to reduce
uncertainty without demanding exhaustive estimation.

Use a score only if it clarifies a choice. Before calculating RICE or another
formula, check:

- Reach has the same population basis and time period for each option.
- Impact uses a defined shared scale and refers to a relevant outcome.
- Confidence has an interpretable common scale tied to evidence. A 1–10 opinion
  is not a probability; normalize only when its meaning supports that mapping.
- Effort is positive, covers comparable scope, and uses the same unit.
- Required inputs exist; unknown is not automatically zero, one, or the average.

For RICE, `reach × impact × confidence / effort` can be used with confidence as
a 0–1 fraction **after** those checks. Keep formulas, inputs, and rounding visible.
If inputs are incompatible, explain the missing conversion and compare
qualitatively or present labeled scenarios. Do not silently calculate an invalid
ranking. Test whether plausible input ranges reverse the priority.

For assumptions, compare consequence of being wrong with strength of evidence
and test cost. An unsupported certainty score should not become a probability
in `(1 − confidence)`. A quadrant or high score is a prompt for judgment, not
automatic authority to ship, discard, or fund a feature.

## Leave an actionable decision

Lead with the choice and whether it is a recommendation or an adopted user
decision. Include the strongest alternative, the meaningful tradeoff, material
assumptions, and a practical trigger for revisiting the choice. Connect selected
scope to an acceptance outcome or next experiment so the decision can be used.

Match scale to the request: a three-sentence recommendation can be enough for
a narrow choice; a delivery handoff needs a clear boundary and dependencies.
Do not add a mandatory strategy workshop, full roadmap, or new approval gate.
