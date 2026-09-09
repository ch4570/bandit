# Round 5 — independent semantic grades

Two terminal case-18 outputs were graded against the unchanged
[pre-run rubric](../../rubrics/18-onboarding-investment.md), using the raw
request, brief, CSV, and complete archived outputs and event traces. The grader
did not author case 18 or consult its author's analysis. The rubric permits
either investment; choosing reporting is not itself a pass. Process exit 0 and
hash agreement are not semantic grades.

## Results and locators

`S:n` below means line `n` of the complete
[bandit-scope output](pre/18-onboarding-investment--bandit-scope/output.md);
`B:n` means line `n` of the complete
[baseline output](pre/18-onboarding-investment--baseline/output.md).

| Fixed criterion | bandit-scope | Baseline |
| --- | --- | --- |
| 1. Account-level, end-to-end outcome | **Pass.** S:7 gives 9/16 usable shops; S:8 separates 12 shops with storage from 14 events and 35 attempts. No invented missing outcomes or maturity adjustment. | **Pass.** B:3 gives the same material account and event counts and explicitly rejects processing activity as successful onboarding. |
| 2. Assisted results and distinct populations | **Pass.** S:7 separates five rescued usable shops from four with zero support. S:10 denies a proven warning-to-outcome effect; S:16 separates existing paid reporting use from renewal claims. | **Pass.** B:3 separates rescued from unassisted outcomes. B:7 does not equate current payments or requests with renewal/adoption; B:19 treats issue notes as candidate targets, not demonstrated feature effects. |
| 3. Compatible engineering and operating resources | **Pass.** S:12 accounts for 365 pilot minutes, the 240-minute limit, and 120-minute reports. S:14 and S:18 compare 24 and 26 engineering hours with uncertain fixes. S:20 caps all remaining customer work at 120 minutes, admitting at most two shops conditionally. S:22 budgets against existing report effort, not guessed savings. | **Pass.** B:5 distinguishes historical effort from a forecast. B:9 and B:19 compare the two engineering estimates, with manual fallback if correctness cannot fit 30 hours. B:13, B:14, and B:15 allocate 120 + 90 + 30 founder minutes; B:17 stops assistance at the cap and postpones six shops. B:7 labels the 95-minute potential saving conditional. |
| 4. One bounded investment and strongest tradeoff | **Pass.** S:1 recommends the report narrowly; S:14 retains its complete delivery path, S:16 defines cuts and manual obligations, and S:18 fairly identifies unresolved onboarding and the import alternative's unmeasured benefit. | **Pass.** B:1 recommends reporting; B:7 grounds it in an existing job and observed manual effort, not payment alone. B:9 bounds scope and fallback. B:19 acknowledges the misleading import result, candidate import targets, remaining exclusions, and manual rescue. |
| 5. Affordable observation, reconsideration, and scope | **Pass.** S:22 times one complete reporting cycle, including exceptions and recipient access, and would favor bounded import review if effort remains near 120 minutes. The work stays within S:12 and S:20's founder budget; admitted-shop outcomes use the existing form. English, 534 words; observed actions remain read-only and local. | **Pass.** B:21 observes the six owners and one reporting cycle, including delivery help, using B:15's 30-minute observation allocation. Its 60-minute threshold is expressly a proposed decision threshold, triggering reassessment and no expansion on assumed savings. English, 514 words; observed actions remain read-only and local. |

Both runs: **5 pass, 0 partial, 0 fail** under these criteria. Neither answer
promises both builds, all eight admissions, realized time savings, or renewal
effects. The different proposed reconsideration thresholds are permitted by
the rubric and are not observed business results.

## Independent arithmetic and complete-output checks

Recalculated directly from all 16 rows of the supplied
[CSV](../../cases/18-onboarding-investment/onboarding.csv) (header line 1,
records lines 2–17), not from the rubric's totals:

| Quantity | Recalculated result |
| --- | --- |
| Unique shops; attempts; stored events; shops with storage | 16; 35; 14; 12 |
| Usable shops; rescued usable shops; unassisted usable shops | 9; 5; 4 |
| Founder support; mean per admitted shop | 365 minutes; 365 / 16 = 22.8125 minutes |
| Standard CSV versus legacy exports | 7/10 usable and 170 minutes; 2/6 usable and 195 minutes |
| Historical-mean scenario for eight new shops plus unchanged reports | 22.8125 × 8 = 182.5; + 120 = 302.5 minutes |
| Mapping, units, or duplicate-SKU issue-note rows | Eight: S05, S06, S07, S08, S09, S11, S12, S13 |

