# Changelog

## 0.2.0 — BANDIT

PM Craft becomes **BANDIT (밴딧)**, a western raccoon planning partner with a cowboy hat, red bandana, pencil, and map.

- Install from a project with one npx command using a versioned GitHub release archive. Node.js 22+ and npm are sufficient; Git and Python are unnecessary for that route.
- Add the dependency-free `bandit` CLI, with the current project as its default destination, personal Codex installation, custom paths, previews, and optional JSON output.
- Package the complete `bandit` skill as `@ch4570/bandit`. Distribute the npm archive through GitHub releases; npm registry publication remains deferred.
- Rename the skill invocation to `$bandit` and add original character artwork, a brand guide, and English and Korean onboarding.
- Use version-specific archive URLs so a new release can replace a previously cached npx package.
- Preserve managed-file conflict checks and leave an existing sibling `pm-craft` installation intact.
- Retain the five planning modes and the historical PM Craft 0.1.0 evaluation records under their original identity.

[Validation](VALIDATION.md) records checks actually completed for this release. Historical evaluation results are not presented as new BANDIT benchmark results.

## 0.1.0 — PM Craft

Initial distribution of PM Craft.

- One installable product-planning skill with research, decide, spec, review, and update modes.
- Shared guidance for evidence, accepted decisions, requirements, changes, and observed checks.
- An optional plan template and fictional examples for development handoffs.
- English and Korean introduction and usage guides.
- A project installer with preview, exact destinations, managed-file updates, and conflict protection.
- Repository validation, installer tests, a release ZIP builder, and a documented evaluation workflow.

See [the original evaluation record](evals/results/2026-09-07/README.md) for behavior evidence. This release did not establish a measured advantage over another PM workflow.
