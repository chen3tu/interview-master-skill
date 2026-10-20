#!/usr/bin/env python3
"""Validate the structure and local references of this Skill repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED_FILES = (
    "README.md",
    "SKILL.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
)
REQUIRED_DIRECTORIES = ("references",)
FRONTMATTER_KEYS = ("name", "description")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_LITERAL_RE = re.compile(r"`(references/[^`\s]+\.md)`")


def _frontmatter_errors(skill_path: Path) -> list[str]:
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return ["SKILL.md must start with YAML frontmatter"]

    closing_index = text.find("\n---\n", 4)
    if closing_index == -1:
        return ["SKILL.md must close its YAML frontmatter"]

    frontmatter = text[4:closing_index]
    values: dict[str, str] = {}
    for line in frontmatter.splitlines():
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip()

    return [
        f"SKILL.md frontmatter missing required key: {key}"
        for key in FRONTMATTER_KEYS
        if not values.get(key)
    ]


def _local_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return unquote(parsed.path)


def _markdown_errors(root: Path) -> list[str]:
    errors: list[str] = []
    for markdown_path in sorted(root.rglob("*.md")):
        relative_path = markdown_path.relative_to(root)
        if ".git" in relative_path.parts or ".worktrees" in relative_path.parts:
            continue
        if not markdown_path.is_file() or markdown_path.is_symlink():
            continue

        relative_source = relative_path.as_posix()
        try:
            text = markdown_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"Unable to read Markdown file: {relative_source}")
            continue

        for raw_target in MARKDOWN_LINK_RE.findall(text):
            local_target = _local_link_target(raw_target)
            if local_target is None:
                continue
            resolved = (markdown_path.parent / local_target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{relative_source} links to missing path: {local_target}"
                )

        if relative_source == "SKILL.md":
            for reference in REFERENCE_LITERAL_RE.findall(text):
                if not (root / reference).exists():
                    errors.append(
                        f"{relative_source} references missing path: {reference}"
                    )

    return errors


def validate_runtime(root: Path) -> list[str]:
    """Check that runtime references are discoverable and contained in the ZIP."""
    root = root.resolve()
    entry = root / "SKILL.md"
    references = root / "references"
    sources = [entry]
    if references.is_dir() and not references.is_symlink():
        sources.extend(sorted(references.rglob("*.md")))
    errors: list[str] = []
    graph: dict[Path, set[Path]] = {}
    for source in sources:
        if not source.is_file() or source.is_symlink():
            continue
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"Unable to read runtime file: {source.relative_to(root)}")
            continue
        targets = [
            (source.parent, target)
            for raw in MARKDOWN_LINK_RE.findall(text)
            if (target := _local_link_target(raw)) is not None
        ]
        targets.extend((root, target) for target in REFERENCE_LITERAL_RE.findall(text))
        edges: set[Path] = set()
        for base, target in targets:
            resolved = (base / target).resolve()
            in_payload = resolved == entry or resolved.is_relative_to(references)
            if Path(target).is_absolute() or not in_payload:
                errors.append(
                    f"{source.relative_to(root)} runtime link outside release payload: {target}"
                )
            elif not resolved.is_file():
                errors.append(
                    f"{source.relative_to(root)} runtime target missing or not a file: {target}"
                )
            else:
                edges.add(resolved)
        graph[source.resolve()] = edges
    reached: set[Path] = set()
    pending = [entry]
    while pending:
        source = pending.pop()
        if source in reached:
            continue
        reached.add(source)
        pending.extend(graph.get(source, set()) - reached)
    for source in graph:
        if source != entry and source not in reached:
            errors.append(f"Runtime reference is unreachable: {source.relative_to(root)}")
    return sorted(set(errors))


def validate_repository(root: Path) -> list[str]:
    """Return repository validation errors, or an empty list when valid."""
    root = root.resolve()
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        path = root / relative_path
        if not path.exists():
            errors.append(f"Missing required path: {relative_path}")
        elif not path.is_file() or path.is_symlink():
            errors.append(f"Required file is not a file: {relative_path}")

    for relative_path in REQUIRED_DIRECTORIES:
        path = root / relative_path
        if not path.exists():
            errors.append(f"Missing required path: {relative_path}")
        elif not path.is_dir() or path.is_symlink():
            errors.append(f"Required directory is not a directory: {relative_path}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file() and not skill_path.is_symlink():
        errors.extend(_frontmatter_errors(skill_path))

    errors.extend(_markdown_errors(root))
    errors.extend(validate_runtime(root))
    return sorted(set(errors))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
