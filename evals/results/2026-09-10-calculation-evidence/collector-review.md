# Collector review and verification

Independent read-only review covered `evals/session_tools.py`, the runner's
opt-in capture integration, and the focused tests. It found one medium-severity
contract issue: buffered header reading could prefetch body bytes before
identity/workspace/source/freshness checks. Rejected sessions still exported
nothing, so this was not a demonstrated export leak.

The strengthened regression measures the underlying file descriptor position
immediately after `readline()`. Before the fix, all seven metadata-mismatch
subcases failed: the stream had read 25 bytes beyond the header. Setting
`buffering=0` made the session suite pass. The independent reviewer repeated
an in-memory mutation back to buffered mode and reproduced all seven failures.
No private host session was read by that review or its synthetic tests.

The review otherwise found no actionable defect in canonical UUID matching,
source/cwd/freshness binding, descriptor-relative no-follow traversal, ambiguous
source rejection, tool-only export, raw provenance, or separate capture/process/
integrity statuses. That is a bounded source review, not a proof against every
possible host change or arbitrary untrusted local process.

The source was frozen during all five captured task runs. After the stream
repair, [re-extraction](attempt-3/reextraction-check.json) with the final helper
produced byte-identical tool records from the same five source hashes. Original
metadata retains the helper hash actually used at task completion.

Windows CI does not provide the required descriptor-relative traversal. The
optional collector fails explicitly there; default ephemeral evaluation and
the installer remain independent of this feature. Capture-dependent tests are
capability-gated. Portable tests still assert unavailable status, nonzero runner
result, retained outputs, and no host-source opens when capabilities are absent.
The focused suite passed 46 tests with zero skips on the development host; a
simulated capability-absent run passed 33 and explicitly skipped 13, including
one pre-existing descriptor snapshot test. Actual Windows evidence belongs to CI.

Source/message exclusion is not a general data sanitizer: tool arguments and
results can contain task data. Only synthetic task content is published here.
The full host sessions are retained locally and are not included in this report.
