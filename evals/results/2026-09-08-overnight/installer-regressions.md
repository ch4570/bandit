# Installer concurrency regression reproduction

Executed 2026-09-08 on macOS with Node v26.8.1. The before run used a fresh
`git archive HEAD` of commit f4a376e and the current three new Node regression
tests copied into it. The after run used the current working tree. Fixtures
create isolated temporary installations; no user installation was modified.

Command in each checkout:

```sh
node --test --test-name-pattern='preflighted|staged|retired file edits after' tests-node/install.test.mjs
```

Before: exit 1. All three tests failed because the old installer did not
reject the injected concurrent edits. The assertion stops before the test's
subsequent full filesystem snapshot comparison.

```text
✖ an edit made while later skills are being preflighted cannot become an overwrite baseline (663.194708ms)
✖ an edit made while a replacement is being staged is preserved with earlier writes rolled back (657.033666ms)
✖ retired file edits after their preflight stop every update and removal (561.062583ms)
ℹ tests 3
ℹ suites 0
ℹ pass 0
ℹ fail 3
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 1960.670292

✖ failing tests:

test at tests-node/install.test.mjs:408:1
✖ an edit made while later skills are being preflighted cannot become an overwrite baseline (663.194708ms)
  AssertionError [ERR_ASSERTION]: Missing expected exception.
      at TestContext.<anonymous> (file://<pre-fix-workspace>/tests-node/install.test.mjs:422:16)
      at Test.runInAsyncScope (node:async_hooks:226:14)
      at Test.run (node:internal/test_runner/test:1402:25)
      at Test.start (node:internal/test_runner/test:1262:17)
      at startSubtestAfterBootstrap (node:internal/test_runner/harness:387:17) {
    generatedMessage: false,
    code: 'ERR_ASSERTION',
    actual: undefined,
    expected: /Destination changed during installation/,
    operator: 'throws',
    diff: 'simple'
  }

test at tests-node/install.test.mjs:429:1
✖ an edit made while a replacement is being staged is preserved with earlier writes rolled back (657.033666ms)
  AssertionError [ERR_ASSERTION]: Missing expected exception.
      at TestContext.<anonymous> (file://<pre-fix-workspace>/tests-node/install.test.mjs:446:16)
      at Test.runInAsyncScope (node:async_hooks:226:14)
      at Test.run (node:internal/test_runner/test:1402:25)
      at Test.processPendingSubtests (node:internal/test_runner/test:974:18)
      at Test.postRun (node:internal/test_runner/test:1542:19)
      at Test.run (node:internal/test_runner/test:1467:12)
      at async startSubtestAfterBootstrap (node:internal/test_runner/harness:387:3) {
    generatedMessage: false,
    code: 'ERR_ASSERTION',
    actual: undefined,
    expected: /Destination changed during installation/,
    operator: 'throws',
    diff: 'simple'
  }

test at tests-node/install.test.mjs:610:1
✖ retired file edits after their preflight stop every update and removal (561.062583ms)
  AssertionError [ERR_ASSERTION]: Missing expected exception.
      at TestContext.<anonymous> (file://<pre-fix-workspace>/tests-node/install.test.mjs:624:16)
      at Test.runInAsyncScope (node:async_hooks:226:14)
      at Test.run (node:internal/test_runner/test:1402:25)
      at Test.processPendingSubtests (node:internal/test_runner/test:974:18)
      at Test.postRun (node:internal/test_runner/test:1542:19)
      at node:internal/test_runner/test:1305:31
      at node:internal/process/task_queues:151:7
      at AsyncResource.runInAsyncScope (node:async_hooks:226:14)
      at AsyncResource.runMicrotask (node:internal/process/task_queues:148:8) {
    generatedMessage: false,
    code: 'ERR_ASSERTION',
    actual: undefined,
    expected: /Destination changed during installation/,
    operator: 'throws',
    diff: 'simple'
  }

```

After: exit 0. All three passed, including full filesystem comparisons
that preserve the injected edit and restore the remaining installation.

```text
✔ an edit made while later skills are being preflighted cannot become an overwrite baseline (771.939959ms)
✔ an edit made while a replacement is being staged is preserved with earlier writes rolled back (650.49525ms)
✔ retired file edits after their preflight stop every update and removal (337.456ms)
ℹ tests 3
ℹ suites 0
ℹ pass 3
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 1838.833375

```

The fix retains preflight bytes, compares all affected destinations before the
first mutation, and checks again after staging replacements. Checks and
rename/unlink are separate filesystem operations: this closes the reproduced
windows but does not guarantee arbitrary concurrent edits in the final syscall
gap or durable rollback after process termination.

