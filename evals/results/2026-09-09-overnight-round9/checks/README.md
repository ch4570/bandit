# Round-9 engineering checks

The integration results and their retained first-harness failure are described
in the [round record](../README.md). These full suites are separate checks:

- [Node](full-node.txt): 78 pass, zero failures/skips, Node 22.23.2.
  Command: `npx --yes --package=node@22 --call 'env -u npm_config_call npm test'`.
  The environment adjustment is the inherited-setting issue already recorded
  in round 2, not a new dependency or installer requirement.
- [Python](full-python.txt): 92 pass, zero failures/skips, Python 3.11.16.
  Command: `/Users/DEVELOPER/.local/bin/python3.11 -m unittest discover -s tests -v`.
- [Validation](validation.txt): 16 synchronized resources, both repository
  validators and all five official metadata checks pass. The existing temporary
  development validator environment is not an end-user dependency.

All commands above completed with exit 0. The new integration harnesses are
one-off retained development evidence, not part of the default test command or
an end-user runtime. No planning-quality benchmark follows from these checks.

Final local artifacts use the previously unused `dist/overnight-round9/`:

```sh
npm pack --pack-destination dist/overnight-round9 --json
/Users/DEVELOPER/.local/bin/python3.11 scripts/build_bundle.py --output-dir dist/overnight-round9
```

The separate ignored `public-sources/` directory retains the actual downloaded
0.4.0 and 0.3.0 tarballs. Those upstream archives are not the newly packed local
candidate and are not included in the source ZIP. Sidecars and an ignored local
`CHECKPOINT.json` record final artifact identity and source/payload verification
without inserting a final checksum into the source being archived.

[Preservation](preservation.json) verifies 1,030 earlier result files and all 34
skill files against the frozen round-8 ZIP, plus the 93 historical PM Craft
files against HEAD. The historical files are included in the 1,030. Both
installers, runner/archiver, package manifest and English/Korean public install
guides are also unchanged. Earlier artifacts remain intact; no public release,
registry publication, new CI run or commit is created.
