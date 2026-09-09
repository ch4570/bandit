# Round 10 — independent case 21 grades

These judgments apply the unchanged [case 21 rubric](../../rubrics/21-standby-admission.md)
to both complete retained answers and the [raw request](../../cases/21-standby-admission/request.md).
The grader did not author the fixture or execute either TASK. The grader did
perform the pre-run scope/general guidance and coverage audit and knows the arm
identities: this is independent, nonblind grading, not a held-out assessment.
No rubric, fixture, instruction, answer or earlier record was changed.

**S** denotes the [standalone scope answer](current/21-standby-admission--bandit-scope/output.md);
**B** denotes the [baseline answer](current/21-standby-admission--baseline/output.md).
Locators below use those retained file line numbers. The funded prototype is
assessed for its stated outcome and constraints, not treated as a required winner.

## Fixed criteria

| Criterion | bandit-scope | Baseline |
| --- | --- | --- |
| C1 — preserve the complete adopted outcome | **Pass.** S:5–13 requires saved acceptance to reach the final admission roster, explains why claim/status alone or a reply CSV cannot deliver admission, and retains closing/recovery as dependencies. S:15 explicitly limits the prototype to a representation, not real offers, confirmed seats or production correctness; S:21 distinguishes the existing 64-attendee service from new standby admission. | **Pass.** B:3–9 connects acceptance to the authoritative gate result, including retries, withdrawals and closing races. The prototype cannot send invitations, save real acceptances, reserve seats or publish a roster. B:1,18 makes continued admission of the existing 64 and leaving eight chairs unfilled a proposed workshop outcome, not delivery of the adopted standby service. |
| C2 — supportable engineering and operating commitment | **Pass.** S:1,7–13 calculates 6 + 5 + 3 = 14 engineering hours against 12 before integration fixes. It rejects fewer offers as a shared-work saving and identifies the CSV's post-20:00 reconciliation dependency, incompatible with Leah's lunchtime availability and gate duties. S:17 spends two engineering hours and Leah's remaining 20 minutes, preserves her existing 25 minutes, and leaves ten engineering hours uncommitted. | **Pass.** B:3,7,13–15 gives the same engineering shortfall, separate operating-time constraint and feasible prototype allocation. It does not omit verification, borrow future hours, add staff, assign reconciliation to gate volunteers or treat noon capacity as post-close availability. B:3,20 bounds the no-launch conclusion to the supplied estimated path rather than proving every conceivable implementation impossible. |
| C3 — authority, permissions and material recovery | **Pass.** S:1,21–23 makes deferral subject to Mara's approval, not an adopted change or Theo's implementation discretion. S:11,13,15,19 keeps roster completion, private status, assignment/withdrawal and recovery material while deferring the connected live service. It neither shortens the response window nor promotes form receipt or gate work to seat allocation. No live substitute is proposed without authority. | **Pass.** B:1,18 explicitly reserves the workshop-outcome change for Mara before invitations. B:5,7 retains the material recovery/roster constraints and gate limits; B:9 prevents the prototype from exposing real users to an incomplete production substitute. Because the recommendation is non-production, the rubric does not require a full permission/state specification for work not being launched. |
| C4 — useful bounded investment and alternatives | **Pass.** S:1,13–19 funds the estimated two-hour walkthrough, names what it produces, deliberately withholds the remaining production allocation, and compares both the full live path and the cheaper export's missing manual work. It defers assignment/acceptance/closing/roster integration together rather than labeling a partial screen a finished launch. | **Pass.** B:3–16 rejects both the incomplete live screen and unavailable CSV/manual path, then allocates the two-hour prototype and included review with ten hours left uncommitted. B:9 defines the learning artifact and its limits. The answer resolves what to fund without an exhaustive specification or a demand to spend every hour. |
| C5 — actionable decision/check, cap and task scope | **Pass.** S:15,17,21–23 gives a bounded Leah walkthrough to reveal workflow misunderstandings, a concrete Theo-to-Mara decision, and a reopening condition: a credible complete plan fitting constraints or an authorized different outcome/resources. Review cannot validate a shorter build estimate or production correctness. Later funding requires revised complete estimates and fix allowance. The entire English answer is 502/600 words; observed commands only read/list permitted files. | **Pass.** B:9,13–20 bounds the review to two engineering hours and Leah's available 20 minutes, assigns the outcome decision to Mara via Theo, and treats a later complete production pilot plus fix allowance as a future funding decision. The walkthrough can inform workflow/usability, not replace integrated verification or validate this workshop's launch. The entire English answer is 472/600 words; observed commands only read/list local inputs. |

Both answers: **five Pass, zero Partial, zero Fail** under the fixed criteria.
No required keyword, table, feature winner or full-specification requirement was
added. Positive process exits do not establish these semantic judgments.

## Independent resource check and additional issues

