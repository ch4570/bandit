# Overnight development, round 3 — 2026-09-09

This round revisits an incomplete historical diagnostic and adds actual public
source research. Eleven fresh task runs preserve two length failures, repeated
denominator omissions, and a manual-test delivery-budget gap. The final
specification fits its cap; the final research answer chooses a bounded
interview/conditional-offer test. Neither result establishes reliable repair or
causal improvement from the instruction changes.

These are synthetic, author-designed development checks, not a held-out
benchmark, a new upstream comparison, or evidence of customer demand. The
broader overnight effort continues; this records one completed local round.

## Changes grounded in observed outputs

- Case 02's original skill output has 994 words against a 900-word request.
  The first specification-reference correction asks for a shared budget across
  current rules, historical evidence and checks. Its fresh output still has
  962 words: that attempt **failed** and remains archived.
- The second correction asks for counting the complete draft when a counting
  tool is available, revising to fit, and delivering that same text. Without a
  tool it asks for headroom, not a claimed exact count. The new case 02 output
  has 887 words. No actual final-output counting command appears in the task
  traces; cap compliance does not prove the counting mechanism was followed.
- All four case 02 runs retain a partial on the unchanged denominator
  criterion. The skill outputs correctly give the opportunity-conditioned
  repeat rate and avoid a causal price claim, but omit two broader descriptive
  repeat fractions. The baseline also omits one. We did not add a universal
  requirement to list every possible denominator or weaken the rubric.
- The first live-source answer proposes a two-week manual service but caps
  only recruitment and preparation. Research guidance now conditionally asks
  manual/concierge tests to budget delivery work and a reduction/stop branch.
  The final answer chooses a different test, so it does **not** demonstrate
  successful use of a manual-delivery budget.
- Only the canonical references under `skills/bandit/` were edited and then
  synchronized. Entry points remain short; no new skill or user command was
  introduced. These are unreleased instruction changes.

## Fresh task results

`pre` uses round 2's final skills, not the original repository commit. `post`
adds the first word-budget paragraph; `post-2` replaces it with the complete
draft/count instruction; `post-3` also adds the manual-delivery research rule.
Each specialist runs with only its own complete folder. General runs use only
the general snapshot. [Run summary](run-summary.json) records distinct source
epochs and artifact hashes; [independent grades](grades.md) provide locators.

| Run | Meaning-based result | Words / request cap |
| --- | --- | ---: |
| [Pre 02 specify](pre/02-offer-change--bandit-specify/output.md) | 3 pass, denominator criterion partial | **994 / 900 — fail** |
| [Pre 02 baseline](pre/02-offer-change--baseline/output.md) | 3 pass, denominator criterion partial | 753 / 900 |
| [Pre 14 research](pre/14-live-source-research--bandit-research/output.md) | 3 pass; source coverage partial; delivery budget partial | 501 / 650 |
| [Post 02 specify](post/02-offer-change--bandit-specify/output.md) | 3 pass, denominator criterion partial | **962 / 900 — fail** |
| [Post 10 specify](post/10-reschedule-handoff--bandit-specify/output.md) | 4/4 pass | 622 / 700 |
| [Post 13 general](post/13-combined-issue-handoff--bandit/output.md) | 5/5 pass | 500 / 600 |
| [Post 03 review](post/03-intent-review--bandit-review/output.md) | 4/4 pass | 283 / 600 |
| [Post-2 02 specify](post-2/02-offer-change--bandit-specify/output.md) | 3 pass, denominator criterion partial | 887 / 900 |
| [Post-2 10 specify](post-2/10-reschedule-handoff--bandit-specify/output.md) | 4/4 pass | 684 / 700 |
| [Post-2 13 general](post-2/13-combined-issue-handoff--bandit/output.md) | 5/5 pass | 510 / 600 |
| [Post-3 14 research](post-3/14-live-source-research--bandit-research/output.md) | 4 pass; source coverage partial | 480 / 650 |

Word counts use the complete final `output.md`, split on whitespace and
including Markdown tokens. An exit code of zero is not a quality grade.
The cap-compliant baseline remains visible; this round establishes no skill
advantage. The two failed caps and persistent partials are not erased by later
outputs. Repeated handoff/general checks found no additional rubric-level
regression in these single runs. Review correctly separates adopted policy
from a newer unadopted code-derived document and from unexecuted tests.

