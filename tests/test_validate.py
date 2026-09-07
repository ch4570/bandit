from _support import DistributionTest
from scripts import validate


class ValidateTests(DistributionTest):
    def test_valid_distribution(self):
        result = validate.validate(self.source)
        self.assertTrue(result["ok"], result["errors"])
        self.assertIn("no claim", result["checks"])

    def test_missing_reference_is_a_failure(self):
        self.write("SKILL.md", '---\nname: pm-craft\ndescription: Product planning\n---\nRead `references/missing.md`.\n')
        result = validate.validate(self.source)
        self.assertFalse(result["ok"])
        self.assertTrue(any("missing.md" in error for error in result["errors"]))

    def test_wrong_skill_name_fails(self):
        self.write("SKILL.md", '---\nname: wrong\ndescription: Product planning\n---\n')
        self.assertFalse(validate.validate(self.source)["ok"])

    def test_missing_ui_metadata_fails(self):
        (self.skill / "agents/openai.yaml").unlink()
        self.assertFalse(validate.validate(self.source)["ok"])

    def test_prompt_must_reference_actual_skill(self):
        self.write("agents/openai.yaml", 'interface:\n  display_name: PM Craft\n  short_description: Product planning\n  default_prompt: Use $wrong\n')
        result = validate.validate(self.source)
        self.assertTrue(any("$pm-craft" in error for error in result["errors"]))

    def test_yaml_duplicate_key_and_unterminated_frontmatter_fail(self):
        for text in ('---\nname: pm-craft\nname: other\ndescription: x\n---\n', '---\nname: pm-craft\n'):
            with self.subTest(text=text):
                self.write("SKILL.md", text)
                self.assertFalse(validate.validate(self.source)["ok"])

    def test_multiline_description_and_nested_ui_are_supported(self):
        self.write("SKILL.md", '---\nname: pm-craft\ndescription: >-\n  Research product plans\n  with useful evidence.\n---\n')
        self.assertTrue(validate.validate(self.source)["ok"])

    def test_external_links_and_example_code_are_not_files(self):
        self.write("references/rules.md", '# Rules\n[web](https://example.com/no-file)\n```markdown\n[example](missing.md)\n```\n')
        self.assertTrue(validate.validate(self.source)["ok"])

    def test_local_link_cannot_escape_installed_skill(self):
        self.write("references/rules.md", '[outside](../../../README.md)\n')
        result = validate.validate(self.source)
        self.assertTrue(any("leaves its package" in error for error in result["errors"]))
