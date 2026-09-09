**Recommendation: hold activation for both pilot workspaces.** Static inspection identifies cross-workspace disclosure and recovery paths that can leave an export permanently unfinished. The scope is limited to access boundaries, repeated requests, and recovery.

1. **Cross-workspace access is not enforced on reads or request-key reuse.**  
   Product notes (`input/product-notes.md:3–7`) prohibit exposing another workspace’s status, filters, or download location. However, `get_export` checks only active membership, and request keys are indexed globally (`input/implementation.py:31–49`).

   **Scenario:** Workspace B requests an ID belonging to A, or independently submits A’s request key. Both paths return A’s export view, potentially including its download location.

   **Smallest fix/check:** Check job ownership before returning any view and scope request-key lookup by authenticated workspace. Verify that B cannot read A’s export by ID; identical keys in A and B produce separate exports; neither response discloses foreign fields. Preserve checks rejecting inactive sessions on both endpoints. New jobs already take their workspace from the session, consistent with the notes.

2. **Changed filters under the same key need an explicit product decision.**  
   The notes promise one logical export for retries of the “same operation,” but do not define reuse with changed content (`input/product-notes.md:9–12`). The implementation ignores newly supplied filters whenever a key exists (`input/implementation.py:33–38`).

   **Scenario:** A member submits August filters, then September filters with the same key. The service silently returns the August export, which could lead to downloading the wrong attachment set.

   **Smallest decision/check:** Define operation identity using workspace, key, and relevant filter content. A conservative proposed policy is to reject changed-content reuse while preserving the original export. If adopted, verify that an exact retry returns the original ID without another logical export, while changed filters yield an explicit conflict and leave the original unchanged. If replacement or a new operation is chosen instead, acceptance checks must require that declared outcome.

3. **A queue outage can strand an accepted export before delivery.**  
   Recovery from one queue outage is required (`input/product-notes.md:14–19`). The implementation saves the job and key before pushing the message; subsequent submissions return the saved job without attempting delivery (`input/implementation.py:42–44`, `33–34`).

   **Scenario:** Queue push raises `RuntimeError` before accepting the message. The adapter returns 503. After the queue recovers, the browser retries the same request, but receives a permanently pending export with no queued work.

   **Smallest fix/check:** Provide recoverable dispatch for the existing job, such as retrying an outstanding dispatch record. Inject one push failure, restore the queue, and verify eventual completion under the original ID. Also check an ambiguous push outcome—message accepted before an error—so recovery remains safe if delivery is duplicated.

4. **Consumed work has no supplied recovery path after timeout or interruption.**  
   Queue delivery removes the message, and failed calls are not requeued (`input/product-notes.md:18–21`). A renderer timeout marks the job failed; a process interruption can leave it running (`input/implementation.py:51–60`). Request retries merely return those states. Although directly calling the worker again can retry an unfinished job, no supplied mechanism arranges that call.

   **Scenario:** The worker consumes a message and times out or exits during rendering. Restarting with the same job store does not, by itself, resume the export.

   **Smallest fix/check:** Add a bounded retry/reclaim path for failed or abandoned work using the same logical export. Verify recovery after one renderer timeout and after worker interruption, preserving the ID and exposing no download location until completion. Then deliver completed work again and assert zero additional renderer calls. The existing complete-state guard supports that last behavior statically; it is not tested here.

**Evidence and limits:** Inspected all five `input/` files. The three existing tests cover sequential exact retry, an owner reading completion, and inactive submission rejection (`input/test_existing.py:15–35`). They do not cover the failures above and are test definitions, not passing execution evidence. No code or tests were run; no files changed. Adapters remain outside scope, and these synthetic artifacts provide no customer or runtime evidence. The next useful step is to settle changed-content reuse and execute the targeted checks above against the corrected implementation.