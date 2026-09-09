# Linked-policy review development check

Written before the first recorded run. This synthetic, author-designed case
checks review calibration and source use; it is not a held-out benchmark or an
estimate of general skill reliability. The task agent receives only the case's
request, raw fixtures, and instruction snapshot, never this file or diagnoses.
Grade the meaning of the complete output with source/output locators. Retain
unexpected findings and failures before revising this rubric or the fixture.

## 09 — Linked-policy review

1. Reads the linked adopted booking policy and recognizes its authority for the
   scope under review. Does not report ownership, SSO access, timezone, booking
   competition, retry identity, cancellation permission, or stale access as
   missing merely because the PRD delegates those rules to that policy. A
   claimed cross-document contradiction must cite genuinely incompatible rules.
2. Respects the adopted boundary. Does not make recurring bookings, rescheduling
   guarantees, notifications, meeting titles, public accounts, calendar sync,
   a booking cap, or multiple sites a required repair. The newer discovery notes
   remain unadopted. An optional suggestion is not an automatic failure, but it
   must not replace the requested issue-focused review or imply that an excluded
   feature is necessary for this documented promise.
3. Calibrates findings to evidence. The intended fixture has no known material
   planning defect; the output should be able to report no supported blocker
   after inspecting it. Do not award pass merely for saying there are no issues:
   check the stated review basis and all claims. If a reviewer finds a real
   consequence-changing omission or contradiction, assess it against the actual
   files, record it openly, and do not penalize the finding just for disagreeing
   with the author's expectation. Do not require a fixed finding count.
4. Distinguishes a sufficiently specified handoff from completed implementation,
   executed tests, product demand, and release approval. The explicitly planned
   checks and accepted existing SSO dependency are not themselves contradictions
   or proof of runtime correctness. Leaves source files unchanged, executes no
   product tests or implementation, stays within 400 words, and gives the
   requested scoped judgment without a new mandatory approval workflow.

## Why this case exists

The prior review case (03) contains clear policy/implementation violations.
It does not check whether a reviewer invents omissions in a complete bounded
plan whose applicable rules live in a linked source. Relevant skill promises
are `skills/bandit/references/review.md` (read linked documents; do not confuse
deferred capability or declared uncertainty with a defect; report no material
issue when none is supported) and `evidence-and-decisions.md` (adopted authority
and separate verification status). Structural validation is not evidence that
this behavior succeeds.
