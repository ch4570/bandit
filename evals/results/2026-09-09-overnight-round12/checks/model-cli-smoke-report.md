# Fake model-option CLI smoke

fake-executable engineering integration smoke; zero real Codex/model/TASK executions.

Status: **failed**. 50/52 recorded checks satisfied.
Fake invocations: 6; these are not native Codex runs or planning TASKs.

| Check | Result |
| --- | --- |
| explicit: runner returns fake child exit | pass |
| explicit: captured argv equals metadata command | pass |
| explicit: prompt bytes preserved | pass |
| explicit: fake version and one exec | pass |
| explicit: explicit request or default metadata | pass |
| explicit: literal model argv | pass |
| explicit: config distinguishes request from backend verification | FAIL |
| explicit: unchanged sandbox and web flags | pass |
| explicit: raw-only unchanged baseline workspace | pass |
| explicit: exited metadata keeps nonzero distinct from launch failure | pass |
| explicit: archive CLI succeeds | pass |
| explicit: archive retains exact requested model | pass |
| explicit: exact metadata path normalization | pass |
| explicit: all archive hashes and transformations | pass |
| explicit: archive preserves completed versus failed child | pass |
| default: runner returns fake child exit | pass |
| default: captured argv equals metadata command | pass |
| default: prompt bytes preserved | pass |
| default: fake version and one exec | pass |
| default: explicit request or default metadata | pass |
| default: literal model argv | pass |
| default: config distinguishes request from backend verification | pass |
| default: unchanged sandbox and web flags | pass |
| default: raw-only unchanged baseline workspace | pass |
| default: exited metadata keeps nonzero distinct from launch failure | pass |
| default: archive CLI succeeds | pass |
| default: archive retains exact requested model | pass |
| default: exact metadata path normalization | pass |
| default: all archive hashes and transformations | pass |
| default: archive preserves completed versus failed child | pass |
| child-failure: runner returns fake child exit | pass |
| child-failure: captured argv equals metadata command | pass |
| child-failure: prompt bytes preserved | pass |
| child-failure: fake version and one exec | pass |
| child-failure: explicit request or default metadata | pass |
| child-failure: literal model argv | pass |
| child-failure: config distinguishes request from backend verification | FAIL |
| child-failure: unchanged sandbox and web flags | pass |
| child-failure: raw-only unchanged baseline workspace | pass |
| child-failure: exited metadata keeps nonzero distinct from launch failure | pass |
| child-failure: archive CLI succeeds | pass |
| child-failure: archive retains exact requested model | pass |
| child-failure: exact metadata path normalization | pass |
| child-failure: all archive hashes and transformations | pass |
| child-failure: archive preserves completed versus failed child | pass |
| invalid empty: CLI exits 2 | pass |
| invalid empty: no fake child or version probe | pass |
| invalid empty: no output/run directory | pass |
| six distinct fake invocations: three version probes plus three execs | pass |
| all expected fake invocation identities, no fallback exec | pass |
| runner, archiver and harness unchanged during smoke | pass |
| synthetic fixture unchanged | pass |

[Complete results](model-cli-smoke-results.json) retain exact argv, UTC timestamps, child exits,
captured prompt/stream hashes, all fake invocation identities, source hashes, and evidence hashes.
Results SHA-256: `3cf0831a086a840576ed89a8a47b577d68081e8571e92aef82a996c555a7486c`.

The literal `synthetic-model.integration` is a synthetic test string, not an available or verified model.
Explicit and default success, explicit child exit 23, and empty-option preflight are exercised sequentially.
All fake calls remain local. A requested model value is not evidence that any backend selected it.
The real runner and archive CLIs are used, but all supplied CLI events/output come from the fake.
Raw originals, archives and capture streams are retained under this check's evidence directory.
The temporary root is retained; this harness deletes nothing. No full suites or release packaging run.
