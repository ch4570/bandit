# Calculation evidence follow-up — 2026-09-10

This follows [Issue 16](https://github.com/ch4570/bandit/issues/16) on child branch
`fix/issue-16-calculation-evidence`, based on PR 17's
`feat/issue-15-product-journey` at `bd96856`. It is unreleased development work,
not a new v0.4.0 release or a comparative quality benchmark.

## Read the corrected conclusion first

CLI JSON stdout is not a complete tool transcript in the tested Codex 0.154.0
host. A [controlled diagnostic](telemetry-diagnostic/manifest.json) captured
successful direct JavaScript in a persisted session while its
[stdout](telemetry-diagnostic/events.jsonl) omitted the call and result. The
[exact selected session rows](telemetry-diagnostic/session-tool-records.jsonl)
preserve the expression and returned `21844025`; no host messages are exported.

Earlier conclusions that missing arithmetic command events proved skipped or
fabricated execution are withdrawn. The first two attempts were ephemeral, so
their computational execution is **inconclusive**, not proved absent or present.
The independently found first-attempt budget error remains valid: listed
allocations sum to 520,000 won, not the reported 620,000 won.

The evaluation also initially misclassified case 08: its raw request prohibits
running code. It is a no-code/verification-status control, not a required
arithmetic-execution case. Its first answer claims prohibited code execution;
the second correctly reports arithmetic as not tool-verified. The full
[protocol and explicit errata](protocol.md) preserve both evaluator mistakes.
No original raw input, output, or meaning criterion was changed to erase them.

## Recorded development attempts

| Condition | Content assessment | Execution evidence |
|---|---|---|
| Attempt 1: shared calculation contract | 30 original conditions pass, 1 partial for the general handoff's cash-total error; scope's claimed code execution separately conflicts with the raw request | Three permitted numerical arms inconclusive; no-code and qualitative controls assessed separately |
| Attempt 2: call/wait/reconcile and honest status | All 31 original conditions pass; independently checked numerical claims match; scope reports the prohibition | Three permitted numerical arms still inconclusive from incomplete stdout |
| Attempt 3: unchanged skills, persisted tool evidence | 30 pass, 1 partial: specify sells a month beyond confirmed staffing; monetary arithmetic passes | Actual paired calculation call/results in all three permitted numerical arms; controls contain no arithmetic calls |

These are criterion counts, not all-or-nothing task success rates. Passing
content conditions do not establish actual execution, real customer demand,
marketing performance, tested UI quality, or business viability.

Both attempts use unchanged raw cases and the same output caps: case 05 research
(800 words, subject to its tighter 200-word user request), case 08 scope (1,000),
case 12 general and specify (1,800 each), and case 13 review (1,400). The executing
agent sees only its request, synthetic artifacts, and copied skill instructions;
not this protocol, criteria, prior answers, or diagnoses. No model or reasoning
override was requested; settings and usage remain in each raw metadata/event
record. Unspecified runtime identity is not inferred from a model nickname.

Independent graders received the frozen meaning criteria and anonymized A–E
inputs/outputs. A maps to case 05 research, B to case 08 scope, C to case 12
general, D to case 12 specify, and E to case 13 review. Their original locator
roots are reproduced in each attempt's `grading-inputs/` directory.

- Attempt 1: [content grade](attempt-1/content-grade.md),
  [execution audit](attempt-1/execution-audit.md),
  [raw run index and instruction hashes](attempt-1/execution-summary.json).
- Attempt 2: [content grade](attempt-2/content-grade.md),
  [execution audit](attempt-2/execution-audit.md),
  [raw run index and instruction hashes](attempt-2/execution-summary.json).
- Attempt 3: [content grade](attempt-3/content-grade.md),
  [execution audit](attempt-3/execution-audit.md),
  [raw run index and instruction hashes](attempt-3/execution-summary.json),
  [final-collector re-extraction](attempt-3/reextraction-check.json).

The third specify answer's prepaid monthly service extends beyond the confirmed
four-week staffing window. Its J12-6 partial is retained and tracked separately
in [Issue 18](https://github.com/ch4570/bandit/issues/18). This numerical-evidence
change does not claim to fix that service-horizon dependency. Some time totals
are passed to the calculation tool as literals rather than derived sums; the
execution audit distinguishes them from the genuinely evaluated monetary
formulas. Do not generalize these three calculation checks to every number.

Exact outputs, prompts, events, before/after inputs, metadata, and instruction
snapshots are retained. Historical PM Craft evidence and the parent PR's raw
results are untouched. The original runner is saved under `runner-snapshots/`.

## Scope of the candidate

All five existing skills route consequential derived figures to one shared
calculation contract. It requires a permitted real call, response inspection,
input/result reconciliation, and an honest incomplete status if the check is
prohibited, skipped, or unavailable. Source quotes and qualitative requests
remain lightweight. Product-journey guidance links to that canonical contract
instead of duplicating it; specialist resources are generated by the existing
sync script. English and Korean usage guidance describe the same behavior.

The evaluation runner gains opt-in task-bound tool-record retention. Its
default remains ephemeral, and its requested capture is separately checked
from process success and workspace integrity. It is evidence collection for
development tasks, not a new product-management runtime or scheduled service.

## Repository verification

- `node scripts/sync-skills.mjs --check`: 25 generated resources agree.
- `npm run validate` and `python3 scripts/validate.py`: all 45 skill files pass
  structural/reference checks; these are not behavioral grades.
- `npm test`: 79 passed. The isolated package-consumption test also passed
  separately with inherited `NODE_TLS_REJECT_UNAUTHORIZED` removed from that
  command's environment; no global environment setting was changed.
- `python3 -m unittest discover -s tests -v`: 213 passed after the collector
  regression and unsupported-platform tests.
- `python3 -m py_compile`: changed Python modules/tests compile. No separate
  project lint/typecheck command is configured; source review and scoped
  `git diff --check` supplement the validators and tests.
- `npm pack`: built successfully in a temporary directory; all 45 packaged
  skill files were compared byte-for-byte with current source.
- Parent evidence inventory: all 159 stored hashes still match. Raw outputs
  retain their exact Markdown whitespace instead of being reformatted.

The collector's independent review, demonstrated regression detection,
capability limits, and same-session re-extraction are recorded in
[collector-review.md](collector-review.md). The optional official skill validator
requiring PyYAML was unavailable; no dependency was installed to run it.

## Limits

This is repeated testing of public synthetic cases, not held-out transfer
evidence. There is no baseline arm, savings claim, or proof of universal model
compliance. The earlier live-research currency/source-payload limitations remain
unresolved by these offline checks. Model trials remain contributor-run; CI
does not schedule paid model evaluations. No merge, release, customer contact,
publication of marketing material, or live commercial experiment is authorized
by these results.
