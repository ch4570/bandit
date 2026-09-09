# Round 8 — case 20 pre-change pair

Independent grading of the complete retained answers against the unchanged
[case 20 rubric](../../rubrics/20-transcript-delivery-review.md) and
[raw request](../../cases/20-transcript-delivery-review/request.md). The grader
did not author case 20 or execute either TASK. The raw files and rubric were
read before these judgments; neither was edited. This record grades the
pre-change pair only.

**S** denotes the [specialist answer](pre-20/20-transcript-delivery-review--bandit-review/output.md);
**B** denotes the [baseline answer](pre-20/20-transcript-delivery-review--baseline/output.md).
Locators are retained file line numbers.

## Fixed criteria

| Criterion | Specialist | Baseline | Evidence and judgment |
| --- | --- | --- | --- |
| C1 — adopted delivery and source-retention policy | Pass | Pass | S:1–3 and B:1–6 reject provider completion as delivery, require saved transcript plus assigned-editor export, and require separate post-export source release. T04 supplies a concrete loss scenario. Both distinguish export from quality approval, propose corrected states/checks, and apply adopted D1 rather than treating the newer handoff as authority. The risk is conditional, not described as an observed production deletion. |
| C2 — counting unit and outcome | Pass | Pass | S:7 and B:13–16 correct 12 attempts versus six recordings, nine provider completions versus four delivered recordings by the cutoff, and the unsupported 75% recording-delivery claim. They identify R04/R06 as saved but not confirmed exported, not proven provider failures; neither infers causal retry benefit, source release, quality approval or later outcomes. Their corrections constrain the release argument rather than merely listing ratios. |
| C3 — dates and preserved provenance | Partial | Pass | S:5,7,9 correctly distinguish policy export, August observations/cutoff, compilation and V1 execution, while leaving D2 adoption and V2 execution dates unknown without erasing their statuses. However, S never states D1's known July 30 adoption date, explicitly covered by rubric lines 35–45. This is incomplete date provenance, not a false September 7 approval assertion. B:14,19 supplies all those material distinctions, including D1 July 30 and the two missing dates. |
| C4 — retry authority and verification scope | Pass | Pass | S:5,9 and B:8–11,19–21 preserve one unresolved attempt and attempt history, reject timeout as reconciled failure, retain staff lookup/retry, and require a no-ID recovery decision before unattended retries. Both keep historical export/access and manual-drill evidence distinct from unexecuted automation checks and require future corrected verification. S does not separately repeat that V2 omitted the no-ID exercise, but it does not use the manual drill to validate that path: no-ID recovery remains unresolved and release verification remains future work. B states that exclusion explicitly. |
| C5 — useful prioritized review, scope and cap | Pass | Pass | S:1–11 and B:1–23 prioritize policy/recovery conflicts and unsupported release evidence, with D1/D2, V1–V3, CSV IDs and/or file-section locators, consequences and corrections. Both retain single-studio access, downloads and other supported boundaries while rejecting a validated next-week promise without estimates/operator capacity. Entire answers are 525/600 and 533/600 words. Verified hashes and complete traces show no input/instruction edits, external actions, implementation or product tests. |

Specialist: four Pass, one Partial. Baseline: five Pass. These are fixed-criterion
observations, not an error-free-artifact or superiority claim.

## Recomputed evidence and additional claims

[pilot-attempts.csv](../../cases/20-transcript-delivery-review/pilot-attempts.csv)
contains 12 attempts for six distinct recordings. Nine attempts are `complete`;
eight have saved artifacts, spanning all six recordings. R01, R02, R03 and R05
have saved artifacts and confirmed editor exports, so 4/6 = 66.7% is a bounded
recording-delivery result under D1. The three timeouts are T02, T08 and T12,
not three recordings established to have failed. T04's missing saved artifact
does not erase R03's later successful T05 export. Neither answer is required
to print all eight-save intermediate counts: the frozen rubric permits concise
decision-relevant counts rather than every intermediate sum or ratio.

