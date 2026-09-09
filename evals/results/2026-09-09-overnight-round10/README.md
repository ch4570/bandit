# Overnight development, round 10 — 2026-09-09

Two fresh raw-only executions add coverage for a scope decision where no
currently supported complete launch fits the imminent engineering and operating
constraints. They use the unchanged scope skill and a baseline; the cumulative
overnight count is **46 executions**, not passing answers. This is a synthetic,
author-designed development case, not a held-out benchmark or customer evidence.

## The decision under test

[SeatRelay](../../cases/21-standby-admission/request.md) has 12 engineering
hours before a community workshop. The estimated complete standby-admission
journey needs 14 hours before integration fixes. A cheaper form export cannot
confirm seats or update the authoritative gate roster. The only coordinator
has 20 unallocated minutes at lunch, but manual reconciliation needs evening
responses; neither extra staff nor gate allocation authority is available.

The question asks what to fund and what decision follows. It does not prescribe
a prototype, an empty workshop seat, or a particular date change. The
[five fixed criteria](../../rubrics/21-standby-admission.md) permit useful
bounded preparation, future components, or a properly conditional revised path,
provided the answer does not silently substitute them for the adopted launch.

## Observed answers

The [independent semantic review](grades-21.md) rates both answers Pass on all
five pre-run criteria: **502/600 words** for scope, **472/600** for baseline.
The grader knows the arms and performed the earlier coverage audit, but neither
authored this fixture nor acted as either TASK agent. No new material instruction
defect is established, so the skills remain unchanged.

The [scope answer](current/21-standby-admission--bandit-scope/output.md) and
[baseline](current/21-standby-admission--baseline/output.md) both recommend the
estimated two-hour non-production walkthrough, using only the coordinator's
available 20 minutes. They leave ten engineering hours uncommitted to standby
production work. Both distinguish this representation from real offers,
confirmed admission, or verified production behavior.

Both reject the incomplete acceptance/CSV workaround, preserve the existing
64-attendee service, and send the proposed standby deferral to Mara for approval.
The adopted outcome has not already changed. Future production investment needs
a complete estimate including verification and an allowance for fixes; the
walkthrough cannot demonstrate that the production launch fits 12 hours.

These are proposed choices, not an executed prototype, approval, event outcome,
or proof that no conceivable implementation could fit. The baseline also makes
the material distinctions; no instruction effect or comparative advantage is
established.

## Evidence boundaries

The [pre-run receipt](before-run.json) fixes all four raw inputs, the rubric,
all 34 current skill files and the selected four-file standalone snapshot
before both executions. TASK workspaces receive no rubric, author analysis,
prior answer, sibling skill or repository AGENTS file. The baseline receives
no instruction snapshot. Host model defaults are unpinned; the CLI version,
commands, UTC times and observed thread identities remain in the metadata and
trace. This is not a blinded or independently sampled benchmark.

Only terminal outputs are archived. Each run retains input and instruction
bytes and [scope](current/21-standby-admission--bandit-scope/archive-provenance.json)
or [baseline](current/21-standby-admission--baseline/archive-provenance.json)
provenance. Log normalization replaces only the temporary run-root string;
originals remain in the scratch directory. Hashes establish local consistency,
not trusted execution attestation. The baseline's first listing reports that
its absent `instructions` directory does not exist, then it reads the four
inputs successfully. That recovered read error is retained, not a failed TASK
or evidence that it loaded a skill.

The [mechanical audit](run-summary.json) checks both terminal threads, output
bytes and counts, every retained original/archive pair, and unchanged raw and
instruction hashes. Its author also authored the fixture; it is not an
independent semantic verdict. Neither TASK browses, edits files, implements
the product or executes product tests in the retained trace.

The receipt's `*_sorted_map_sha256` fields hash compact JSON **objects** in
sorted-key order. Previous rounds and the fixture author's separate check hash
compact arrays of sorted `[path, hash]` entries instead. Under the earlier
array convention the raw map is
`05eaf239055591e8288fd998e0d32e146b1160f173c5bf2c6c7969eaffff9ad1`
and the skill map is
`471a85742d3858b5383ad9d51953f60cc755783af0e5b96495f7fe85c1cde7c7`.
The underlying file hashes are identical; neither the receipt nor historical
records have been rewritten to unify serialization.

## Engineering and preservation

[Full checks](checks/README.md) report structural validation and regressions
separately from answer quality: 78 Node tests on Node 22.23.2 and 92 Python
tests on Python 3.11.16 pass, along with resource sync, both repository
validators and all five official metadata checks. Compared with the frozen
round-9 ZIP, all 34 skill files and 1,080 previous result files remain identical.
The separate [npm packaging check](checks/packaging.md) produces the same
43-file uncompressed tar as round 9 with different compressed bytes; both
archive identities are retained. Final source packaging is a local checkpoint,
not a new public release or an additional network installation test.
No skill, installer, runner, archive tool,
package manifest or public onboarding command changes in this round. No new CI,
commit, public release or npm registry publication occurs. Existing failures,
partial grades and historical PM Craft evidence remain unchanged.
