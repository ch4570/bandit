# Round 8 — case 19 post-change rewrite

Independent grading of the actual retained [edited PRD](post/19-library-pickup-reminders--bandit-specify/after/docs/PRD.md)
against the unchanged [case 19 rubric](../../rubrics/19-library-pickup-reminders.md)
and [raw request](../../cases/19-library-pickup-reminders/request.md). The final
chat summary is not the graded artifact. The grader did not author this fixture
or execute the TASK, but had reviewed the earlier case 19 results; this is not
a blind-to-history assessment. **P** locators below are final PRD line numbers.
No rubric, raw fixture, output, instruction or prior grade was changed.

## Fixed criteria

| Criterion | Grade | Evidence and judgment |
| --- | --- | --- |
| C1 — coherent rewrite and adopted boundaries | Pass | P:7–13 distinguishes adopted queue automation and retained D1–D3 from the proposed original-50 availability boundary. Mandatory email, explicit withdrawable consent/confirmed phone, authentication, own-reader/branch-staff access, generic SMS and seven-day holds versus 72-hour measurement are retained. P:27–35 turns the recommendation into current queue and recovery requirements while preserving the desk scan as collection authority. |
| C2 — decision-relevant evidence interpretation | Pass | P:17–21 keeps 50 participants, 30 index-hold opportunities, 14 reached readers and their early/final pickups distinct. The 20 without an opportunity are inapplicable, not failures or missing observations. It neither adds overlapping pickup columns nor extends observed rates to the 200 unobserved readers. Manual handling, universal email, nonrandom recruitment and unknown pickup motivation prevent an SMS-causal claim; P:23 uses uncertainty to support bounded continuation, not extrapolation. |
| C3 — complete notification-to-pickup path | Pass | P:27–35 gives authoritative reader state/deadline, eligible Ready queue creation, per-event deduplication, staff-visible delivery/exception states, immediate pre-send eligibility and hold-state rechecks, and visible suppression after withdrawal, phone invalidation or terminal hold state. It preserves provider-response uncertainty without blind resend, limits retries to definitive failures after recheck, and relies on email where reconciliation cannot establish an outcome. Notification delivery remains distinct from desk-recorded collection. |
| C4 — operating bound and decision-changing observation | Pass | P:23 explicitly says 50 readers does not prove capacity, proposes 30 minutes each for enrollment, exceptions and follow-up within the shared 90-minute allowance, and records actual use. Observed budget exhaustion pauses new SMS enqueueing and enrollment assistance while preserving pending-work visibility and ordinary email/pickup: this is a concrete condition that changes continuation. Support demand, eligible opportunities, unresolved backlog and outstanding implementation estimates inform reconsideration of expansion. P:39 retains five developer-days including verification/fixes, with no invented measured estimate. A separate numerical expansion target is not required by the fixed rubric. |
| C5 — preserved history, planned checks and execution scope | Pass | P:7,17,21 preserve the obsolete manual context as history, while P:23 leaves H1 unproven without an adopted threshold. P:41 retains the reported August 2 v1-staging lifecycle/link/access passes as v1 evidence, not a production audit or queue pass; integration needs recheck and V3 remains unimplemented/unverified. P:43 supplies planned ordinary, permission, stale-state, consent and uncertain-send checks without claiming execution. The complete English PRD is 748/800 words; only the permitted PRD changed, and no external action, product implementation or product test is observed. |

Five fixed criteria pass. This does not establish an error-free artifact, broad
reliability or a causal benefit from the instruction change.

## Arithmetic, units and date claims

Independent recomputation from the unchanged reader CSV gives 50 readers,
30 ready index-hold opportunities, 14 SMS-reached readers, 18 early pickups
and 23 before expiry. Delivered readers account for 12 early and 13 final
pickups; failed-delivery, no-consent and unconfirmed-phone groups contribute
1/2, 3/5 and 2/3 respectively. These figures match P:19. Early collections
remain included within final collections; the 20 no-opportunity readers are
not added to observed pickup failures.

