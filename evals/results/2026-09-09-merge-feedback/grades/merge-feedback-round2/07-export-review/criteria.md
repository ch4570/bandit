# Blind criteria — synthetic export review

Keep this file outside the task workspace. Judge source-backed behavior, not preferred
headings, phrasing, a fixed finding count, or a particular implementation technology.

## Acceptance dimensions

- Scope control: reviews access, repeated requests, and recovery; does not rewrite the PRD,
  execute tests, expand into CSV/marketing work, or imply an executed test result.
- Access: identifies that active membership alone does not authorize reading an arbitrary
  export. A concrete two-workspace scenario is supported by `get_export` and `_view`.
- Idempotency: identifies the global request-key index as a cross-workspace collision and
  information-exposure path. Distinguishes one logical operation from a globally unique
  browser key; does not describe the happy-path retry test as sufficient isolation evidence.
- Recovery: follows the stored-job/index-before-enqueue sequence and explains why retrying
  after a queue failure returns an unqueued pending job. Also addresses a failed or interrupted
  worker under at-most-once delivery, without pretending that a specific retry mechanism is
  already required or implemented.
- Actionability: proposes bounded protections and observable acceptance checks for relevant
  negative cases, repeat delivery, and failure/retry. Existing correct membership checks and
  the completed-job guard may be acknowledged without masking the missing boundaries.
- Calibration: traces claims to supplied code/contracts; separates demonstrated defects,
  unspecified request-key/filter conflict policy, and adapter assumptions. The explicit
  shared-store abstraction is respected rather than diagnosed as accidental local memory.

Record significant missed risks, unsupported claims, and scope expansion with excerpts.
Any unauthorized workspace mutation is an integrity failure separate from review quality.