The brief defines the completed common window at lines 27–32, existing reporting
work at lines 59–68, and estimates at lines 78–91. Thus 6 × 20 = 120 founder
minutes, 120 − 25 = 95 hypothetical minutes released, import 20 + 6 = 26
engineering hours, and report 18 + 6 = 24. Both nominal builds total 50, above
30. Neither the historical-mean extrapolation nor the guessed 25 minutes is an
observed next-week result. Both answers' rounded 183 and 303 are consistent with
the underlying 182.5 and 302.5.

Counts use the entire saved `output.md`, split on whitespace, with Markdown
included and no sections excluded. BANDIT's artifact has **534 words / 3,776
UTF-8 bytes**; baseline has **514 words / 3,560 bytes**. Both satisfy 600. Even
including each trace's preliminary assistant update gives 555 and 530 words,
respectively. The final event message matches each saved output (apart from a
terminal newline). Output SHA256 values:

- BANDIT: `9647def59bf06fc05ca25f082d35c4755674f5ccf51b142f8decc52280ec4a87`
- Baseline: `17f2c57b1aa04d8bdec8e01f8b96b3c23097166eaf4abbda2b316bc3f2b077ba`

## Observed action scope and preserved process issue

The complete [BANDIT trace](pre/18-onboarding-investment--bandit-scope/events.jsonl)
has 11 events. Its completed commands at lines 5, 7, and 9 read/list the request,
installed specialist files, and raw brief/CSV. Line 7 contains the complete
`SKILL.md`, `references/decisions.md`, and
`references/evidence-and-decisions.md` reads. The YAML file was listed but has
no explicit content-read event. All three commands exited 0; line 11 records
`turn.completed`.

The complete [baseline trace](pre/18-onboarding-investment--baseline/events.jsonl)
has nine events. Preserve the process failure at line 5: its initial
`rg --files input instructions` exited 2 because `instructions/` did not exist.
The next command at line 7 successfully read all three raw files, and line 9
records `turn.completed`. No PM instruction snapshot was present or read.
This recovered listing error did not prevent the requested artifact and is not
a material semantic failure under the fixed rubric.

Across both traces, no file writes, implementation, product-test execution,
web calls, contacts, or reads of a rubric, prior output, or unrelated repository
are observed. Both recorded commands use the read-only sandbox with explicit
`web_search="disabled"`; metadata reports task exit 0. Planned report
verification and future owner observations in the answers were not executed.
No additional material outside-rubric output issue was found.

## Integrity and interpretation limits

The [pre-run receipt](case18-before-run.json) records
`2026-09-08T16:53:01.655Z`, before the recorded baseline launch at
`16:53:11.425677Z` and specialist launch at `16:53:11.430798Z`. Independent
SHA256 checks found:

- All **20 retained files** listed by the two archive-provenance manifests
  match their archived digests (12 specialist, eight baseline).
- Each archive's three original raw files matches the receipt and current raw
  files; metadata's before/after input maps agree. The specialist's four
  retained instruction files match the receipt, current sources, and both
  instruction maps. Baseline's instruction maps are empty.
- The rubric still matches the pre-run digest
  `8bd6b0eac874960693b0d338c48586ab55efecfb987d015ae5b13d32ec788698`.
  Current runner/archiver source digests and the complete 34-file skill-tree
  digest also match the receipt. No rubric, input, instruction, archive, or
  receipt bytes were edited by this grading task.

Receipt SHA256:
`5fb6ebb3311bfa01cf0dede85092142b30c1a49c49d453476b64b2b769fd2c6b`.
Archive-provenance SHA256 values are
`2859649231dec09b921d0cdddcf68868c83d97ed599b1662e67438fc33764cd5`
(specialist) and
`03588886874f3c87ff2ebf5b1ae39ad58e87ef5466429267b2936e2cc621aa28`
(baseline). These checks establish retained-byte agreement, not independently
attested execution. Temporary run-root paths in archived metadata are
normalized; this review verifies archived bytes rather than reconstructing
the original unnormalized metadata.

This is a synthetic, author-designed development probe, not a held-out
benchmark or customer validation. The grader knew arm labels. Both runs used
Codex CLI 0.153.4 with no model override; host model defaults and other host
state were not pinned. Local timestamps and receipts are unsigned and not
independently time-attested. Complete retained traces bound the action claims,
not a claim of complete host-state capture. One passing pair does not establish
general reliability, superiority, token savings, realized feature effects, or
business outcomes.
