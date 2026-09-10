---
name: bandit-review
description: Review existing product plans and PRDs for consequential gaps, conflicting rules, unsupported claims, and verification limits, including consistency across marketing promises, design flows, and business model assumptions. Use for scoped planning critique and proposed corrections; leaves the reviewed artifacts unchanged and excludes standalone UI or code-quality audits.
---

# BANDIT Review

Review the requested planning artifact directly using
[review guidance](references/review.md) and shared
[work boundaries](references/work-boundaries.md). Read the relevant source sections and
linked domain decisions before reporting an omission. This skill does not
require the general BANDIT router or a new discovery workshop.

Keep the reviewed documents and product code unchanged. Return findings in the
conversation, or in a separate review document if requested. Focus on issues
that could change what gets built or cause a wrong product decision; do not
invent missing rules, a fixed finding count, or a mandatory redesign.

Distinguish intended requirements, claims recovered from code, observed runtime
behavior, and actual customer evidence. Reading a PRD does not exercise the
product, and agreement with a PRD derived from the same code is not independent
proof of fidelity. For a durable review or handoff, also apply
[evidence and decision guidance](references/evidence-and-decisions.md).
When the review spans marketing, design, pricing, or business viability, apply
the relevant [product journey guidance](references/product-journey.md) and trace
the same offer from its public promise through use, fulfillment, and payment.

Give the source location, concrete scenario, consequence, and correction for
each material finding. State what was inspected, what remains unavailable,
and the next useful check. Use the user's language and professional prose;
keep BANDIT's western character light in introductions unless requested.
