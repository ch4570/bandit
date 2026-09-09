# Continued research development check — 2026-09-09

Both the no-BANDIT baseline and `$bandit-research` passed 2/2 anonymous task
grades. This check found no reason to change the research instructions. It does
not establish a skill advantage, reliability estimate, business validation, or
cost savings. The [computed comparison](summary.json) is `incomplete`: actual
model and reasoning-effort identity are absent from raw events. Monetary cost
and cost per successful task are unavailable, not zero.

## Task and method

The synthetic [Backstage Bin task](../../cases/11-backstage-research/request.md)
asks a two-person team to assess mixed prop-storage evidence and propose one
feasible next test. Intercepts, a voluntary poll, and a partial venue log have
different units, recruitment sources, and unknowns. The available exercise has
explicit time, participant, material, consent, and production-stock boundaries.
All names, quotations, organizations, and data are fictional.

An independent author created the four raw documents and the separate six
[meaning criteria](grades/criteria.md) without reading candidate instructions or
earlier grades. The [protocol](protocol.md) preceded execution. No skill file
changed from `5e65d47`; the fixture and runner route were committed at `9ab5662`.
The four runs record that runner's hash. Later preflight/JSON hardening did not
alter the saved runs or their instructions.

Replicate 1 ran baseline then research; replicate 2 ran research then baseline.
These two lanes overlapped on one host, so load and cache effects are not causal
controls. Every cell used a new ephemeral CLI session, requested `gpt-6-astra`
with `low` effort, a 240-second timeout, an 800-word prompt limit, and disabled
browsing/multi-agent use. The recorded CLI version is 0.153.4. Prompt limits are
not provider billing caps; requested settings do not attest backend routing.

Research runs received the frozen complete five-skill bundle and invoked the
specialist directly. Baseline runs received no local skill snapshot and were
instructed not to load a PM skill. Raw inputs and, where applicable, instructions
were the only task materials supplied; criteria, diagnoses, and previous answers
were excluded from executing workspaces and prompts.

One independent grader received anonymous A–D outputs, raw sources, and unchanged
criteria, but not conditions, skill instructions, or execution logs. All 24
criterion judgments passed. The [grade explanations](grades/grades.md) cover
source-specific denominators, competing causes, feasible paper exercises,
prospective decision rules, low-attendance handling, and unsupported demand or
payment claims. The labels resolve through [the manifest](comparison.json).
The grader's `raw/` locators refer to each run's `original-input/` files.

## Observations

| Condition | Quality | Process/integrity | Input | Cached input, included | Output | Summed run seconds |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| Baseline | 2/2 | 2/2 | 145,349 | 94,464 | 2,290 | 112.366 |
| Research | 2/2 | 2/2 | 154,198 | 96,256 | 2,708 | 128.132 |

Research used more reported input and output and more summed elapsed time here.
No price or savings estimate was inferred. Cache is already part of input and
reasoning is already part of output. Every attempt is retained; none was retried.
Development and grading agent costs are unavailable and are not silently included.

The [inventory](evidence-sha256.json) binds 58 files exported before this README:
original/final input bytes, raw events, stderr, prompts, outputs, metadata, grades,
criteria, protocol, manifest, and computed summary. Grades bind actual output
hashes. Duplicate installed skill folders/assets are omitted from published
workspaces; source revision and instruction hashes identify the frozen snapshot.
Previous results, including all earlier failures, remain unchanged.

An independent execution audit confirmed four distinct threads, 22 scoped
read/listing commands, 24 complete input/instruction reads, exact before/after
inventories including root `.`, and matching telemetry. All 609 earlier result
files were byte-identical to `5e65d47`. This is separate from the blind grades.

The two baseline runs initially tried listing an absent optional `instructions/`
directory and received exit 2; subsequent reads of all inputs succeeded. Both
research runs recorded a nonfatal skill-description/context-budget advisory.
These warnings remain in raw events; none was a failed turn or subtracted from
usage. Logs do not attest the absence of implicit host instructions.

The unchanged research bundle also passed independent static review,
SkillEvaluator 0.2.1 Tier 1, and a zero-finding SkillSpector 2.3.5 keyless scan.
Those checks are separate from behavior and do not prove product effectiveness.
One small public synthetic task with two replicates cannot establish general
quality, demand, or the value of using a skill. Output style can reveal clues to
a grader; this is not an attested double-blind or hermetically isolated study.
