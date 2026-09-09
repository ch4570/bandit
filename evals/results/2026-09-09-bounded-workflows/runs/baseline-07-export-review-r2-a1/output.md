**Recommendation: hold activation for both pilot workspaces until workspace isolation and recovery checks pass.** The supplied implementation demonstrates access leaks and stranded-export paths. Existing tests are source evidence only; they were not run.

### 1. Cross-workspace access through export IDs and request keys — blocker

**Demonstrated:** `get_export` checks active membership but never compares the job’s workspace with the session’s workspace. `request_keys` is indexed globally by key, and a match returns the existing job without an ownership check. Both paths expose status, filters, and any download location.

**Failure scenarios:**
- An active workspace-B member supplies a known workspace-A export ID and receives A’s export details.
- A and B independently submit `"key-1"`. B receives A’s export instead of creating its own; no knowledge of A’s export ID is needed.

**Smallest fix:** Scope request keys by `(session.workspace_id, request_key)` and enforce workspace ownership before returning any job view. Derive ownership from the authenticated session.

**Acceptance checks:** Using A and B, verify that B cannot read A’s pending, failed, or completed export by ID; denial must reveal no filters, status, or location. Identical keys in A and B must create separate exports. Same-workspace retries must retain the original ID. Verify inactive members cannot read exports as well as request them.

### 2. Queue outage strands an accepted logical export — blocker

**Demonstrated:** The job and request-key mapping are saved before `queue.push`. If push raises `RuntimeError`, the adapter returns 503, but a retry finds the saved key and returns the pending job without attempting dispatch again.

**Failure scenario:** The queue rejects the first push. The browser retries after the 503 or an ambiguous network timeout. It repeatedly receives the same pending export, which has no queued work.

**Smallest fix:** Persist recoverable dispatch intent with the logical export and provide a retry path for unconfirmed dispatch. Preserve the ID and key mapping. The mechanism remains a product/implementation choice; its required outcome is eventual dispatch without creating another logical export.

**Acceptance checks:** Inject one push failure before acceptance, restore the queue, and verify completion under the original ID. Also cover an ambiguous push that accepts work before reporting failure: recovery must tolerate duplicate delivery without creating another export.

### 3. Renderer timeout or worker interruption has no recovery path — blocker

**Demonstrated:** A renderer timeout marks the job `failed`; a worker interruption can leave it `running`. Queue consumption removes the message, failed calls are not requeued, and submission retries only return the existing job. Although a direct later `run_export` call can retry either state, no mechanism that makes that call is supplied.

**Failure scenario:** A worker consumes the message and times out or stops. After restart, the durable job remains available but never progresses, unless someone manually supplies another worker invocation.

**Smallest fix:** Add bounded recovery for failed work and abandoned running attempts, using the original export ID. Track attempt ownership or expiry so recovery can distinguish abandoned work from active work.

**Acceptance checks:** Simulate one renderer timeout and one interruption after consumption, then restart with the same store. Each export must complete under its original ID without support creating a replacement. A timeout-created temporary object must remain undisclosed.

### 4. Duplicate execution and completion visibility need focused checks

**Demonstrated protection:** Sequential delivery after `complete` returns before rendering.

**Missing evidence:** Concurrent workers can both pass that guard; no atomic claim is shown. Also, `download_location` is assigned before state becomes `complete`, while `_view` returns it unconditionally. Whether a reader can observe that intermediate state depends on storage atomicity, which is unspecified.

**Smallest fix/check:** Enforce one active attempt per job; publish completion atomically or suppress locations in every non-complete view. Verify a delivery after completion causes no renderer call, overlapping deliveries do not render concurrently, and pending/running/failed responses never expose a location.

### Evidence limits and pilot scope

Existing tests cover a sequential same-member retry, an owner’s completed-state read, and inactive-member submission denial. They do not establish isolation or recovery.

Atomic simultaneous key creation is also unproven: require concurrent same-workspace submissions to return one logical export. Define how reusing a key with different filters behaves; the snapshot silently returns the original filters.

Authentication adapters are outside scope. CSV exports, article titles, and ZIP artwork do not block this pilot.