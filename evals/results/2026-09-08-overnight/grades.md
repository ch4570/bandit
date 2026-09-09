# Independent meaning-based grades

A separate grading agent received raw inputs, the pre-run rubrics, completed
outputs and run metadata/logs. It received no author diagnosis. It knew the
condition names, so this is independent grading, not blinded condition grading.
All conditions below use the original rubric; none was changed after execution.

## Specialist runs

| Case and condition | Grade | Output evidence |
| --- | --- | --- |
| 07.1: launch within capacity | Pass | Lines 1, 28: manual pilot; 1 day setup + 1 day verification + 3 days corrections/buffer, explicitly a plan rather than a delivery guarantee. |
| 07.2: manual operating capacity | Pass | Lines 9–12: unconstrained 108-minute peak; separate 2-request/2-pickup/2-return caps; 36 minutes + 10 for one exception + 14 spare. |
| 07.3: complete lending path | Pass | Lines 8, 16–20: damaged drill excluded; receipt/confirmation separated; eligibility, active loans, physical items, inspection and affected promises addressed. |
| 07.4: cuts and prelaunch check | Pass | Lines 12, 26–34: deferred features, provisional capacity and named failure scenarios to rehearse within Mina's working hour. |
| 08.1: maturity and missing outcomes | Pass | Lines 22–26: A 8/20; mature B 5/10; three missing outcomes imply 50–80% bounds; four early repeaters and 20 immature teams separate. |
| 08.2: cash, recurrence and causality | Pass | Lines 11–13, 28: 60% first-payment conversion each; $400/$300 after refunds; missing team-level join, unmeasured renewals and simultaneous changes limit conclusions. |
| 08.3: cash versus time cost | Pass | Lines 14–18: vendor-adjusted $350/$225, 3/22.5 hours, time-adjusted $260/−$450; imputed time distinguished from paid cash and full profitability. |
| 08.4: bounded decision | Pass | Lines 3, 32–36: defer broad rollout, observe one renewal among existing customers with linked activity and incremental costs; criteria labeled proposed. |
| 09.1: linked authority | Pass | Lines 3–7: linked P1–P4 policy governs delegated access, conflict, retry and cancellation rules; log confirms it was read. |
| 09.2: scope boundary | Pass | Line 8: discovery notes remain unadopted; excluded capabilities do not become required repairs. |
| 09.3: calibrated review | Pass | Lines 1, 5–10: no supported material issue, with source-specific reasoning independently checked against the raw files. |
| 09.4: verification and task limits | Pass | Lines 1, 10–12: document consistency distinguished from implementation and release approval; 208 whitespace-delimited words, no product tests or edits. |
| 10.1: original booking | Pass | Lines 3, 12, 14–15, 27, 32: replaces cancellation-first; original survives failure; joint replacement/release with entitlement transfer. |
| 10.2: states and time | Pass | Lines 7, 11–14, 17–22: hold/booking/replacement and authority; server expiry, exact 24-hour boundary and labeled proposed rules; explicit timezone. |
| 10.3: contention and recovery | Pass | Lines 12, 14–15, 19–23: capacity, one owner hold, stale requests, recorded same-attempt outcomes and actual-booking lookup. |
| 10.4: observable acceptance | Pass | Lines 25–37: success, expiry, contention, stale tabs and response loss; planned checks, synthetic sources and unmeasured five-day delivery; 658 words. |

For case 09, the suggested future check of result recovery after start is
supported by policy P3's recorded-attempt behavior and P4's shared retry/refresh
behavior. It does not claim a new cancellation may succeed after start.
For case 10, the ordinary-cancellation race rule is a labeled recommendation
and does not restore cancellation-first behavior.

Outside the rubric, the grader noted one minor gap in 08: the next-observation
criteria do not explicitly choose an action if renewals are positive but do not
cover incremental contribution costs. No arithmetic error or material
unsupported claim was found.

## Baseline counterparts

| Case and condition | Grade | Output evidence |
| --- | --- | --- |
| 09.1: linked authority | Pass | Lines 3–8 apply the linked P1–P4 policy correctly; events confirm it and discovery notes were read. |
| 09.2: scope boundary | Pass | Line 10 preserves future ideas as unadopted without requiring excluded features. |
| 09.3: calibrated review | Pass | Lines 1, 5–12 support the no-material-issue judgment with accurate source-specific reasoning. |
| 09.4: verification and task limits | Pass | Lines 1, 12 distinguish documented requirements from implementation, release approval and demand; 205 words. |
| 10.1: original booking | Pass | Lines 3, 10, 13–14 reject cancellation-first and require replacement/release/entitlement transfer together. |
| 10.2: states and time | Pass | Lines 9–13, 16–20 distinguish browsing/holds/confirmation, ownership, server time, timezone and proposed boundary rules. |
| 10.3: contention and recovery | Pass | Lines 19–22, 31–37 define exclusive capacity, atomic hold replacement, stale-state rejection and same-attempt recovery. |
| 10.4: observable acceptance | Pass | Lines 5, 24–37, 41 give acceptance outcomes, separate walkthroughs from executed tests, preserve exclusions and qualify delivery; 614 words. |

Both baseline outputs are complete. Their events contain discovery and file
reads only, with no product tests, implementation or skill reads. All before/
after input hashes match. Baseline 09's optional lookup for an absent instruction
directory returned exit 1 before successful task completion.

Both arms produce supported no-issue reviews for 09. For 10, the specialist
recommends rejecting a second target until explicit release; baseline recommends
atomic hold replacement that preserves the earlier hold if acquisition fails.
The raw policy allows either recommendation. No rubric-level quality difference
was observed in these two single-run comparisons.
