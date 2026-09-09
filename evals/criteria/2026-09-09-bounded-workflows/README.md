# Issue 6 held-out fixture draft

Every organization, person, product, metric, and implementation in this draft is synthetic.
These tasks were authored independently of candidate skill instructions. No model runs have
been performed with this draft.

## Layout and delivery

- `evals/cases/07-export-review/`: initial inputs for a narrow, read-only review.
- `evals/cases/08-callback-scope/`: initial inputs for a delivery-scoping task with several decisions.
- `evals/cases/09-pickup-prd-rewrite/`: initial inputs for rewriting an existing PRD.
- `evals/follow-ups/09-pickup-prd-rewrite/request.md`: a later user message; never include it in the initial workspace.
- `evals/criteria/2026-09-09-bounded-workflows/`: blind grading criteria; never copy into a task workspace or agent context.

For an initial run, copy only the chosen `evals/cases/<case>/` contents into the isolated
workspace's `input/` folder. The first two tasks permit no workspace edits. The rewrite
permits editing only `input/docs/PRD.md`. Preserve its initial input tree outside the
workspace before running. Select the appropriate installed skill through the outer
runner, keeping that selection separate from these raw inputs.

For the rewrite continuation, retain the first response and revised PRD in the same
conversation, then send the follow-up file's contents as an actual second user message.
Do not preload that file, concatenate the two requests, or start a fresh conversation
and describe it as a continuation. Archive the first-turn PRD before the second turn.

Each raw directory contains relevant evidence and ordinary unrelated operational
material. The latter is context noise, not embedded instructions or an attack.
Grade behavior against the separately stored criteria, not heading names or a preferred
template. Preserve unedited outputs and disclose failures before changing any criterion.
