# Fake model-option smoke: preserved first failure and contract correction

The first smoke attempt exited **1** with **50/52** checks satisfied. Its two
failures demanded the words “requested” and “unverified” in the metadata config.
The agreed explicit config is
`--ignore-user-config; explicit model override; explicit web_search`;
that value does not claim a verified backend. This was an over-specific harness
expectation, not an observed runner forwarding defect or a PM rubric change.

The authorized, separately named v2 attempt exited **0**, satisfying **52/52**
checks. Its only source changes are the evidence prefix and config assertion
shown below. The same runner and archive source bytes were used in both attempts.
All **83 v1 source/report/result/evidence files** were rehashed after v2 and
remained unchanged. Neither old failure nor old source was overwritten.

| Attempt | Harness SHA-256 | Results SHA-256 |
| --- | --- | --- |
| [v1](model-cli-smoke-report.md) | `a2540c6bbed61a120931c299a0d3903e7bb45b93a718ce0c237c7f9cdf34fe20` | `3cf0831a086a840576ed89a8a47b577d68081e8571e92aef82a996c555a7486c` |
| [v2](model-cli-smoke-v2-report.md) | `6f629044d298a0f380624d0ba1235faa3c113267703679615d5fb7731d8e5ea2` | `a5728acc726a9bd07480c04ec14bde7ca8cd15418ecd26aee559e851087e1e58` |

Temporary roots, both retained without deletion:

- v1: `/TEMP/bandit-round12-4a9iyv/fake-model-cli-kel72fjh`
- v2: `/TEMP/bandit-round12-4a9iyv/fake-model-cli-pa_nce5k`

## All runner/archive command outcomes

Each row occurred once in each attempt: **14 real local CLI subprocesses**
in total. The child failure and invalid argument are deliberately nonzero.

| Command | v1 exit | v2 exit |
| --- | ---: | ---: |
| runner-explicit | 0 | 0 |
| archive-explicit | 0 | 0 |
| runner-default | 0 | 0 |
| archive-default | 0 | 0 |
| runner-child-failure | 23 | 23 |
| archive-child-failure | 0 | 0 |
| runner-invalid-empty | 2 | 2 |

The six valid runner launches produced **12 fake-executable calls**: six version
probes and six fake execs across both attempts. Empty-model validation produced
no fake call and no output/run directory. There were **zero real Codex,
backend/model calls or planning TASKs**. Attempt-qualified capture paths
distinguish fake invocation labels; they are not native thread identities.

Explicit/default success and explicit child exit 23 archived successfully with
their original completion/failure status. Literal model forwarding, default
omission/null, sandbox/web flags, prompt bytes and metadata path normalization
were already correct under v1's checks. V2 changes no such condition.
The post-run evidence audit also compared the retained raw config strings
directly to the agreed values, without normalization.

[The correction receipt](model-cli-smoke-correction.json) records both attempts'
UTC intervals, all 14 command outcomes, source/result/report hashes, unchanged
v1 evidence and verification totals. All **160 evidence-file hashes**, including
raw streams, were recomputed without mismatch. Full argv and stream hashes
remain in [v1 results](model-cli-smoke-results.json) and
[v2 results](model-cli-smoke-v2-results.json).

## Exact harness source diff

```diff
--- model-cli-smoke.py
+++ model-cli-smoke-v2.py
@@ -25,7 +25,7 @@
 MODEL = "synthetic-model.integration"  # Test string, not an available model.
 FAKE_VERSION = "fake-codex model-cli-smoke 0 (no backend)"
 REQUEST = b"Synthetic fake-executable integration fixture. No product-planning task or backend call is requested.\n"
-PREFIX = "model-cli-smoke"
+PREFIX = "model-cli-smoke-v2"
 
 FAKE_SOURCE = r'''
 """FAKE CODEX: deterministic local argv plumbing, no auth/network/model use."""
@@ -194,10 +194,9 @@
         check(label + ": literal model argv", captured_argv.count("--model") == (0 if requested is None else 1)
               and (requested is None or captured_argv[captured_argv.index("--model") + 1] == requested))
         config = metadata["config"].lower()
-        check(label + ": config distinguishes request from backend verification",
-              "host model defaults" in config if requested is None else
-              "requested" in config and "host model defaults" not in config
-              and any(phrase in config for phrase in ("not verified", "unverified", "not independently verified")),
+        check(label + ": config matches explicit/default request contract",
+              config == ("--ignore-user-config; host model defaults; explicit web_search" if requested is None
+                         else "--ignore-user-config; explicit model override; explicit web_search"),
               metadata["config"])
         check(label + ": unchanged sandbox and web flags",
               all(flag in captured_argv for flag in ("--ignore-user-config", "--ephemeral", "--skip-git-repo-check", "--json"))
```

The synthetic model name is a literal plumbing test string, not an available
model or verified backend. This check does not validate native CLI/backend
selection, planning quality, network integration or reliability. No source fix,
new smoke, full suite or packaging command is introduced by this receipt.