The raw engineering notes give additive point estimates and explicitly exclude
integration fixes (`engineering-notes.md:3–7,11–15`). The complete supplied
production path totals 14 hours. Building claim/status and close/publish alone
uses 11, leaving one of the available 12 hours for a separately estimated
three-hour integrated check. The two-hour prototype includes its coordinator
review, leaving ten engineering hours uncommitted under both recommendations.

Leah's 45-minute block minus 25 committed minutes leaves 20, entirely before
the 18:00–20:00 offer window (`pilot-brief.md:16–22`, `adopted-rules.md:11–14`).
The manual alternative requires 15 minutes after closing plus five per uncertain
response/withdrawal (`engineering-notes.md:17–21`). Its failure here is temporal
availability and authority, not merely whether 15 is less than 20. Both answers
preserve that distinction. The proposed eight unfilled chairs equal 72 minus
64; they are not all 12 standby members promised admission.

No additional material unsupported factual claim or resource/authority violation
was established. The prototype's review benefits are proposed learning purposes,
not observed outcomes. Both answers expressly retain Mara's authority; their
opening recommendation to defer is not read as already executed or approved.
Neither uncommitted engineering time nor an approved outcome change is invented
as additional production capacity. The useful no-launch result in these two
answers does not establish that this response is universal or that the skill
caused it; baseline reaches the same bounded decision.

## Complete traces and artifact boundaries

The [specialist trace](current/21-standby-admission--bandit-scope/events.jsonl)
contains nine events and two completed shell commands. Line 5 reads the request
and lists the four inputs and standalone skill files. Line 7 reads the complete
scope entrypoint, scope/priority and shared-evidence references, plus all three
supporting raw files. Returned text exactly matches the retained snapshots.
There is no explicit content read of `agents/openai.yaml` or a sibling skill.
Line 8 is the final answer and line 9 is `turn.completed`; both shell commands
and the runner exit 0.

The [baseline trace](current/21-standby-admission--baseline/events.jsonl) also has
nine events and two completed shell commands. Line 5 tries
`rg --files input instructions`; the optional `instructions/` directory is
absent, so `rg` reports the error and exits 2 while listing the inputs. Line 7
then reads all four raw files successfully. Line 8 is the final answer and line
9 is `turn.completed`; runner exit is 0. The initial listing failure is retained,
not disguised as success. No PM skill snapshot was supplied or read.

Both prompts prohibit changes and external actions; metadata records read-only
sandboxing and explicit `web_search="disabled"`. Neither complete trace shows
a file write, external action, product implementation/test, rubric/prior-answer
read or unrelated repository inspection. No word-count command is observed;
the counts here independently split the complete archived answer on whitespace,
including Markdown. The answers are conversation artifacts saved by the runner,
not edited product documents. Trace scope does not audit unretained host state.

## Receipt and archive integrity

All 22 listed archive-file hashes verify: 13 specialist and nine baseline. Each
run's four raw inputs match current fixture bytes, unchanged before/after
metadata and [before-run.json](before-run.json). The four selected specialist
instruction hashes match that receipt, retained bytes and unchanged run hashes;
baseline instruction maps are empty. All 34 current skill files and both
runner/archiver source hashes also match the receipt. The frozen rubric remains
`cd43adfb483bc64f1c4d3a5efd833f418fbd56578735bbd83d19c660fa67d846`.

| Retained item | Whitespace words | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Specialist answer | 502 | 3,596 | `8a149de9181378a0d40e8fc45a71c8260401ece83e1f12d6c3bca755aeed44a3` |
| Baseline answer | 472 | 3,253 | `0b7fa8f990dec036f2e67b36d05a6210a5efec60144a4b18a4134e1b45f67544` |
| Pre-run receipt | — | — | `be910b403e4bb56c1beeee3eba3cea423fedafd2901245ed18f6a6a714fddf8e` |
| Specialist archive provenance | — | — | `2c482ce78583ca2c5a8e22afde27a27346a5f0447a94598b20e9db09916e1e60` |
| Baseline archive provenance | — | — | `266d4e692b17fbf28dadd375024f48dfef0ffbb5a27dc53d972100ec79581e39` |

The local unsigned receipt time is 2026-09-08 19:05:45.009 UTC. Metadata records
19:05:45.171418–19:06:27.152577 UTC for the specialist, thread
`01a08269-7851-7201-9c7c-ca986cf3cec2`, and
19:05:46.354612–19:06:16.823212 UTC for baseline, thread
`01a08269-7cf2-7a43-8ab7-a96d49d15853`. CLI 0.153.4 uses unpinned host-default
model configuration. Archive checks verify retained bytes with documented
run-root path normalization, not original raw log-path reconstruction or trusted
execution attestation. These synthetic development observations do not establish
working software, a successful workshop, customer value, comparative superiority
or an instruction-caused improvement. Earlier failures and partials remain intact.
