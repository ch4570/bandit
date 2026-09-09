# Round 7 — independent case 02 grades

The grader inspected both complete outputs, the raw request/plan/observations,
the unchanged [case 02 rubric](../../RUBRIC.md), and complete retained traces.
The grader was neither a TASK agent nor this fixture's author, but knew the arm
labels and prior case-02 findings. No rubric, output, instruction, or historical
record was edited. Exit 0 is reported separately from semantic quality.

## Results

`S:n` denotes line `n` of the
[standalone bandit-specify output](pre/02-offer-change--bandit-specify/output.md);
`B:n` denotes line `n` of the
[baseline output](pre/02-offer-change--baseline/output.md).

| Fixed criterion, in rubric order | bandit-specify | Baseline |
| --- | --- | --- |
| 1. Replace current payment/revenue and creator-only editing, preserve designated customer authority | **Pass.** S:7 adopts free team drafting; S:15 and S:19 replace creator-only editing and payment gates. S:23 retains designated-customer decisions. S:52 makes the old paid revenue premise historical rather than a current forecast. | **Pass.** B:9 adopts free shared drafting; B:38 and B:44 replace the old editing/payment rules while retaining customer decision authority. B:15 makes the monthly revenue assumption inapplicable to the free pilot. |
| 2. Preserve eight payments/two refunds and distinguish actual collections from hypothetical revenue | **Pass.** S:35 retains eight purchases, two full refunds, 72,000 − 18,000 = 54,000 KRW collected, not profit; later payments remain unreported. S:52 labels ten monthly quotes and 90,000 KRW as an unobserved historical assumption. | **Pass.** B:19 and B:20 preserve the same payment/refund arithmetic and distinguish collections from profit. B:15 labels ten quotes/month and the resulting 90,000 KRW as an unverified assumption. |
| 3. Avoid causal price claims and explicitly distinguish the three repeat denominators | **Partial.** S:36 correctly gives four repeat users among six senders with another opportunity, alongside 24 registrants, 14 senders, eight without a further opportunity and ten with uncollected opportunity status. S:37 rejects causal improvement and failure-imputation claims. The descriptive 4/14 sender and 4/24 registrant repeat shares are not stated. | **Partial.** B:26, B:27 and B:28 preserve the same nested counts and distinguish unknown/no-opportunity cases. B:32 rejects attributing the rate difference to price or sharing. Both broader repeat shares are omitted. |
| 4. Retain applicable v1 approval evidence; checkout historical; new sharing checks unexecuted | **Pass.** S:55 preserves the dated v1 staging approval result and limits its reuse. S:56 makes checkout historical, not a failed old test. S:38 and S:57 distinguish manual sharing from software concurrency execution. S:59 and S:68 make new checks planned/unexecuted. | **Pass.** B:60 retains dated v1 approval evidence with its scope; B:61 treats checkout as historical. B:30 and B:62 reject manual sharing as software concurrency validation; B:64 labels the new verification list as not yet executed. |

Both runs: **3 pass, 1 partial, 0 fail** on the four fixed conditions. Neither
is an all-pass result.

| Complete requested PRD | Whitespace words / cap | UTF-8 bytes | Cap result |
| --- | ---: | ---: | --- |
| bandit-specify | 900 / 900 | 8,889 | **Pass**, exactly at the cap |
| Baseline | 722 / 900 | 6,655 | **Pass** |

Counts use the entire saved `output.md` with
`text.trim().split(/\s+/u).length`, including Markdown and all artifact sections.
The request caps the PRD, not preliminary progress messages. Including those
messages would give 953 and 738 words respectively; they are not silently
removed from a larger delivered PRD. Each final event message is byte-identical
to its saved output. No word-count command appears in either trace; cap
compliance does not establish a tool-backed counting mechanism.

## C3 meaning and independently recomputed evidence

The [raw observations](../../cases/02-offer-change/observations.md), lines 3–15,
support the following calculations:

- Initial gross collections: 8 × 9,000 = 72,000 KRW; two full refunds remove
  18,000, leaving 54,000. August repeat use is 2/8 = 25% over 30 days.
