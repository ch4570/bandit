# Review feedback loop — 2026-09-09

The first corrective round passed 2/4 blind task grades; the second passed 4/4.
Both first-round failures are retained. These are small synthetic development
checks, not a held-out benchmark, a reliability estimate, or a quality/cost
advantage claim. The [computed comparison](summary.json) remains `incomplete`
because actual model and reasoning-effort identity are absent from the raw CLI
events. Monetary cost and cost per successful task are unavailable, not zero.

## What changed and what failed

The earlier [18-run development comparison](../2026-09-09-bounded-workflows/README.md)
is unchanged, including its three failed reviews. Those reviews identified the
principal defects but some omitted the undefined same-key/changed-content policy.

Round 1 added a conditional check of repeated-action identity in the canonical
review reference (`faba4ec`). The existing export case then passed twice. The new
reservation case correctly distinguished adopted revision rules from an open
withdrawal decision, but both outputs merely deferred writing acceptance criteria
for that decision. They failed one of six required dimensions. The failures were
disclosed before the next edit; neither rubric was changed.

Round 2 added general guidance to connect an unresolved decision to a concrete
scenario and observable check when acceptance guidance is requested (`c074a5d`).
Policy-dependent outcomes must remain conditional. Both cases passed twice:
the reservation reviews gave conditional late-delivery/overlap checks without
inventing a winning action or an automatic release policy.

| Round | Export review | Reservation review | All grades | Input | Cached input, included | Output | Summed run seconds |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1: identity check | 2/2 | 0/2 | 2/4 | 316,850 | 206,464 | 4,767 | 206.729 |
| 2: conditional acceptance check | 2/2 | 2/2 | 4/4 | 315,396 | 216,960 | 4,753 | 212.676 |

All eight processes exited zero and passed workspace integrity checks. All runs,
including failed quality grades, contribute to usage totals. Cache is already
included in input; reasoning is already included in output. No whole-task retry
occurred within a condition. A changed instruction condition is a new development
round, not a way to replace an earlier failed attempt.

## Method and evidence

The [first protocol](protocol-round1.md) and [second protocol](protocol-round2.md)
were written before their respective executions. Each round used four fresh
ephemeral CLI sessions and a separate frozen five-skill snapshot, explicitly
invoking `$bandit-review`. Both raw cases ran twice, with an 800-word prompt limit,
240-second timeout, disabled browsing/multi-agent use, and requested
`gpt-6-astra` / `low`. The recorded CLI version is 0.153.4. Prompt limits are not
provider billing caps, and requested settings do not attest actual routing.

Case 10 and its criteria were independently authored without candidate
instructions or prior grades. It was held out only from the first instruction
edit; after round 1 it became a development fixture. Executing tasks were given
raw inputs and the skill snapshot, with no criteria, diagnoses, or earlier outputs
in their workspaces or prompts. Fresh independent graders received anonymous
A/B outputs, raw sources, and unchanged criteria, not conditions or instructions.
Different graders handled each case/round; grading variation remains possible.

The [manifest](comparison.json) resolves each anonymous label and binds its grade
to output bytes. The grade packets preserve their criteria and explanations;
their `raw/` locators correspond to each run's `original-input/` files. Original
inputs, final inputs, prompts, raw events, stderr, outputs, and metadata are
copied byte-for-byte. The [inventory](evidence-sha256.json) binds 128 evidence files
exported before this README. Duplicate installed skills/assets are omitted from
published workspaces; the recorded instruction hashes and commits identify them.

All eight event streams contain a host advisory that skill descriptions were
shortened to fit the skill-context budget. It was not a turn failure and is not
hidden. The full selected references were read, but this does not establish a
hermetically isolated host instruction context. Shared-host load, cache effects,
instruction edits informed by failures, and unobserved runtime identity prevent
causal efficiency or general-reliability conclusions. Grading and development
agent cost is also unavailable and is not included in product-run usage.

The final instructions separately passed independent static review, five
SkillEvaluator 0.2.1 Tier 1 checks, and a zero-finding SkillSpector 2.3.5 keyless
scan. Those checks do not constitute a behavioral benchmark or proof of security.
