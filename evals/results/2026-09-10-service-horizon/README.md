# Service coverage and response windows — 2026-09-10

This is the Issue 18 follow-up on `fix/issue-18-service-horizon`, based on
`fix/issue-16-calculation-evidence` at `6a2ba34`. It is unreleased development
work. No merge, release, customer contact, payment, or real service was performed.

**Not ready to close Issue 18.** The final candidate passes the two original
launch handoffs, but case 15 still promises a final-week follow-up that its
Friday schedule cannot provide. Preserve the failing output and keep the PR
draft; a numerical score or clean package checks do not override that finding.

## What was tested

The candidate connects preparation, sales, billing, service/support, resource
availability, and observation windows. It follows the final customer and the
latest allowed request through response and closeout, checks work within actual
response windows, and carries affected conditions into marketing and commitment
flows. Already confirmed later resources remain usable: a short preparation
period is not automatically a short service period.

The rule lives in one canonical product-journey reference, with an existing
specification link and optional template reminder. Specialist copies are generated
by the existing sync script. There are still five skills, no new command,
dependency, installer behavior, or PM runtime. English and Korean usage guidance
remain aligned. The only runner change adds the new local case to its local-only
case inventory, so it is not silently treated as an upstream comparison.

The [protocol](protocol.md) records each candidate's reason before its execution.
The first two attempts each contain six fresh tasks: case 05 research, case 08
scope, case 12 general and specify, case 13 review, and case 15 general.
The final-request clarification repeats the three directly relevant paid-service
tasks only. Its controls are earlier evidence, not new final-candidate executions.
Original criteria and all earlier outputs remain unchanged.

## Preserve the partial results

| Attempt | Original regression criteria | Separately scored case 15 | Separate calendar/execution observations |
|---|---|---|---|
| 1 — full service horizon | 30 pass / 1 partial across 31 conditions | 96/100; supported later delivery preserved | Case 12 outer service dates fit staffing. Case 15's unstaged first-week work is 528 minutes against at most 480 minutes in its promised two-session reply window. |
| 2 — response-window workload | 30 pass / 1 partial across 31 conditions | 98/100; no substantiated critical finding | Case 15 assigns eight initial customers per session: 176 minutes fit 220 available minutes. D's final request/next-support-day response boundary remains unresolved. |
| 3 — final request and response | 14 pass / 0 partial / 0 fail across the two repeated launch handoffs | 90/100, with a critical operational-promise finding under its frozen rubric | C/D explicitly close the final request and response within coverage. F's final Friday reply occurs after its clarification cutoff; that included follow-up is unavailable. |

The two 31-condition partials concern different issues. Attempt 1's D changes
monthly storage cost to a half-month assumption without a plan to establish
that billing basis; its one-payer outcome also lacks a decision. Attempt 2's E
classifies “two or more pairs” wording as a P0 conflict despite an existing
two-pair input cap. The genuine price errors remain valid findings. These gaps
are preserved for separately scoped follow-up; they are not erased by a later
answer choosing conservative costs or clearer terms.

The attempt-2 D calendar finding is an unresolved latest-response allowance,
not proof that a reply actually occurred after staffing. A same-Saturday reply
is possible, but the stated next support day can be Monday after coverage ends.
Independent content scores and the narrower calendar audit are reported
separately rather than silently rewriting either verdict.

Attempt 3's F assigns eight customers to Friday, promises a clarification after
every weekly answer, and finishes the last Friday answers by 22:00. Yet final
clarifications close that same Friday at 18:00, when staffing only begins. The
ordinary next-operating-day rule would instead reach November 9, beyond the
November 8 contract. Enforcing the hard cutoff denies the included interaction;
allowing the ordinary rule needs unconfirmed staffing. This is a planning
contradiction, not evidence of actual late work or customer harm. The next
correction must trace dependent interactions and usable customer response time,
not just place isolated dates inside the contract. Keep that work under Issue 18.

Case 15's 98/100 is not a task pass rate or general quality benchmark. Its grader
also retains modest research and recovery-handoff gaps: budget objections should
remain distinct, and stopping sales after enrollment has closed does not by
itself protect already accepted customers. Scores do not establish paid demand,
real workload, marketing effectiveness, validated UI, or business viability.

## Inspect the evidence

- Attempt 1: [content grade](attempt-1/content-grade.md),
  [case-15 grade](attempt-1/supported-offer-grade.md),
  [calendar and execution audit](attempt-1/execution-audit.md),
  [run index and hashes](attempt-1/execution-summary.json).