- September has four repeat users: **4/6 = 66.7%** among senders with another
  opportunity, **4/14 = 28.6%** among all senders, and **4/24 = 16.7%** among
  all registrants at the elapsed ten-day report point.
- **14/24 = 58.3%** is sending conversion, not the missing repeat fraction.
  Six opportunity-bearing plus eight not-yet-opportunity-bearing senders make
  fourteen; the ten non-senders' opportunity status is unknown.

Both outputs correctly preserve the underlying counts and meaningful
conditions. Neither labels 4/6 as whole-cohort retention, treats unknown or
not-yet-eligible people as observed repeat failures, or attributes improvement
to a single simultaneously changed factor. The broader repeat shares are
descriptive, not opportunity-adjusted retention or comparable causal effects.

The partial preserves the established explicit-comparison interpretation of
`RUBRIC.md:12`, also documented in
[historical grades](../2026-09-07/grades-02-03-05.md), lines 64–70, and
[round-3 grades](../2026-09-09-overnight-round3/grades.md), lines 53–60.
The historical grader acknowledged that “separates” can also be read as avoiding
conflation rather than requiring every view to be stated. The raw user request
does not explicitly request all three fractions. This is therefore incomplete
explicit metric reporting under the retained rubric interpretation, **not an
observed arithmetic or causal-reasoning error**. No criteria are softened after
seeing these runs, and prior partials and cap failures remain unchanged.

## Action scope and extra observations

The complete [specialist trace](pre/02-offer-change--bandit-specify/events.jsonl)
has twelve events. Completed commands at lines 5, 7 and 9 read the entrypoint,
all three raw files, and `specification.md`, `changes.md`,
`evidence-and-decisions.md`, and `research.md`. Their returned text matches the
archived snapshots. The optional template, review reference and YAML metadata
were listed but have no explicit content-read event. All three commands exited
0; line 12 records `turn.completed`.

The complete [baseline trace](pre/02-offer-change--baseline/events.jsonl) has
nine events. Preserve the recovered tool failure at line 5: listing
`input instructions` exited 2 because the optional `instructions/` directory
did not exist. Line 7 successfully read all three raw files; no PM instruction
snapshot was supplied or read. Line 9 records `turn.completed`.

Neither trace contains file edits, product execution/tests, external actions,
or reads of rubrics, prior outputs, or unrelated repositories. Both wrappers
restrict the task to local raw inputs and assigned instructions; metadata
records read-only sandboxing, explicit web-disabled configuration and exit 0.
New verification and pilot work in the PRDs remain proposals, not actions taken.
No additional material output failure was established outside the four rubric
conditions and the separately checked artifact cap.

## Integrity and limitations

Independent checks verified all **24 retained file hashes** in the two archive
manifests (16 specialist, eight baseline). The three raw files in each archive
match current fixtures, the [pre-run receipt](case02-before-run.json), and
metadata before/after maps. The specialist's eight instruction files match
the receipt, current selected sources and unchanged before/after maps; baseline
instruction maps are empty. The rubric matches the receipt and pinned
`f4a376e23b16f311931b4d06853a0943575e09e7:evals/RUBRIC.md` bytes.

The receipt's recorded `2026-09-08T17:36:11.025Z` precedes both recorded launches.
Its SHA256 is
`d1675a15772b8ba16d849f4bbfa42b93b961fbaf2369ab4efd4befe84f2c3a33`.
Complete output SHA256 values:

- Specialist: `9c396fe8ff43744f43917df23cb1af5d060f65d9335f858040a2b3179488be01`
- Baseline: `6259e42b085fee412c23164281b1e947216c1346e316e6d18f8820d4f24286e9`

This is a repeated synthetic development case, not hidden or representative
coverage, customer evidence, or an independent field experiment. Codex CLI
0.153.4 used unmodified host model defaults; those defaults and wider host state
are unpinned. Receipts/timestamps are local, unsigned and not independently
time-attested. Archive metadata normalizes temporary-root paths; this grading
verifies retained hashes, not original unnormalized log bytes or all host
activity. Neither these two outputs nor their lengths establish reliability,
skill superiority, token savings, or an instruction-caused improvement.
