# Working on BANDIT

The product is the five skills under `skills/`: general `bandit` and the
`bandit-research`, `bandit-scope`, `bandit-specify`, and `bandit-review`
specialists. Each specialist must be independently invocable
with its own metadata and complete referenced resources. Keep entrypoints short.

Maintain reference sources under `skills/bandit/`, then run
`node scripts/sync-skills.mjs` to synchronize the resources needed by each
specialist. Do not hand-edit the generated reference copies. Installer,
packaging, examples, and evaluations support these skills; they are not a
product-management runtime.

End users install with the versioned GitHub release tarball through `npx --yes`
from their project. One command installs all five sibling skill folders. Copy
the current command from INSTALL.md. Do not present a
mutable `releases/latest` URL as an update path: npm can reuse its old cached
package even with `--prefer-online`.
Keep that path noninteractive, dependency-free, and independent of Python.
Do not add package lifecycle scripts that modify the user's project on download.
Node.js 22+ is the primary development tool; Python 3.11+ supports the optional
legacy installer and ZIP tooling. Before shipping, run:

```sh
node scripts/sync-skills.mjs --check
npm run validate
npm test
npm pack
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build_bundle.py
```

Specification work includes creating a new spec and rewriting an existing one
for a changed direction. Match the extent of content and structural rewriting
to the request, while preserving the original meaning of historical evidence.
Do not split specification changes into a separate user-facing command.

For behavioral changes, run a fresh realistic task with the changed skill and
only its raw fixtures. Keep expected results and author diagnoses out of that
agent's context. Preserve outputs and disclose failures before changing a rubric.
Do not present structural validation or a worked example as a quality benchmark.

Keep English and Korean onboarding consistent. Specialist examples use their
actual `$bandit-*` commands; reserve `$bandit` examples for general or combined
requests. Upgrade instructions must use the current versioned command and
refresh host discovery. Migration from 0.3 retires the old decide and update skills: remove
only unchanged managed files, preserve unrelated notes, and stop the entire
upgrade on conflicting customizations. Link comparative claims to a
pinned upstream source or recorded run. Describe what was observed; avoid
unmeasured claims of superiority, token savings, or business validation.

The BANDIT mascot is an original raccoon outlaw with a pencil and a planning map.
Brand illustrations may be expressive; product requirements remain clear and
practical. Preserve the historical PM Craft 0.1.0 evaluation outputs and hashes.
They are historical evidence, not fresh BANDIT measurements. npm registry
publication is deferred; GitHub npx/tarball installation must work before release.

Do not copy private customer documents or credentials into public examples.
Use synthetic fixtures and label them. Preserve contributors' unrelated work.
