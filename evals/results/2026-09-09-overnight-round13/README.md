# Overnight development, round 13 — 2026-09-09

Two fresh executions review Korean source documents for a synthetic exhibition
photo-delivery feature: standalone `$bandit-review` and a no-PM-skill baseline.
The cumulative overnight total is **48 native planning executions**, not a count
of passing answers. Round 12's fake CLI calls remain excluded.

The [five raw files](../../cases/22-photo-export-consent/request.md) contain a
Korean request, implementation-derived PRD, linked adopted policy, static Python
excerpt and supplied historical test report. The 809 whitespace-delimited words
and 7,750 bytes are fictional; no customer photos, credentials, live service or
legal/compliance claim is involved. This is not the first Korean review check:
cases 03 and 09 already have Korean requests. This case combines Korean source
documents and output with a queued export/permission-withdrawal boundary.

## What ran

[Before-run hashes](before-run.json) freeze the raw inputs, five-condition
[rubric](../../rubrics/22-photo-export-consent.md), all 34 skill files and tooling
before either TASK starts. The rubric and author analysis stay outside both
TASK workspaces. The specialist receives only its complete selected skill;
the baseline receives no PM instructions. Both use the same product request.

The fresh CLI sessions use read-only workspaces, disabled web search,
`--ignore-user-config` and `--ephemeral`. Neither explicitly requests a model;
metadata retains `model_override: null`. These are host-default runs, not pinned
model comparisons or verified backend identity. The runner is the unchanged
round-12 version; no instruction change occurs between these runs.

| Arm | Output words / cap | Native thread | Complete answer |
| --- | ---: | --- | --- |
| Standalone review | 326 / 450 | `01a082a5-b41b-7f11-af32-c4d036bf56af` | [Korean review](bandit-review/output.md) |
| Baseline | 313 / 450 | `01a082a5-b8b4-7c12-a5e1-a5200332a638` | [Korean baseline](baseline/output.md) |

Both runner processes exit 0 and emit `turn.completed` with Codex CLI 0.153.4.
The [mechanical summary](run-summary.json) verifies all 18 specialist and 10
baseline archive file mappings against the retained temporary originals, with
literal run-root normalization only where recorded. Inputs and instructions
remain unchanged. Completion is not the semantic grade.

The specialist's three completed shell commands read the entrypoint, review
and evidence references, and all raw files. The baseline's initial file listing
exits 2 because its intentionally absent `instructions` directory does not exist;
it then reads all five input files with successful commands and completes. This
inspection error is retained, not treated as a product failure or hidden rerun.
No supplied code/tests, file edits, web requests or external product actions
appear in either trace.

## What the answers actually distinguish

Both answers identify the adopted rule: saved permission withdrawal must affect
new downloads even when a ZIP was requested or prepared beforehand. They compare
that rule with the draft/code's queue-time grant snapshot and propose preserving
current authorization at the new-download boundary. Both distinguish a static
path inference from an observed leak and preserve the existing requester,
project/private-photo, readiness and expiry controls.

Both also reject promoting two reported v0.3 unit checks into v0.4 asynchronous
withdrawal verification. The historical passes remain limited positive evidence,
not retroactively failed tests or current release proof. Suggested new checks
are future work. Neither expands the promise to recalling downloaded files,
interrupting in-flight transfers, public sharing or a new authentication system.

The independently graded case and recorded example are development evidence,
not customer validation, a held-out benchmark, general Korean-language quality,
or proof that BANDIT caused an improvement. A correct baseline stays visible.
The [independent nonblind assessment](grades-22.md) records five Pass criteria
for each answer, no Partial/Fail or additional material issue. It explains the
limits of the omitted exact calendar dates without changing the fixed rubric
or any older date-detail Partial. There is no demonstrated new instruction
defect to repair. The [recorded review example](../../../examples/photo-export-review.md)
connects these artifacts with adapted English/Korean prompts, not a new test.

## Engineering checkpoint

[All local gates](checks/README.md) pass: 79 Node tests, 99 Python tests,
resource sync, both repository validators and all five official metadata checks.
A separate npm pack contains the same 43 files and exact compressed bytes as
round 12. Final source ZIP verification checks current payloads and all 1,451
previous result files, 34 skill files, 87 existing raw/rubric/sequence files and
93 historical PM Craft files; older failures and partials remain intact.

No skill, installer, runner, archive implementation or existing rubric is changed
in this round. No new CI, commit, release or registry publication is performed.
