# Optional model selection: frozen mock-test baseline

These are engineering tests of an optional runner argument and evidence metadata, not PM-quality measurements. No native Codex TASK, actual model override, account call, or web request was executed. Child execution and version probes are mocked; CLI tests mock `run_case` itself.

Seven focused methods were added to [the runner tests](../../../../tests/test_eval_runner.py), covering:

- Unchanged default argv, permissions, and `model_override: null`/host-default metadata.
- One opaque explicit `--model` argv value before the final stdin `-`, with independent disabled/live web-search settings and unchanged read-only scope.
- Rejection before staging or subprocess calls of empty values, whitespace, C0/DEL/C1 controls, leading dashes, and non-string values; no model catalog or trimming.
- Requested-model metadata after nonzero task exit, missing task executable, missing version-probe executable, and nonzero version probe, without inventing a child exit code for launch failures.
- CLI forwarding of the new optional argument after `web_search`, with omission remaining `None`.

The existing helper forwards `model` only when supplied, preserving its old default call shape. The test identifiers `synthetic-model` and `vendor/model:vNext+canary` are synthetic opaque strings, not claims about available models or a verified serving backend.

Before source implementation, [the selected-test capture](model-tests-before.py) ran Python **3.11.16** with `-B` and bytecode writes disabled:

```text
/Users/DEVELOPER/.local/bin/python3.11 -B -m unittest discover -s tests -p test_eval_runner.py -k model -v
```

Result: **exit 1; 7 test methods; unittest reports `failures=1, errors=25`; no skips**. One method, the unchanged-default control, passed. Five methods produced error records, including repeated subtest errors because the old `run_case` rejects the `model` keyword; the explicit CLI option also remains unsupported. The remaining method failed because old CLI forwarding lacks the newly specified trailing `None`. Thus 25 error records are not 25 distinct test methods. This is the expected feature-absence baseline, not evidence that the preexisting default is broken.

Full [stderr](model-tests-before.stderr.txt), [stdout](model-tests-before.stdout.txt), and [command/status/timestamps/hash receipt](model-tests-before.json) are preserved. The [old runner snapshot](run-local-before.py) is byte-identical to the runner used for this test. Main received the safe-to-implement signal only after the selected run had terminated.

| Artifact | SHA-256 |
| --- | --- |
| Runner before / `run-local-before.py` | `1d06a3878e62ca045ef5be05a8184fc95cbe379a9584faebb78139ba51d70298` |
| Frozen test file | `763e45ebcf89ea628b8904d6f2efcd3163d085f02f57ecf61def25f5d8e568d5` |
| Raw stderr | `deedf65ac3cf4b5ed3e2b9f92327a860224f8393b4937c3a4a5225c92d3e3102` |
| Command receipt | `c638f4b88416655e601341471f20da1991346de01d9f5caba09cb3798fb43343` |

Runner and test hashes were unchanged across execution. A read-only free-space check before this work reported 395 MiB available. This subtask made no deletions, implementation edits, full-suite runs, or package builds. Preserve all before-fix files unchanged; subsequent evidence belongs in separate files.
