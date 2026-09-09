# Case 22 — independent nonblind assessment

Both answers meet all five frozen meaning criteria: **5 Pass, 0 Partial,
0 Fail** each. This is an assessment of these two reviews, not proof of working
software, comparative superiority, or an instruction-caused improvement.

The grader read all five [raw files](../../cases/22-photo-export-consent/request.md)
and the complete [pre-run rubric](../../rubrics/22-photo-export-consent.md)
before opening either answer. The grader knew arm identities and had performed
earlier BANDIT maintenance audits, but did not author this fixture/rubric or
execute either TASK. Root supplied terminal status and preliminary mechanical
counts, not a semantic grade; counts and retained hashes were rechecked here.
No author analysis or earlier task outputs were consulted for this assessment.

## Answers and fixed criteria

`S` means [standalone bandit-review output](bandit-review/output.md); `B` means
[baseline output](baseline/output.md). Line numbers refer to those complete
saved answers, not intermediate messages. Both outputs have 15 lines and two
numbered material findings. Entire-file whitespace counts, including headings,
source locators and closing qualifications, are **326/450 words** for S and
**313/450 words** for B. Neither needs a third finding to satisfy the request.

| Fixed criterion | Standalone bandit-review | Baseline |
| --- | --- | --- |
| C1 — Adopted withdrawal boundary and supported static path | **Pass.** S:3–7 ties policy:21–28 to PRD:21–23 and the queue/download functions, describes a mixed-project ZIP still containing withdrawn photos, and explicitly distinguishes this inference from an observed execution. S:6 gives the approved policy priority over the conflicting draft. | **Pass.** B:3–7 identifies queue-time-only grants, the later ready-ZIP return, the same-requester pre-expiry consequence, and the draft's inability to replace policy. B:15 limits the conclusion to static inspection. |
| C2 — Readiness claim versus supplied historical checks | **Pass.** S:9–13 preserves the two reported v0.3 requester/expiry passes while rejecting their expansion to v0.4 withdrawal verification. It identifies fixed grants and absent asynchronous/withdrawal coverage, retains past passes, and marks current verification unconfirmed. | **Pass.** B:9–13 distinguishes the pre-asynchronous v0.3 report from absent v0.4/end-to-end results, preserves the limited earlier passes, and removes the unsupported completion claim. It does not relabel the old checks as failed or unexecuted. |
| C3 — Usable correction and observable future check | **Pass.** S:6–7 proposes current permission at a new download, whole-bundle denial or rebuilding an allowed subset with exclusions explained. The stated denial outcome and queued/ready/mixed-project withdrawal checks form a concrete acceptance direction; S:13 keeps the existing two checks. These are proposals, not adopted or executed changes. | **Pass.** B:6–7 offers the same permitted correction alternatives and explicitly asks whether new downloads are blocked after withdrawal. The check-to-transfer boundary remains within the supplied new-download promise. B:13 preserves requester and UTC expiry checks and adds readiness verification. |
| C4 — Positive controls and intentional exclusions | **Pass.** S:15 preserves initial project/private-photo filters and requester/readiness/expiry guards, and excludes public sharing, nonmembers, new SSO, in-flight interruption and remote recovery. It invents no public URL, coordinator bypass or missing authentication requirement. | **Pass.** B:15 explicitly preserves project/classification filters, coordinator restrictions and the existing download guards. It keeps the declared deferred capabilities and already-started/already-saved transfers outside this correction. |
| C5 — Prioritized Korean review and task boundaries | **Pass.** S:1–15 gives two prioritized Korean findings with exact source lines, consequences, corrections and next checks within 326 words. The observed commands are read-only inspections; raw/instruction hashes remain unchanged. | **Pass.** B:1–15 gives two prioritized Korean findings within 313 words. File names, named functions and the quoted conflicting PRD rule provide usable locators without line numbers. The observed commands read supplied files only; the recovered listing error below does not change the review or permission scope. |

