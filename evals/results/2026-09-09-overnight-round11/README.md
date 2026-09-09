# Overnight development, round 11 — 2026-09-09

This round corrects a misleading installer note and makes recorded skill
outputs easier to find in the usage guide. It adds **zero planning TASKs**;
the cumulative overnight count remains **46 executions**. All five skills
remain unchanged. Curating examples is documentation work, not a fresh
planning-quality result or a regrading of earlier answers.

## Incorrect cleanup advice for a custom destination

[INSTALL.md](../../../INSTALL.md) permits an arbitrary general-skill folder
name except the active/retired specialist names. A valid `--dest .../pm-craft`
therefore installs BANDIT at that exact location. The previous CLI then saw
the same directory as a separate PM Craft installation and advised manual
removal while claiming it had left that directory untouched.

The [before-fix reproduction](checks/legacy-note-before-results.json) runs the
real local CLI under Node 22.23.2 in fresh macOS scratch directories. Both
`pm-craft` and case-aliased `PM-Craft` exhibit the false note after installation,
on repeat, in the later preview, and in ordinary text output. Fresh previews
do not exhibit it because the directory does not exist yet. A genuinely
separate legacy folder remains correctly reported and its sentinel preserved.
All 12 CLI commands exit 0: this is a reporting defect, not failed installation
or an observed deletion of the newly installed files.

The fix excludes the actual normalized core destination before adding the
legacy note. It changes no destination selection, ownership check, skill payload,
migration decision or removal rule. Python has no corresponding legacy note,
so its installer remains unchanged.

One new focused regression retains the same assertions before and after the
source change. Before, the genuine-sibling control passes and the custom-core
test fails on eight false-note observations. Main's first post-fix run passes
both selected tests. The [retained regression record](checks/legacy-note-regression.md)
contains the immutable old source, raw failure, separately retained post-fix
checks and exact source/test identities. These scratch checks are not another
public GitHub download, host-discovery test or cross-platform measurement.

## Usable examples without relabeling history

- [ChangeDesk](../../../examples/change-desk.md) now invokes `$bandit-specify`
  for its single existing-PRD rewrite; GatherTrip's general request retains
  `$bandit`. No historical input or output command is rewritten.
- The Korean [scope prompt](../../../docs/usage.ko.md) now says the customer
  accepts or rejects the request, then retrieves the result. This removes the
  ambiguity of merely “checking” it and aligns with the English approval
  journey. Both usage guides link the same new examples.
- [HoldHarbor](../../../examples/library-pickup.md) links the original inputs
  and actual edited PRD from round 8, distinguishing adopted rules, proposed
  availability, historical observations and planned checks.
- [SeatRelay](../../../examples/standby-admission.md) links round 10's scope
  recommendation and explains the difference between a bounded prototype
  and the promised admission outcome. It retains the baseline's successful
  reasoning and the limits of the supplied estimates.

The [examples index](../../../examples/README.md) separates **unreleased local
BANDIT development** from historical **PM Craft 0.1.0** records. Both new pages
label their shorter English/Korean prompts as adaptations, not the exact
evaluated requests. Neither page is a public 0.4.0 result, customer evidence,
quality benchmark or proof of an instruction-caused gain.

Independent read-only documentation review verifies 108 local file-link
occurrences across nine onboarding/example documents, aligned command and
language meaning, and unchanged linked raw/output/grade bytes. That check
does not validate heading anchors or establish model behavior. The original
fixture author's separate fact selection is not independent quality grading.

## Verification and preservation

[Full checks](checks/README.md) separate engineering regressions and structural
validation from planning behavior: **79 Node tests** on Node 22.23.2 and
**92 Python tests** on Python 3.11.16 pass, along with resource sync, both
repository validators and all five official metadata checks. The separate
[npm pack check](checks/packaging.md) contains the same 43 paths as round 10,
with only the installer source changed. Final npm/source-ZIP packaging is recorded
in the local ignored `dist/overnight-round11/CHECKPOINT.json`, not a new public
release. Compared with the frozen round-10 ZIP, all 34 skill files and 1,141
prior result files remain unchanged. Earlier failures/partials and the 93
historical PM Craft files are preserved. No new CI, commit, public release or
npm registry publication occurs; the public installation command still pins
0.4.0.
