# Round 8 — case 20 post-change review

Independent grading of the complete retained [answer](post/20-transcript-delivery-review--bandit-review/output.md)
against the unchanged [case 20 rubric](../../rubrics/20-transcript-delivery-review.md)
and [raw request](../../cases/20-transcript-delivery-review/request.md). The
grader did not author the fixture or execute this TASK. The pre-change pair was
graded first; this is not a blind-to-phase assessment. No rubric, raw fixture,
instruction, output or prior grade was changed. **P** locators below refer to
the final answer's retained line numbers.

## Fixed criteria

| Criterion | Grade | Evidence and judgment |
| --- | --- | --- |
| C1 — adopted delivery and source-retention policy | Pass | P:1–3 rejects the proposed provider-completion/deletion rule against D1, requires storage plus assigned-editor export, and makes source release a separate explicit action afterward. T04 supports a conditional source-loss scenario, not a claimed production incident. Corrected states, acceptance criteria and retained 30-day downloads at P:11 preserve the useful journey. P:3 keeps quality approval outside this automation rather than inferring it from export. |
| C2 — counting unit and outcome | Pass | P:7 corrects 12 attempts versus six recordings and nine provider completions versus four recording-level deliveries by the August cutoff. R04/R06 have stored transcripts without confirmed exports; the answer does not call them established provider failures or claim retry automation fixes their remaining step. This correction directly challenges the proposed release justification without inferring release, quality approval or later outcomes. |
| C3 — dates and preserved provenance | Partial | P:7 gives the August 17–21 observation window and August 21, 18:00 UTC cutoff. P:9 distinguishes September 8 compilation from execution, preserves V1's August 5 pass, leaves V2's execution date unknown, and supplies D1 July 30 and D2 adopted-with-date-unavailable. However, it never identifies September 7 as the policy-copy export date, expressly covered by rubric lines 35–45. Its rejection of September 7 as an established D2 approval date does not supply that missing source-date meaning. This is incomplete provenance detail, not an invented approval/execution date. |
| C4 — retry authority and verification scope | Pass | P:5 preserves one unresolved attempt and full attempt history, rejects timeout as confirmed failure, retains manual lookup where an ID exists, and blocks unattended no-ID retry pending Leah/Omar's decision. P:9 scopes V1 to historical export/access, V2 to an undated manual drill excluding automation/no-ID, and V3 to a checklist without results. P:3,9,11 calls for corrected future verification rather than claiming a new release pass. |
| C5 — useful prioritized review, scope and cap | Pass | P:1–13 gives an actionable readiness judgment with file/section, policy, verification and CSV-ID locators; consequences and corrections accompany the prioritized findings. It retains existing accounts/ownership, one-studio isolation and downloads while rejecting a substantiated next-week promise without estimates/operator capacity. The entire English answer is 533/600 words. Verified hashes and the complete trace show no input/instruction edit, external action, implementation or product test. |

Four Pass, one Partial. The phase label and positive process exit do not
establish an improvement mechanism or semantic success beyond these judgments.

## Arithmetic and additional factual-claim review

Independent CSV recomputation confirms 12 attempts for six recordings, nine
provider completions and eight saved-attempt artifacts across all six recordings.
Only R01, R02, R03 and R05 have both saved artifacts and confirmed exports;
4/6 = 66.7% is recording-level delivery under D1 at the stated cutoff. T02, T08
and T12 are client timeouts, not three definitively failed recordings. P:7
preserves these distinctions; omitting the eight-save intermediate total is
not a failure under a rubric that explicitly permits concise material counts.

The C3 Partial is narrowly an omitted source-date explanation. P:9 says D2's
approval date is unavailable, “not September 7.” In context this rejects the
handoff's unsupported attribution; it does not supply an alternative date.
The supplied record cannot rule out every possible actual D2 approval date,
and this grade does not treat that phrase as proof D2 could never have been
approved on September 7. What is missing is the positive explanation that
September 7 dates the policy copy, as `delivery-policy.md:3–4` states. D1's
July 30 date, unlike in the pre-change specialist answer, is present here.

No additional material unsupported factual claim was established. Source-loss
and overlapping-submission consequences are framed conditionally at P:3–5.
The answer does not treat an undated adopted rule as a draft or an undated
reported pass as unexecuted. The date omissions in the two specialist answers
differ; neither omission establishes a false date assertion or a causal effect
of the changed instruction.

## Trace, immutability and limits

The complete [trace](post/20-transcript-delivery-review--bandit-review/events.jsonl)
contains nine events and two completed read-only shell commands. Line 5 reads
the raw request, standalone entrypoint, review and changed shared-evidence
references, then lists the five input files. Line 7 reads the four supporting
files plus specification guidance. Returned text matches the retained snapshots
exactly. No explicit content read of the other four supplied skill files is
recorded. Line 8 is the final answer and line 9 is `turn.completed`.

Both shell commands and the runner exit 0. The run uses read-only sandboxing and
explicit `web_search="disabled"`. No word-count command, file write, external
action, implementation, product test, rubric/prior-output read or unrelated
repository inspection appears in the trace. The full-answer word count was
computed independently; the model's internal counting process is not observable.

All 18 archive-file hashes verify. Five raw files match their before/after
metadata, current raw sources, [case20-before-run.json](case20-before-run.json)
and the case 20 entry in [post-before-run.json](post-before-run.json). The rubric
hash is unchanged across those receipts. All eight selected skill files match
the post receipt, current source and unchanged before/after instruction hashes.
The shared-evidence reference is the recorded post-change version; original
pre-change instructions remain in the separate pre archive.

| Retained item | Words | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Complete answer | 533 | 3,828 | `3193e8af302418969be8fba88d37a3f7fd59b0533443f9b91924fc2ea1a13b3e` |
| Fixed rubric | — | — | `a9a7f73c01351f1d8f669fbe6e6363ff3c141c3fb44e3bab8051203823239fed` |
| Post pre-run receipt | — | — | `df3acb1b17a51f4fd32e66f6a5e6c4ef65d64b94317cf2bac03c790b15ff6417` |
| Archive provenance | — | — | `1d4b64b9d748a6fed1b4ca8279a60070e75427626c7dd6864f259ea057e09aae` |

The unsigned post receipt is dated 2026-09-08 18:10:48.771 UTC. Run metadata
records 18:10:55.218625–18:12:09.900291 UTC, CLI 0.153.4 and thread
`01a08237-44f3-7dd3-9104-ed24ecbf9ab9`, with unpinned host-default model
configuration. Archive verification concerns retained bytes with documented
run-root path normalization, not original raw log-path reconstruction or
unretained host state. This is one synthetic development observation, not
business validation, general reliability, superiority or instruction-caused
improvement. Hash agreement and exit status are not semantic grades.
