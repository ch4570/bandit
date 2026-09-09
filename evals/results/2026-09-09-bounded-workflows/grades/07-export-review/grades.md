# Blind review grades

Each output was evaluated independently against `criteria.md` and the supplied `source/` files. No condition identity was inferred. Output hashes below are SHA-256 of the actual `output.md` bytes. Statements about execution and unchanged files were not independently verified and do not establish integrity here.

All six outputs identify the principal workspace-isolation and stranded-job defects and give useful acceptance checks. The failed grades below concern the explicit calibration obligation in `criteria.md:22–24`: identifying the unspecified same-key/different-filter policy. They do not imply that the outputs missed the principal access or recovery defects.

| Output | Overall quality | Material distinction |
| --- | --- | --- |
| Q01 | passed | Covers the core defects, checks, and undefined filter-conflict policy; qualifies adapter-dependent risks. |
| Q02 | failed | Omits the undefined filter-conflict policy and overgeneralizes the same-operation retry contract. |
| Q03 | passed | Covers all core obligations and explicitly separates defects, policy gaps, and adapter assumptions. |
| Q04 | passed | Covers all core obligations, including interrupted consumption and unspecified filter conflicts. |
| Q05 | failed | Omits the undefined filter-conflict policy despite otherwise strong core findings and checks. |
| Q06 | failed | Omits the undefined filter-conflict policy despite otherwise strong core findings and checks. |

## Q01 — passed

- `Q01/output.md:5–13` gives both concrete two-workspace disclosure paths, workspace-scoped key protection, and negative access checks. These follow `source/implementation.py:22–34,47–49` and `source/product-notes.md:3–12`.
- `Q01/output.md:17–23` correctly traces saved job and key before enqueue to an unqueued pending job on retry (`source/implementation.py:33–44`). It covers rejected and ambiguous queue submission while retaining the logical export.
- `Q01/output.md:27–33` connects consumed messages, failed/running states, and the absence of a recovery trigger to `source/product-notes.md:14–21` and `source/implementation.py:51–60`. Proposed recovery is not presented as an already approved mechanism.
- `Q01/output.md:37–47` acknowledges the completed-job guard, proposes observable duplicate/concurrency checks, qualifies publication visibility with “depends on storage atomicity,” and asks to define changed-filter reuse. It does not misdiagnose the durable-store abstraction. Existing tests are accurately bounded at line 45.
- No material missed core risk, unsupported finding, or scope expansion identified in the review text.

SHA-256: `e723022abc463f35bd4bf076172cebdb3b005ba7df4c4e9f42fd37d2a2ab76d0`

## Q02 — failed

- The principal review is useful: `Q02/output.md:5–10` covers ID/key disclosure and workspace isolation; lines 12–24 trace both dispatch failure and consumed-worker failure and propose same-ID recovery checks. These match `source/implementation.py:31–60` and `source/product-notes.md:3–20`.
- **Material calibration miss:** `Q02/output.md:33–38` says the notes “promise one logical export for repeated submissions,” then discusses atomic key claims and identical requests. The contract actually limits this promise to “the same operation” (`source/product-notes.md:9–12`). Reusing a workspace/key with different filters silently returns the first export (`source/implementation.py:31–38`), but neither the expected conflict behavior nor the policy's unspecified status is discussed anywhere in the output. That leaves the explicit `criteria.md:22–24` obligation unmet. A bounded addition would identify this as an open policy choice and request a check of the chosen conflict behavior, without declaring a particular response already required.
- **Additional qualification weakness:** `Q02/output.md:26–31` states interruption “leaves a running job with a visible location.” The code supports a possible intermediate state (`source/implementation.py:61–62`), but its visibility depends on unprovided storage atomicity. Unlike its concurrency discussion at line 36, this finding does not qualify that dependency. The proposed conditional-location check is still useful; actual adapter behavior is not established by the snapshot.
- Lines 38–40 correctly request completed-delivery suppression, distinguish test definitions from execution evidence, and explicitly respect the shared durable-store abstraction. No textual scope expansion identified.

SHA-256: `d136a49331d56ab8afa0124081b48bca05c3d09a173301224447c0f5652b2f84`

## Q03 — passed

