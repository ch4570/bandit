# 12 — Access transition across two specification revisions

Predeclared before the first sequence run. This is a synthetic, author-designed
development diagnostic, not a held-out benchmark or a reliability estimate.
Grade each criterion pass/partial/fail using fixture and output locators. Keep
unexpected findings, failures, exact outputs and source hashes before changing
this rubric. Semantic equivalents count; no heading structure, wording, or
technical architecture is prescribed.

## Isolation and staging

1. For stage 1, create an isolated task workspace containing only the chosen
   `bandit-specify` instruction snapshot and the contents of
   `evals/sequences/12-access-transition/stage-1/` under `input/`. Execute
   `input/request.md`. Only `input/docs/PRD.md` is editable; its limit is 900
   whitespace-delimited words. Keep the final response brief and archive both
   the resulting PRD and task trace.
2. Do not put stage-2 files, this rubric, expected results, author notes, prior
   diagnoses, the repository root, or other skill versions in that agent's
   workspace/context. Merely asking an agent not to read reachable future files
   is weaker isolation than this sequence requires.
3. Preserve stage 1 before grading or preparing stage 2. Stage 2 starts in a new
   isolated agent with the same skill snapshot, the actual stage-1 input tree,
   and the actual resulting PRD. Overlay only the contents of `stage-2/`:
   replace `input/request.md` and add its two new documents under `input/docs/`.
   All original stage-1 source documents remain available without edits.
4. Never repair, summarize, or replace the stage-1 PRD with an expected answer
   before stage 2. Record stage-1 failures even if stage 2 repairs them. If stage
   1 produces no edited PRD, retain that outcome; using the unchanged baseline
   for stage 2 must be disclosed as that branch, not called successful revision
   accumulation. Run stage 2 even after a partial stage 1 if a usable artifact
   exists, and report both stages separately.
5. Archive and hash every staged raw input, instruction snapshot, request and
   PRD before and after each stage. No product implementation, product test run,
   or source-document editing is authorized. Do not interpret a written planned
   acceptance scenario as an executed check.

## Stage 1 — Public board to private team intake

1. **Coherent new product.** Rewrites the current PRD around internal team
   intake, replacing public discovery, anonymous current reading and the public
   acquisition goal as current behavior. A short history is acceptable; an
   appended new policy alongside equally current public rules is not. Makes
   the new internal pilot goal measurable as a proposed check without inventing
   team adoption or reusing the public sample as internal demand evidence.
2. **Current access and migration.** Requires existing company identity plus
   current invited organization membership. Old public accounts and possession
   of an old URL confer no access. Covers old and new requests, other
   organizations, sensitive information at the login/denied boundary, and
   membership removal including a save from a previously open editing page.
   Does not promise to retract already copied or externally indexed public
   content. No project access or external sharing is invented for this stage.
3. **Policy and processing continuity.** Preserves organization data ownership,
   original attribution after departure, exactly 180 days from closure,
   unchanged retention on access loss, and owner-only early deletion through
   the existing manual console. Uses `data-policy.md` as authority without
   changing it. Continuing author-only editing while `접수`, restricted
   processing authority and `접수 → 검토 중 → 종료` remain coherent; does not
   silently add reopening or author deletion. A concise policy link may carry
   detailed invariants if the PRD creates no competing conflicting rule.
4. **Historical evidence stays truthful.** Retains accessible provenance for
   E1's original public-v1 conditions: 36 invite recipients, 21 writers and
   38 requests, not 36 measured visitors or private-team results. V1 remains an
   executed pass for the former public requirement, historical for current
   access. V2 stays an executed staging pass for the same 180-day rule, with its
   fake-clock/synthetic-data limits; does not reset every prior check to failed
   or claim V2 verifies production/new access. The 9 repeat writers may be
   retained or omitted, but must not be transformed if used.
5. **Implementable bounded handoff.** Observable planned scenarios cover current
   member submission/editing, nonmember old-link denial, removal and stale save,
   and processing/retention policy continuity. Distinguishes adopted changes
   from recommended small defaults and unexecuted checks. Edits only the PRD,
   stays within 900 words, and does not require a new command or approval cycle
   for a delegated reversible detail.

## Stage 2 — Project access and selective external progress sharing

1. **Targeted supersession without reset.** Replaces organization-wide reading
   with membership in the organization and relevant project, plus the explicit
   organization-owner exception. Project processing authority is limited to
   that project's members. Original authorship alone does not restore access.
   Does not retain the old broad team rule as an equally current alternative,
   use the implementation shortcut as authority, or restore the public board.
2. **Existing requests and movement.** Every request belongs to one project;
   migrated requests start in the owner-only `분류 대기` project until assigned.
   Describes owner-led movement, the resulting old/new project visibility and
   stale read/edit behavior. Moving is not cloning, changing attribution or
   resetting closure/retention. Recognizes the open external-grant disposition
   on movement and selects a reasoned, explicitly proposed rule that prevents
   silent transfer of external authorization to the new project's content. Do
   not demand one implementation: revoke-and-reinvite is a sufficient option,
   and another coherent explicit authorization model may satisfy the request.
3. **External scope is precise.** Only an authorized owner or project processor
   creates/updates a request-specific external summary and names one recipient
   email. Verified recipient identity is distinct from possession of the URL,
   organization membership and internal editing permission. Shares only the
   prepared summary and current status, excluding original body, original
   author, internal assignee and other requests. Defines view-only access,
   summary update behavior and revocation on subsequent access; a forwarded
   link does not authorize its new holder. Does not promise erasure of content
   that a recipient already read or copied.
4. **Unaffected rules survive two revisions.** Keeps the original data-policy
   authority, organization ownership, attribution after departure, 180-day
   closure retention, no retention reset on revocation/movement and owner-only
   early deletion. Keeps author-only `접수` body editing, processor status
   changes, no reopening and the remaining exclusions unless the second
   decision actually changes them. Project membership and sharing cannot imply
   ownership transfer or an unrequested external-contribution workflow.
5. **Evidence accumulates under its original conditions.** E1 and V1 keep the
   same public-v1 meanings and provenance after the second edit. V2 remains
   bounded evidence about unchanged retention, not newly rerun. V3's 4 current
   organization-member reads, including two outside the informal HR tag, remain
   a pass for the prior organization-wide requirement; project isolation now
   needs a new check. Its three other-organization denials can inform the
   unchanged organization boundary without proving project isolation. Its one
   removed-member page denial does not become a stale-save test. The prototype
   is not a real-customer pilot, and external sharing remains unexecuted. The
   PRD can cite concise source summaries rather than reproduce every count, but
   must not erase, reverse, relabel or invent these observations.
6. **Observable changed outcomes and artifact scope.** Planned scenarios cover
   a same-organization nonmember's denial, owner access to unassigned requests,
   an old member acting after movement/removal, intended-recipient-only external
   reading, no internal-field disclosure, and revocation/move behavior. Source
   documents remain byte-identical and only the carried PRD changes, within
   900 words. Current decisions, proposals, implementation observations and
   verification are distinguishable. Report sequence accumulation separately
   from mere single-stage plausibility or structural validity.

## Promises exercised

`skills/bandit-specify/SKILL.md` and the canonical `specification.md`,
`changes.md`, and `evidence-and-decisions.md` references promise coherent
rewrites, selective dependency updates, preserved historical conditions,
source authority, shared-access/revocation rules, bounded artifact edits and
honest verification status. This sequence exercises those promises over two
successive adopted changes using the first actual output as the second
baseline. It does not measure implementation quality, security of a deployed
service, customer demand or general comparative superiority.
