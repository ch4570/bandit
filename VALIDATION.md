# Validation record

Validation concerns both the distributable skill and its behavior. The two are
reported separately. All product fixtures in this repository are synthetic.

## Local checks — 2026-09-07

On macOS arm64, Python 3.11 and 3.12:

- Repository installer, archive, and validation tests: **38 passed**.
- Skill structure and references: **passed**, nine distributable skill files.
- OpenAI skill-creator `quick_validate.py`: **passed** using an isolated Python
  3.12 environment with PyYAML 6.0.3. PyYAML is not a runtime dependency.
- Actual skill installation into a temporary project: files matched the source;
  a repeated install returned `unchanged`.
- The archive test extracts a bundle, hides its source checkout, and installs
  using the extracted installer, checking the complete skill contents.

An independent installation review found case-insensitive filesystem defects:
case-only file renames could delete a managed file, and aliased path casing could
bypass source/destination and bundle-output containment. These were reproduced
on APFS, fixed before release, and added to the regression suite. Case-only managed
renames are now a preflight conflict that preserves the existing installation.

The tool tests cover meaningful preservation and packaging behavior. They do not
evaluate product demand, the quality of a PRD, every filesystem, or every agent host.

## Behavior

See [evaluation inputs, methods, outputs, and limitations](evals/README.md).
Forward testing uses fresh task contexts without the rubric or author diagnoses.
The comparison has baseline, pinned upstream, and PM Craft conditions; source
differences alone are not treated as evidence of superior model behavior.

## Reproduce repository checks

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build_bundle.py
```

Requires Python 3.11+. GitHub [CI](.github/workflows/ci.yml) defines Linux, macOS,
and Windows jobs on Python 3.11 and 3.14. A configured workflow is not itself a
completed remote run. Release assets are built from the version tag by the
[release workflow](.github/workflows/release.yml).

## Limits

Package tests use temporary directories and local fixtures, not external services.
PM behavior depends on the model, the supplied context, and the host's tools.
No real customer interviews, live launch experiments, or production application
tests were performed to validate PM Craft. No claim of general superiority,
token savings, or product-market fit follows from these checks.