Task agents saw only raw fixtures, their request, and the applicable skill
snapshot, plus authorized public sources for case 14. They received no rubric,
author diagnosis, expected answer or prior output. A separate grader received
the artifacts and rubrics; grading was not blinded to condition names. Rubrics
were not revised after observing these outputs. Cases 02/03 have a verified
starting-commit anchor and case 13 has a previous-round digest. Cases 10/14 lack
a separately retained earlier digest: current hashes are recorded, but
cryptographic before/after rubric identity is **not verified** for those two.

## Public-source research and provenance

Case 14's synthetic brief authorizes official-source reading of Geekbot and
Dailybot only. It asks whether a 12-person internal workflow fits a monthly
budget before allocating two developer-weeks to a new product. The 18-member
Slack workspace, one billing manager, unmeasured founder time and untested
price hypothesis create distinct billing and evidence populations.

Both outputs cite official pages, distinguish monthly payment from annual
prepayment, expose conflicting vendor documentation and keep demand unproven.
Later independent source checks corroborated the consequential pricing,
population and feature claims. No installed behavior, checkout, invoice,
payment, customer interview or retention was observed. Proposed tests were
not executed. The final test asks for written conditional commitments and
explicitly does not count those as payment or retention.

The two traces contain **five and seven completed web-activity records**,
respectively. They omit returned page bodies and some batched-open targets.
Thus contemporaneous retrieval of every cited detail is not proven. Both
source-use criteria retain a **partial coverage** grade, separate from the
first answer's actual delivery-budget omission. This logging limitation alone
is not a fabricated-citation or unsupported-fact finding. Timestamped later
source receipts in [grades](grades.md) are corroboration, not exact replay of
the pages seen by the task agent. Live sources are not frozen fixtures.

The optional evaluation runner now exposes `--web-search live` with explicit
public-reading scope and configures `disabled` by default. It records UTC
start/finish times without broadening the sandbox or file-edit permissions.
The setting follows the
[official CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli).
Earlier runner versions only instructed no browsing and left tool defaults to
the host; the first case 02 skill run here still has that older configuration.
No web calls appear in the other case traces. New mock tests check both modes,
default behavior, metadata, failure retention and rejected invalid modes.

## Integrity and engineering checks

All eleven runs used `codex-cli 0.153.4`, `--ignore-user-config`, `--ephemeral`,
host model defaults without a pinned override, and a read-only sandbox. All
finished with exit 0 and unchanged raw inputs/instructions. All retained
archive hashes and original source records were independently verified.
General archives retain mascot PNG hashes rather than the image bytes; their
original bytes were also checked. This is not a full binary snapshot.

The two live runs use identical raw local fixtures but cannot control mutable
web pages or host services. Other repeated conditions also use unpinned model
defaults. These single runs cannot establish reliability or causality. The
original PM Craft 0.1.0 evidence and hashes remain untouched.

Resource synchronization, both repository validators, all five official
skill-creator metadata checks, **73 Node tests** on Node 22.23.2 and **87 Python
tests** on Python 3.11.16 passed locally. The system Python 3.9.6 is unsupported;
the optional tests use the existing Python 3.11 installation. The Node command
removes the previously diagnosed inherited `npm_config_call` option before
running nested npm tests. No new cross-platform CI ran.

The [engineering record](checks/README.md) preserves failing-before regression
checks for missing launch/probe error evidence and recursive source/output
copy routes, including nested links. The fixed runner records explicit errors
with null task exit codes and rejects those copy paths before staging. An
actual deliberately missing executable was archived successfully as a failed
runner attempt, not a model response or a twelfth planning run. These
preflight checks are not locks against concurrent filesystem mutation or
protection against every disk/finalization failure.

Case 15 is prepared for a later manual-delivery transfer check, with a separate
[pre-run digest receipt](../2026-09-09-overnight-round4/pre-run-manifest.json).
It has not run at this checkpoint and is not part of the eleven results.

`npm pack` and source ZIP creation pass, separately from behavior. Existing
round 1/2 artifacts are preserved, and the public install command still pins
0.4.0. No commit, tag, release, npm registry publication or external
coordination was performed in this round.
