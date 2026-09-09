# Round 7 — independent case 19 grades

Grades apply to the actual edited `after/docs/PRD.md` artifacts, not the short
final replies. The grader read the frozen [rubric](../../rubrics/19-library-pickup-reminders.md),
all four raw files, both complete PRDs and the retained traces. The grader was
neither a TASK agent nor the fixture/rubric author. No artifact, rubric, skill,
or prior record was edited. Either rollout recommendation was permitted;
choosing the original 50 is not itself a pass.

## Results and artifact locators

`S:n` denotes line `n` of the
[specialist PRD](pre/19-library-pickup-reminders--bandit-specify/after/docs/PRD.md);
`B:n` denotes line `n` of the
[baseline PRD](pre/19-library-pickup-reminders--baseline/after/docs/PRD.md).

| Fixed criterion | bandit-specify | Baseline |
| --- | --- | --- |
| 1. Coherent adopted queue direction, recommended availability, preserved service rules | **Pass.** S:7 preserves mandatory email, consent/confirmed phone, account authentication, generic content, scoped access and seven-day holds. S:9 proposes the original 50, distinct from Nora's adopted automation; S:28 operationalizes that cohort. S:30 retains deadline/state and desk-scan collection. | **Pass.** B:7 distinguishes adopted automation from undecided availability. B:9 recommends the original 50, retaining optional enrollment even without a current hold. B:29, B:30, B:31 and B:33 preserve all adopted service/access/collection rules; B:35 applies the rollout boundary to queue eligibility. |
| 2. Decision-relevant population, opportunity, reach and outcome interpretation | **Pass, with the unsupported attempt-rate claim below.** S:17 separates 30 opportunities from 20 inapplicable outcomes; S:18 separates reach from S:19's delivered-group and whole-opportunity pickups. S:22 preserves maturity, email exposure and absence of causal attribution; S:24 treats the other 200 as unknown and connects uncertainty to continuation. | **Pass.** B:13 distinguishes first-hold opportunities and mature outcomes. B:17 through B:23 preserve disjoint groups, reach, selected-group pickup and whole-opportunity pickup without adding overlapping columns. B:23 rejects causal attribution/extrapolation; B:9 connects unknown demand and effort to its bounded recommendation. |
| 3. Complete notification-to-pickup path and uncertain-send handling | **Pass.** S:28 queues eligible Ready work once; S:30 preserves reader access to state/deadline and actual collection authority. S:32 rechecks eligibility and suppresses stale/withdrawn work. S:34 distinguishes delivery confirmation from acceptance, retains unknown responses, forbids automatic uncertain retries, limits staff retry and preserves email. | **Pass.** B:33 retains pickup authority and deadline/state. B:35 and B:37 define eligible, deduplicated Ready work and pre-send suppression. B:39 specifies staff outcomes, ID lookup, unresolved lost responses, no automatic resubmission, conditional retry and email fallback. Deferred reader-facing SMS status does not remove access to actual hold state/deadline. |
| 4. Feasible operating boundary and decision-changing observation | **Pass.** S:11 and S:40 account for five developer-days including checks/fixes without asserting feasibility. S:38 budgets 20 + 50 + 20 = 90 staff minutes, with enrollment/dispatch stop branches and email preserved. S:44 reopens expansion using measured effort, reach and mature first-hold outcomes, subject to capacity and queue checks. | **Pass.** B:43 requires estimating the retained journey and defers activation if it does not fit five days. B:45 budgets 30 + 45 + 15 = 90 minutes and pauses expansion/dispatch at capacity. Its economical next observation is logged support demand, reach and queue reliability during the proposed bounded next-week operation (B:9, B:45), rather than an assumed pickup lift. |
| 5. Historical evidence, planned checks, actual edit, cap and action scope | **Pass, with the unsupported adoption-date claim below.** S:22 retains H1 as unresolved; S:42 retains reported v1 staging passes separately from manual operation and unexecuted automation. S:40 gives observable eligibility, permission, stale-state, consent and uncertain-send checks. The actual PRD is 795 words; only that raw file changed, and the final summary is short. | **Pass.** B:23 leaves H1 unproven; B:47 preserves reported v1 staging outcomes and distinguishes operational records from new acceptance results. Its planned checks cover ordinary behavior, permissions, withdrawn consent, terminal holds and uncertain sends. The actual PRD is 741 words; only that raw file changed, and the summary is short. |

Both runs satisfy **5/5 criteria by decision-relevant meaning**. This is not an
error-free-output claim: the specialist's unsupported local claims below are
retained. The rubric does not require a menu of fractions or a particular
rollout verdict; no extra ratio requirements were imported from case 02.

## Independent arithmetic and artifact counts

The five disjoint [CSV rows](../../cases/19-library-pickup-reminders/reader-outcomes.csv),
lines 2–6, sum to **50 readers, 30 ready index holds, 14 delivered readers,
18 early pickups and 23 pickups before expiry**. Thus seven index holds were
uncollected at expiry. The twenty no-ready-hold readers have inapplicable pickup
outcomes, not failures or missing outcomes. Early pickups are included in the
23; adding early and final columns would double-count them.

Among delivered readers, 12/14 = 85.7% collected early and 13/14 = 92.9% before
expiry. Across opportunities those figures are 18/30 = 60% and 23/30 = 76.7%.
Reach is 14/30 = 46.7%, or 14/50 = 28% of pilot readers. The two
consented/confirmed-phone groups contain 18 readers, giving 14/18 = 77.8%
reached readers in that subgroup. No message-attempt count is supplied.
Neither these calculations nor the nonrandom, email-exposed pilot establishes
an SMS-caused improvement or results for the unobserved 200.