For C2, the controlling raw locations are `verification-note.md:6–18` and
`delivery-prd.md:27–29`: October 14 is compilation, October 9 is the reported
v0.3 execution, and the asynchronous change is October 13. Neither answer
repeats those calendar dates, but both preserve the decision-relevant version,
order, tested cases and absent current coverage. Neither asserts that
compilation was re-execution. This is not the same as a false date claim or
erasure of the historical passes.

## Actual command scope

The complete [S trace](bandit-review/events.jsonl) contains 11 events and three
completed shell commands, all exit 0. Event line 5 lists `input/` and the
selected specialist folder; line 7 reads its entrypoint, review guidance and
shared evidence guidance; line 9 reads the request and all four supporting
files using `cat`/`nl`. The final answer is event line 10 and completion line 11.
No other specialist, rubric or prior answer is read. The remaining packaged
resources were available, not claimed to have been read.

The complete [B trace](baseline/events.jsonl) contains 17 events and six
completed shell commands. Event line 5's `rg --files input instructions` exits
2 because the optional `instructions/` directory is absent. Its error is
preserved. Lines 9–11 and 14–15 then successfully read each of the five raw
files; no PM instruction is loaded. The final answer is line 16 and completion
line 17. This recovered discovery error is not a supplied-code/test execution
or a material defect in the final review.

Both traces contain only assistant messages and these command events: no
recorded browsing, outreach, external write, file edit, supplied-code/test
execution or implementation. Neither trace records a word-count command; the
counts above are this audit's calculations, not a claimed TASK self-check.
The static-path finding is not evidence of an actual download, disclosure,
browser result, production defect occurrence or successful repair.

## Additional material issues

No additional material factual or scope issue was found in either final answer.
Baseline's stronger opening recommendation to withhold approval is supported
by the same policy conflict and missing current verification; it does not
claim that approval was actually withheld. Both retain next checks as future
work. A five-criterion pass is not an exhaustive correctness guarantee.

## Integrity and limits

The [before-run receipt](before-run.json) was recorded at
`2026-09-08T20:11:32.489Z`, before both recorded starts. Its SHA-256 is
`7bd36f1b3f92b48b28930cbd82e812d2304efa645f842b3996675e3ad12fda18`.
The unchanged rubric matches its pre-run SHA-256
`0408de8c0611a3e8d54b33e28eb873682d2160a09db702bbb28f0247f0c1e6cd`.

All 28 archived file digests were independently verified against provenance
(18 S, 10 B). Both five-file input snapshots match the receipt, current raw
sources and equal metadata before/after maps. S's eight instruction files match
the selected receipt, current sources and equal before/after maps; B has none.
All 34 current skill file hashes still match the receipt. Each saved output
equals its trace's final assistant-message text exactly.

| Saved artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| S output | 3,383 | `e0fbb0c47013f04ea9fb6a5dc786064557d954e369ca93a92cbeb3965aa80b58` |
| B output | 3,141 | `84b3fc71b0db1258c727087e0e19ad656308232026ce2ab8804313c211e5ca3e` |
| S archive provenance | — | `a31d824d62febc0525d2a551003c99a12100cfeb1897173c68833046ae611274` |
| B archive provenance | — | `b837e87d60b2734126937d7e04e1e53d7b664f4d1782d3d98947c885867d5e10` |

Both metadata records identify Codex CLI 0.153.4, read-only sandbox, explicit
web-search disabled, no editable artifact and `model_override: null`. Host
defaults are unpinned, not a verified backend identity. Both child exit codes
are 0 and both traces end in `turn.completed`; these mechanical facts were
not used as semantic pass criteria. Timestamps are local unsigned records;
hash equality and traces do not attest every unrecorded host action.

This is one synthetic, author-designed Korean-source development case with one
answer per condition, not a held-out or representative benchmark, legal or
compliance assessment, first-ever Korean review, measured customer outcome,
reliability estimate, or causal comparison. The baseline also passes. No skill,
rubric, input or output was changed by this grading; no model or product test
was executed by the grader.
