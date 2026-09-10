# Issue 16: executed numerical evidence

Parent: PR 17, commit bd96856. Its two second-round handoffs read the numerical
guidance but performed no arithmetic tool calls. Correct final arithmetic and
an independent grader's calculations did not satisfy the execution criterion.
The prior outputs and criteria remain unchanged.

This candidate moves one conditional calculation check into the shared evidence
contract and links it from each entrypoint. It requires execution, returned
results, unit/result reconciliation, and rechecking changed inputs. Source quotes
and qualitative requests do not require artificial calculations. No script,
dependency, mandatory calculator language, or separate output file is added.

Before execution, freeze this test scope:

| Case | Arm | Output cap | Check |
|---|---|---:|---|
| 12-launch-handoff | bandit | 1800 words | Existing full-journey criteria plus actual calculation execution/result agreement |
| 12-launch-handoff | bandit-specify | 1800 words | Same, through direct specialist invocation |
| 08-callback-scope | bandit-scope | 1000 words | Existing scope criteria; derived delivery-capacity calculations |
| 13-offer-consistency-review | bandit-review | 1400 words | Existing review criteria; derived order totals |
| 05-small-research | bandit-research | 800 words | Original small-research criteria; qualitative work stays bounded |

Use the unchanged runner, host-default model/effort, 600-second timeout, offline
read-only workspaces, and only raw fixtures plus copied skill instructions.
Do not provide these criteria, prior outputs, diagnoses, or expected arithmetic
to executing agents. Each attempt is fresh; retain failures without rewriting
criteria. No baseline comparison or quality/cost advantage is inferred.

An independent content grader receives only anonymized outputs, inputs and the
original meaning criteria. Separately inspect actual raw commands/tool results
to establish that consequential calculations executed and agree with the final
figures, without counting file reads or the grader's calculations as execution.
An unsupported claim of tool execution fails that additional Issue 16 check.
Preserve exact outputs, prompts, raw events, metadata, and hashes.

This is a synthetic development check. It does not resolve every live-source
currency or capture payloads omitted by the host's web-search event interface.
Those limits remain attached to the earlier research records.

## Attempt 1 outcome and next candidate

All five processes completed with input integrity passing. All four numerical
outputs claimed JavaScript execution, but their completed event records contain
only file-location and file-read commands. This fails the additional execution
check in every numerical arm. The general handoff also reports a 620,000-won
allocation whose listed entries sum to 520,000 won. Its claimed calculation did
not protect the budget reconciliation. The small qualitative answer makes no
execution claim. Preserve this failed candidate under `attempt-1/`, including
its exact instruction snapshot; independent content grading is separate.

Before running attempt 2, replace the prose-only requirement with an ordered
call/wait/reconcile sequence and a final claim check against the actual completed
tool response. If a call was skipped or failed, require an explicit unverified
status instead of fabricated execution evidence. Use the same five cases,
unmodified raw fixtures, runner, settings, caps, and criteria. The execution
criterion still requires actual calculation; an honest omission is not a pass.

## Scope-fixture authority erratum

During attempt-2 assessment, the content grader identified an author oversight:
case 08's raw request expressly prohibits running code. The runner's narrower
prohibition on supplied product code does not override that task instruction.
The earlier selection of case 08 as a mandatory code-calculation arm was wrong.
Its arithmetic must remain unverified when no permitted calculator is available;
do not weaken the user's constraint or change the raw fixture to obtain a call.
Attempt 1 still fails for claiming an execution that did not happen. Attempt 2's
honest non-execution can satisfy the authority/verification-status behavior,
but is not positive evidence of executed calculation. Cases 12 and 13 remain
the positive execution checks; case 05 is the small qualitative control.
This erratum preserves the original protocol above and changes no original
meaning criteria, source input, prior output, or claimed execution count.

## CLI-telemetry erratum: earlier execution conclusions withdrawn

A subsequent controlled synthetic diagnostic reproduced an observability gap:
direct JavaScript in `functions.exec` really executed, with the call and returned
value present in its persisted session, but neither appeared in `codex exec
--json` stdout. Therefore the earlier inference from "only file commands were
recorded" to "no arithmetic executed" was invalid. Withdraw the execution-failure
and fabrication conclusions above. Attempts 1 and 2 used `--ephemeral`, so their
complete session transcripts were not retained and execution is **inconclusive**,
not proved absent or present. The independently recalculated attempt-1 budget
error remains valid. This preserves the initial protocol and its mistakes rather
than silently rewriting the evaluation history. See the telemetry diagnostic and
execution audit reports for the final interpretation.

## Before the captured rerun

Keep attempt-2 skill instructions unchanged. Run the same five original cases
with the same task prompts and caps, adding the runner's explicit
`--capture-session-tools` option. This changes evidence retention: Codex persists
this run's session, and the runner exports only supported tool records bound to
the new thread and workspace. It does not add arithmetic hints or assessment
criteria to the task prompt. Retain the runner and helper source hashes as well
as the instruction/input hashes. Grade meaning separately with no access to
prior attempts or diagnoses. Audit actual paired call/results against final
figures, with case 08 still a no-code control and case 05 qualitative.

This third condition is not a controlled skill-effect comparison with the
ephemeral attempts. It tests the final candidate with sufficient evidence to
assess computation. If capture fails, preserve the output as incomplete rather
than rerunning into the same path or inferring success from its answer.

## Post-run collector repair

The captured tasks completed before a narrow source-reader repair. Independent
review found that buffered `readline()` could prefetch source-body bytes before
the header's identity/workspace checks. A strengthened descriptor-offset test
failed in all seven metadata-mismatch subcases. After changing the stream to
unbuffered mode, all 13 session tests passed. The original collector is preserved
in `runner-snapshots/captured-run-session_tools.py.txt`; the final one is saved
separately. This is not a skill-instruction change or an additional model trial.

The final collector re-extracted the same five completed source sessions. All
source hashes and tool-export bytes match the originals, as recorded in
`attempt-3/reextraction-check.json`. No original result or metadata was rewritten.
The tests were also capability-gated for the repository's Windows CI lane,
where the optional descriptor-based collector deliberately fails closed; the
unsupported-host failure contract is tested separately.