- Attempt 2: [content grade](attempt-2/content-grade.md),
  [case-15 grade](attempt-2/supported-offer-grade.md),
  [calendar and execution audit](attempt-2/execution-audit.md),
  [run index and hashes](attempt-2/execution-summary.json).
- Attempt 3: [content grade](attempt-3/content-grade.md),
  [case-15 grade](attempt-3/supported-offer-grade.md),
  [calendar and execution audit](attempt-3/execution-audit.md),
  [run index and hashes](attempt-3/execution-summary.json).

For each attempt, A is case 05 research, B is case 08 scope, C is case 12 general,
D is case 12 specify, E is case 13 review, and F is case 15 general. Graders saw
only raw inputs, outputs, and the unchanged criteria. Their `A/`–`F/` or
`grading/A/`–`grading/F/` textual locators are reproduced under `grading-inputs/`.
Reports are copied byte-for-byte; temporary absolute locator roots remain
historical locators, not links to remote evidence. Audit links use local `runs/`.

Each run retains exact request/prompt, output, stdout events, stderr, metadata,
before/after inputs, and supported raw tool call/result rows. Instruction snapshots
and runner/helper snapshots bind the tested candidate. Persisted host messages
and reasoning are not exported. Tool content can still contain task material;
these public fixtures are synthetic, not private customer documents.

Case 15 was independently authored without access to candidate instructions,
earlier outputs, diagnoses, or issue/PR text. Its four raw files and separate
[meaning criteria](../../criteria/2026-09-10-service-horizon/criteria.md) were
[hash-frozen](../../criteria/2026-09-10-service-horizon/freeze.json) before the first
execution. Different offer lengths and prices can satisfy that criterion. The
first use is targeted transfer evidence, not a random benchmark; after use it
is a public development case, and subsequent attempts are not held out.

## Repository verification and limits

- `node scripts/sync-skills.mjs --check`: 25 generated resources agree.
- `npm run validate` and `python3 scripts/validate.py`: all 45 skill files pass
  structure/reference checks. These do not grade planning effectiveness.
- Final-source `npm test`: 79 passed; Python unittest discovery: 213 passed.
  Local host: macOS, Node 25.2.1, Python 3.14.7. The inherited
  `NODE_TLS_REJECT_UNAUTHORIZED` setting was removed only for the npm test
  command; no global environment or package configuration was changed.
- Python compilation and scoped `git diff --check` pass. There is no separately
  configured project lint/typecheck command. Raw model Markdown whitespace is
  preserved instead of reformatted to satisfy a style check.
- `npm pack` succeeds. All 45 packaged skill files match the final source
  byte-for-byte; the local archive SHA-256 is
  `3955d7825b9e931da6c33f7d156d7660195048afa2f720419b117b155f3828df`.
  An initial ad hoc comparison hit its default 1 MiB output buffer on the mascot;
  the completed comparison uses an 8 MiB buffer. This was a verification-helper
  limit, not a corrupted package.
- Parent evidence inventories still match all 159 and 434 stored hashes.
  The frozen case-15 raw files and rubric also still match their pre-run hashes.
- Supplemental SkillEvaluator 0.2.1 Tier 1 passes all five skills, exit 0,
  with no incomplete scan or HIGH/CRITICAL finding. Medium/low advisories are
  retained in local reports; heading/metadata heuristics do not replace this
  repository's short-entrypoint contract. SkillSpector 2.3.5 static `--no-llm`
  scanning reports zero findings across five skills. Raw scanner reports remain
  outside the repository under `/private/tmp/bandit-horizon.CtY2LG/` as required
  by that optional workflow. No dependency was installed. Tier 2/3, a full
  multi-scanner security tier, and general prompt-injection resistance are not
  claimed verified.

Runs use Codex CLI 0.154.0, read-only workspaces, disabled browsing, a 600-second
timeout, and host-default model/effort without overrides. Exact runtime identity
is not guessed from an alias; metadata records settings and raw usage. The
capture opt-in and its portability limits are unchanged from the parent PR.
Absent CLI stdout events are not treated as absent calculations.

No baseline comparison, universal reliability, savings, or superiority claim is
made. Earlier live-research currency and retrieved-payload limits remain outside
these offline tasks. Evaluations remain contributor-run; CI does not schedule
paid model trials. Historical PM Craft and earlier BANDIT evidence are preserved.
