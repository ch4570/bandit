# Working on BANDIT

The product is `skills/bandit/`. Keep its entrypoint short and route conditional
guidance to references. Installer, packaging, examples, and evaluations support
that skill; they are not a product-management runtime.

End users install with the versioned GitHub release tarball through `npx --yes`
from their project. Copy the current command from INSTALL.md. Do not present a
mutable `releases/latest` URL as an update path: npm can reuse its old cached
package even with `--prefer-online`.
Keep that path noninteractive, dependency-free, and independent of Python.
Do not add package lifecycle scripts that modify the user's project on download.
Node.js 22+ is the primary development tool; Python 3.11+ supports the optional
legacy installer and ZIP tooling. Before shipping, run:

```sh
npm run validate
npm test
npm pack
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build_bundle.py
```

For behavioral changes, run a fresh realistic task with the changed skill and
only its raw fixtures. Keep expected results and author diagnoses out of that
agent's context. Preserve outputs and disclose failures before changing a rubric.
Do not present structural validation or a worked example as a quality benchmark.

Keep English and Korean onboarding consistent. Link comparative claims to a
pinned upstream source or recorded run. Describe what was observed; avoid
unmeasured claims of superiority, token savings, or business validation.

The BANDIT mascot is an original raccoon outlaw with a pencil and a planning map.
Brand illustrations may be expressive; product requirements remain clear and
practical. Preserve the historical PM Craft 0.1.0 evaluation outputs and hashes.
They are historical evidence, not fresh BANDIT measurements. npm registry
publication is deferred; GitHub npx/tarball installation must work before release.

Do not copy private customer documents or credentials into public examples.
Use synthetic fixtures and label them. Preserve contributors' unrelated work.
