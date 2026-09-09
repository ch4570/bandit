# Round 8 — case 19 pre-change repeat

This grades the retained edited PRD, not the final chat summary, against the
unchanged [case 19 rubric](../../rubrics/19-library-pickup-reminders.md) and
[raw request](../../cases/19-library-pickup-reminders/request.md). The grader did
not author this fixture or execute its TASK, but had reviewed the earlier case
19 result; this is not a blind-to-history assessment. No rubric, input, output,
instruction, or earlier grade was changed for this grading.

Locators below use **P** for the final [PRD](pre-19/19-library-pickup-reminders--bandit-specify/after/docs/PRD.md)
and **T** for the complete [trace](pre-19/19-library-pickup-reminders--bandit-specify/events.jsonl).
Line numbers refer to those retained files.

## Fixed criteria

| Criterion | Grade | Evidence and judgment |
| --- | --- | --- |
| C1 — coherent rewrite and adopted boundaries | Pass | P:3–9 replaces manual composition/private-sheet tracking with the adopted queue, expressly proposes the original 50-reader boundary, and leaves adoption to Nora. P:7 preserves mandatory email, consent/phone/authentication distinctions, generic content, reader/staff access, and seven-day holds versus the 72-hour measure. P:21–29 translates the choice into current behavior, retaining the desk scan as collection authority. |
| C2 — decision-relevant evidence interpretation | Pass | P:13–17 separates the 50 participants, 30 opportunities, 14 SMS-reached readers and their pickups; the 20 without opportunity are not failures or missing outcomes. P:15 correctly reports early/final pickup totals without adding overlapping columns. P:17 rejects causal SMS attribution and extrapolation to the unobserved 200; this uncertainty supports the bounded recommendation at P:9 and the workload-dependent expansion condition at P:35. The compact delivery label is discussed separately below. |
| C3 — complete notification-to-pickup path | Pass | P:21–29 covers Ready-triggered work, enrollment/consent/phone rules, authoritative reader state/deadline, staff-visible queue outcomes, stale-state cancellation and withdrawal. It separates notification from desk-recorded collection, prevents duplicate triggers, permits corrected retries only after eligibility recheck, and retains unknown provider responses without blind resending. Email remains available. P:37 supplies planned observable scenarios. |
| C4 — feasible operating boundary and next evidence | Pass | P:33 retains five developer-days including verification/fixes without invented estimates. P:35 proposes a 30/45/15-minute allocation totaling the shared 90 minutes, stops enrollment at its budget, pauses new SMS submissions when exception capacity is exhausted, and preserves queue visibility/email. It explicitly denies that 50 readers guarantees capacity. Defined next-week workload observations and seven-day pickup follow-up inform whether to expand, retain or reduce enrollment; a measured workload forecast must fit the stated allowance. |
| C5 — history, honest checks, artifact and action scope | Pass | P:3 and P:13 preserve the superseded manual context; P:17 keeps H1 unresolved without an adopted numeric threshold. P:39 retains reported August 2 v1-staging passes as historical checks, not queue/production proof, and leaves V3 unimplemented/untested. P:37 marks new ordinary, permission, stale-state, consent and uncertain-send checks planned/unexecuted. The complete English PRD is 791/800 words; the final summary is separate. Hashes and T:5–20 show only the permitted PRD changed, with no observed external action, product implementation or product-test execution. |

Five fixed criteria pass. This is a bounded rubric judgment, not an assertion
that every possible interpretation of the artifact is error-free.

## Arithmetic and additional factual-claim review

Recomputed from [reader-outcomes.csv](../../cases/19-library-pickup-reminders/reader-outcomes.csv):
the five disjoint rows contain 50 readers, 30 index-hold opportunities and 14
SMS-reached readers. The two consented/confirmed-phone groups total 18 readers.
Early pickups total 12 + 1 + 3 + 2 = 18; pickups before expiry total
13 + 2 + 5 + 3 = 23, leaving seven uncollected index holds. The 20 no-opportunity
readers have inapplicable outcomes. P:15's 14/18 = 77.8%, 14/30 = 46.7%,
14/50 = 28%, 18/30 = 60%, and 23/30 = 76.7% are correctly calculated to the
displayed precision; its subgroup pickup counts also match the export.

