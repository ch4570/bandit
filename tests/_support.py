from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


class DistributionTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="bandit tests ")
        self.addCleanup(temporary.cleanup)
        self.area = Path(temporary.name).resolve()
        self.source = self.area / "source"
        self.skill = self.source / "skills/bandit"
        self.skill.mkdir(parents=True)
        (self.source / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        (self.source / "README.md").write_text("# BANDIT\n", encoding="utf-8")
        (self.source / "LICENSE").write_text("MIT fixture\n", encoding="utf-8")
        (self.source / "install.py").write_bytes((ROOT / "install.py").read_bytes())
        self.write("SKILL.md", '---\nname: bandit\ndescription: "Product planning skill"\n---\n# BANDIT\nRead [rules](references/rules.md).\n')
        self.write("references/rules.md", "# Rules\nUse the actual product context.\n")
        self.write("agents/openai.yaml", 'interface:\n  display_name: "BANDIT"\n  short_description: "Plan useful products"\n  default_prompt: "Use $bandit to scope my product."\n')
        self.write("assets/template.md", "# Plan\n")
        self.destination = self.area / "project with spaces" / ".agents/skills/bandit"

    def write(self, name, text):
        path = self.skill / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def link(self, source, target, directory=False):
        try:
            source.symlink_to(target, target_is_directory=directory)
        except OSError:
            self.skipTest("This Windows environment does not permit test symlinks")
