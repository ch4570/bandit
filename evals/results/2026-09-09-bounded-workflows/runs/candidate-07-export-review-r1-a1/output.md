**Recommendation: hold the two-workspace pilot** until workspace isolation and recovery of the same logical export are addressed. The supplied implementation suggests direct conflicts with the product notes; these are static findings, not observed runtime failures.

1. **Export lookup and repeated submissions can disclose another workspace’s data.**  
   `product-notes.md:3–7` forbids disclosure of another workspace’s status, filters, or download location. In `implementation.py:31–34`, request keys are global and a matching key returns the stored job without checking its workspace. `get_export` likewise checks active membership but not job ownership (`:47–49`).

   **Scenario:** workspace A creates an export; an active member of B submits the same key or requests A’s export ID. The inspected paths return A’s export view, including its filters and potentially its download location.

   **Smallest fix/check:** scope request keys by authenticated workspace and authorize job ownership before returning either response. Verify that two workspaces using the same key receive distinct exports, and that B cannot retrieve A’s export by ID. Include completed exports so download-location disclosure is covered.

2. **A queue outage strands an accepted export despite a successful browser retry.**  
   `product-notes.md:9–19` requires safe submission retries and recovery from one queue outage without creating another logical export. `implementation.py:42–44` stores the job and request key before queue submission. If `push` raises `RuntimeError`, the adapter returns 503, but retrying the key returns the pending job without attempting dispatch (`:33–34`).

   **Scenario:** the queue rejects the first submission before accepting a message. The browser retries after 503 and receives an export that has no queued work.

   **Smallest fix/check:** retain a recoverable dispatch obligation for that job and retry dispatch through an explicit mechanism. With the first push failing, verify eventual completion after recovery using the original key and export ID. Also cover an ambiguous push outcome—message accepted, response lost—without creating a second logical export.

3. **Renderer failure or worker interruption has no recovery trigger.**  
   `product-notes.md:14–21` specifies at-most-once delivery, no automatic requeue, and a shared job store after restart. `implementation.py:55–60` leaves a renderer timeout as `failed`; interruption after marking the job `running` leaves that state behind. Neither submission retry nor any supplied recovery path schedules those jobs again.

   **Scenario:** a worker consumes the message and then times out or stops. The user repeatedly receives the same failed or running export, but it never completes. Calling `run_export` again could retry it; the missing piece is a mechanism that actually does so.

   **Smallest fix/check:** adopt a bounded retry/reconciliation mechanism for failed and abandoned jobs, preserving their IDs. Verify recovery after one renderer timeout and after a worker restart following message removal, without support creating another export.

4. **Download visibility is not explicitly gated on completion.**  
   `product-notes.md:21` allows a download location only for a complete job. `_view` returns the stored location unconditionally (`implementation.py:22–28`), while completion writes the location before changing state (`:61–62`).

   **Scenario:** a read or interruption between those writes could expose a location while the job remains running. Whether that interval is externally visible depends on storage atomicity, which the snapshot does not establish.

   **Smallest fix/check:** return no download location unless state is `complete`; verify a persisted running job containing a location still hides it. Renderer timeout alone does not assign a location in the inspected code.

5. **Repeated-request guarantees need targeted concurrency and payload checks.**  
   The sequential same-key path returns one job, but lookup and creation are separate operations (`implementation.py:33–44`). Concurrent submissions could create two jobs unless the shared store provides atomic uniqueness. Same-key submissions with changed filters silently return the original export; the notes do not define that case.

   **Smallest fix/check:** enforce atomic workspace/key uniqueness and verify concurrent identical submissions return one ID. Define changed-filter behavior; rejecting conflicting reuse is a small, explicit option. The completed-worker guard (`:53–54`) supports sequential duplicate delivery, but has no supplied test; verify the renderer is not called again after completion.

I inspected all four supporting artifacts and the request. `test_existing.py:16–35` contains only sequential retry, own-workspace completed-read, and inactive-request cases; none were executed. Support’s cosmetic changes and CSV work are explicitly outside pilot scope. Adapter behavior, storage atomicity, runtime results, and customer evidence remain unavailable. The next useful step is the focused acceptance checks above after the proposed corrections; existing test presence does not establish pilot readiness.