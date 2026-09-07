import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

from _support import DistributionTest
from scripts import build_bundle
import install


class BundleTests(DistributionTest):
    def test_npm_source_and_tests_are_included_in_offline_bundle(self):
        payload = {
            "package.json": '{"name":"@ch4570/bandit","version":"0.2.0"}\n',
            "bin/bandit.mjs": "#!/usr/bin/env node\nimport '../lib/install.mjs';\n",
            "lib/install.mjs": "export const fixture = true;\n",
            "scripts/validate-node.mjs": "export const fixture = true;\n",
            "tests-node/install.test.mjs": "// Distribution test fixture.\n",
        }
        for relative, content in payload.items():
            target = self.source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        result = build_bundle.build_bundle(self.source, self.area / "dist")
        with zipfile.ZipFile(result["artifact"]) as archive:
            for relative in payload:
                self.assertEqual(archive.read("bandit-0.2.0/" + relative), (self.source / relative).read_bytes())
            self.assertEqual(archive.getinfo("bandit-0.2.0/bin/bandit.mjs").external_attr >> 16, 0o100755)

    def test_reproducible_archive_and_inventory(self):
        one = build_bundle.build_bundle(self.source, self.area / "first")
        two = build_bundle.build_bundle(self.source, self.area / "second")
        self.assertEqual(Path(one["artifact"]).read_bytes(), Path(two["artifact"]).read_bytes())
        with zipfile.ZipFile(one["artifact"]) as archive:
            prefix = "bandit-0.2.0/"
            inventory = json.loads(archive.read(prefix + build_bundle.INVENTORY))
            self.assertEqual(set(archive.namelist()), {prefix + name for name in inventory["files"]} | {prefix + build_bundle.INVENTORY})
            for name, expected in inventory["files"].items():
                self.assertEqual(hashlib.sha256(archive.read(prefix + name)).hexdigest(), expected)
            self.assertTrue(all(info.date_time == (1980, 1, 1, 0, 0, 0) for info in archive.infolist()))

    def test_extracted_bundle_installs_without_original_checkout(self):
        result = build_bundle.build_bundle(self.source, self.area / "dist")
        extracted = self.area / "extracted"
        with zipfile.ZipFile(result["artifact"]) as archive:
            archive.extractall(extracted)
        self.source.rename(self.area / "original hidden")
        entrypoint = extracted / "bandit-0.2.0/install.py"
        process = subprocess.run([sys.executable, str(entrypoint), "--dest", str(self.destination)], cwd=self.area, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertTrue((self.destination / "references/rules.md").is_file())
        self.assertTrue((self.destination / "agents/openai.yaml").is_file())
        self.assertTrue((self.destination / "assets/template.md").is_file())

    def test_output_preserves_unrelated_files_and_identical_build_is_noop(self):
        output = self.area / "custom output"
        output.mkdir()
        (output / "keep.txt").write_text("local")
        result = build_bundle.build_bundle(self.source, output)
        before = Path(result["artifact"]).stat().st_mtime_ns
        build_bundle.build_bundle(self.source, output)
        self.assertEqual(Path(result["artifact"]).stat().st_mtime_ns, before)
        self.assertEqual((output / "keep.txt").read_text(), "local")

    def test_different_artifact_at_same_version_is_not_overwritten(self):
        output = self.area / "dist"
        result = build_bundle.build_bundle(self.source, output)
        before = Path(result["artifact"]).read_bytes()
        self.write("references/rules.md", "changed")
        with self.assertRaisesRegex(install.InstallError, "different checksum"):
            build_bundle.build_bundle(self.source, output)
        self.assertEqual(Path(result["artifact"]).read_bytes(), before)

    def test_build_rejects_output_inside_input(self):
        with self.assertRaisesRegex(install.InstallError, "bundled input"):
            build_bundle.build_bundle(self.source, self.skill / "generated")
        self.assertFalse((self.skill / "generated").exists())

    def test_case_alias_cannot_hide_output_inside_bundled_docs(self):
        docs = self.source / "docs"
        docs.mkdir()
        with self.assertRaisesRegex(install.InstallError, "bundled input"):
            build_bundle.build_bundle(self.source, self.source / "DOCS/generated")
        self.assertEqual(list(docs.iterdir()), [])

    def test_symlinked_artifact_is_rejected(self):
        output = self.area / "dist"
        output.mkdir()
        victim = self.area / "victim.txt"
        victim.write_text("keep")
        self.link(output / "bandit-0.2.0.zip", victim)
        with self.assertRaisesRegex(install.InstallError, "Symlink or junction"):
            build_bundle.build_bundle(self.source, output)
        self.assertEqual(victim.read_text(), "keep")

    def test_dist_and_git_are_not_archived(self):
        (self.source / "dist").mkdir()
        (self.source / "dist/private.txt").write_text("not an input")
        (self.source / ".git").mkdir()
        (self.source / ".git/config").write_text("not an input")
        result = build_bundle.build_bundle(self.source, self.area / "out")
        with zipfile.ZipFile(result["artifact"]) as archive:
            self.assertFalse(any("/dist/" in name or "/.git/" in name for name in archive.namelist()))

    def test_invalid_skill_cannot_be_packaged(self):
        (self.skill / "agents/openai.yaml").unlink()
        with self.assertRaisesRegex(install.InstallError, "validation failed"):
            build_bundle.build_bundle(self.source, self.area / "out")
        self.assertFalse((self.area / "out").exists())
