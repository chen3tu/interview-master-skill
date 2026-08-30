import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


class ValidateRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name) / ".worktrees" / "repository"
        (self.root / "references").mkdir(parents=True)
        (self.root / "README.md").write_text(
            "# Demo\n\n[Contributing](CONTRIBUTING.md)\n", encoding="utf-8"
        )
        (self.root / "SKILL.md").write_text(
            "---\n"
            "name: demo-skill\n"
            "description: Demo skill\n"
            "---\n\n"
            "Read `references/guide.md`.\n",
            encoding="utf-8",
        )
        (self.root / "CHANGELOG.md").write_text("# Changelog\n", encoding="utf-8")
        (self.root / "CONTRIBUTING.md").write_text(
            "# Contributing\n", encoding="utf-8"
        )
        (self.root / "LICENSE").write_text("MIT\n", encoding="utf-8")
        (self.root / "references" / "guide.md").write_text(
            "# Guide\n", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_valid_repository_has_no_errors(self) -> None:
        self.assertEqual(validate_repository(self.root), [])

    def test_missing_required_file_is_reported(self) -> None:
        (self.root / "LICENSE").unlink()

        errors = validate_repository(self.root)

        self.assertIn("Missing required path: LICENSE", errors)

    def test_malformed_skill_frontmatter_is_reported(self) -> None:
        (self.root / "SKILL.md").write_text("# No frontmatter\n", encoding="utf-8")

        errors = validate_repository(self.root)

        self.assertIn("SKILL.md must start with YAML frontmatter", errors)

    def test_broken_markdown_relative_link_is_reported(self) -> None:
        (self.root / "README.md").write_text(
            "# Demo\n\n[Missing](docs/missing.md)\n", encoding="utf-8"
        )

        errors = validate_repository(self.root)

        self.assertIn(
            "README.md links to missing path: docs/missing.md",
            errors,
        )

    def test_missing_reference_literal_is_reported(self) -> None:
        skill_path = self.root / "SKILL.md"
        skill_path.write_text(
            skill_path.read_text(encoding="utf-8")
            + "Read `references/missing.md`.\n",
            encoding="utf-8",
        )

        errors = validate_repository(self.root)

        self.assertIn(
            "SKILL.md references missing path: references/missing.md",
            errors,
        )

    def test_required_file_replaced_by_directory_is_reported(self) -> None:
        (self.root / "README.md").unlink()
        (self.root / "README.md").mkdir()

        errors = validate_repository(self.root)

        self.assertIn("Required file is not a file: README.md", errors)

    def test_references_replaced_by_file_is_reported(self) -> None:
        shutil.rmtree(self.root / "references")
        (self.root / "references").write_text("not a directory\n", encoding="utf-8")

        errors = validate_repository(self.root)

        self.assertIn(
            "Required directory is not a directory: references",
            errors,
        )

    def test_documentation_reference_example_is_not_a_runtime_dependency(self) -> None:
        (self.root / "CONTRIBUTING.md").write_text(
            "# Contributing\n\nExample: `references/future-role.md`\n",
            encoding="utf-8",
        )

        self.assertEqual(validate_repository(self.root), [])


if __name__ == "__main__":
    unittest.main()
