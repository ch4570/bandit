# BANDIT 0.4.0 scope and specification checks

Three fresh Codex CLI tasks checked the renamed scope command, new-spec planning,
and rewriting an existing PRD. These are development checks with fictional
inputs, not a comparison with another skill or evidence of real customer demand.

All runs used `codex-cli 0.153.4`, `--ignore-user-config`, and host-default model
settings; no model override was pinned. The first two runs used a read-only
sandbox. Case 06 used `workspace-write` with instructions to edit only
`input/docs/PRD.md`. No customer outreach, live experiment, or product test ran.

| Case | Entrypoint read in the execution log | Final words | Observed result |
| --- | --- | ---: | --- |
| [01 — multiple decisions](01-multiple-decisions--bandit-specify/output.md) | `bandit-specify/SKILL.md` | 843 | Separate lodging/date decisions, per-decision responses and closing rules, identity limits, and proposed acceptance scenarios. |
| [04 — incomparable scores](04-incomparable-scores--bandit-scope/output.md) | `bandit-scope/SKILL.md` | 273 | Recommends a bounded recovery scope without ranking incompatible RICE inputs or inventing missing reach and effort. |
| [06 — existing spec rewrite](06-existing-spec-rewrite--bandit-specify/after/docs/PRD.md) | `bandit-specify/SKILL.md` | 728 in PRD; 42 in final reply | Reorganizes the paid individual PRD around free team collaboration; keeps designated-customer decisions and renewed approval for changed terms. |

Counts use Python whitespace splitting. These are maintainer observations after
reading the outputs and logs, not independent rubric scores. Case 06 was checked
against its supplied request and the original document; the existing rubric
covers cases 01–05.

For case 06, compare the [original PRD](06-existing-spec-rewrite--bandit-specify/input/docs/PRD.md)
with the [rewritten PRD](06-existing-spec-rewrite--bandit-specify/after/docs/PRD.md).
The new document removes the payment gate and obsolete revenue structure,
distinguishes team editing from customer approval, and specifies conflict,
duplicate-send, and stale-version handling. The paid pilot observations and old
staging check retain their original conditions; they are not presented as proof
of the new free collaboration flow. Additional policies are marked as drafts.

All three runs exited 0. All 34 recorded instruction files were unchanged during
each run, and their hashes matched the reviewed v0.4.0 source at archive time.
Cases 01 and 04 left all inputs unchanged. Case 06 changed only `docs/PRD.md`;
its request and observation files stayed byte-identical. Its log also records an
intermediate `python` command failing with exit 127, followed by successful
recovery using `python3`. The final artifact, not an earlier draft in the log,
is the 728-word document linked above.

Each run retains its prompt, final reply, events, stderr, metadata, and original
inputs. Case 06 has a separate `after/` fixture set so the rewritten PRD's source
links remain readable. Temporary run paths in logs and metadata are replaced by
`<temporary-run-root>`; [archive provenance](archive-provenance.json) records the
original and archived file hashes. Temporary workspaces and copied skill trees
are omitted. [Run summary](run-summary.json) records per-case hashes and checks.

The separate [npm upgrade receipt](npm-upgrade.json) records actual npm execution
from the public v0.3.0 package to a local HTTP-served v0.4.0 package, including
preview, upgrade, unchanged rerun, and edited-retired-skill protection. It does
not establish availability of the public v0.4.0 release asset.

After release, the [public installation receipt](public-install.json) verified
the exact README command with a fresh npm cache and without Git or Python on
PATH. All five skills and 34 files matched the source. Repeat installation,
isolated global installation, and public v0.3.0-to-v0.4.0 migration passed,
including retirement of the old commands and preservation of user notes.
The [release archive receipt](release-archives.json) records verified checksums
for the three published archives and the release commit.

These three single runs do not establish reliability, superiority, or token
savings. Earlier [v0.3.0 results](../2026-09-08-bandit-commands/README.md) retain
their original commands and instruction hashes.
