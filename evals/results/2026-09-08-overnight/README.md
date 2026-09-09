# Overnight development — 2026-09-08

This round found and fixed installer concurrency defects and added four
synthetic product-planning cases. All four specialist outputs and two baseline
counterparts passed their predeclared meaning-based conditions. The two paired
cases show no rubric-level difference between the skill and baseline outputs.
No product skill instructions were changed on the basis of these passing runs.

These are author-designed development checks, not a hidden benchmark, a
reliability estimate, or evidence of real customer demand. The broader overnight
improvement effort remains in progress; this directory records one completed
evaluation round and its concrete engineering changes.

## Planning tasks

| Case | Arm and installation | Independent result | Output |
| --- | --- | --- | --- |
| 07: manual operating capacity | `$bandit-scope`, all five skills available | 4/4 conditions pass | [Scope recommendation](07-concierge-capacity--bandit-scope/output.md) |
| 08: incomplete cohort evidence | `$bandit-research`, all five skills available | 4/4 conditions pass | [Decision memo](08-cohort-evidence--bandit-research/output.md) |
| 09: review with linked policy | `$bandit-review`, only that skill installed | 4/4 conditions pass | [Review](09-linked-policy-review--bandit-review/output.md) |
| 10: reservation reschedule | `$bandit-specify`, only that skill installed | 4/4 conditions pass | [Handoff](10-reschedule-handoff--bandit-specify/output.md) |
| 09: same review | Baseline, no planning skill | 4/4 conditions pass | [Baseline review](09-linked-policy-review--baseline/output.md) |
| 10: same reschedule | Baseline, no planning skill | 4/4 conditions pass | [Baseline handoff](10-reschedule-handoff--baseline/output.md) |

See [independent grades](grades.md) and the pre-run rubrics for
[07–08](../../rubrics/07-08-operations-and-evidence.md),
[09](../../rubrics/09-linked-policy-review.md), and
[10](../../rubrics/10-reschedule-handoff.md). Each task agent received only the
raw case and applicable skill snapshot, with no rubric, expected answer,
previous output, or author diagnosis. A separate grader inspected those outputs
against the fixed rubrics; grading was not blinded to condition names.

All six tasks used `codex-cli 0.153.4`, `--ignore-user-config`, `--ephemeral`,
read-only mode and host-default model settings. No model override was pinned,
so identical model sampling across arms is not established. The Korean task
requests supply their output limits. All tasks exited 0 and left input and
instruction hashes unchanged. Logs show the selected specialist entrypoints
were read, and no product implementation, product test, browsing or outreach ran.
The baseline 09 log includes an optional lookup of the absent `instructions`
directory returning exit 1; the task then completed normally.

The sources for these skill snapshots match the unchanged v0.4.0 skill tree at
starting commit `f4a376e`. New local installer and evaluation-tool changes are
unreleased. The public installation command remains pinned to release 0.4.0.
Historical PM Craft 0.1.0 outputs and hashes remain untouched.

Each run directory preserves prompt, output, events, stderr, metadata, original
fixtures and instruction text. Its `archive-provenance.json` records original
and archived hashes, path normalization and hash-only PNG omissions. All
archived file hashes were verified after copying; instruction hashes were also
compared against the current source. [Run summary](run-summary.json) records
these checks and output word counts. No task scope violation or missing original
text was found.

## What changed

The Node and optional Python installers now keep the bytes inspected during
preflight as their recovery baseline, compare all affected files before the
first write, and check replacements again after staging. This protects edits
made during later-skill checks or temporary-file writes, including retirement
of old skills. Python recovery also continues restoring other files when a
concurrent edit prevents one restoration.

The [reproduction record](installer-regressions.md) retains the same three Node
tests failing against the original code and passing against the corrected code,
including full filesystem comparisons. These guards do not provide filesystem
compare-and-swap or durable recovery after process termination: there is still
a small interval between the final check and the rename/unlink syscall.

The evaluation runner can now copy only the selected specialist with
`--standalone`. It discovers new raw cases, refuses unreviewed upstream workflow
mappings, writes starting metadata before task execution, and retains original
input and instruction bytes for future runs, including unexpected modifications.
The new archival helper verifies run hashes and keeps completed failures as
failures; it does not silently relabel a task failure as a passing evaluation.

## Local engineering checks

Resource synchronization, Node validation, all 71 Node tests, `npm pack`,
Python validation, all 75 Python tests and source ZIP creation passed on macOS.
Node was 26.8.1; the optional Python checks used 3.11.16 rather than the system's
unsupported 3.9.6. The first ZIP output path used macOS's `/tmp` symlink and was
refused by the existing linked-path guard; retrying its real `/TEMP` path
succeeded. No checker or rubric was changed to suppress that refusal.

These are local checks, not new cross-platform CI or public installation
measurements. [Validation](../../../VALIDATION.md) keeps this development record
separate from previously published releases.

## Open evidence and next work

Case 08's next-observation recommendation leaves the response to positive but
contribution-negative renewals implicit. The grader recorded this minor gap;
it does not overturn the bounded present decision or justify a universal rule
change. No rubric was relaxed or rewritten after seeing the outputs.

An audit also found that the historical 0.3 offer-change output omits the
`4/14` and `4/24` repeat shares required by its original rubric, although it
correctly reports `4/6` eligible repetition. This omission is not evidence of
wrong arithmetic or a bad product decision, and it has not been presented as
fixed. The original outputs and rubric remain unchanged.

Further useful evidence would come from decisions evolving across several
turns and an experiment with inconsistent assignment/exposure records. Preserve
baseline successes and any new failures, then change product guidance only
where a demonstrated weakness supports the change. This round alone does not
establish a quality advantage or token savings.
