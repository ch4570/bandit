# Packaging checkpoint

The initial packaging checks both completed with exit 0:

- `npm pack --pack-destination /TEMP/bandit-round6-9Y1jS3/pack-check --json`:
  43 entries, 2677333 compressed bytes.
- `/Users/DEVELOPER/.local/bin/python3.11 scripts/build_bundle.py --output-dir /TEMP/bandit-round6-9Y1jS3/pack-check`:
  959 entries, 10862848 bytes,
  SHA-256 `a8c222d1d6038605dea8e80e5a4883938d2bc5a97d576503ed7bc2cd32257e5b`.

That scratch ZIP predates this packaging receipt and the final documentation
updates. It is retained as an intermediate check, not mislabeled as the final
source snapshot. The full Node suite also passed its extracted-package CLI
test; these local checks do not establish that unpublished source is present
in the public 0.4.0 GitHub release.

Final artifacts use the previously unused `dist/overnight-round6/` directory:

```sh
npm pack --pack-destination dist/overnight-round6 --json
/Users/DEVELOPER/.local/bin/python3.11 scripts/build_bundle.py --output-dir dist/overnight-round6
```

The generated ZIP checksum sidecar and `SHA256SUMS.txt` identify that exact final
archive without inserting its own hash into its source payload. Earlier
same-version builds remain untouched. No registry publication, GitHub release,
or remote installation is performed.

