**Recommendation: hold the two-workspace pilot until access isolation and recovery are corrected.** Static inspection identifies paths that conflict with the product notes. Repeated-request identity also needs one explicit product decision.

Reviewed all four supporting files: product notes, implementation, existing tests, and support handoff. No code or tests were executed. These are synthetic artifacts, with no runtime results or customer evidence supplied.

1. **Cross-workspace information is exposed through two paths.**  
   `product-notes.md:3–7` prohibits receiving another workspace’s status, filters, or download location. However, `implementation.py:47–49` reads any known export ID after checking only active membership. Separately, `implementation.py:31–34` looks up request keys globally. If workspace A submits a key and workspace B reuses it, B receives A’s export view, potentially including its completed download location.

   **Smallest fix/check:** Require workspace ownership before returning any export; scope request-key lookup and storage by authenticated workspace. Check that B cannot read A’s pending or completed export by ID, and that identical keys in A and B create separate exports with no cross-workspace fields returned. Preserve same-workspace retries and inactive-member rejection.

2. **An exact retry can remain stranded after a queue outage.**  
   `product-notes.md:9–19` promises safe submission retries and recovery without a different logical export. In `implementation.py:42–44`, the job and key are stored before queue submission. If `push()` raises `RuntimeError` before accepting the message, the adapter returns 503, but retrying the same key merely returns the existing pending job without submitting work (`33–34`). There is no supplied recovery path.

   **Smallest fix/check:** Retain recoverable dispatch state and provide a retry or reconciliation path for that same job. Inject one queue failure, retry the original submission, and verify eventual completion under the original export ID. Also check interrupted submission after persistence but before dispatch.

3. **Renderer failure and worker interruption have no recovery trigger.**  
   `product-notes.md:14–20` specifies at-most-once delivery, no requeue after failure, and restart access to the same store. `implementation.py:55–60` leaves a timeout as `failed`; process interruption can leave `running`. Repeating the request returns that state without scheduling another attempt. Although calling `run_export` again could retry it, nothing supplied causes that call after the message is removed.

   **Smallest fix/check:** Add a bounded recovery path for failed and abandoned running jobs, preserving their IDs and avoiding jobs still actively running. Check one renderer timeout followed by success, and a restart after message removal/before completion. Both must complete the original logical export without support creating another.

4. **A download location can be exposed before completion.**  
   `product-notes.md:20–21` allows exposure only for completed jobs. In `implementation.py:61–62`, location is assigned before completion; `_view` returns it unconditionally (`22–29`). Interruption between those assignments can leave a stored `running` job exposing a location.

   **Smallest fix/check:** Gate the returned location on `state == "complete"` and make completion publication atomic where supported. Check a persisted running job with a location: reads must hide it. Check that timeout-created temporary objects are never exposed.

5. **Reusing a key with changed filters has no adopted meaning.**  
   `product-notes.md:9–12` defines retries of the “same operation,” but does not settle changed-content reuse. `implementation.py:33–34` silently returns the earlier export regardless of new filters. A member changing the requested month while retaining the key could receive the wrong attachment set.

   **Smallest decision/check:** Adopt an explicit policy. Recommended: identical filters reuse the export; changed filters produce a clear conflict without changing or dispatching the original job. Test both cases. This is a proposed policy, not an existing requirement.

The existing tests (`test_existing.py:16–35`) cover sequential exact retry, owner reading completion, and inactive submission rejection; their execution status is unknown. The completed-worker guard (`implementation.py:53–54`) supports skipping later duplicate deliveries, but lacks a corresponding test. Add a renderer-call-count check. Concurrent request deduplication and worker claiming also remain unverified; check simultaneous submissions/deliveries against the chosen durable-store behavior.

The next useful evidence is these targeted acceptance checks against the corrected implementation. Adapter internals remain outside scope; dictionary representation does not establish a durability defect. The support handoff adds no relevant blocking requirement.