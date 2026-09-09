# Independent static review

A separate reviewer inspected the round-6 implementation and test changes
without editing files, executing tests, adding fault probes, or retrying the
blocked diagnostic. It found no blocking defect on the ordinary paths examined.
This is code inspection, not execution evidence or a completeness guarantee.

The review confirmed three limitations:

- If writing, flushing, or identity capture fails before a completed staging
  identity is available, the unverified temporary file may remain. This can
  leave unmanaged staging debris after an ordinary I/O failure.
- A lock identity-capture or close failure before registration in the acquired
  lock list can leave that lock unregistered for cleanup. This existing
  exceptional-path limitation was inferred from the code, not reproduced in
  this round and not corrected by the staged-source patch.
- Destination/staged-source checks and pathname replacement are separate;
  a final check-to-use interval remains.

The two languages' new regression injections have different timing. Node
changes the staged pathname immediately after writing, before descriptor
identity capture. Python injects during the destination reread, after completed
identity capture. Each uses the same test before and after its implementation
change, but the cross-language runs are not identical filesystem interleavings.
Neither new staging test covers write/flush failure or asserts parent-directory
lock cleanup; existing installer tests remain separate coverage.

No unsupported Node 22 or Python 3.11 API/syntax was apparent to the reviewer.
Actual local runtime results are retained in the full test logs. Other operating
systems and filesystems were not executed as part of this round.
