import contextlib
import io
import json
from pathlib import Path
from unittest.mock import patch

from _support import DistributionTest
import install


class InstallTests(DistributionTest):
    def test_dry_run_creates_nothing(self):
        result = install.install_into(self.source, self.destination, dry_run=True)
        self.assertEqual(result["status"], "plan")
        self.assertFalse(self.destination.parent.exists())

    def test_install_copies_all_skill_files_and_repeated_install_is_noop(self):
        self.assertEqual(install.install_into(self.source, self.destination)["status"], "installed")
        for relative, expected in install.tree_files(self.skill).items():
            self.assertEqual((self.destination / relative).read_bytes(), expected)
        marker = self.destination / install.MARKER
        before = marker.stat().st_mtime_ns
        self.assertEqual(install.install_into(self.source, self.destination)["status"], "unchanged")
        self.assertEqual(marker.stat().st_mtime_ns, before)

    def test_safe_update_adds_removes_and_preserves_unrelated_files(self):
        install.install_into(self.source, self.destination)
        (self.destination / "my-notes.txt").write_text("keep me", encoding="utf-8")
        self.write("references/rules.md", "updated\n")
        self.write("references/new.md", "new\n")
        (self.skill / "assets/template.md").unlink()
        (self.source / "VERSION").write_text("0.3.0\n", encoding="utf-8")
        result = install.install_into(self.source, self.destination)
        self.assertEqual(result["status"], "updated")
        self.assertEqual((self.destination / "references/rules.md").read_text(), "updated\n")
        self.assertFalse((self.destination / "assets/template.md").exists())
        self.assertEqual((self.destination / "my-notes.txt").read_text(), "keep me")

    def test_modified_managed_file_aborts_all_changes(self):
        install.install_into(self.source, self.destination)
        self.write("SKILL.md", "upstream change\n")
        (self.destination / "references/rules.md").write_text("local edit\n")
        before = install.tree_files(self.destination)
        with self.assertRaisesRegex(install.InstallError, "local modification"):
            install.install_into(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination), before)

    def test_unmanaged_conflict_is_not_overwritten(self):
        self.destination.mkdir(parents=True)
        (self.destination / "SKILL.md").write_text("my skill")
        with self.assertRaisesRegex(install.InstallError, "unmanaged conflict"):
            install.install_into(self.source, self.destination)
        self.assertEqual((self.destination / "SKILL.md").read_text(), "my skill")
        self.assertFalse((self.destination / install.MARKER).exists())

    def test_identical_unmanaged_files_can_be_adopted(self):
        self.destination.mkdir(parents=True)
        (self.destination / "SKILL.md").write_bytes((self.skill / "SKILL.md").read_bytes())
        self.assertEqual(install.install_into(self.source, self.destination)["status"], "installed")

    def test_locally_deleted_file_is_not_silently_restored(self):
        install.install_into(self.source, self.destination)
        (self.destination / "references/rules.md").unlink()
        with self.assertRaisesRegex(install.InstallError, "deleted locally"):
            install.install_into(self.source, self.destination)

    def test_modified_removed_upstream_file_is_preserved(self):
        install.install_into(self.source, self.destination)
        self.write("assets/template.md", "upstream")
        (self.destination / "assets/template.md").write_text("mine")
        (self.skill / "assets/template.md").unlink()
        with self.assertRaises(install.InstallError):
            install.install_into(self.source, self.destination)
        self.assertEqual((self.destination / "assets/template.md").read_text(), "mine")

    def test_marker_traversal_rejected_before_writes(self):
        install.install_into(self.source, self.destination)
        marker = self.destination / install.MARKER
        value = json.loads(marker.read_text())
        value["files"]["../../victim.txt"] = "0" * 64
        marker.write_text(json.dumps(value))
        with self.assertRaisesRegex(install.InstallError, "Unsafe relative"):
            install.install_into(self.source, self.destination)

    def test_symlinked_parent_cannot_escape_destination(self):
        outside = self.area / "outside"
        outside.mkdir()
        self.destination.parent.mkdir(parents=True)
        self.link(self.destination, outside, directory=True)
        with self.assertRaisesRegex(install.InstallError, "Symlink or junction"):
            install.install_into(self.source, self.destination)
        self.assertEqual(list(outside.iterdir()), [])

    def test_source_symlink_is_rejected(self):
        secret = self.area / "private.txt"
        secret.write_text("secret")
        self.link(self.skill / "assets/linked.txt", secret)
        with self.assertRaisesRegex(install.InstallError, "Symlink or junction"):
            install.install_into(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_dangling_marker_symlink_is_rejected(self):
        self.destination.mkdir(parents=True)
        self.link(self.destination / install.MARKER, self.area / "absent.json")
        with self.assertRaisesRegex(install.InstallError, "Symlink or junction"):
            install.install_into(self.source, self.destination)

    def test_file_in_parent_position_is_a_conflict(self):
        self.destination.mkdir(parents=True)
        (self.destination / "references").write_text("not a directory")
        with self.assertRaisesRegex(install.InstallError, "Parent path"):
            install.install_into(self.source, self.destination)
        self.assertFalse((self.destination / "SKILL.md").exists())

    def test_cli_repo_and_destination_are_mutually_exclusive(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as failure:
            install.main(["--repo", str(self.area), "--dest", str(self.destination)])
        self.assertEqual(failure.exception.code, 2)

    def test_cli_repo_layout(self):
        project = self.area / "project"
        project.mkdir()
        output = io.StringIO()
        with patch.object(install, "ROOT", self.source), contextlib.redirect_stdout(output):
            self.assertEqual(install.main(["--repo", str(project)]), 0)
        self.assertTrue((project / ".agents/skills/bandit/SKILL.md").is_file())
        self.assertFalse((project / "AGENTS.md").exists())

    def test_io_failure_restores_previously_updated_content(self):
        install.install_into(self.source, self.destination)
        self.write("SKILL.md", "new spec")
        self.write("references/rules.md", "new rules")
        before = install.tree_files(self.destination)
        original = install.atomic_write
        failed = False

        def fail_once(path, data):
            nonlocal failed
            if path.name == "rules.md" and not failed:
                failed = True
                raise OSError("simulated disk failure")
            return original(path, data)

        with patch.object(install, "atomic_write", side_effect=fail_once), self.assertRaisesRegex(OSError, "disk failure"):
            install.install_into(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination), before)

    def test_concurrent_edit_is_kept_and_earlier_writes_are_rolled_back(self):
        install.install_into(self.source, self.destination)
        old_spec = (self.destination / "SKILL.md").read_bytes()
        self.write("SKILL.md", "new spec")
        self.write("references/rules.md", "new rules")
        original = install.atomic_write
        edited = False

        def edit_next_file(path, data):
            nonlocal edited
            result = original(path, data)
            if path.name == "SKILL.md" and not edited:
                edited = True
                (self.destination / "references/rules.md").write_text("concurrent user edit")
            return result

        with patch.object(install, "atomic_write", side_effect=edit_next_file), self.assertRaisesRegex(install.InstallError, "changed during"):
            install.install_into(self.source, self.destination)
        self.assertEqual((self.destination / "SKILL.md").read_bytes(), old_spec)
        self.assertEqual((self.destination / "references/rules.md").read_text(), "concurrent user edit")

    def test_source_destination_overlap_is_rejected(self):
        with self.assertRaisesRegex(install.InstallError, "overlap"):
            install.install_into(self.source, self.skill)

    def test_source_case_alias_cannot_be_used_as_destination(self):
        alias = self.source / "SKILLS/BANDIT"
        with self.assertRaisesRegex(install.InstallError, "overlap"):
            install.install_into(self.source, alias)
        self.assertFalse((self.skill / install.MARKER).exists())

    def test_case_only_rename_is_a_preflight_conflict_without_data_loss(self):
        self.write("references/Guide.md", "same contents")
        install.install_into(self.source, self.destination)
        (self.skill / "references/Guide.md").rename(self.skill / "references/guide.md")
        before = install.tree_files(self.destination)
        with self.assertRaisesRegex(install.InstallError, "Case-only managed path rename"):
            install.install_into(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination), before)
        self.assertEqual((self.destination / "references/Guide.md").read_text(), "same contents")