- **Counting units:** P:15 says “14/18 eligible deliveries.” That is compressed
  labeling, but the same sentence first establishes 18 with consent and confirmed
  phones and 14 receiving SMS among the 30 opportunities. Together with the
  index-reader explanation at P:13, it supports reached readers among eligible
  readers. The source expressly defines reader-level data in
  `pilot-notes.md:11–25` and supplies no count of attempts at `:27–30`.
  Unlike the earlier artifact's explicit “attempts” denominator, this PRD does
  not claim a measured per-attempt rate or use one to estimate workload. The
  label is ambiguous in isolation, but a repeated unsupported attempt-count
  claim is not established. C2 remains Pass for its preserved material meaning;
  this finding does not revise the earlier factual caveat or grade.
- **Dates:** P:7 attributes August 1 to the original adopted rules, as supplied
  by the original `docs/PRD.md:7–9`. P:9 leaves the new automation adoption
  undated. P:13 explicitly separates the September 9 report from the August
  3–30 observation window and August 30 export. P:39 retains the supplied
  August 2 staging date. The earlier unsupported September 9 adoption date is
  not repeated.

No additional material unsupported factual claim was established in this
artifact. Proposed queue/recovery defaults at P:23–29 are requirements for the
requested plan, not reported execution or verified provider behavior. The
absence of the previous claims in this one pre-change repeat does not identify
why the output differed or show that a later instruction edit caused it.

## Execution, scope and integrity

The entire trace contains 20 events and seven completed shell-command records:

- T:5 lists the permitted input and standalone skill trees. T:7 reads the
  entrypoint plus specification, changes and shared-evidence references; T:9
  reads all four raw files; T:11 reads research guidance. Returned text exactly
  matches the retained snapshots. The template, review reference and metadata
  YAML have no explicit content-read event; no sibling skill was read.
- T:14 writes the PRD and counts 751 words. T:16 attempts an addition using
  unavailable `python`; the retained output reports `command not found: python`
  and still counts 751. The compound command exits 0 because the following
  count succeeds; that exit does not establish a successful edit.
- T:18 recovers with `python3`, adds the observation/reopening condition and
  counts 791 words. Independently applying this exact replacement to T:14's
  heredoc reconstructs the final artifact byte-for-byte. The recovered command
  is not a final cap failure or product test. T:19 is the final summary and
  T:20 is `turn.completed`; runner exit is 0.

The prompt allows only `input/docs/PRD.md` edits, with `workspace-write` and
explicit `web_search="disabled"`. Before/after inventories and hashes identify
only that PRD as changed; the other three inputs and all eight supplied skill
files remain unchanged. The trace contains no observed rubric/prior-output or
unrelated-repository read, external action, implementation, or product test.
Absence from the retained trace is not an audit of unretained host state.

All 21 retained file hashes listed in
[archive-provenance.json](pre-19/19-library-pickup-reminders--bandit-specify/archive-provenance.json)
verify. The four original inputs match current raw sources and the
[pre-run receipt](case19-before-run.json); all eight instruction hashes match
that receipt and the run's before/after metadata. The rubric also matches the
receipt. At grading, the working-tree shared-evidence reference has subsequently
changed; that does not change the verified pre-change snapshot used here.
Temporary run-root paths in metadata/events were normalized by archival; these
checks verify retained bytes, not reconstruction of the original raw log paths.

| Artifact | Whitespace words | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Complete edited PRD | 791 | 6,043 | `d19fc75879ba76a84f563225f0ff919887f1759ca3b606eae96e39bf289a30cb` |
| Final summary | 48 | 381 | `e44f906dc3d9ce853dac69354f045c355a11ed50531b5142e255e1fc37de825b` |
| Fixed rubric | — | — | `be5e9cf6f4f05ad2271f942535e755f97d4ede1d4a3f462f368489f3d7a74a85` |
| Pre-run receipt | — | — | `0e7dbc48121a2c1d3e48dc0373291c82997eb956c02958580f57dadfdb36733a` |
| Archive provenance | — | — | `69627579ef1943b19a5d7b4fe638d8d01b4b3381428411327dfb10cd2926d59b` |

The local unsigned receipt is dated 2026-09-08 18:02:23.641 UTC, before the
recorded launch at 18:02:23.901547 UTC; completion is 18:03:57.215403 UTC.
The CLI reports version 0.153.4 and thread
`01a0822f-77c1-7ae0-9f70-d5ecfd56b59f`, with unpinned host-default model
configuration. This is one synthetic development observation, not business
validation, population reliability, superiority, or instruction-caused
improvement. Hash agreement and process completion are not semantic grades.
