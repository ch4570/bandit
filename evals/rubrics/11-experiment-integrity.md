# Experiment integrity development check

Written before the first recorded run. Synthetic, author-designed diagnostic
case; not a held-out benchmark, population-level reliability estimate, or
statistical method validation. Grade the meaning of the full output with
source/output locators. The task agent receives only the request, raw fixtures,
and instruction snapshot, never this rubric or an author's interpretation.
Preserve all outputs, failures, and unexpected findings before changing criteria.

## 11 — Experiment integrity

1. Uses the actual assignment and outcome units. The assignment intervals sum
   to 1,000 accounts per arm. Backend observed purchases are A 95/1,000 = 9.5%
   and B 93/1,000 = 9.3% during the current window. These are partial follow-up
   observations, not final seven-day conversion rates or evidence that B is
   statistically worse. No account has completed seven full observation days.
2. Explains why the dashboard's apparent doubling does not establish purchase
   lift. B's 124 delivery rows contain 93 distinct event/order/account IDs, with
   31 deliveries beyond the distinct-event count. Browser exposures are 950
   versus 620 and use different render triggers. Deduplicating to 93/620 = 15%
   does not turn that selected exposure comparison into the adopted outcome.
   Does not equate exposure imbalance with demonstrated assignment failure:
   recorded assignment is balanced and backend outcomes cover both full arms.
3. Interprets time and monitoring without invented certainty. The snapshot is
   three days after enrollment began; enrollment is planned for 14 days and the
   final review follows seven further days. Hourly dashboard viewing and choosing
   the first apparent doubling supply no planned early efficacy boundary.
   Exact confidence intervals or p-values are not required. Neither apparent
   doubling nor the small opposite backend difference justifies a winner claim.
4. Applies the predeclared operational guardrail using accounts, not tickets:
   A 8/1,000 = 0.8%; B 39/1,000 = 3.9%. B has exceeded 1.0% after reaching 500
   assignments. Recommends pausing new B assignments under the adopted rule,
   with the documented route to A for current participants and recording any
   resulting crossover. Merely continuing B unchanged until a larger sample
   arrives fails this condition. No claim of statistically proven harm is needed
   to apply the operating rule.
5. Gives one useful immediate recommendation and one economical next check tied
   to the decision, such as inspecting B checkout/support traces before deciding
   whether it can resume. Does not treat all supplied backend observations as
   worthless, fabricate missing participant histories or a fix, change experiment
   settings, run product tests, browse, or edit files. Stays within 500 words and
   attributes supplied synthetic observations without claiming live validation.

## Source-based rationale

`skills/bandit/references/research.md` asks for assignment/exposure integrity,
observation windows, denominators, repeated peeking, and intended guardrails
before relying on an experiment's lift claim. Existing cases cover a combined
offer change and immature cohorts; this case adds random assignment with
unequal exposure recording, duplicate client deliveries, and an adopted stop
rule that can drive a decision before efficacy is established. Structural
checks do not establish whether the skill performs this reasoning correctly.
