# Overnight development, round 14 — 2026-09-09

Engineering-only handoff of the overnight work. There are **no new native
planning executions**; the cumulative count remains 48, not passing answers.
No skill, installer, runner, test or existing rubric changes in this round.

The [Korean handoff](../../../docs/overnight-handoff.md) groups the substantive
skill, installer, evaluation-tool and onboarding changes, links actual artifacts,
and puts unresolved failures and evidence limitations beside them. It is a
review aid, not another benchmark or a claim that all observed defects are fixed.
The evaluation index's stale rubric range is corrected from 07–20 to 07–22;
no rubric text or grade changes.

## Exact candidate installation

The [fresh local integration](checks/integration-audit.md) checks the exact
round-13 candidate rather than assuming the older round-9 package covers the
later installer change. Its immutable input has SHA-256
`7f8592028d1b2f350dd304526e57a550c4b133a0f93d5b971d2a133d67bb5f84`.
The [before-run receipt](checks/before-run.json) freezes the candidate, retained
authentic 0.3 archive and relevant repository sources before the new harness.

The first attempt passes six synthetic project fixtures: default preview/install/
repeat, lowercase and mixed-case custom core names, a genuine legacy sibling,
clean 0.3 migration, and customized retired-skill refusal. Of 19 commands, 17 exit
0 and two expected conflict preview/install commands exit 2. Complete project
inventories check exact payloads and ownership maps; rejected upgrades preserve
all 69 recorded paths including the root. Real sibling notes and unrelated old
notes remain, while custom cores no longer receive the misleading legacy notice.
No unexpected failure or corrected harness attempt occurs here.

This local check uses explicitly selected tarballs and offline npm, not a new
public URL or API check. The earlier [public-command result](../2026-09-09-overnight-round9/README.md)
remains separate. Both the public package and local candidate retain a 0.4.0
version string; identical version labels do not mean identical payloads.

## Review and verification

Independent read-only audits check evidence claims and skill changes separately
from onboarding and release boundaries. They are nonblind maintenance reviews,
not fresh semantic grading. The onboarding review catches two overstatements in
the handoff draft: not all linked examples include a baseline output, and the
baseline is a no-PM-instruction condition, not a verified different/base model.
Both are corrected before final packaging. The evidence audit verifies complete
standalone reference copies, all five skills among the 48 distinct native
threads, preserved historical files and the disclosed incomplete results. Its
scope clarification replaces ambiguous web “experiment” wording with explicitly
authorized public-source research; no runtime permission is expanded.

The final [engineering receipt](checks/README.md) records the required local
gates and packaging separately from installation behavior. Source ZIP verification
compares the current tree, archive inventories, linked documents, all 1,517
prior result files, 34 skill files, 93 existing raw/rubric/sequence files and
93 historical PM Craft files. No previous failure or partial is overwritten.

The work stays local and uncommitted for user review. There is no new version,
public release, registry publication, CI change or host-discovery claim.
