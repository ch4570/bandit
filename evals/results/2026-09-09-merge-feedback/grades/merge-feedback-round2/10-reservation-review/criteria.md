# Blind criteria: synthetic organizer-response review

Never include this file in the executing agent's workspace or context. Judge source-backed
reasoning and practical consequences, not headings, wording, a fixed finding count, or a
preferred storage design. All sources and data are synthetic. This case was authored without
consulting candidate instructions or prior grades.

## Acceptance dimensions

- Follow the linked adopted policy and distinguish it from proposed endpoint behavior.
  The policy already defines the logical repeat boundary and changed-content semantics.
  A review must not report those product rules as missing or ask the user to choose them
  again. Unspecified technical retry-token design is a separate implementation question.
- Explain why exact retries and acceptance of changed offer contents can have different
  meanings. The one-row lookup by reservation/member runs before revision validation and
  can replay an earlier acceptance for a newer revision; it can also bypass the required
  superseded-revision response. Connect any proposed correction to the existing policy,
  without assuming every repeated request is a duplicate or every new request is unique.
- Assess permission enforcement against assigned-organizer authority, not merely active
  membership and workspace boundaries. The plan correctly checks the workspace but allows
  other members of that same workspace to accept. Do not falsely claim it lacks all access
  checks or assert an unspecified external authentication vulnerability.
- Trace a publication failure after the durable insert: the later retry can return the
  existing accepted row without publishing the missing event. Explain the potential stuck
  operation and the misleading room-allocation message with reference to the ledger's
  authority. Existing consumer deduplication alone does not repair an unpublished event.
- Treat acceptance-versus-withdrawal during ledger application as a genuinely unresolved
  operations decision. State the decision needed and useful acceptance implications; do not
  invent a winner, cancellation right, or automatic release rule and present it as adopted.
- Recommend observable checks or bounded changes that distinguish appropriate reuse,
  changed revisions, wrong actors, and interrupted handoff. Separate static observations
  from test results and assumptions. No broad redesign, public-signup work, payments work,
  or community-event analysis is needed.

Preserve output excerpts for substantive omissions, unsupported claims, or false reports of
missing rules. Evaluate unauthorized workspace edits separately as integrity failures. Do not
rewrite these criteria after seeing results without preserving and disclosing the original.
