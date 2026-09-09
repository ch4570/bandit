# Blind grades: export review

Both anonymous outputs pass all six acceptance dimensions. This assessment uses only `criteria.md`, the supplied `raw/` files, and `A.md`/`B.md`. No supplied code or tests were executed.

## A — passed

SHA256: `5bd6f7555ba79848c8f56d905cf2e84bf54c877f0128b0842513dd6dfcf8cbcc`

| Criterion | Grade | Evidence and justification |
| --- | --- | --- |
| Scope control | passed | A:1 describes “static inspection, not observed execution”; A:3–21 stays within access, request identity, dispatch/worker recovery, and download visibility. A:23 says “No files changed and no code or tests ran” and correctly excludes the support handoff. There is no replacement PRD, CSV/marketing expansion, or claimed executed result. |
| Access | passed | A:3 gives the concrete scenario: “an active B member knowing A’s export ID can retrieve that same view without a workspace check.” This follows `raw/implementation.py:47–49`, while `_view` at lines 22–29 exposes workspace, filters, state, and location. A:5 requires ownership checks and explicit non-disclosure checks. |
| Idempotency | passed | A:3 says “request keys are global” and explains B receiving A’s export when reusing A’s key. A:5 scopes lookup to the authenticated workspace and requires distinct exports for identical keys across A/B. A:7–9 distinguishes the same operation from changed-filter reuse; A:23 labels the existing retry coverage “sequential identical retries,” not workspace-isolation evidence. These match the global index at `raw/implementation.py:33–34,43` and independently chosen keys in `raw/product-notes.md:9–12`. |
| Recovery | passed | A:11 traces saved job/key → failed queue submission → 503 → retry returning pending without re-enqueue, matching `raw/implementation.py:33–44` and the HTTP contract. A:15 separately explains at-most-once removal, timeout leaving failed, interruption leaving running, and the absence of a trigger for another worker call. A:13,17 propose recovery paths without treating a particular mechanism as already mandated or implemented. |
| Actionability | passed | A:5 proposes concrete cross-workspace and inactive-member negative checks; A:9 covers exact retries and changed filters; A:13 tests a failed enqueue and uncertain acknowledgement while retaining one export ID; A:17 tests timeout, restart, and duplicate completed delivery with no additional renderer call. A:21 adds an observable noncomplete-location check. These are bounded protections and checks tied to the supplied failures. |
| Calibration | passed | Code/contract anchors accompany each finding. A:9 explicitly calls filter-conflict handling “a proposed policy, not an existing requirement.” A:21 says “Adapter atomicity is unavailable, so the intermediate-state scenario is conditional.” A:23 treats dictionaries as “shared durable-store stand-ins,” reports no test execution, and keeps adapter internals outside scope. Demonstrated defects, policy gaps, and adapter-dependent visibility are distinguished. |

Significant missed required risks: none. Unsupported claims or scope expansion: none identified. The cross-member rule in A:9 is framed as a decision/check, not an asserted defect or adopted requirement. Download visibility is explicitly conditional on the unavailable atomicity contract.

## B — passed

SHA256: `d855d3cebe3d63329eb2544e2e18257c8daa5226a6e5d5389716b23034adb800`

| Criterion | Grade | Evidence and justification |
| --- | --- | --- |
| Scope control | passed | B:3 says “No code or tests were executed” and identifies the material as synthetic with no runtime results. B:5–30 addresses access, repeated requests, recovery, and related download publication; B:32 excludes the support handoff. No replacement PRD, CSV/marketing work, or executed-result claim appears. |
| Access | passed | B:6 identifies that lookup “reads any known export ID after checking only active membership,” backed by `raw/implementation.py:47–49`. B:8 supplies the concrete A/B denial check for pending and completed exports and requires no cross-workspace fields. The listed exposure is supported by `_view` at `raw/implementation.py:22–29`. |
| Idempotency | passed | B:6 explains the global request-key lookup: “If workspace A submits a key and workspace B reuses it, B receives A’s export view.” B:8 requires workspace-scoped lookup/storage, separate exports for equal keys in A/B, and preservation of same-workspace retries. B:25–28 distinguishes same-operation retries from changed-filter reuse; B:30 accurately limits existing coverage to sequential exact retry. |
| Recovery | passed | B:11 traces job/key persistence before `push`, a RuntimeError mapped to 503, and the exact retry returning pending without scheduling work. B:16 addresses both failed and interrupted workers under the stated at-most-once/no-requeue contract and explains why manually calling `run_export` again is not a supplied recovery trigger. B:13,18 propose bounded recovery for the original job rather than claiming an approved or implemented retry design. |
| Actionability | passed | B:8 covers unauthorized reads, cross-workspace key collisions, and inactive members. B:13 checks enqueue failure/retry and interruption between persistence and dispatch. B:18 checks renderer timeout and restart without changing logical identity. B:23 checks hidden locations before completion; B:28 checks exact/conflicting repeats. B:30 proposes a renderer-call-count assertion for completed duplicate delivery and labels concurrency as unverified. |
| Calibration | passed | Findings cite the supplied code and product contracts. B:28 says changed-filter conflict is “a proposed policy, not an existing requirement.” B:30 labels concurrency “unverified” and ties checks to the “chosen durable-store behavior”; B:32 says “dictionary representation does not establish a durability defect.” B:21 describes the specific interruption-between-assignments scenario supported by the snapshot, while B:23 qualifies atomic publication with “where supported.” It does not claim a live adapter observation or an executed failure. |

Significant missed required risks: none. Unsupported claims or scope expansion: none identified. B:21 could more explicitly state that an adapter making completion publication atomic would rule out the intermediate-state exposure. This is an evidentiary precision limitation, not a demonstrated false positive: the stated failure scenario follows the supplied separate assignments and unconditional view, and the output does not claim observed adapter behavior. Concurrent deduplication/claiming in B:30 is appropriately presented as missing evidence, not a proved defect.

## Integrity and totals

- Overall: 2 passed, 0 failed; 12 of 12 criterion judgments passed.
- No significant required-risk omissions or established false positives identified.
- The outputs show no unauthorized workspace mutation. Execution traces are not included in this packet, so an independent mutation audit is unavailable; this does not turn a review-quality judgment into an assertion about unseen execution.
- Only these grading artifacts were written; supplied inputs and outputs were preserved.
