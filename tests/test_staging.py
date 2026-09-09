from pathlib import Path
from unittest.mock import patch

from _support import DistributionTest
import install


class StagingTests(DistributionTest):
    """Synthetic staged-source changes inside an ordinary local installation."""

    def prepare_update(self):
        install.install_into(self.source, self.destination)
        before = install.tree_files(self.destination)
        self.write("SKILL.md", "Updated synthetic instructions.\n")
        self.write("references/rules.md", "Updated synthetic rules.\n")
        return before

    def update_with_staged_change(self, mutate):
        create = install.tempfile.mkstemp
        read = install.regular_bytes
        staged = None
        injected = False
        error = None

        def remember_staged(*args, **kwargs):
            nonlocal staged
            descriptor, temporary = create(*args, **kwargs)
            if Path(temporary).parent == self.destination / "references" and not injected:
                staged = Path(temporary)
            return descriptor, temporary

        def change_before_destination_read(path):
            nonlocal injected
            if staged is not None and not injected and path == self.destination / "references/rules.md":
                injected = True
                mutate(staged)
            return read(path)

        with patch.object(install.tempfile, "mkstemp", side_effect=remember_staged), \
                patch.object(install, "regular_bytes", side_effect=change_before_destination_read):
            try:
                install.install_into(self.source, self.destination)
            except (OSError, install.InstallError) as exc:
                error = exc
        self.assertTrue(injected, "The change must follow a real completed staging write")
        return staged, error

    def test_changed_staged_bytes_are_preserved_without_promotion_and_prior_writes_roll_back(self):
        before = self.prepare_update()
        edited = b"Concurrent work in the staged file.\n"
        staged, error = self.update_with_staged_change(lambda target: target.write_bytes(edited))
        self.assertTrue(staged.exists(), "The changed staging file must remain at its own path")
        self.assertEqual(staged.read_bytes(), edited)
        self.assertIsInstance(error, install.InstallError)
        self.assertEqual(install.tree_files(self.destination), {
            **before, staged.relative_to(self.destination).as_posix(): edited,
        })

    def test_identical_bytes_in_a_different_staged_file_are_not_promoted(self):
        before = self.prepare_update()
        saved = self.area / "moved-owned-staging-file"
        replacement = None

        def replace_staged(target):
            nonlocal replacement
            data = target.read_bytes()
            target.rename(saved)
            target.write_bytes(data)
            replacement = target.stat()

        staged, error = self.update_with_staged_change(replace_staged)
        self.assertNotEqual(replacement.st_ino, saved.stat().st_ino)
        self.assertTrue(staged.exists(), "A replacement staging file must remain at its own path")
        self.assertEqual(staged.stat().st_ino, replacement.st_ino)
        self.assertIsInstance(error, install.InstallError)
        self.assertEqual(staged.read_bytes(), saved.read_bytes())
        self.assertEqual(install.tree_files(self.destination), {
            **before, staged.relative_to(self.destination).as_posix(): staged.read_bytes(),
        })
