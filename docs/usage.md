# Use BANDIT

[한국어](usage.ko.md) · [Install](../INSTALL.md) · [Examples](../examples/README.md)

Install from your project folder, then start a new agent session if needed:

```sh
npx --yes https://github.com/ch4570/bandit/releases/download/v0.2.0/bandit.tgz
```

Ask for the product result you need. You do not need to name a mode, choose a framework, or complete an interview before receiving a useful draft.

BANDIT keeps its working voice direct and professional; you do not need cowboy prompts or roleplay. Include the existing plan or source material when you have it, the decision to make, and constraints that would change the answer. Specify whether you want a proposal, a read-only review, or edits to a named document.

## Research a problem or test an assumption

```text
$bandit We have two competitor feature pages and no customer interviews.
Draft a one-page opportunity brief for a shared planning app. Separate
what the sources show from assumptions about adoption and payment.
Suggest the smallest next test that could change the build decision.
```

Expect sources tied to the claims they support, gaps that matter to the decision, and a test suited to the uncertainty. A free signup can support an interest claim; it does not establish willingness to pay. Missing research does not become an invented interview or a fabricated market estimate.

If live research tools are unavailable, the agent can assess supplied sources and prepare an investigation plan. It should state which facts remain unchecked. Proposed thresholds are decision criteria, not observed results.

## Choose a useful MVP

```text
$bandit This plan has eleven P0 requirements. We have one developer
and two weeks for a paid pilot. Keep the complete change-request approval
journey, explain manual alternatives, and recommend what to defer.
```

Expect a first use case that can be completed, a reason for each meaningful trade-off, and explicit effort assumptions. A rule such as “only five P0s” is not a substitute for preserving the conditions that make approval valid. Authorization, version identity, and duplicate effects may be conditions of one capability rather than separate features to cut.

## Write a spec with product meaning

```text
$bandit Turn these voting rules into a development handoff. There are
five participants, two votes for each option, and one missing response.
Explain who can change a response, when the coordinator can finalize,
and what must be preserved if the decision is reopened.
```

Expect concrete actors, objects, conditions, state changes, exceptions, and acceptance scenarios. The agent should identify missing decisions, propose reasonable draft choices where delegated, and distinguish those proposals from accepted policy. A generic record CRUD list cannot define the meaning of a vote or an approval.

The handoff can describe the minimum data relationships needed to explain behavior. It does not need to choose a database, invent APIs, or rewrite the application's architecture.

## Review without rewriting

```text
$bandit Review only the renewal experiment in docs/PRD.md. Five
subscribers say they will continue, but nobody has reached the next
billing date. Preserve the original success criterion. Do not edit files.
```

Expect a scoped assessment with the scenario, expected rule, available evidence, consequence, and a proposed correction. The agent should acknowledge rules already present. Intention to renew and a successful renewal payment are different events; a cohort that has not reached its observation date is still unmeasured.

Reviewing a PRD does not exercise the product. Source inspection, a screenshot, a local demonstration, a passing test, and customer outcomes support different claims.

## Update a decision and its consequences

```text
$bandit Update our existing plan for a free shared workspace instead
of a paid solo plan. Trace changes to permissions, costs, onboarding,
metrics, and the next experiment. Preserve the old pilot results with
their original price and product conditions.
```

Expect a bounded change that follows the affected decisions through the plan. Existing evidence remains attached to the conditions under which it was collected. A new price and new sharing feature do not retroactively explain the old pilot's results or isolate the causal effect of price.

If different documents own product scope, transaction rules, and business assumptions, keep those responsibilities and update the relevant references. A new master document is not required.

## Keep the output proportionate

For a short decision, a paragraph or small table may be enough. For an ongoing plan, keep important evidence, decisions, requirements, and checks connected in the existing artifact. IDs and the optional plan template are useful when they improve traceability; they are not prerequisites for using the skill.

Distinguish accepted goals from descriptions recovered from code. If the PRD says only the owner may edit and the code allows every signed-in user, report the mismatch. Do not redefine the goal to make the implementation appear correct.

## Hand off to implementation or UI work

Give the next contributor the user role, main task, accepted and proposed decisions, state conditions, failure/recovery expectations, persistence boundary, and acceptance scenarios. UI work can then refine layout, interaction feedback, and wording around those rules.

BANDIT does not require a UI skill, Figma, an issue tracker, or an external account. A planning request does not authorize code changes, contacting customers, posting tickets, or deploying an application. Use the host's existing permissions for any separately requested action.

[Design](design.md) explains the shared rules. [Evaluation](../evals/README.md) describes how to assess actual outputs; [Validation](../VALIDATION.md) lists checks that have been run.