The observation window is August 17–21, reconciled through August 21 at 18:00
UTC (`verification-note.md:7–18`); September 8 is export/compilation. D1's July
30 adoption is explicit (`delivery-policy.md:6`); D2's date is absent despite
adopted status (`:21–24`). V1's execution is August 5; V2 is a reported v1.1
manual-drill pass with an unknown date and no no-ID exercise; V3 has no execution
result (`verification-note.md:22–30`).

Neither answer invents a missing approval/execution date. The specialist's C3
Partial records the omitted known D1 date, not a conflated or fabricated one.
No additional material unsupported factual claim was established. Both frame
the proposed source-loss and duplicate-processing consequences as risks of
the handoff rules, not evidence that this production implementation exists.

## Trace and integrity

The complete [specialist trace](pre-20/20-transcript-delivery-review--bandit-review/events.jsonl)
has 12 events and three completed read-only shell commands. Line 5 reads the
request, standalone entrypoint, review and shared-evidence references; line 7
lists input files; line 9 reads the four supporting files plus specification
guidance. Returned text exactly matches those retained snapshots. No explicit
content read of the other four supplied skill files is recorded. Final answer
is line 11; line 12 is `turn.completed`.

The complete [baseline trace](pre-20/20-transcript-delivery-review--baseline/events.jsonl)
has nine events and two completed shell commands. Line 5 lists inputs while
also checking absent optional `instructions/`; `rg` reports that absence and
exits 2. Line 7 then reads all five raw files successfully; line 8 is the final
answer and line 9 is `turn.completed`. No PM skill snapshot was supplied or
read. The recovered listing error is not a semantic or final-answer failure.

Both runner exits are 0, with read-only sandbox and explicit
`web_search="disabled"`. Neither trace contains a word-count command, file
write, external action, implementation, product test, rubric/prior-output read,
or unrelated-repository inspection. Counts above were computed independently
from each complete archived answer, not inferred from process completion.

All 28 listed archive-file hashes verify: 18 specialist and 10 baseline.
Each run's five input hashes match its before/after metadata, current raw files
and [case20-before-run.json](case20-before-run.json). The specialist's eight
instruction hashes match that pre-change receipt and remain unchanged during
the run; baseline instruction maps are empty. The fixed rubric matches the
receipt. Archive path normalization changes only the documented run-root paths;
these checks verify retained archive bytes, not the original raw log paths.

| Retained item | Words | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Specialist answer | 525 | 3,999 | `541d62e6510d9f20376bf93669fd0747397897084ca9808baa23a9c537cc353b` |
| Baseline answer | 533 | 3,872 | `025288fb391c802cda6dbe7cddf86be75fca9a0aa7bea7c5721c89dc269abec6` |
| Fixed rubric | — | — | `a9a7f73c01351f1d8f669fbe6e6363ff3c141c3fb44e3bab8051203823239fed` |
| Pre-run receipt | — | — | `ee4c0f59464a1a76ee1dc8e24d2b43ec30797a82492ca6ffd5a1817a04306989` |
| Specialist archive provenance | — | — | `d02876d28cfb5635dd5d59ee8c599574d7c6c5dfc146246417bbdbad9cbc8075` |
| Baseline archive provenance | — | — | `391b813608bc3953b59c596a8902d090f8440fc87d7d3a645e7954b51e0d9e66` |

The unsigned receipt time is 2026-09-08 18:09:15.947 UTC. Recorded runs are
18:09:16.324399–18:10:58.282734 UTC (specialist, thread
`01a08235-c29b-7d11-97d2-9c0a3ed04755`) and
18:09:17.511634–18:09:55.873116 UTC (baseline, thread
`01a08235-c739-7f02-b6b5-04661c2ba3c7`). CLI 0.153.4 uses unpinned host-default
model configuration. These synthetic development observations do not establish
business demand, general reliability, comparative superiority, or an
instruction-caused difference. Trace scope does not audit unretained host state;
hash agreement and exit status are not semantic grades.
