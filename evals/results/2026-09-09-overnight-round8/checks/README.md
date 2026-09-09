# Round-8 engineering checks

These local checks are separate from the eight fresh planning TASKs and grades.

- [Node suite](full-node.txt): 78 pass, zero failures/skips, Node 22.23.2.
  Command: `npx --yes --package=node@22 --call 'env -u npm_config_call npm test'`.
  This retains the previously documented inherited-environment adjustment.
- [Python suite](full-python.txt): 92 pass, zero failures/skips, Python 3.11.16.
  Command: `/Users/DEVELOPER/.local/bin/python3.11 -m unittest discover -s tests -v`.
- [Validation](validation.txt): synchronization checks all 16 generated
  resources; both repository validators and all five official metadata checks
  pass. Official checks use the existing development-only temporary validator
  environment, not a new install dependency.

All commands completed with exit 0. Structural validation and packaging do not
measure planning quality or customer value. No installer or runner change was
made in this round.

Initial packaging checks use `/TEMP/bandit-round8-9PIwDl/pack-check/`:

```sh
npm pack --pack-destination /TEMP/bandit-round8-9PIwDl/pack-check --json
/Users/DEVELOPER/.local/bin/python3.11 scripts/build_bundle.py --output-dir /TEMP/bandit-round8-9PIwDl/pack-check
```

The [npm output](pack-check-npm.json) lists 43 files and 2,677,442 compressed
bytes. The [ZIP output](pack-check-zip.json) records 1,171 entries, 12,020,648
bytes, SHA-256 `feca2dd6bf24515ffab0ae59eba63d9cae03483c6c8294215f352beea7e3aea2`.
This intermediate ZIP predates the final case-13 archive, grading, audit and
documentation; it is not the final source checkpoint.

Final local artifacts use the previously unused `dist/overnight-round8/`:

```sh
npm pack --pack-destination dist/overnight-round8 --json
/Users/DEVELOPER/.local/bin/python3.11 scripts/build_bundle.py --output-dir dist/overnight-round8
```

Generated sidecars and the ignored local `CHECKPOINT.json` identify that final
ZIP without inserting its own checksum into the source being archived. Earlier
same-version artifacts remain intact. The [preservation check](preservation.json)
compares 876 prior result files to the frozen round-7 ZIP, including all 93
historical PM Craft files also checked against HEAD. None changed.

No commit, new CI run, public release, registry publication, or network install
check occurred. The public installation command remains pinned to 0.4.0.
