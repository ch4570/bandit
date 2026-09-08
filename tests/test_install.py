import contextlib
import io
import json
import shutil
from pathlib import Path
from unittest.mock import patch

from _support import DistributionTest
import install


class InstallTests(DistributionTest):
    def old_install(self, name, files=None):
        """A synthetic 0.3 installation, independent of the new active skill list."""
        target = self.destination.parent / name
        payload = files or {"SKILL.md": f"# {name}\n".encode(), "references/rules.md": b"old rules\n"}
        for relative, content in payload.items():
            filename = target / relative
            filename.parent.mkdir(parents=True, exist_ok=True)
            filename.write_bytes(content)
        marker = {"format": 1, "name": name, "version": "0.3.0", "files": {relative: install.digest(content) for relative, content in payload.items()}}
        (target / install.MARKER).write_text(json.dumps(marker))
        return target

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
        self.assertEqual(len(json.loads(output.getvalue())["skills"]), 5)
        for skill_name in install.SKILL_NAMES:
            self.assertTrue((project / ".agents/skills" / skill_name / "SKILL.md").is_file())
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

    def test_bundle_installs_every_skill_with_its_own_ownership_and_is_idempotent(self):
        report = install.install_bundle(self.source, self.destination)
        self.assertEqual(report["status"], "installed")
        self.assertEqual(report["destination"], str(self.destination))
        self.assertEqual(report["commands"], ["$" + name for name in install.SKILL_NAMES])
        for name in install.SKILL_NAMES:
            target = self.destination.parent / name
            for relative, data in install.tree_files(self.source / "skills" / name).items():
                self.assertEqual((target / relative).read_bytes(), data)
            self.assertEqual(json.loads((target / install.MARKER).read_text())["name"], name)
        before = install.tree_files(self.destination.parent)
        self.assertEqual(install.install_bundle(self.source, self.destination)["status"], "unchanged")
        self.assertEqual(install.tree_files(self.destination.parent), before)

    def test_bundle_plan_has_all_five_destinations_without_creating_directories(self):
        report = install.install_bundle(self.source, self.destination, dry_run=True)
        self.assertEqual(report["status"], "plan")
        self.assertEqual(len(report["skills"]), 5)
        self.assertTrue(any(item["path"] == "bandit-review/SKILL.md" for item in report["changes"]))
        self.assertFalse(self.destination.parent.exists())

    def test_later_specialist_conflict_prevents_every_update(self):
        install.install_bundle(self.source, self.destination)
        self.write("SKILL.md", "updated core")
        (self.destination.parent / "bandit-review/SKILL.md").write_text("local specialist edit")
        before = install.tree_files(self.destination.parent)
        with patch.object(install, "atomic_write") as writer, self.assertRaisesRegex(install.InstallError, "local modification"):
            install.install_bundle(self.source, self.destination)
        writer.assert_not_called()
        self.assertEqual(install.tree_files(self.destination.parent), before)

    def test_old_single_skill_install_upgrades_and_adds_specialists(self):
        install.install_into(self.source, self.destination)
        (self.destination / "notes.txt").write_text("my existing notes")
        self.write("SKILL.md", "new orchestrator")
        (self.source / "VERSION").write_text("0.3.0\n")
        report = install.install_bundle(self.source, self.destination)
        self.assertEqual(report["status"], "updated")
        self.assertEqual((self.destination / "notes.txt").read_text(), "my existing notes")
        for name in install.SKILL_NAMES:
            target = self.destination.parent / name
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertEqual(json.loads((target / install.MARKER).read_text())["version"], "0.3.0")

    def test_missing_later_specialist_source_prevents_core_update(self):
        install.install_into(self.source, self.destination)
        self.write("SKILL.md", "updated core")
        shutil.rmtree(self.source / "skills/bandit-review")
        before = install.tree_files(self.destination.parent)
        with self.assertRaisesRegex(install.InstallError, "Missing directory"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination.parent), before)

    def test_later_specialist_io_failure_rolls_back_prior_skills_and_markers(self):
        install.install_bundle(self.source, self.destination)
        for name in install.SKILL_NAMES:
            self.write_skill(name, "references/rules.md", "updated rules")
        (self.source / "VERSION").write_text("0.3.0\n")
        before = install.tree_files(self.destination.parent)
        original = install.atomic_write
        failed = False

        def fail_later(path, data):
            nonlocal failed
            if "bandit-review" in path.parts and path.name == "rules.md" and not failed:
                failed = True
                raise OSError("simulated later-skill I/O failure")
            return original(path, data)

        with patch.object(install, "atomic_write", side_effect=fail_later), self.assertRaisesRegex(OSError, "later-skill"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination.parent), before)

    def test_concurrent_later_skill_edit_survives_cross_skill_rollback(self):
        install.install_bundle(self.source, self.destination)
        before_core = install.tree_files(self.destination)
        self.write("SKILL.md", "updated core")
        self.write_skill("bandit-review", "references/rules.md", "updated specialist")
        later = self.destination.parent / "bandit-review/references/rules.md"
        original = install.atomic_write
        edited = False

        def edit_later(path, data):
            nonlocal edited
            result = original(path, data)
            if path == self.destination / "SKILL.md" and not edited:
                edited = True
                later.write_text("concurrent specialist edit")
            return result

        with patch.object(install, "atomic_write", side_effect=edit_later), self.assertRaisesRegex(install.InstallError, "changed during"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination), before_core)
        self.assertEqual(later.read_text(), "concurrent specialist edit")

    def test_custom_core_destination_keeps_specialists_as_fixed_siblings(self):
        destination = self.area / "custom skills/core-planner"
        report = install.install_bundle(self.source, destination)
        self.assertEqual(report["destination"], str(destination))
        self.assertTrue((destination / "SKILL.md").is_file())
        for name in install.SKILL_NAMES[1:]:
            self.assertTrue((destination.parent / name / "SKILL.md").is_file())

    def test_core_destination_cannot_alias_a_specialist(self):
        destination = self.destination.parent / "BANDIT-REVIEW"
        with self.assertRaisesRegex(install.InstallError, "collides"):
            install.install_bundle(self.source, destination)
        self.assertFalse(destination.parent.exists())

    def test_core_destination_cannot_overlap_another_specialist_source(self):
        with self.assertRaisesRegex(install.InstallError, "overlap"):
            install.install_bundle(self.source, self.source / "skills/bandit-review/custom-core")

    def test_existing_later_skill_lock_prevents_updates_and_keeps_that_lock(self):
        install.install_bundle(self.source, self.destination)
        self.write("SKILL.md", "updated core")
        lock = self.destination.parent / ".bandit-review.bandit.lock"
        lock.write_text("other installer")
        before = install.tree_files(self.destination.parent)
        with self.assertRaisesRegex(install.InstallError, "Install lock exists"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination.parent), before)

    def test_managed_retired_skills_are_removed_while_five_active_skills_are_installed(self):
        for name in install.RETIRED_NAMES:
            self.old_install(name)
        report = install.install_bundle(self.source, self.destination)
        self.assertEqual(report["status"], "updated")
        self.assertEqual([item["name"] for item in report["skills"]], list(install.SKILL_NAMES))
        self.assertEqual(len(report["commands"]), 5)
        self.assertTrue(all(item["status"] == "retired" for item in report["retirements"]))
        self.assertEqual({item["from"]: item["to"] for item in report["migrations"]}, install.MIGRATIONS)
        for name in install.RETIRED_NAMES:
            self.assertFalse((self.destination.parent / name).exists())
            self.assertNotIn("$" + name, report["commands"])
            self.assertTrue(any(item["skill"] == name and item["action"] == "remove" for item in report["changes"]))

    def test_retirement_preserves_unmanaged_notes_and_removes_only_empty_owned_directories(self):
        target = self.old_install("bandit-update")
        (target / "my-notes.txt").write_text("keep my notes")
        (target / "my-empty-directory").mkdir()
        report = install.install_bundle(self.source, self.destination)
        self.assertEqual((target / "my-notes.txt").read_text(), "keep my notes")
        self.assertFalse((target / "SKILL.md").exists())
        self.assertFalse((target / install.MARKER).exists())
        self.assertFalse((target / "references").exists())
        self.assertTrue((target / "my-empty-directory").is_dir())
        self.assertEqual(next(item for item in report["retirements"] if item["name"] == "bandit-update")["status"], "retired")

    def test_modified_retired_file_stops_every_install_before_writes(self):
        install.install_into(self.source, self.destination)
        self.write("SKILL.md", "updated core")
        target = self.old_install("bandit-decide")
        (target / "references/rules.md").write_text("local retirement edit")
        before = install.tree_files(self.destination.parent)
        with patch.object(install, "atomic_write") as writer, self.assertRaisesRegex(install.InstallError, "local modification in retired"):
            install.install_bundle(self.source, self.destination)
        writer.assert_not_called()
        self.assertEqual(install.tree_files(self.destination.parent), before)

    def test_unmanaged_retired_entrypoint_is_never_silently_left_or_removed(self):
        target = self.destination.parent / "bandit-update"
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("my handwritten update skill")
        before = install.tree_files(self.destination.parent)
        with self.assertRaisesRegex(install.InstallError, "unmanaged retired SKILL.md"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination.parent), before)
        self.assertFalse(self.destination.exists())

    def test_unmanaged_retired_entrypoint_conflicts_even_when_other_files_are_managed(self):
        target = self.old_install("bandit-decide", {"references/rules.md": b"managed rule"})
        (target / "SKILL.md").write_text("unmanaged entrypoint")
        with self.assertRaisesRegex(install.InstallError, "unmanaged retired SKILL.md"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual((target / "SKILL.md").read_text(), "unmanaged entrypoint")
        self.assertFalse(self.destination.exists())

    def test_missing_retired_owned_files_do_not_block_safe_retirement(self):
        target = self.old_install("bandit-update")
        (target / "SKILL.md").unlink()
        report = install.install_bundle(self.source, self.destination)
        self.assertEqual(report["status"], "updated")
        self.assertFalse(target.exists())

    def test_already_deleted_retired_contents_allow_marker_and_empty_directory_cleanup(self):
        target = self.old_install("bandit-update")
        (target / "SKILL.md").unlink()
        (target / "references/rules.md").unlink()
        install.install_bundle(self.source, self.destination)
        self.assertFalse(target.exists())

    def test_retired_deletions_roll_back_when_an_active_marker_write_fails(self):
        install.install_into(self.source, self.destination)
        old_targets = [self.old_install(name) for name in install.RETIRED_NAMES]
        self.write("SKILL.md", "updated core")
        before = install.tree_files(self.destination.parent)
        original = install.atomic_write
        failed = False

        def fail_marker(path, data):
            nonlocal failed
            if path == self.destination / install.MARKER and not failed:
                failed = True
                self.assertTrue(all(not (target / "SKILL.md").exists() for target in old_targets))
                raise OSError("simulated migration marker failure")
            return original(path, data)

        with patch.object(install, "atomic_write", side_effect=fail_marker), self.assertRaisesRegex(OSError, "migration marker"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination.parent), before)

    def test_retirement_rollback_preserves_a_concurrent_recreated_file(self):
        install.install_into(self.source, self.destination)
        target = self.old_install("bandit-update")
        self.write("SKILL.md", "updated core")
        before_core = install.tree_files(self.destination)
        original = install.atomic_write
        failed = False

        def fail_after_edit(path, data):
            nonlocal failed
            if path == self.destination / install.MARKER and not failed:
                failed = True
                (target / "SKILL.md").write_text("concurrent replacement")
                raise OSError("migration failure after concurrent edit")
            return original(path, data)

        with patch.object(install, "atomic_write", side_effect=fail_after_edit), self.assertRaisesRegex(OSError, "migration failure"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual((target / "SKILL.md").read_text(), "concurrent replacement")
        self.assertTrue((target / install.MARKER).exists())
        self.assertEqual(install.tree_files(self.destination), before_core)

    def test_retired_skill_lock_blocks_the_whole_transaction(self):
        self.destination.parent.mkdir(parents=True)
        lock = self.destination.parent / ".bandit-update.bandit.lock"
        lock.write_text("another installer")
        before = install.tree_files(self.destination.parent)
        with self.assertRaisesRegex(install.InstallError, "Install lock exists"):
            install.install_bundle(self.source, self.destination)
        self.assertEqual(install.tree_files(self.destination.parent), before)
        self.assertFalse(self.destination.exists())

    def test_custom_core_destination_cannot_use_a_retired_name(self):
        with self.assertRaisesRegex(install.InstallError, "collides"):
            install.install_bundle(self.source, self.destination.parent / "BANDIT-DECIDE")
        self.assertFalse(self.destination.parent.exists())

    def test_unmanaged_notes_without_a_retired_entrypoint_are_preserved(self):
        target = self.destination.parent / "bandit-update"
        target.mkdir(parents=True)
        (target / "notes.md").write_text("unmanaged notes")
        report = install.install_bundle(self.source, self.destination)
        self.assertEqual((target / "notes.md").read_text(), "unmanaged notes")
        self.assertEqual(next(item for item in report["retirements"] if item["name"] == "bandit-update")["status"], "preserved")

    def test_migration_plan_never_removes_retired_files(self):
        target = self.old_install("bandit-decide")
        before = install.tree_files(self.destination.parent)
        report = install.install_bundle(self.source, self.destination, dry_run=True)
        self.assertEqual(report["status"], "plan")
        self.assertEqual(len(report["skills"]), 5)
        self.assertEqual(install.tree_files(self.destination.parent), before)
        self.assertTrue((target / "SKILL.md").exists())
