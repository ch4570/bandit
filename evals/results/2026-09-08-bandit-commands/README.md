# BANDIT 0.3.0 — direct specialist invocations

Five fresh Codex CLI 0.153.4 tasks exercised the five `$bandit-*` commands.
Each temporary project contained all six skills under `.agents/skills/`, the
raw case inputs, and no prior outputs or rubric. The prompt invoked the named
specialist. Host defaults were used with `--ignore-user-config`, `--ephemeral`,
and a read-only workspace; no model revision was pinned.

The directory layout and `$skill-name` syntax follow the
[official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).
Each run acknowledged the selected specialist and read its task-specific
references. Four logs additionally show an explicit SKILL.md read; the specify
run used the named skill and read its specification reference directly. These
are observed invocation checks, not a claim about every host's skill selector.

| Command | Raw task and output | Maintainer observation |
| --- | --- | --- |
| `$bandit-research` | [Input](05-small-research--bandit-research/input/request.md) · [Output](05-small-research--bandit-research/output.md) | Chose a provisional segment and low-cost test; distinguished reservation interest from paid demand. |
| `$bandit-decide` | [Input](04-incomparable-scores--bandit-decide/input/request.md) · [Output](04-incomparable-scores--bandit-decide/output.md) | Recommended a scope without inventing a comparable RICE ranking from incompatible inputs. |
| `$bandit-specify` | [Input](01-multiple-decisions--bandit-specify/input/request.md) · [Output](01-multiple-decisions--bandit-specify/output.md) | Kept two independent decisions in one trip and marked delegated policies as drafts. |
| `$bandit-review` | [Input](03-intent-review--bandit-review/input/request.md) · [Output](03-intent-review--bandit-review/output.md) | Used adopted policy to assess the code-derived PRD; distinguished an existing test from observed execution. |
| `$bandit-update` | [Input](02-offer-change--bandit-update/input/request.md) · [Output](02-offer-change--bandit-update/output.md) | Updated the offer and sharing rules while retaining historical observations and their original conditions. |

All five exited with code 0 and stayed within their requested output limits.
Input and instruction hashes were unchanged and matched the source skills.
Logs show only reads of the supplied inputs and specialist resources; the
product code and tests were not executed, and no browsing or outreach occurred.
The runner returned the updated plan in the answer because the fixtures require
read-only work; these runs do not test file-edit behavior.

[Run summary](run-summary.json) records output hashes and whitespace-delimited
word counts. Each run folder retains its raw `prompt.txt`, `events.jsonl`,
`stderr.txt`, `metadata.json`, output, and input files. The recorded observations
are maintainer inspection, not independent blind grades or a new comparison
with baseline or upstream.

## Installer upgrade check

The [npm upgrade receipt](npm-upgrade.json) records actual `npx` use with a fresh
cache and a Korean/spaced temporary project. The old installer came from the
public v0.2.0 release. Version 0.3.0 was served from a temporary HTTP server;
it updated the core and added all five specialists, totaling 37 skill files.
Existing package files and a planning note were preserved.

A synthetic 0.3.1 package then changed the core after the last specialist had
a user edit. The command returned exit 2, leaving all project bytes and all
six installed versions unchanged. This synthetic version was not released.
Temporary paths are redacted in the shared receipt, with the original receipt's
SHA-256 retained. This check is separate from planning behavior.

After publication, the [public installation receipt](public-install.json)
confirmed the exact v0.3.0 README command with only Node/npm/npx/sh on PATH.
Fresh project, unchanged repeat, isolated global, and public v0.2.0-to-v0.3.0
upgrade checks all passed. Each installed skill file matched the release source.