- `Q03/output.md:3–8` explains both workspace-isolation defects with an A/B scenario, appropriate ownership/key fixes, and observable checks (`source/implementation.py:22–34,47–49`).
- Lines 10–22 correctly follow persist/index-before-push, same-key early return, and at-most-once consumption to stranded pending/failed/running jobs. They preserve the original export and distinguish the ability to call the worker again from the missing trigger that would do so (`source/product-notes.md:14–20`).
- Lines 24–29 explicitly qualify the publication window by unknown storage atomicity and correctly note that renderer timeout itself does not assign a location (`source/implementation.py:57–62`).
- Lines 31–36 distinguish unproven atomic uniqueness, the undefined changed-filter policy, the existing completed-worker guard, and the limited test selection. “The notes do not define that case” accurately calibrates `source/product-notes.md:9–12`; conflict rejection is offered as an option, not an existing requirement.
- No material missed core risk, unsupported finding, or scope expansion identified in the review text.

SHA-256: `daff444af81c47745b9b2efda390c3bb684211626f1aebe8d0b6dcb21cfca846`

## Q04 — passed

- `Q04/output.md:7–12` identifies both cross-workspace disclosure paths, independent request-key selection, and bounded ownership/key checks, consistent with `source/product-notes.md:3–12` and `source/implementation.py:31–49`.
- Lines 16–20 trace the job/index-before-enqueue ordering and both rejected and ambiguous submission outcomes. Recovery retains the original logical export instead of assuming a new key solves the required outcome (`source/product-notes.md:14–16`).
- Lines 24–30 cover renderer timeout and interruption after message removal, including pending/running states, the absence of automatic redelivery, and the missing recovery trigger. The mechanism remains explicitly a choice.
- Lines 34–40 qualify concurrent-key atomicity as unproven, ask to define same-key/different-filter behavior, recognize completed-job suppression, and request repeat-delivery and download-visibility checks. Overlapping-worker protection is conditional on recovery creating that overlap. Lines 3 and 42 preserve the provided store contract and static-evidence limits.
- No material missed core risk or scope expansion identified. The brief finalization-window recommendation is supported as a check; it does not establish actual adapter behavior.

SHA-256: `6cf548aa6e41e58e1fdf4dd2bc093bc5eac6ef5041df0ee505b8d2fcc3bb5fb0`

## Q05 — failed

- `Q05/output.md:5–15` gives both A/B leakage scenarios, workspace ownership/key fixes, and relevant negative checks. Lines 17–27 correctly explain queue-failure and consumed-worker stranding and propose checks that retain the original ID (`source/implementation.py:31–60`; `source/product-notes.md:3–20`).
- **Material calibration miss:** the repeated-request discussion at `Q05/output.md:11–15,29–32` covers per-workspace identity and concurrency, but never identifies same-key/different-filter reuse. The early return ignores the new filters (`source/implementation.py:33–38`); the notes guarantee reuse only for the same operation and specify no conflicting-filter response (`source/product-notes.md:9–12`). No open policy decision or corresponding acceptance check is stated. This leaves `criteria.md:22–24` unmet. Identify that policy gap explicitly and make any conflict-response suggestion an option.
- Lines 20 and 26 correctly treat retry mechanisms as proposed choices. Lines 29–34 qualify adapter serialization, call the publication gap “possible,” request completed/overlapping-delivery checks, and avoid treating test definitions as passing results. The dictionaries are not falsely diagnosed as process-local storage.
- No other material false positive or textual scope expansion identified.

SHA-256: `d962528ff2cd8cbefa8ac89c63f8f50114662e8a0a5fd0310b8a07908bb94e73`

## Q06 — failed

- `Q06/output.md:3–9` covers cross-workspace reads and globally indexed key collisions with concrete scenarios and isolation checks. Lines 11–25 correctly connect persist-before-enqueue, early return, at-most-once consumption, and the lack of a worker recovery trigger, while preserving the logical export (`source/implementation.py:31–60`; `source/product-notes.md:3–20`).
- **Material calibration miss:** same-workspace reuse is preserved at `Q06/output.md:9`, and overlapping submissions are discussed at line 37, but changed-filter reuse is absent. `source/implementation.py:33–38` returns the prior job regardless of new filters; `source/product-notes.md:9–12` covers only the same operation and leaves conflict behavior unspecified. The required distinction between a demonstrated defect and this policy gap (`criteria.md:22–24`) is therefore missing. Add an explicit open-policy statement and a check for whichever conflict behavior is selected.
- Lines 27–33 tie potential premature download visibility to the exact assignment order and ultimately acknowledge unknown adapter atomicity. Lines 35–39 correctly bound existing tests, recognize the completed-job guard, request a no-render-on-repeat check, and identify unavailable concurrency evidence.
- “Permanently” in line 11 is stronger than necessary: the supplied request path cannot recover, while another explicit worker invocation can run the saved job. The body at lines 19–25 supplies this distinction, so this wording is not a separate failing finding. No textual scope expansion identified.

SHA-256: `45853509ee3f16de42f48a2d32d6d54519e28337d268d852007f75cb6a8667fe`
