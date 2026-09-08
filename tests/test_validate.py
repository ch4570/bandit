from _support import DistributionTest
from scripts import validate
import install
import shutil


class ValidateTests(DistributionTest):
    def test_valid_distribution(self):
        result = validate.validate(self.source)
        self.assertTrue(result["ok"], result["errors"])
        self.assertIn("no claim", result["checks"])
        self.assertEqual([item["name"] for item in result["skills"]], list(install.SKILL_NAMES))

    def test_missing_reference_is_a_failure(self):
        self.write("SKILL.md", '---\nname: bandit\ndescription: Product planning\n---\nRead `references/missing.md`.\n')
        result = validate.validate(self.source)
        self.assertFalse(result["ok"])
        self.assertTrue(any("missing.md" in error for error in result["errors"]))

    def test_wrong_skill_name_fails(self):
        self.write("SKILL.md", '---\nname: wrong\ndescription: Product planning\n---\n')
        self.assertFalse(validate.validate(self.source)["ok"])

    def test_optional_npm_metadata_cannot_disagree_with_source_version(self):
        (self.source / "package.json").write_text('{"name":"@ch4570/bandit","version":"0.1.0"}', encoding="utf-8")
        result = validate.validate(self.source)
        self.assertFalse(result["ok"])
        self.assertTrue(any("package.json" in error for error in result["errors"]))

    def test_missing_ui_metadata_fails(self):
        (self.skill / "agents/openai.yaml").unlink()
        self.assertFalse(validate.validate(self.source)["ok"])

    def test_prompt_must_reference_actual_skill(self):
        self.write("agents/openai.yaml", 'interface:\n  display_name: BANDIT\n  short_description: Product planning\n  default_prompt: Use $wrong\n')
        result = validate.validate(self.source)
        self.assertTrue(any("$bandit" in error for error in result["errors"]))

    def test_yaml_duplicate_key_and_unterminated_frontmatter_fail(self):
        for text in ('---\nname: bandit\nname: other\ndescription: x\n---\n', '---\nname: bandit\n'):
            with self.subTest(text=text):
                self.write("SKILL.md", text)
                self.assertFalse(validate.validate(self.source)["ok"])

    def test_multiline_description_and_nested_ui_are_supported(self):
        self.write("SKILL.md", '---\nname: bandit\ndescription: >-\n  Research product plans\n  with useful evidence.\n---\n')
        self.assertTrue(validate.validate(self.source)["ok"])

    def test_external_links_and_example_code_are_not_files(self):
        self.write("references/rules.md", '# Rules\n[web](https://example.com/no-file)\n```markdown\n[example](missing.md)\n```\n')
        self.assertTrue(validate.validate(self.source)["ok"])

    def test_local_link_cannot_escape_installed_skill(self):
        self.write("references/rules.md", '[outside](../../../README.md)\n')
        result = validate.validate(self.source)
        self.assertTrue(any("leaves its package" in error for error in result["errors"]))

    def test_missing_specialist_fails_even_with_a_valid_core(self):
        shutil.rmtree(self.source / "skills/bandit-update")
        result = validate.validate(self.source)
        self.assertFalse(result["ok"])
        self.assertTrue(any("bandit-update" in error for error in result["errors"]))

    def test_specialist_prompt_requires_its_exact_invocation(self):
        self.write_skill("bandit-research", "agents/openai.yaml", 'interface:\n  display_name: "BANDIT Research"\n  short_description: "Plan useful products"\n  default_prompt: "Use $bandit-research-extra"\n')
        result = validate.validate(self.source)
        self.assertFalse(result["ok"])
        self.assertTrue(any("default_prompt must mention $bandit-research" in error for error in result["errors"]))

    def test_specialist_reference_cannot_depend_on_existing_sibling_files(self):
        self.write_skill("bandit-review", "references/rules.md", "[Core rules](../../bandit/references/rules.md)\n")
        result = validate.validate(self.source)
        self.assertFalse(result["ok"])
        self.assertTrue(any("bandit-review" in error and "leaves its package" in error for error in result["errors"]))
