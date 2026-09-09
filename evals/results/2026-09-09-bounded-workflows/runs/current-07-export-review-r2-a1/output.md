**Recommendation: hold the two-workspace pilot until access isolation and recovery are corrected and verified.** Static inspection identifies paths that contradict the product notes; no runtime failures were observed because code and tests were not executed.

Reviewed `input/product-notes.md`, `input/implementation.py`, `input/test_existing.py`, and `input/support-handoff.md`. The handoff adds no requirements within this review’s scope.

1. **Cross-workspace access is possible through both lookup paths.**  
   Product notes lines 3–7 prohibit exposing another workspace’s status, filters, or download location. However, `implementation.py:33–34` indexes request keys globally, and lines 47–49 retrieve an export without checking its workspace.

   **Scenario:** workspace A creates an export. An active member of B either supplies A’s export ID or independently submits the same request key. Both paths return A’s export view; key reuse also prevents B from creating its own export.

   **Smallest fix/check:** scope request keys by authenticated workspace and enforce workspace ownership before returning any existing job. Check that A and B using identical keys receive distinct exports, B cannot retrieve A’s export by ID, and neither path discloses A’s fields. Retain same-workspace retry behavior. Creation already uses the session workspace; the defect is in retrieval.

2. **A queue outage leaves a saved export with no recovery path.**  
   Product notes lines 14–19 require recovery from one queue outage without a different logical export. In `implementation.py:42–44`, the job and key are saved before queue submission. If `push()` raises `RuntimeError` before accepting the message, the adapter returns 503, but a retry returns the saved pending job without attempting dispatch.

   **Consequence:** the browser’s prescribed retry can report an export that never runs.

   **Smallest fix/check:** retain recoverable dispatch state and provide a retry path for the same job. Simulate one rejected queue submission, then retry with the original key: the original ID must eventually complete. Also check an ambiguous submission where the queue accepted the message before the response failed; recovery must tolerate duplicate delivery.

3. **Renderer failure or worker interruption consumes the only delivery.**  
   Product notes lines 18–21 specify at-most-once delivery, no automatic requeue, and restart access to the shared job store. `implementation.py:55–60` leaves a renderer timeout as `failed`; interruption after setting `running` can leave that state indefinitely. Repeating the submission only returns the existing job (`33–34`).

   **Consequence:** neither restarting the worker nor retrying the browser request schedules recovery. Although explicitly calling `run_export()` again could retry, no supplied path arranges that call.

   **Smallest fix/check:** choose a bounded recovery mechanism for failed and abandoned running jobs that preserves their ID. Check one renderer timeout followed by success, and interruption after message removal followed by restart. Both must complete the original export without requiring a new key.

4. **A download location can be exposed before completion.**  
   Product notes line 21 permits download exposure only for complete jobs. `implementation.py:61–62` assigns the location before changing the state, while `_view()` returns it unconditionally (`22–28`).

   **Scenario:** interruption between those assignments leaves a running job with a visible location; a concurrent status read could also encounter that intermediate state.

   **Smallest fix/check:** suppress the location unless state is `complete`, and publish completion consistently. Check a stored non-complete job with a populated location: its public view must hide that location.

5. **Sequential deduplication does not establish overlapping-request safety.**  
   Product notes lines 9–12 promise one logical export for repeated submissions. `implementation.py:33–44` separates key lookup from job/key creation without an atomic claim.

   **Scenario:** if requests overlap, both can find the key absent and create separate exports. The supplied snapshot does not establish adapter-level serialization or atomic uniqueness.

   **Smallest fix/check:** make the workspace/key claim atomic. Submit overlapping identical requests and require one logical ID. Separately, verify duplicate worker delivery after completion makes no renderer call—the complete-state guard exists (`53–54`), but current tests do not cover it.

The three existing tests cover sequential retry, an owner reading completion, and inactive-member submission rejection. They are test definitions, not passing execution evidence. No customer evidence or adapter execution results were supplied; the dictionaries explicitly represent durable stores, so process-local storage is not a finding. The next useful gate is targeted execution of the acceptance checks above after correction. All files remain unchanged.