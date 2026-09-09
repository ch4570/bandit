# Overnight development, round 6 — 2026-09-09

This engineering-only round corrects staged-source handling in both installers.
It adds **zero planning TASKs**; the cumulative overnight count remains **32**
(6 + 9 + 11 + 4 + 2). Those are executions, not a count of passing answers.
The [previous round](../2026-09-09-overnight-round5/README.md), its results,
and the historical PM Craft evidence remain unchanged.

## Reproduced defect and correction

After writing a temporary payload, the installers rechecked the destination
but did not verify the staged source before promoting it. Two controlled
ordinary-file changes reproduced this gap in each implementation:

- Editing staged bytes in place allowed those edited bytes to become the
  installed file.
- Replacing the staged object with a different file containing identical bytes
  allowed a file not owned by this write to be promoted from that pathname.

The [before receipt](checks/before.md) records both failing tests per language,
with full output and frozen hashes. The existing 48 Node installer tests still
passed. Four old post-write test hooks were adapted to accept pathname or
descriptor writes, with the same injection boundaries and assertions; the
adapted hooks passed before the implementation changed.

Both installers now write through the created descriptor, retain its completed
file identity and metadata, and verify the staging pathname's regular-file
identity and exact bytes after the destination check and before replacement.
Cleanup removes a staged file only while those checks still establish ownership.
The existing lock-release predicate is shared without changing its fields.

The unchanged new tests now pass in [Node](checks/after-node.txt) and
[Python](checks/after-python.txt). Their complete destination snapshots verify
that the staged edit or replacement remains, the earlier managed-file change
rolls back, and the old ownership marker survives. These are synthetic local
regressions, not reported user incidents or customer evidence.

## Limits and disclosure

Checks and replacement/unlink are still separate filesystem operations, not an
atomic compare-and-swap primitive. The final check-to-use intervals remain.
Changed or unverifiable temporary files, including writes without a verified
completed identity, may intentionally remain for inspection. This does not
establish crash durability, complete partial-write cleanup, or protection
against every concurrent filesystem change.

A separate agent diagnostic was stopped by the tool's safety filter; it produced
no usable finding and was not retried or used as evidence. The two independently
underway staged-source regressions above are the evidence for this correction.
No claim is made about the unrun diagnostic.

An [independent static review](checks/static-review.md) found no blocking
ordinary-path defect and records additional exceptional-path limits. It also
distinguishes the new tests' injection timing: Node changes the staged path
before identity capture, Python afterward. Their before/after comparisons are
frozen within each language, not identical cross-language interleavings.

## Verification

- Full [Node suite](checks/full-node.txt): **78/78** pass on Node **22.23.2**.
- Full [Python suite](checks/full-python.txt): **92/92** pass on Python **3.11.16**.
- [Synchronization, repository validators and all five official metadata checks](checks/validation.txt)
  pass. These are structural/engineering checks, not planning-quality scores.
- [Preservation hashes](checks/preservation.json) confirm all 34 skill files
  match the start-of-round snapshot and all 93 historical PM Craft files match
  HEAD. The new staging tests and adapted legacy hooks match their before hashes.
- `npm pack` and source ZIP creation pass separately from the test suites;
  the [packaging receipt](checks/packaging.md) distinguishes the initial check
  from the final same-version local artifacts.

The Node command is
`npx --yes --package=node@22 --call 'env -u npm_config_call npm test'`;
the Python command is
`/Users/DEVELOPER/.local/bin/python3.11 -m unittest discover -s tests -v`.
The environment adjustment is the previously documented inherited npx setting,
not an installer dependency or behavioral change.

This round's local artifacts use `dist/overnight-round6/`, leaving every earlier
same-version build intact. No commit, new CI run, public release, registry
publication, or skill-instruction change is part of this checkpoint.
The public installation command still pins release 0.4.0.
