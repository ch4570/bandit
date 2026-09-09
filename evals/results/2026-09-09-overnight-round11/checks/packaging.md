# Round-11 local candidate

The separate [npm pack receipt](npm-pack.json) records Node 22.23.2/npm 11.19.0,
closed stdin, the exact command, UTC times and exit 0. The new local candidate
is `dist/overnight-round11/ch4570-bandit-0.4.0.tgz`: 43 files, 2,677,718 bytes,
SHA-256 `7f8592028d1b2f350dd304526e57a550c4b133a0f93d5b971d2a133d67bb5f84`.

Read-only comparison finds the same 43 paths as round 10, with only
`lib/installer.mjs` differing. Every packaged file matches current source;
all 34 skill files are unchanged. The new usage/example pages belong to the
source repository/ZIP, not the installed skill payload. This pack command is
not a fresh npx or GitHub network installation.

Final source-ZIP construction and exact-source, inventory, checksum and link
verification are recorded in ignored `dist/overnight-round11/CHECKPOINT.json`
after documentation is complete. Earlier candidate archives are retained.
The public install command remains pinned to release 0.4.0; this candidate
has not been published.