- **Units:** P:19 explicitly labels the reach denominators as opportunity
  readers and participants, and the subgroups as readers. It does not relabel
  reader counts as message attempts or report an unsupported per-attempt rate.
  Omission of a separate 14/18 confirmed/consented-reader rate is not a defect:
  the fixed rubric does not require every calculable fraction.
- **Dates:** P:7 leaves the next-release automation decision undated, then
  introduces the following D1–D3 rules as adopted August 1, 2026, consistent with
  the original PRD. It does not assign September 9 to automation adoption.
  P:17 distinguishes the September 9 report from August 3–30 observations and
  the August 30 reconciliation cutoff. P:41 retains August 2 v1-staging checks.

No additional material unsupported factual claim was established. The queue
and recovery clauses at P:29–35 describe the requested future plan; they do
not report implemented or tested provider behavior. The fixed C4 judgment
uses the explicit budget-exhaustion stop condition, not an invented measured
expansion threshold. The pre-change repeat also avoided the earlier explicit
attempt-count and adoption-date claims, so this post result cannot show that
the wording change caused their absence. Earlier factual caveats remain intact.

## Complete trace and artifact preservation

The [trace](post/19-library-pickup-reminders--bandit-specify/events.jsonl) has
14 events and four completed shell commands:

- Line 5 reads the standalone entrypoint plus specification, changes and
  changed shared-evidence references, then lists input files. Line 7 reads all
  four raw files. Returned text matches the retained snapshots exactly. There
  is no explicit content read of research, review, template or metadata YAML,
  and no sibling skill read.
- Line 10 attempts to write a draft using `python`, but the command is missing
  and exits 127. The trace contains that candidate text, not a successfully
  saved or counted draft. It is not the final artifact and is not graded here.
- Line 12 recovers with a heredoc, writes the actual PRD and counts 748 words.
  The complete heredoc body exactly matches the retained final PRD bytes.
  Line 13 is the 50-word summary; line 14 is `turn.completed`. Runner exit is 0.

The run uses workspace-write sandboxing for the one permitted PRD edit and
explicit `web_search="disabled"`. Before/after raw inventories and hashes
identify only `docs/PRD.md` as changed; the other three inputs and all eight
skill files remain unchanged during the run. No rubric/prior-output or
unrelated-repository read, external action, implementation or product-test
execution appears in the complete trace. Editing and counting the document
are not product execution. Trace scope does not audit unretained host state.

All 21 listed archive-file hashes verify. Original inputs match current raw
sources, [case19-before-run.json](case19-before-run.json) and the case 19 entry
in [post-before-run.json](post-before-run.json). The fixed rubric matches both
receipts. All eight selected instruction files match current source, the post
receipt and unchanged before/after metadata. The shared-evidence reference is
the recorded post-change version; no pre-change archive was overwritten.

| Retained item | Whitespace words | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Complete edited PRD | 748 | 5,794 | `298db6e48fc19a0f883033a3a7e5ea845d2e679d6b9d3400ecd3fb7e2e1a7e4a` |
| Final summary | 50 | 384 | `effaf2918047d5fd72ab959fabfd169078a44120765caa55733856249c9140b3` |
| Fixed rubric | — | — | `be5e9cf6f4f05ad2271f942535e755f97d4ede1d4a3f462f368489f3d7a74a85` |
| Post pre-run receipt | — | — | `df3acb1b17a51f4fd32e66f6a5e6c4ef65d64b94317cf2bac03c790b15ff6417` |
| Archive provenance | — | — | `e025c684aa41ff063638f5d0291e4a4c1341d2657b0a5f7de885bda4f9330694` |

The unsigned post receipt is dated 2026-09-08 18:10:48.771 UTC. Run metadata
records 18:10:54.044772–18:12:44.993393 UTC, CLI 0.153.4 and thread
`01a08237-4089-7e33-91fd-13e10a4c6bb3`, with unpinned host-default model
configuration. Hash checks concern retained bytes with documented run-root
path normalization, not original raw log-path reconstruction. This is one
synthetic development observation, not business validation, superiority,
general reliability or instruction-caused improvement. Process completion
and matching hashes are not semantic grades.
