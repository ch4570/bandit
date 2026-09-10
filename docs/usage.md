# Use BANDIT

[한국어](usage.ko.md) · [Install](../INSTALL.md) · [Examples](../examples/README.md)

Install from your project folder, then start a new agent session if needed:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.4.0/bandit.tgz
```

The installer adds four specialist skills and the general `$bandit` skill. Use the command below for the task you need, then describe the desired result in your own words. For a combined request, use `$bandit` and let it choose the planning workflow.

**Upgrading from 0.2 or 0.3:** use the 0.4.0 command above in the same project, then start a new agent session. Preserve your previous `--global` or destination option when applicable. [Migration details](../INSTALL.md#upgrade-from-02-or-03).

BANDIT keeps its working voice direct and professional; you do not need cowboy prompts or roleplay. Include the existing plan or source material when you have it, the decision to make, and constraints that would change the answer. Specify whether you want a proposal, a read-only review, or edits to a named document.

## Research a problem or test an assumption · `$bandit-research`

```text
$bandit-research We have two competitor feature pages and no customer interviews.
Draft a one-page opportunity brief for a shared planning app. Separate
what the sources show from assumptions about adoption and payment.
Suggest the smallest next test that could change the build decision.
```

Expect sources tied to the claims they support, gaps that matter to the decision, and a test suited to the uncertainty. A free signup can support an interest claim; it does not establish willingness to pay. Missing research does not become an invented interview or a fabricated market estimate.

If live research tools are unavailable, the agent can assess supplied sources and prepare an investigation plan. It should state which facts remain unchecked. Proposed thresholds are decision criteria, not observed results.

[Skill instructions](../skills/bandit-research/SKILL.md).

## Choose a useful MVP · `$bandit-scope`

```text
$bandit-scope This plan has eleven P0 requirements. We have one developer
and two weeks for a paid pilot. Keep the complete change-request approval
journey, explain manual alternatives, and recommend what to defer.
```

Expect a first use case that can be completed, a reason for each meaningful trade-off, and explicit effort assumptions. A rule such as “only five P0s” is not a substitute for preserving the conditions that make approval valid. Authorization, version identity, and duplicate effects may be conditions of one capability rather than separate features to cut.

[Skill instructions](../skills/bandit-scope/SKILL.md).

## Create or rewrite a spec · `$bandit-specify`

```text
$bandit-specify Turn these voting rules into a development handoff. There are
five participants, two votes for each option, and one missing response.
Explain who can change a response, when the coordinator can finalize,
and what must be preserved if the decision is reopened.
```

Expect concrete actors, objects, conditions, state changes, exceptions, and acceptance scenarios. The agent should identify missing decisions, propose reasonable draft choices where delegated, and distinguish those proposals from accepted policy. A generic record CRUD list cannot define the meaning of a vote or an approval.

The handoff can describe the minimum data relationships needed to explain behavior. It does not need to choose a database, invent APIs, or rewrite the application's architecture.

Use the same command when an existing spec needs a new direction:

```text
$bandit-specify Rewrite docs/PRD.md for a free shared workspace instead
of our paid solo plan. Reorganize the sections and replace rules that no
longer fit. Make permissions, onboarding, metrics, and acceptance criteria
agree. Keep old pilot results with their original price and conditions.
```

Expect a coherent revised specification, including any needed restructuring and rule changes. The requested scope determines how much to rewrite. Follow changed requirements into related metrics, experiments, and checks; preserve unrelated accepted decisions and the meaning of historical results. A new direction does not retroactively validate itself with an old pilot.

[Skill instructions](../skills/bandit-specify/SKILL.md).

## Review without rewriting · `$bandit-review`

```text
$bandit-review Review only the renewal experiment in docs/PRD.md. Five
subscribers say they will continue, but nobody has reached the next
billing date. Preserve the original success criterion. Do not edit files.
```

Expect a scoped assessment with the scenario, expected rule, available evidence, consequence, and a proposed correction. The agent should acknowledge rules already present. Intention to renew and a successful renewal payment are different events; a cohort that has not reached its observation date is still unmeasured.

Reviewing a PRD does not exercise the product. Source inspection, a screenshot, a local demonstration, a passing test, and customer outcomes support different claims.

[Skill instructions](../skills/bandit-review/SKILL.md).

## Upcoming: connect research, planning, marketing, design, and BM

**Unreleased branch guidance.** The v0.4.0 command at the top installs the published release; it does not include the new [product journey guidance](../skills/bandit/references/product-journey.md) described in this section. The command set remains the same five skills.

For a combined request, `$bandit` connects research → product planning → marketing → product design handoff → business model (BM), then checks that the artifacts describe the same offer. This is not a fixed sequence for every request. Start with provisional price and delivery limits so marketing and design reflect a feasible offer; later findings can reopen affected scope, copy, flows, and checks.

The following examples are synthetic. Replace their idea, constraints, and document paths with your own sources.

```text
$bandit Use the supplied sources to assess a scope-change approval service
for freelancers. Recommend a two-week MVP for one developer, then connect
a marketing brief, a product flow/content and text-wireframe brief, and
a business model with explicit price, cost, and delivery-capacity assumptions.
Keep the audience, promise, and offer terms consistent. Label proposed
choices and unverified claims, and suggest the next useful test.
```

Expect linked deliverables at the requested depth:

| Work | Useful handoff |
| --- | --- |
| Research | Evidence about the customer, alternatives, and offer, with sources, conditions, and unresolved assumptions |
| Product planning | A complete first outcome, included/deferred scope, delivery limits, and acceptance scenarios |
| Marketing | Positioning, headline/supporting copy, a call to action, and a channel test with an audience, owner, time window, capacity, spending limit, and decision criteria |
| Product design | Task flow, screen/content order or text wireframes, visible offer terms, relevant states and recovery, accessibility needs, and a proposed prototype check |
| Business model | Customer and payer, charging unit, delivery activities/resources, price and cost assumptions, contribution and capacity calculations, and a next test |

Keep the customer, promise, eligibility, price/unit, delivery timing, capacity, and cancellation terms consistent. Compare the business model's break-even needs with both reachable demand and delivery capacity. Calculations based on assumptions remain estimates; a coherent plan does not establish paid demand. A product design brief describes what to prototype and check; it is not a rendered or tested interface.

For consequential derived budgets, fees, capacity, or economic figures, expect a
calculation check with an available tool and a compact note of the method and
returned result. Showing a formula alone does not demonstrate execution. If a
calculation is prohibited, skipped, or unavailable, verification stays incomplete.
An explicit no-code request includes arithmetic code; it does not mean only
product code. Use a permitted non-code calculator or disclose the unverified check.
Quoting a source number or answering a qualitative question does not require
artificial arithmetic.

For time-bounded offers, distinguish sales and billing dates from actual service,
support, resource availability, and observation periods. Check the last accepted
customer's full interaction chain, including time to review a result and use
any included follow-up. Work backwards from staffed completion, then check that
the latest eligible customer can perform each step in order, including allowed
late inputs and stated customer availability. Check capacity within the remaining
response windows and batched starts. Confirm additional resources before
committing to uncovered service, or adjust affected terms. A short preparation window
does not prohibit longer delivery when its resources are already confirmed.

Use a specialist directly when you need only one part.

Evidence for an offer decision:

```text
$bandit-research Assess the supplied customer notes and competitor pages for
this freelancer approval service. Which audience, promise, channel, and
price assumptions do they support? Keep source dates and offer conditions,
separate interest from payment, and propose one test of the largest unknown.
Return an evidence brief only.
```

A UX and commercial brief from an existing plan:

```text
$bandit-specify Use docs/PRD.md to draft a UX and commercial handoff for the
paid pilot. Include positioning copy and a channel test, entry-to-approval
flows, screen/content order and text wireframes, price and cancellation
terms at commitment, and relevant failure/recovery states. Connect payer,
delivery work, costs, and capacity in the business model. Label draft choices
and give acceptance scenarios; write the handoff in docs/PRD.md.
```

Consistency across the same offer:

```text
$bandit-review Review docs/PRD.md, docs/marketing.md, docs/design-brief.md,
and docs/business-model.md for conflicting audience, promise, eligibility,
price/unit, delivery limits, or cancellation terms. Trace one customer from
the message through use, delivery, and payment, plus one recovery case.
Recheck decision-changing calculations and cite each conflict's location,
consequence, and correction. Leave the documents unchanged.
```

`$bandit-scope` remains the command for choosing or cutting delivery scope. No marketing, design, or BM command is added. A proposal does not authorize publishing copy, contacting customers, spending money, implementing screens, or running an experiment. Use separately authorized work for those actions.

## Keep the output proportionate

Start with the named specialist; research, scope, specify, and review are not a
required sequence. BANDIT uses the request's inputs, deliverable, completion
checks, and any time or search limits without asking you to fill in another form.
You can bound the work in ordinary language:

```text
$bandit-review Check only permissions, duplicate requests, and failure recovery
in docs/PRD.md and docs/approval-policy.md. Do not edit them. Follow links needed
to resolve each finding, then report its location, trigger, impact, and correction.
Separate unanswered questions that could change the conclusion.
```

Selected instructions are read fully; unrelated references are not preloaded.
Once the requested checks are complete, unresolved details that cannot change
the decision do not require more exploration. A changed request, material
conflict, stale source, or failed check reopens the affected scope. Necessary
permission, recovery, and evidence checks still apply. At a stated limit, expect
confirmed results and remaining work, not a claim that everything is done.
Time and search limits in a prompt are not provider billing caps.

For a short decision, a paragraph or small table may be enough. For an ongoing plan, keep important evidence, decisions, requirements, and checks connected in the existing artifact. IDs and the optional plan template are useful when they improve traceability; they are not prerequisites for using the skill.

Distinguish accepted goals from descriptions recovered from code. If the PRD says only the owner may edit and the code allows every signed-in user, report the mismatch. Do not redefine the goal to make the implementation appear correct.

## Hand off to implementation or UI work

Give the next contributor the user role, main task, accepted and proposed decisions, state conditions, failure/recovery expectations, persistence boundary, and acceptance scenarios. UI work can then refine layout, interaction feedback, and wording around those rules.

BANDIT does not require a UI skill, Figma, an issue tracker, or an external account. A planning request does not authorize code changes, contacting customers, posting tickets, or deploying an application. Use the host's existing permissions for any separately requested action.

[Design](design.md) explains the shared rules. [Evaluation](../evals/README.md) describes how to assess actual outputs; [Validation](../VALIDATION.md) lists checks that have been run.
