# Optional model argument: selected mock-test evidence

The same seven selected engineering-test methods passed after the runner added optional model selection. This is feature-support evidence for argument handling and metadata, not a legacy installer defect, a real model run, or a PM-quality comparison.

| Phase | Result |
| --- | --- |
| [Before implementation](model-tests-before.md) | Exit 1; 7 methods; unchanged-default control passed; unittest reported 1 failure and 25 error records, including repeated unsupported-keyword subtests |
| After implementation | Exit 0; 7 methods passed; 0 failures, errors, or skips |

Both phases used Python **3.11.16**, `-B`, the same selected unittest command, and the same frozen test bytes. Codex task/version calls were mocked; CLI-parser tests mocked `run_case`. No native TASK or actual model override was invoked.

The tests cover the agreed contract: an optional argument after `web_search`; a separate `--model` argv value before stdin `-`; unchanged default argv/configuration; explicit requested-model metadata without a host-default claim; rejection before staging/probing of invalid identifiers; and requested-model preservation after nonzero child exit or version/task launch failures. Model identifiers are opaque: no catalog or claimed backend identity is required. Sandbox/web scope is not widened by model selection.

The implementation changes are confined to optional-argument validation, argv construction, requested-model/config metadata, and CLI forwarding. The [before source](run-local-before.py) is retained independently. Tests in [test_eval_runner.py](../../../../tests/test_eval_runner.py) were not changed between the failing and passing runs.

After evidence: [capture script](model-tests-after.py), [command/timestamps/status and before/after hashes](model-tests-after.json), [full stderr test report](model-tests-after.stderr.txt), and [stdout](model-tests-after.stdout.txt). The before receipt, raw stderr, and source snapshot remain unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Runner before | `1d06a3878e62ca045ef5be05a8184fc95cbe379a9584faebb78139ba51d70298` |
| Runner after | `6243624462aae5ff9e9f9eff76c6692f6e3b63d3373cf328cc73a1e2be31be55` |
| Frozen tests | `763e45ebcf89ea628b8904d6f2efcd3163d085f02f57ecf61def25f5d8e568d5` |
| After command receipt | `a2c5b88da9c12aa896c731301138c17fc921cc437ad7cea2c5466b23be30b973` |
| After stderr | `4e6aabf810519c81802a47959abe5384fc3474547cf5fdfef1ae0587d7b27e31` |

These selected mocks do not prove model availability, actual backend routing, full-suite health, public package installation, or task-output quality. They do not change default model selection, authorize account/outreach actions, or establish publication readiness. Full gates and any separate fake-CLI integration smoke are outside these counts.
