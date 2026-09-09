**Recommendation: hold the two-workspace pilot until access isolation and recovery are corrected and checked.** The supplied snapshot conflicts with explicit pilot requirements in the following scenarios. These are static findings, not observed runtime failures.

1. **Another workspace’s export is accessible through both reads and repeated requests.**

   `product-notes.md:3–7` prohibits disclosure of another workspace’s status, filters, or download location. However, `implementation.py:47–49` retrieves any known export ID without checking its workspace. Separately, lines 33–34 use a globally keyed request lookup.

   **Scenario:** Workspace B reads workspace A’s export ID, or independently submits the same request key. B receives A’s export view, including its download location if complete. The key collision also prevents B from creating its own export.

   **Smallest fix/check:** Require workspace ownership before returning any export view and scope request keys by authenticated workspace. Check cross-workspace reads for pending and complete exports; neither may disclose protected fields. Submit an identical key in A and B and verify distinct, correctly owned exports. Preserve same-workspace retry reuse.

2. **A queue outage strands an accepted export permanently.**

   `product-notes.md:9–19` requires safe submission retries and recovery from one queue outage. `implementation.py:42–44` saves the job and request key before pushing the message.

   **Scenario:** Queue push raises `RuntimeError` before accepting the message. The adapter returns 503, but the pending job and key remain. Retrying the same submission takes the early return at lines 33–34 and never queues work. A new key would create a different logical export, contrary to the requirement.

   **Smallest fix/check:** Provide a recoverable dispatch path for saved, unfinished jobs; the precise mechanism remains a proposed implementation choice. Fail the first push, restore the queue, and verify recovery completes the original export ID without a replacement key. Also check an ambiguous submission timeout after acceptance: retry must still identify the same logical export.

3. **Renderer failure and worker interruption have no supplied recovery trigger.**

   `product-notes.md:14–21` specifies recovery, at-most-once queue consumption, and restart access to the same store. `implementation.py:55–60` leaves a renderer timeout as `failed`; a process interruption after setting `running` leaves that state behind. Neither request retries nor any supplied recovery routine schedule another attempt.

   **Scenario:** The worker consumes the only message, then times out or stops. Restarting restores access to the stranded job but supplies no work to resume it. Calling `run_export` manually could retry it; that is not an established recovery journey.

   **Smallest fix/check:** Define a trigger to retry failed jobs and reclaim interrupted running jobs using the existing ID. Check one renderer timeout followed by success, and interruption after consumption followed by restart. Both must reach completion without creating another export. A timeout-created temporary object must remain unavailable as a download.

4. **An interruption can expose a download location before completion.**

   `product-notes.md:21` permits download exposure only for complete jobs. `implementation.py:61–62` writes the location before marking completion, while `_view` exposes the location unconditionally at line 28.

   **Scenario:** Execution stops between those writes. The retained job is still `running` but its status response exposes a location.

   **Smallest fix/check:** Gate the returned location on `state == "complete"` or establish an atomic completion update. Check interruption at this boundary and assert every noncomplete response has no download location. Adapter atomicity is unavailable, so the snapshot does not establish protection against this window.

The existing tests (`test_existing.py:16–35`) cover sequential same-workspace reuse, an owner reading completion, and inactive-member submission denial. They contain no checks for the failures above and are not execution evidence. Static inspection also supports session-derived workspace assignment and a completed-job guard (`implementation.py:37,53–54`). Add a duplicate delivery check after completion that asserts no further renderer call.

For overlapping same-workspace submissions, the lookup/create sequence has no visible atomic protection (`implementation.py:33–44`). Concurrent execution and store guarantees are unavailable; verify this condition before claiming retry safety under overlap.

I inspected all five input files. Support’s cosmetic changes and CSV work are outside this pilot. No files changed; no code or tests ran. Authentication, storage, queue, and renderer adapters remain uninspected, and no runtime or customer evidence was supplied. The next useful step is the focused acceptance checks above against the corrected service and its actual adapter contracts.