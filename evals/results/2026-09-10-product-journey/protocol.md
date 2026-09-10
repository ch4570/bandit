# Product journey development check

Written before task execution on the Issue 15 candidate. The source baseline
was main `f3ae10e`. An independent fixture author was given the requested
capabilities, not candidate instructions, previous grades, or intended fixes.
Cases 12 and 13 and their separate criteria must be frozen before any trial.
The instruction author did not read those criteria while making this candidate.

Run five fresh, isolated Codex CLI tasks using the repository runner:

| Case | Direct arm | Prompt output cap | Purpose |
|---|---|---|---|
| 12-launch-handoff | bandit | 1800 words | Connected research, planning, marketing, design, BM deliverable |
| 12-launch-handoff | bandit-specify | 1800 words | Direct specialist delivery of the same requested handoff |
| 13-offer-consistency-review | bandit-review | 1400 words | Cross-artifact review with original inputs unchanged |
| 11-backstage-research | bandit-research | 1000 words | Existing narrow research regression |
| 08-callback-scope | bandit-scope | 1000 words | Existing narrow scope regression |

Use host-default model and effort, a 600-second CLI timeout per attempt,
web search and subagents disabled, and read-only product workspaces. Record
requested settings separately from observed runtime identity; missing telemetry
is unavailable, not inferred. Product executions receive only the raw fixture
and frozen copied skill package, not rubrics, diagnoses, or other outputs.

The existing runner records original inputs, prompt, output, events, stderr,
metadata, skill/input hashes, and workspace integrity. Grade the completed
artifacts independently against the frozen meaning-based criteria and raw inputs.
Preserve failures before repairs and run a fresh attempt after a behavioral
change. Do not revise criteria to fit an answer. Existing cases are public
regressions; the new cases become public development cases after this run.

These are synthetic development checks. There is no old-skill or no-skill
comparison, no representative reliability estimate, no measured business
validation, and no cost/superiority claim. Browsing is deliberately disabled in
these fixture trials, so they do not prove live market research or UI rendering.
Source research performed while authoring instructions is separate evidence.
Normal repository/packaging checks and GitHub CI remain structural and installer
evidence; the contributor loop documents when to repeat actual skill trials.
