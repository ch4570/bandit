**Recommendation: hold activation for both pilot workspaces.** The supplied implementation exposes cross-workspace export data and lacks a demonstrated recovery path after queue or worker failure. The repeated-request policy also needs one clarification.

This review inspected all five `input/` files as documents and source. No code or tests were executed, and no files were changed. Findings below describe behavior implied by the snapshot, not observed production failures.

1. **Workspace isolation is missing on both lookup paths.**  
   `product-notes.md:3–7` prohibits returning another workspace’s status, filters, or download location. However, `implementation.py:31–34` resolves request keys globally, while `47–49` retrieves an export by ID after checking only active membership.

   **Scenario:** workspace B submits a key already used by A, or requests A’s known export ID. Both paths return A’s export view, including its download location if populated. Independent key selection makes this relevant even without deliberate probing.

   **Smallest fix/check:** scope request keys by authenticated workspace and enforce workspace ownership before returning any export view. Check that A and B using the same key receive distinct exports; B cannot read A’s pending or completed export by ID; and inactive sessions cannot retrieve exports. Preserve the existing session-derived workspace assignment.

2. **Reuse of a key with changed filters has no agreed meaning.**  
   `product-notes.md:9–12` defines retries of the “same operation,” but does not resolve changed content under the same key. `implementation.py:33–34` silently returns the original export without comparing filters.

   **Scenario:** a user changes August to September but retains the key. The service returns August’s export, potentially causing the wrong attachment set to be used.

   **Required decision/check:** define operation identity and changed-filter behavior. For this pilot, rejecting changed filters with an explicit conflict is a small proposed resolution that preserves the original job. If adopted, verify identical retries return the same ID, changed filters receive a conflict, and the original filters remain unchanged. If replacement is chosen instead, specify which version subsequent retries identify. Also verify simultaneous identical submissions produce one logical export; the snapshot’s check-then-create sequence does not establish atomicity.

3. **A queue outage can strand an accepted export.**  
   Recovery without creating a different logical export is required by `product-notes.md:14–19`. In `implementation.py:42–44`, the job and request-key mapping are saved before enqueueing.

   **Scenario:** `queue.push` raises `RuntimeError` before accepting the message. The documented adapter returns 503, but the browser’s same-key retry finds the saved job and returns it without enqueueing. The export remains pending indefinitely.

   **Smallest fix/check:** provide retryable dispatch for saved, undispatched jobs, preserving their IDs. Inject one pre-acceptance queue failure, restore the queue, and verify the same-key retry or recovery mechanism completes the original export. Also cover interruption between saving the job and saving its key mapping: retry must not create a second logical export.

4. **Renderer timeout and worker interruption have no recovery trigger.**  
   `implementation.py:51–60` marks renderer timeouts failed; interruption after setting `running` can leave a job running. `product-notes.md:18–20` explicitly says queue messages are removed on delivery and failed calls are not requeued. Browser retries only return the existing job.

   **Scenario:** the sole delivery times out or its worker stops. Although another `run_export` call could retry that job, nothing supplied causes that call.

   **Smallest fix/check:** adopt a bounded retry or recovery mechanism for failed and abandoned running jobs, keeping the same logical export. Verify one renderer timeout and one worker restart each lead to completion of the original ID. Separately verify a duplicate delivery after completion never invokes the renderer; the existing completion guard supports that requirement, but the supplied tests do not check it.

5. **Download visibility is not explicitly gated on completion.**  
   `product-notes.md:20–21` permits locations only for completed jobs. `implementation.py:61–62` assigns the location before marking completion, and `_view` exposes it unconditionally (`22–29`).

   **Scenario:** an intervening read or interruption exposes a location while state remains running. Whether storage makes these updates atomic is unavailable.

   **Smallest fix/check:** gate returned locations on `complete`, or establish an atomic completion update. Verify pending, running, and failed views never expose a location.

`test_existing.py:16–35` covers sequential identical retries, same-workspace completed reads, and inactive submission rejection only. No execution results establish readiness. The next useful evidence is the focused acceptance checks above; adapter behavior beyond the supplied contracts remains unverified.