# Round-7 engineering checks

These local checks are separate from the four planning TASKs and their grades.
All commands below completed with exit 0:

- `node scripts/sync-skills.mjs --check`: 16 synchronized specialist resources.
- `npm run validate` and Python 3.11.16's `scripts/validate.py`: five skills,
  34 files, no structural/reference errors.
- `npx --yes --package=node@22 --call 'env -u npm_config_call npm test'`:
  **78 passed**, no failures or skips, on Node 22.23.2.
- `/Users/DEVELOPER/.local/bin/python3.11 -m unittest discover -s tests -v`:
  **92 passed**, no failures or skips, on Python 3.11.16.
- All five official metadata validators pass using the existing temporary
  development-only validator environment. No end-user dependency was added.

Complete outputs are retained in [Node](full-node.txt),
[Python](full-python.txt), and [validation](validation.txt) logs.
The npx environment adjustment is the inherited-setting issue already documented
in round 2, not a new runtime or product requirement. These counts do not measure
planning quality, token savings, or customer value.

Initial packaging also passes in the new scratch directory
`/TEMP/bandit-round7-UmJkjg/pack-check/`:

- `npm pack --pack-destination /TEMP/bandit-round7-UmJkjg/pack-check --json`
  includes 43 files.
- `/Users/DEVELOPER/.local/bin/python3.11 scripts/build_bundle.py --output-dir /TEMP/bandit-round7-UmJkjg/pack-check`
  produces 1032 entries and 11226721 bytes, SHA-256
  `3da2c54e78272907eac09d7a2ed5648a1bd447636092239db0d8f5c37728f8df`.

That intermediate ZIP predates the final grading, audit and documentation files;
it is retained as a packaging check, not the final source snapshot.
Final same-version artifacts use the previously unused `dist/overnight-round7/`:

```sh
npm pack --pack-destination dist/overnight-round7 --json
/Users/DEVELOPER/.local/bin/python3.11 scripts/build_bundle.py --output-dir dist/overnight-round7
```

The generated sidecars identify the final ZIP without inserting its own checksum
into its source payload. Earlier builds and all historical PM Craft records are
preserved. There was no new CI run, commit, public release, registry publication,
or network installation check. The public command still points to release 0.4.0.
