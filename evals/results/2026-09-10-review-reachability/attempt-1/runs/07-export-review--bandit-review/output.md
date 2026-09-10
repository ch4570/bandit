**Recommendation: hold the two-workspace pilot until access isolation and recovery are corrected and checked.** The supplied snapshot exposes cross-workspace data and leaves accepted exports stranded after the failures the pilot promises to recover from.

This is a static review of all five `input/` files. Product notes establish intended behavior; implementation and test files provide source evidence, not observed runtime results. No code or tests were run, and no files were changed.

1. **Cross-workspace access is possible through both lookup and request-key reuse.**  
   Sources: `product-notes.md:3–7, 9–11`; `implementation.py:31–34, 47–49`.

   An active member of workspace B who knows workspace A’s export ID can call `get_export` and receive A’s filters, status, and download location. Alternatively, B can submit a request key already used by A: the global key lookup returns A’s export without checking ownership. Independently chosen keys therefore cause both disclosure and incorrect export selection.

   **Smallest correction:** scope request keys by authenticated workspace and enforce job ownership before returning any view, including retry responses.

   **Acceptance checks:** create an export in A; B’s lookup by its ID must return no export data. Submit the same key independently in A and B; each must receive its own workspace’s export. Repeat after A completes to check download-location isolation. Preserve active-membership checks on both request and status paths.

2. **A queue outage leaves a stored export that submission retries cannot dispatch.**  
   Sources: `product-notes.md:9–15, 18`; `implementation.py:33–44`.

   If `queue.push` raises `RuntimeError` before accepting the message, the job and request key already exist. The client receives a 503, but retrying the same key returns the pending job without another dispatch attempt. It can remain pending indefinitely despite the required recovery from one queue outage.

   **Smallest correction:** provide a recoverable dispatch path for the existing job. Preserve its ID and key; do not require a new logical export. The retry mechanism remains a design choice.

   **Acceptance checks:** inject one push failure before acceptance, restore the queue, and invoke the chosen recovery path. The original export must complete with the same ID. Separately check a lost response after successful acceptance: retry must still identify that export, and any duplicate delivery must not regenerate it after completion.

3. **Renderer timeout and worker interruption have no reachable recovery path in the supplied flow.**  
   Sources: `product-notes.md:14–21`; `implementation.py:33–34, 51–60`.

   A renderer timeout marks the job failed and raises. Because delivery removes the message and failed calls are not requeued, no subsequent worker invocation is arranged. A worker interruption after setting `running` similarly leaves an unfinished job in the shared store. Restarting with that store does not itself schedule recovery; repeating the browser request only returns the stored view.

   **Smallest correction:** choose an explicit recovery trigger that retries eligible failed or abandoned jobs under their original IDs. Define when a running job is considered abandoned so recovery does not mistake active work for interruption.

   **Acceptance checks:** use the stated at-most-once delivery behavior, consume the message, then inject one renderer timeout. After recovery, the same export must complete. Separately interrupt a worker after `running`, restart against the same store, and demonstrate recovery without a replacement export. Directly calling `run_export` twice would not establish that the recovery trigger works.

4. **Download visibility is not guarded by completion state.**  
   Sources: `product-notes.md:20–21`; `implementation.py:22–28, 61–62`.

   The worker stores the location before marking the job complete, and `_view` returns the location regardless of state. A read or interruption between those writes could expose a download location while the job remains running. Whether that window is externally observable depends on the unavailable storage adapter’s atomicity; the snapshot supplies no guard.

   **Smallest correction:** return no download location unless state is `complete`; publish completion and location together where supported.

   **Acceptance check:** a non-complete stored job containing a location must still return no location. Also check that a renderer timeout which creates a temporary object does not make it downloadable through the export response.

5. **Reusing a key with changed filters needs an explicit product decision.**  
   Sources: `product-notes.md:9–12`; `implementation.py:33–38`.

   The notes define exact retries but do not settle changed-content reuse. If a member submits August filters, then September filters under the same key, the implementation silently returns the August export. The UI may associate that response with the September request.

   **Proposed resolution:** reject changed filters under an existing workspace/key, requiring a new key for a new operation. This preserves reliable retries, but is a recommendation, not an adopted requirement.

   **Conditional acceptance check:** if adopted, identical filters return the same ID; changed filters produce an explicit conflict without altering or dispatching the existing job.

The existing tests (`test_existing.py:16–35`) cover sequential identical retries, an owning member reading completed status, and inactive submission rejection. They do not cover the findings above. Source inspection also shows session-derived workspace assignment and a guard against deliveries that begin after completion (`implementation.py:53–54`); add a duplicate-delivery check asserting no additional renderer call.

Concurrent submission atomicity remains unverified because storage adapters are excluded. Check overlapping identical requests against the actual store for one logical export. The next useful step is the focused acceptance checks above, including real recovery scheduling. Support handoff items do not change this pilot’s boundaries.