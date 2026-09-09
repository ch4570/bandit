# Preserve the failed local-tarball invocation

The first [harness](checks/npx-flow.mjs) and [pre-run receipt](before-run.json)
remain unchanged. Its [terminal failure](attempt1/failure.json) records a
test-command mistake, not a BANDIT installer rejection: under Node 22.23.2 and
npm 11.19.0, positional `npx --yes /absolute/candidate.tgz --plan --json`
attempted to execute the archive path and exited 126 with permission denied.
The candidate installer did not run. The documented public URL install and
unchanged repeat had already succeeded; the original scratch files remain.

The [second harness](checks/npx-flow-v2.mjs) changes only candidate argument
construction to `npx --yes --package=/absolute/candidate.tgz -- bandit ...`.
Public 0.4.0 and bootstrap 0.3.0 commands retain their original positional URLs.
This follows the explicit package/command form in the
[npm npx documentation](https://docs.npmjs.com/cli/v11/commands/npx/).
No permission bit, installer behavior, expected assertion, or rubric is changed
to make the first command pass. The failed source and logs remain visible.

The second run uses a different fresh scratch directory and initially empty
caches. This is a corrected engineering invocation after a terminal failure,
not a restart caused by a timeout, and neither attempt is a planning TASK.
