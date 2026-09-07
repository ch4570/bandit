# Working on PM Craft

The product is `skills/pm-craft/`. Keep its entrypoint short and route conditional
guidance to references. Installer, packaging, examples, and evaluations support
that skill; they are not a product-management runtime.

Use Python 3.11+ for repository tools. Before shipping, run:

```sh
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

Do not copy private customer documents or credentials into public examples.
Use synthetic fixtures and label them. Preserve contributors' unrelated work.
