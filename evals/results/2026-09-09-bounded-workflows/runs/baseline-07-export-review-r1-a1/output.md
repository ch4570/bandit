**Recommendation: hold the two-workspace pilot** until workspace isolation and recovery checks pass. The snapshot shows cross-workspace disclosures and exports that can remain stranded after a single queue outage or renderer timeout.

This is a static review of the supplied files. Tests were not run; adapter behavior and shared-store durability are taken from the product notes.

**1. Access boundaries fail through two paths — pilot blocker**

- **Known export ID:** `get_export()` checks active membership but never compares the job’s workspace with the session workspace. An active member of workspace B can retrieve workspace A’s status, filters, and completed download location.
- **Reused request key:** `request_keys` is keyed globally. If B submits a key already used by A, `request_export()` returns A’s export, including its filters and download location. Independent key selection makes this a realistic accidental collision as well as an intentional access path.

**Smallest fix:** Scope request-key lookup and uniqueness to `(session.workspace_id, request_key)`. Check workspace ownership before returning any job view. Use the authenticated session as the workspace source, as creation already does.

**Acceptance checks:** Create A’s export and attempt to read it as B, both before and after completion; neither response may expose its status, filters, or location. Submit identical keys in A and B; each must receive a distinct export belonging to its own workspace. Verify inactive sessions cannot read exports as well as request them.

**2. A queue outage strands an accepted request — pilot blocker**

`request_export()` stores the job and request-key mapping before `queue.push()`. If push raises `RuntimeError`, the adapter returns 503, but the mapping remains. A browser retry returns the existing `pending` job without enqueueing it. If the first push accepted nothing, the export never runs.

**Smallest fix:** Retain the same logical export and provide recoverable dispatch for pending jobs whose delivery is unconfirmed. Do not require a new request key or simply delete the job after an ambiguous push failure: the queue may already have accepted it.

**Acceptance checks:** Simulate push failure before acceptance, restore the queue, and retry the same key. The original export must eventually complete. Also simulate acceptance followed by an error or lost response; recovery must preserve one logical export and tolerate duplicate delivery.

**3. Failed or interrupted workers have no recovery path — pilot blocker**

On renderer timeout, `run_export()` marks the job `failed` and raises. Delivery is at most once, so the consumed message will not return. Repeating the submission only returns the failed job. A process interruption after message removal can similarly leave a `pending` or `running` job without work scheduled.

Calling `run_export()` again could retry these states, but no supplied mechanism arranges that call.

**Smallest fix:** Add a bounded recovery path using persisted job state to reschedule failed or abandoned work under the existing export ID. The specific retry mechanism remains a product/implementation choice.

**Acceptance checks:** Consume a message, cause one renderer timeout, then restore successful rendering; the same export must complete without a new logical request. Repeat with process interruption after dequeue and during rendering, restarting against the same store. A temporary object created during timeout must never appear as a download location.

**4. Repeat-request guarantees need stronger evidence**

Sequential same-key retries reuse one job. Concurrent submissions, however, use a check-then-create sequence with no visible atomic uniqueness guarantee. Two callers could create separate jobs; whether external storage prevents this is unproven.

**Smallest fix/check:** Atomically enforce workspace-scoped key uniqueness and test simultaneous same-operation submissions returning one export ID. Define same-key/different-filter behavior; rejecting conflicting reuse is a small, explicit option.

The completed-job guard correctly skips a subsequent worker call once state is `complete`, but no existing test verifies renderer invocation count. Add that check. Overlapping deliveries can both enter rendering before completion; use an atomic claim if recovery can create that overlap.

`_view()` also returns the stored location regardless of state, while completion writes location before state. Make location visibility conditional on `complete`, and check visibility during interrupted finalization.

**Existing evidence:** The three supplied tests cover sequential retry identity and queue count, same-workspace completed status, and inactive request rejection. They do not establish workspace isolation, concurrent idempotency, recovery, duplicate-worker suppression, or download visibility. Auth, storage, queue, and renderer adapter validation remains outside this review.