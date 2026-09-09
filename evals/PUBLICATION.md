# Public-copy path normalization

This PR publishes the overnight development work without personal checkout,
home or scratch roots. It does not rerun or regrade the recorded tasks.
The original working tree and immutable local round-14 source ZIP remain
unchanged. All previously committed PM Craft evidence stays byte-identical.

The [publication manifest](publication-paths.json) records the original and
published SHA-256 for each of 164 normalized files, the substitution classes
and their occurrence counts. Only literal path prefixes change:

| Original path class | Public placeholder |
| --- | --- |
| Personal BANDIT checkout root | `/WORKSPACE/bandit` |
| Personal home root | `/Users/DEVELOPER` |
| Local scratch root | `/TEMP` |
| Darwin temporary/cache root | `/TEMP/SYSTEM` |

The private prefix values are deliberately not included. Product instructions,
installer implementations, tests, raw product fixtures, rubrics and native
planning output artifacts receive no path substitutions. Normalized files are
engineering/evaluation records and their one-off helpers, plus the validation
record. PM task archive files were already subject to their documented
run-root normalization; this publication step is a separate mapping.

Original receipt hashes, UTC times, command outcomes, failures, partial grades
and explanatory claims are not rewritten to imply a new execution. A hash in an
older receipt continues to describe its retained original bytes; it may not
match a path-normalized public copy. Use this manifest's `published_sha256`
for that copy. The manifest also identifies the unchanged original round-14
ZIP and checkpoint by digest. Its original ZIP does not contain these later
publication notes or normalized copies.

The one-off engineering helpers document commands actually used on the original
machine. Placeholder paths are not directly executable and must be adapted to
an appropriate local environment; do not treat these retained helpers as a
portable test framework. The supported repository checks are documented in
[CONTRIBUTING](../CONTRIBUTING.md).

The publication transformation can be reviewed separately from the source
changes. It is not an improvement in planning quality, new installer behavior,
an independently authenticated original, or a general secret-safety guarantee.
The PR lists checks run on this public copy separately from the original
overnight execution record.
