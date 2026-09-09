# Overnight development, round 5 — 2026-09-09

This round corrects a reproduced installer cleanup defect and a nondefault
installation-path ambiguity, and adds two fresh scope-planning checks. These
are separate engineering, onboarding, and behavioral findings; passing one
does not establish the others. The broader overnight effort continues locally.

## Installer lock ownership

The [failing-before receipt](checks/lock-cleanup-regressions.md) records three
fault-injected failures in both installers. A changed parent could redirect
final cleanup into seven unrelated lock files; another empty file at an old
lock pathname could be deleted; one missing lock could strand the other six.
Normal path checks already rejected the changed parent, but cleanup did not
respect that rejection. This defect existed before the earlier overnight
exact-byte update protections; it was not introduced by those changes.

The fix records the newly created lock's filesystem identity and metadata from
its open descriptor. Cleanup rechecks safe ancestry, regular-file type, and
that recorded identity before unlinking, and handles each lock independently.
The [after-fix record](checks/lock-cleanup-after.md) preserves the version-matched
comparison, frozen test hashes, and additional diagnostics. The same three
Node regressions fail on the retained pre-fix source under Node 22 and pass
afterward; all three Python regressions pass after their before-state failures.

Changed or unverifiable locks may intentionally remain for inspection. This is
not an atomic compare-and-unlink primitive, protection against every hostile
filesystem race, or crash-durable recovery. The final check-to-unlink interval
remains. All reproductions use disposable synthetic files, not reported user
incidents or live installations.

## Discover the file actually installed

The [route smoke](checks/discovery-paths.md) confirms that the current-project
fallback path is absent in the tested global, other-repository, and custom
installations. Their actual printed roots contain both specialist entrypoints.
`README.md`, `README.ko.md`, and `INSTALL.md` now distinguish the default-project
example from those destinations. The public command still pins release 0.4.0;
no host configuration, discovery policy, or skill metadata changed.

## Scope-planning results

Case 18 asks, in English, how to allocate one engineering week between inventory
import review and a useful reporting alternative. Account-level rows distinguish
retry events, stored data, usable customer outcomes, manual rescue, and founder
effort. The existing paid reporting obligation competes for the same limited
founder time. Unlike the earlier cohort comparison, there are no immature
windows, missing outcomes, price changes, or aggregate-only joins.

| Arm | Fixed criteria | Complete output / cap |
| --- | --- | ---: |
| Standalone `$bandit-scope` | 5/5 pass | [534 / 600 words](pre/18-onboarding-investment--bandit-scope/output.md) |
| Baseline, same raw inputs | 5/5 pass | [514 / 600 words](pre/18-onboarding-investment--baseline/output.md) |

Both distinguish nine usable outcomes among sixteen shops from stored events
and five rescued successes. Both choose reporting, protect the existing service
obligation, limit trial admissions, and treat savings as unobserved. Neither
choice was predetermined by the [rubric](../../rubrics/18-onboarding-investment.md).
[Independent grades](grades.md) record criterion-level locators and limitations.
These results do not justify a further instruction change or a skill-advantage
claim; all five skills remain byte-identical to the start of this round.

The [pre-run receipt](case18-before-run.json) and
[execution summary](run-summary.json) retain the raw/rubric/instruction hashes
and observed scope. Fresh task agents received only raw inputs and their assigned
instructions, not grading materials or author diagnoses. Both ran with web
disabled and unchanged read-only inputs; no product tests, outreach, or trials
were executed. The baseline's recovered missing-instruction-directory listing
error remains in its trace. Host defaults are unpinned and timestamps unsigned.
This synthetic, author-designed pair is not a held-out benchmark, reliability
estimate, causal improvement result, or real customer evidence. Earlier failures
and partial grades remain intact.

## Engineering checkpoint

Resource synchronization, Node/Python repository validators, and all five
official skill metadata checks pass. Full suites pass **76 Node tests on
Node 22.23.2** and **90 Python tests on Python 3.11.16**, including package
consumption and the six new lock-cleanup regressions. These counts are not
planning-quality scores. The older system Python was not used; temporary
development tooling adds no end-user dependency.

`npm pack` and source ZIP creation pass separately from these behavioral
findings. This round uses `dist/overnight-round5/` for its final local artifacts,
preserving earlier same-version builds. No commit, new CI run, public release,
or registry publication occurred. Previous artifacts and historical PM Craft
evidence are preserved.