| Retained artifact | Complete words | UTF-8 bytes | Cap |
| --- | ---: | ---: | --- |
| Specialist `after/docs/PRD.md` | 795 | 5,995 | Pass: 795/800 |
| Specialist final summary `output.md` | 49 | 376 | Separate short reply, not the capped PRD |
| Baseline `after/docs/PRD.md` | 741 | 5,313 | Pass: 741/800 |
| Baseline final summary `output.md` | 41 | 291 | Separate short reply, not the capped PRD |

Counts independently use complete UTF-8 text split on whitespace, including
Markdown. No PRD section is excluded. Each saved summary exactly matches its
final event message. Final PRD SHA256 values:

- Specialist: `e177246d7c9a49bff299919c45228540797a13cf9a32fe38279ead73b558496c`
- Baseline: `b12079536e3c179ad6402dea648769188d36cda1c08bc93696634485a0d7839d`

## Unsupported local claims, not suppressed by the passes

- **S:18 labels 14/18 as delivered “attempts.”** The export's unit is a reader
  (`pilot-notes.md:12`), and message-attempt totals are absent. The supported
  interpretation is fourteen reached readers among eighteen consented readers
  with confirmed phones, not a measured per-attempt delivery rate. As written,
  the attempt-based claim is unsupported, not merely a style preference.
  **C2 remains Pass** because S:15 frames reader-level calculations, the
  opportunity/reach/pickup populations are correctly distinguished, and the
  unsupported attempt label is not used to estimate branch-wide outcomes or
  capacity. That decision-relevant success does not make the local claim correct.
- **S:7 dates Nora's automation adoption specifically to September 9.** That is
  the pilot report's date; `pilot-notes.md:42` says she approved the direction
  but does not supply an exact adoption date. The claimed date is unsupported,
  not an observed fact or simply a formatting choice. **C1 and C5 remain Pass**
  because the actual adopted rules and authority are retained, the 50-reader
  boundary is expressly proposed rather than attributed to Nora, and original
  v1 checks keep their reported date, environment and execution status. The
  erroneous extra adoption-date claim does not alter those material distinctions.

These are factual caveats, not reasons to demand more arithmetic or rewrite
the frozen rubric. No additional material rollout, authority, edit-scope or
final-cap failure was established. Baseline has no corresponding extra issue.

## Observed edits and recovered commands

The complete [specialist trace](pre/19-library-pickup-reminders--bandit-specify/events.jsonl)
has eighteen events and six completed shell-command records:

- Lines 5, 7 and 9 read the standalone entrypoint, specification/change/shared
  evidence/research references and all four raw files. Returned text matches
  the complete retained snapshots. The template, review reference and metadata
  YAML have no explicit content-read event; no sibling skill was read.
- Line 12 writes the permitted PRD with a heredoc and counts **774 words**.
- Line 14 attempts a history addition using `python`, which is unavailable.
  The retained output says `command not found: python`; the following `wc`
  still reports 774. The compound shell command's exit is **0**, so that exit
  must not be mistaken for a successful edit.
- Line 16 recovers with `python3`, adds the historical manual-workflow sentence
  and counts **795 words**. Reconstruction from the first written text plus
  this replacement exactly matches the retained final PRD. The missing-command
  recovery is not a final artifact or cap failure. Line 18 is `turn.completed`.

The complete [baseline trace](pre/19-library-pickup-reminders--baseline/events.jsonl)
has twelve events and three completed shell commands. Line 5 lists the workspace
and inputs with exit **2** while checking the absent optional `instructions/`
directory; stderr is redirected, so no error message is retained there.
Line 7 successfully reads all raw files, and line 10 writes only the PRD and
counts **741 words**. Its heredoc body exactly matches the final artifact.
Line 12 records `turn.completed`. No PM instruction snapshot was supplied/read.

Both use workspace-write sandboxing for the expressly permitted PRD edit and
explicit `web_search="disabled"`. Neither trace shows product implementation,
product-test execution, external actions, or access to a rubric, prior output
or unrelated repository. The counting/editing commands are document operations,
not execution of the proposed library system or pilot.

## Integrity and interpretation limits

All **34 retained file hashes** match archive provenance (21 specialist,
13 baseline). Each archive preserves all four original raw files matching the
[pre-run receipt](case19-before-run.json) and current fixture. Independent
before/after comparisons find exactly one changed input, `docs/PRD.md`;
request, notes and CSV remain byte-identical. The specialist's eight retained
instruction files match the receipt, current selected sources and metadata
before/after maps. Baseline instruction maps are empty. The rubric still
matches its frozen digest
`be5e9cf6f4f05ad2271f942535e755f97d4ede1d4a3f462f368489f3d7a74a85`.

Receipt SHA256:
`4e5cbc9bc5a7c87617cb96ef1458597b9e58acaa44b90a145e64b7facd4ae13f`.
Its recorded `2026-09-08T17:44:57.809Z` precedes both recorded launches. Both
TASK processes exited 0, independently of the recovered command issues and
semantic grades above. This check verifies retained bytes; normalized log paths
and input/instruction manifests are not a complete capture of host state.

This synthetic, author-designed development pair is not a held-out benchmark,
real library outcome, reliability estimate, or proof of instruction effect or
superiority. The grader knew arm labels. Both used Codex CLI 0.153.4 with no
model override; host defaults are unpinned. Local timestamps/receipts are
unsigned and not independently time-attested. No skill or earlier grade was
changed to obtain these results.
