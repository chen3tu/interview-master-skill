import hashlib
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.build_release import build_release


class BuildReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name) / "repository"
        (self.root / "references" / "nested").mkdir(parents=True)
        (self.root / "SKILL.md").write_text("# Skill\n", encoding="utf-8")
        (self.root / "references" / "guide.md").write_text(
            "# Guide\n", encoding="utf-8"
        )
        (self.root / "references" / "nested" / "example.txt").write_text(
            "example\n", encoding="utf-8"
        )
        (self.root / "README.md").write_text("# Repository\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_archive_contains_only_skill_payload(self) -> None:
        archive = build_release(self.root, "3.0.0", self.root / "dist")

        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()

        self.assertEqual(
            names,
            [
                "interview-master/SKILL.md",
                "interview-master/references/guide.md",
                "interview-master/references/nested/example.txt",
            ],
        )
        self.assertNotIn("interview-master/README.md", names)

    def test_repeated_builds_have_identical_hashes(self) -> None:
        first = build_release(self.root, "3.0.0", self.root / "first")
        second = build_release(self.root, "3.0.0", self.root / "second")

        first_hash = hashlib.sha256(first.read_bytes()).hexdigest()
        second_hash = hashlib.sha256(second.read_bytes()).hexdigest()

        self.assertEqual(first_hash, second_hash)

    def test_symlinked_payload_file_is_rejected(self) -> None:
        external_path = Path(self.temp_dir.name) / "private.txt"
        external_path.write_text("must not be packaged\n", encoding="utf-8")
        (self.root / "references" / "external.md").symlink_to(external_path)

        with self.assertRaisesRegex(
            ValueError,
            "Symlinks are not allowed in release payload",
        ):
            build_release(self.root, "3.0.0", self.root / "dist")


if __name__ == "__main__":
    unittest.main()
