# Round-10 packaging identity

After the full verification commands, main ran a separate `npm pack` under
Node 22.23.2/npm 11.19.0 with closed stdin and `npm_config_call` removed.
[npm-pack.json](npm-pack.json) retains the exact argv, UTC times, status and
stdout/stderr. It exited 0 and produced 43 files in the local artifact
`dist/overnight-round10/ch4570-bandit-0.4.0.tgz` (2,677,668 bytes), SHA-256
`6d50b00dad167714bbcf145e95c507246b19f0713287d55a2dff66acadc031f4`.

Its compressed bytes differ from the retained round-9 candidate
(`a2fb5d29889010c2c0c8d0da3783be052667d6c295ffac72039ac99045655252`,
2,677,442 bytes). Read-only comparison finds identical decompressed tar bytes:
2,885,120 bytes, SHA-256
`11fdead0a84ad074420be6ca25b179b026cb4852c9e7af2e2e24be2ca159c56a`.
All 43 file payloads and tar member metadata are identical. This is a compressed
representation difference, not evidence of changed skill or installer content;
the exact compressor mechanism was not isolated. No repack was used to force
the earlier compressed hash, and neither archive was overwritten.

Final source-ZIP construction and exact current-source/inventory verification
are recorded separately in ignored `dist/overnight-round10/CHECKPOINT.json`
after source documentation is complete. The ZIP includes the development
fixtures and evidence; the npm archive still contains the five-skill product
and installer support, not the evaluation suite. These local artifacts are
not a new public release, registry publication or network-install execution.
