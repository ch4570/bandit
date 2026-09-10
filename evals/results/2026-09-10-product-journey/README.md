# Product journey development checks — 2026-09-10

This record covers research → planning → marketing → product-design handoff →
business-model design for [Issue 15](https://github.com/ch4570/bandit/issues/15)
and [Issue 16](https://github.com/ch4570/bandit/issues/16). Inputs are synthetic.
These are development checks, not business validation, a quality advantage,
a reliability estimate, or a cost comparison.

## Tasks and outputs

| Label | Task and direct skill | Outputs |
|---|---|---|
| A | Callback MVP scope, `$bandit-scope` | [First](runs/08-callback-scope--bandit-scope/output.md), [second](round2/runs/08-callback-scope--bandit-scope/output.md) |
| B | Backstage research, `$bandit-research` | [First](runs/11-backstage-research--bandit-research/output.md), [second](round2/runs/11-backstage-research--bandit-research/output.md) |
| C | Café launch: research, scope, marketing, UX, BM, `$bandit` | [First](runs/12-launch-handoff--bandit/output.md), [second](round2/runs/12-launch-handoff--bandit/output.md) |
| D | Same requested handoff, direct `$bandit-specify` | [First](runs/12-launch-handoff--bandit-specify/output.md), [second](round2/runs/12-launch-handoff--bandit-specify/output.md) |
| E | Shoe-service offer/price/UX/delivery review, `$bandit-review` | [First](runs/13-offer-consistency-review--bandit-review/output.md), [second](round2/runs/13-offer-consistency-review--bandit-review/output.md) |
| F | Live official competitor research, `$bandit-research` | [Native first task](live-research/output.md), [second CLI task](round2/runs/14-live-channel-research--bandit-research/output.md) |

The first five offline tasks passed their mandatory meaning criteria, but C
listed 700,000 KRW of budget items while reporting 800,000 KRW. It stayed within
the cap, so the original criterion passed; the arithmetic was still wrong.
The native live task received four passes and two partial judgments: its quoted
Cal.com currency was unspecified, and its transport did not export original
web-retrieval events. These limitations are preserved in the first
[journey](grades/round1-journey.md), [regression](grades/round1-regression.md),
and [live research](grades/round1-live-research.md) grades.

The second candidate adds general numerical reconciliation and currency checks.
All six fresh CLI tasks exited successfully with unchanged input/instruction
inventories. The [second journey grades](grades/round2-journey.md) pass all
mandatory criteria for C/D/E and find no substantive arithmetic error; A/B also
pass all criteria in the [second research/scope grades](grades/round2-research-scope.md).
The live answer F still has four passes and two partials: quoted currencies
remain explicitly unresolved, and completed search events do not include the
original returned page payloads. Its consequential source claims were independently
corroborated. Unlike the initial answer, it expressly withholds cross-company
monetary comparisons while currency is unknown, as the raw task permits.
The trace records five completed web-search events, available separately as a
[web-only extract](round2/retrieval-events.json). This improves audit evidence
without claiming full original-page capture. No criterion or output was rewritten
to turn the first results into successes.

## Method and provenance

See the [first protocol](protocol.md), [native protocol](live-protocol.md), and
[corrective protocol](round2-protocol.md). Cases 12–13 and their criteria were
authored independently of product instructions and previous outputs; their
[freeze manifest](../../criteria/2026-09-10-product-journey/freeze.json) predates
the relevant runs. Cases 08/11 are public regressions. Case 14 is primary-authored,
not independently held out.

CLI tasks received only their raw request/fixtures and copied skill package.
Graders received anonymous answers, raw inputs, and unchanged criteria without
skill instructions or author diagnoses. The final live grader also received
completed web events and independently checked official source claims. Styles
may reveal clues; no attested double-blind study or hermetic isolation is claimed.

CLI version: 0.154.0. Model/effort: host defaults, without attested backend identity.
Timeout: 600 seconds per attempt. Prompt caps: handoff 1800 words, review 1400,
narrow regressions 1000, final live research 1800. These are not billing caps.
Per-attempt usage and elapsed times remain in the [first](execution-summary.json)
and [second](round2/execution-summary.json) execution summaries. Monetary cost,
native usage, and development/grading usage are unavailable, not zero.

All CLI runs preserve original/final inputs, prompts, outputs, events, stderr,
metadata, and hashes. Duplicate instruction folders/assets are omitted from
published workspaces. Final source matches every second-round instruction hash.
The [first reference bytes](instruction-snapshots/round1-product-journey.md.txt)
preserve the changed instruction; other skill files match final source. The
[first runner bytes](instruction-snapshots/round1-run-local.py.txt) were reconstructed
from `f3ae10e` plus the exact local-case patch and verified against recorded hashes.
The native task has a separate [limited receipt](live-research/receipt.json).

Both general-skill runs tried a misspelled `SILL.md` path before reading the real
`SKILL.md`; the recovered failures remain in raw traces. Neither second-round
handoff trace used a calculation tool. Independent arithmetic checks can verify
those outputs, but do not prove consistent adherence to the tool-use instruction.

Live retrieval does not demonstrate customer contact, payment, or product use.
UX checks assess a design handoff, not rendered screens or observed usability.
The contributor [repeat-check procedure](../../../CONTRIBUTING.md#repeat-skill-quality-checks)
is manual for behavior changes/releases; CI does not schedule model evaluations.

## Repository checks

- Source synchronization: 25 resources matched; Node/Python structural validators: 45 skill files passed.
- Node tests: 79 passed, including isolated npm package consumption.
- Python tests: 194 passed, including 27 runner tests.
- Python compilation, Issue-form YAML parsing, and staged whitespace checks for authored sources passed. Raw `output.md` files retain their original Markdown two-space line breaks; the unfiltered staged check reports those as trailing whitespace, and their bytes were preserved for hash/grade integrity.
- npm archive and source ZIP built in temporary directories; no new release was published.
- Optional official `quick_validate.py` was unavailable because host Python lacks PyYAML. No dependency was added; both dependency-free repository validators passed.

Historical PM Craft 0.1.0 outputs and hashes remain unchanged. This guidance is
unreleased and is not in the published v0.4.0 install archive.
