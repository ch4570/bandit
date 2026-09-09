# Overnight development, round 12 — 2026-09-09

The optional development runner now accepts an explicit `--model MODEL_ID`
request. Omitting it preserves the previous command, host-default selection and
`model_override: null`. The runner passes the supplied identifier unchanged to
the CLI and records the request before probing the CLI version or launching the
task. A model request does not expand web access or file-write permissions.

This round adds **zero native planning TASKs**; the cumulative overnight count
remains **46**. Its mock calls and fake executable are engineering checks, not
model executions, a skill-quality benchmark, or a causal comparison. All five
skills, raw cases, fixed rubrics, prior outputs and historical partial/failure
assessments are unchanged.

## Request, not verified identity

The [official CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli)
documents `codex exec --model` as a per-run override. The installed CLI help
also exposes the flag. The runner does not choose a model, consult a catalog,
change account configuration or silently retry another model. CLI/account
availability is not established by these local tests.

The existing `model_override` field records the exact requested string;
`config` distinguishes an explicit override from host defaults. Neither field
attests which backend served a request. A mutable alias and remaining host or
external settings prevent treating this flag alone as reproducibility proof.
Earlier records keep their original metadata rather than receiving an inferred
model label. The [usage instructions](../../README.md#optional-model-request)
show an explicitly replaceable placeholder, not a recorded model invocation.

Empty/non-string identifiers, whitespace, C0/DEL/C1 controls and leading `-`
are rejected before any fixture staging or subprocess. Once staged, version
probe, task launch and completed child failures retain the requested identifier
and the existing failure classification. There is no new archive schema.

## Frozen tests and retained failure

The [seven focused mock tests](checks/model-tests-summary.md) cover unchanged
defaults, exact argument forwarding, invalid-input side effects and failure
metadata. Before implementation, the old runner does not support the new
option: the default control passes while the new expectations fail. With the
same frozen test file, all seven methods pass after implementation. This is an
unsupported-feature baseline, not a claim that the previous default was broken.

The [first fake-executable smoke](checks/model-cli-smoke-report.md) retains
50/52 satisfied checks and two failures. Both failures concern a harness-only
requirement for particular warning words in `config`; the actual agreed string
is `--ignore-user-config; explicit model override; explicit web_search`.
Literal argv, requested-model metadata, default/null behavior, failure exit,
isolation and archive transformations all satisfy their checks in that attempt.
No native Codex executable or model backend is called by this smoke.

The first harness, logs and assertions remain intact. A
[separate second attempt](checks/model-cli-smoke-v2-report.md) changes only the
output prefix and the config assertion/label to match the agreed explicit or
default string; all 52 checks satisfy that corrected contract. No runner,
archiver, frozen unit test or PM rubric is changed between the two attempts.
The [correction record](checks/model-cli-smoke-correction.md) includes the exact
diff, unchanged first-attempt hashes and every runner/archive command outcome.
Across both attempts, 14 runner/archive subprocesses drive 12 **fake** calls
(six version probes, six execs), not native planning TASKs. The fake's success
output and failure exit 23 are synthetic test behavior, not model results.

## Full engineering checks

[Sequential local gates](checks/README.md) pass 79 Node tests on Node 22.23.2
and 99 Python tests on Python 3.11.16, including the seven added model-option
tests. Sync, both repository validators and all five official metadata checks
also pass. The standalone npm pack has the same 43 payloads and exact compressed
bytes as round 11; the optional development runner is not installed by npm.

Final source packaging verifies all 1,239 earlier result files, 34 skill files
and 87 raw/rubric/sequence files against the round-11 ZIP, and all 93 historical
PM Craft files against HEAD. Installers, archiver, English/Korean onboarding
and existing examples are unchanged in this round. These are local artifact
and engineering checks, not another public network installation or host discovery.

## Disk-space interruption

Before implementation, temporary-directory creation failed with `ENOSPC`.
Work paused without source/test writes, evaluation launches or deletion. The
last round's source and distribution hashes were rechecked read-only. A later
external-state change increased available space and temporary creation succeeded;
no cleanup by this task caused that change. Subsequent verification commands
run sequentially to reduce simultaneous temporary storage, not to omit gates.

This remains unreleased local work. The versioned public install command is
unchanged; no new CI run, commit, release or registry publication is performed.
