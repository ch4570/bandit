Hold the two-workspace pilot until access isolation and recovery are corrected. The supplied snapshot exposes cross-workspace data and has no recovery path for accepted exports whose queue submission or worker execution fails.

This review covers all five `input/` files through document and static code inspection only. No code or tests were executed. Product notes establish intended behavior; code suggests implementation behavior; existing tests establish coverage intent, not passing results. Authentication, storage, queue, and renderer adapters remain outside the supplied evidence.

1. **Export IDs bypass workspace isolation.**  
   **Source:** `product-notes.md`, access rules; `implementation.py:47–49`.  
   An active member of workspace B who knows workspace A’s export ID can retrieve A’s status, filters, and download location. `get_export` checks active membership but never checks ownership.  
   **Smallest fix:** Require the stored workspace to match the authenticated session before returning any export view.  
   **Acceptance check:** Create A’s export; attempt reads from B while pending and complete. Both must deny access without returning protected fields. Preserve A’s permitted read and verify inactive members cannot read.

2. **Request keys cross workspace boundaries.**  
   **Source:** `product-notes.md`, access and retry rules; `implementation.py:31–44`.  
   If A submits `key-1`, B’s independent submission of `key-1` returns A’s export, including its filters and any completed download location. B also fails to create its own export.  
   **Smallest fix:** Scope key lookup and reservation to `(session.workspace_id, request_key)` and enforce ownership before returning an existing job.  
   **Acceptance check:** Identical keys in A and B produce distinct, correctly owned exports. Repeating each request returns its own original ID.

3. **A queue outage strands the accepted export.**  
   **Source:** `product-notes.md`, timeout and queue-outage rules; `implementation.py:42–45`, with duplicate return at `33–34`.  
   The job and key are stored before queue submission. If `push` raises `RuntimeError` before accepting the message, the adapter returns 503. Retrying the same key returns the pending job without attempting delivery; it can remain pending indefinitely.  
   **Smallest fix:** Add recoverable dispatch for the existing job, with dispatch intent retained until delivery is resolved. Same-key retries must retain the logical export ID. The exact retry mechanism is a proposed implementation decision, not an approved requirement.  
   **Acceptance check:** Fail the first queue push, restore the queue, and retry the submission. The original job must eventually complete without a new key or logical export. Also check a lost HTTP response after successful submission.

4. **Consumed worker failures and interruptions have no recovery path.**  
   **Source:** `product-notes.md`, at-most-once delivery and restart rules; `implementation.py:51–62`.  
   A renderer timeout marks the job failed, but its message has already been removed. A process interruption after marking it running can leave it running indefinitely. Restarting with the same store does not itself schedule either job; same-key submissions only return status.  
   **Smallest fix:** Define a bounded recovery mechanism for failed and abandoned running jobs that resumes the same logical export. Recoverable worker ownership must distinguish abandoned work from work still executing.  
   **Acceptance check:** Consume a message, inject one renderer timeout, restore rendering, and verify completion under the original ID. Separately interrupt a worker after it marks the job running, restart with the retained store, and verify recovery. Failed or unfinished jobs must expose no download location.

5. **Atomicity and duplicate protection remain unverified.**  
   **Source:** `implementation.py:33–44, 53–62`; `test_existing.py:16–35`.  
   Sequential completed deliveries are guarded, but concurrent requests can both pass the key check, and overlapping workers can both pass the completion check unless an unavailable adapter serializes them. The location is also assigned before the complete state, creating a possible interrupted-publication gap.  
   **Smallest checks/fixes:** Verify atomic key reservation and worker ownership; publish completion and location atomically, or hide location unless complete. Check simultaneous same-key submissions, overlapping deliveries, interruption during publication, and replay after completion with no renderer invocation.

Existing tests cover only sequential same-workspace retries, an owner’s completed read, and inactive-member submission denial. These targeted checks are the next useful pilot gate; none has an observed result here. Files remain unchanged.