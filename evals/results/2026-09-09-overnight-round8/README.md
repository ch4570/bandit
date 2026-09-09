# Overnight development, round 8 — 2026-09-09

Eight fresh TASKs accompany a narrow shared-reference clarification and a new
synthetic review case. Cumulative overnight count: **44 executions**, not 44
passing answers. Two date-detail partials remain in this round. No historical
output, rubric or grade is rewritten to improve the apparent result.

## Change and its limits

The [previous library PRD](../2026-09-09-overnight-round7/grades-19.md) contained
two unsupported claims despite meeting its five decision-relevant criteria:
a reader-based denominator labeled attempts and a report date asserted as
adoption date. The shared evidence reference now says derived claims must
preserve what was counted and that a source/report date alone does not establish
when an observation occurred or a decision was adopted.

Following skill-creator's minimality guidance, the change stays in one canonical
reference, synchronized into four specialists. Its length changes from 669 to
692 whitespace words and 4,507 to 4,656 bytes. This is source length, not model
tokens. All entrypoints, metadata and the other 29 skill files remain unchanged;
there is no new output format, ratio/date inventory or user-facing command.
The [post pre-run receipt](post-before-run.json) records the exact source epochs.

Crucially, the unchanged-instruction library repeat already avoids the previous
two unsupported claims. Its “eligible deliveries” label remains compressed,
but its immediate reader-level context does not establish an invented attempt
count. Both the pre-change and post-change artifacts preserve undated queue
adoption and separate the report from the observation period. These observations
do not show an instruction-caused repair or improved reliability.

## Actual PRD rewrites and broader coverage

| Fresh TASK | Complete artifact words / cap | Grading record |
| --- | ---: | --- |
| Library, specify before | 791 / 800 | [Pre-change grade](grades-19-pre.md) |
| Transcript review before | 525 / 600 | [Pre-change pair](grades-20-pre.md) |
| Transcript baseline | 533 / 600 | [Pre-change pair](grades-20-pre.md) |
| Library, specify after | 748 / 800 | [Post-change grade](grades-19-post.md) |
| Transcript review after | 533 / 600 | [Post-change grade](grades-20-post.md) |
| Combined warehouse handoff, general after | 505 / 600 | [Regression grades](grades-regression.md) |
| Reachable-market research after | 405 / 600 | [Regression grades](grades-regression.md) |
| Onboarding-investment scope after | 540 / 600 | [Regression grades](grades-regression.md) |

The library runs edit only the authorized `input/docs/PRD.md`. Their complete
[before-instruction](pre-19/19-library-pickup-reminders--bandit-specify/after/docs/PRD.md)
and [after-instruction](post/19-library-pickup-reminders--bandit-specify/after/docs/PRD.md)
PRDs, not short final summaries, determine the word counts above. Both propose
continuing with 50 readers, preserve email, consent, physical collection and
uncertain-send recovery, and leave development/support feasibility unmeasured.
All three general/research/scope regression answers meet their five fixed
criteria; proposed scope and experiments are not observed product outcomes.

## New domain: transcript delivery and source retention

[Case 20](../../cases/20-transcript-delivery-review/request.md) asks for a useful
developer-readiness review, not a rewritten PRD or metric worksheet. Five raw
files distinguish 12 provider attempts from six recordings and four confirmed
recording deliveries. Provider completion, storage, editor export, quality
approval and explicit source release have different meanings. Adopted policy
and reported manual checks also carry known or missing dates distinct from
document-copy and compilation dates. The [rubric](../../rubrics/20-transcript-delivery-review.md)
was finalized and [hashed before launch](case20-before-run.json).

All three answers identify the consequential delivery/deletion and unresolved-
retry conflicts, correct the recording/attempt interpretation, and reject an
unsupported automated-release pass. The baseline meets all five criteria.
Both specialist answers receive **Pass, Pass, Partial, Pass, Pass**: before
the edit, D1's known July 30 adoption date is omitted; afterward, September 7's
meaning as the policy-copy export date is omitted. Neither answer invents a
missing date. Different omissions under the unchanged provenance criterion
are not a demonstrated correction, superiority result or new false-date claim.

## Execution and evidence boundaries

The [library pre-run receipt](case19-before-run.json), case-20 receipt and post
receipt bind raw fixtures, rubrics and instruction snapshots before their
respective TASKs. Specialists receive only their complete standalone folders;
the general arm receives its general folder and the baseline no PM instruction
snapshot. TASKs receive no rubric, diagnosis or previous answer. Web search is
disabled, sessions are fresh/ephemeral, and host model defaults remain unpinned.

The [facts-only audit](run-summary.json) separately checks raw/archive bytes,
actual scopes, distinct terminal threads and available versus explicitly read
instructions. Its author designed case 20 and is not that case's semantic
grader. General instructions include ten original files; the archived mascot
PNG is retained by hash only. Research returns its two references, without a
separate entrypoint-read event; the trace does not reveal any automatic loading.

Recovered failures stay visible. The library pre-run's missing `python` is
masked by a later successful `wc` in the same command, then recovers using
`python3`. Its post-run records missing `python` with exit 127, then writes and
counts the final PRD successfully. These are document edits/checks, not product
tests. The transcript baseline recovers from listing an absent instruction
directory. A rejected general-arm `--standalone` CLI invocation is documented
in the [launch correction](general-launch-correction.md); it creates no TASK
and is excluded from the execution count.

These are synthetic author-designed development observations, not a held-out
benchmark, customer validation, causal instruction study or reliability estimate.
Earlier failures and partials remain evidence under their original conditions.

## Engineering checkpoint

[Full checks](checks/README.md) pass: 78 Node tests on Node 22.23.2, 92 Python
tests on Python 3.11.16, resource synchronization, both repository validators,
all five official metadata checks, npm packaging and source ZIP creation.
These distribution checks are separate from semantic grades. Installers,
runner and archiver are unchanged in this round.

Final local artifacts use `dist/overnight-round8/`, preserving earlier builds.
The [preservation check](checks/preservation.json) verifies all 876 previous
result files against the frozen round-7 ZIP, including the 93 historical PM
Craft files also checked against HEAD. No new CI, commit, public release or
registry publication occurred; the public install command still pins 0.4.0.
