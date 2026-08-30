#!/usr/bin/env python3
"""Build a reproducible Claude Skill ZIP for GitHub Releases."""

from __future__ import annotations

import argparse
import stat
import zipfile
from pathlib import Path


ARCHIVE_ROOT = Path("interview-master")
FIXED_TIMESTAMP = (2026, 4, 6, 0, 0, 0)


def _payload_files(root: Path) -> list[Path]:
    skill_path = root / "SKILL.md"
    references_path = root / "references"
    if skill_path.is_symlink():
        raise ValueError(f"Symlinks are not allowed in release payload: {skill_path}")
    if not skill_path.is_file():
        raise FileNotFoundError(f"Missing Skill entrypoint: {skill_path}")
    if references_path.is_symlink():
        raise ValueError(
            f"Symlinks are not allowed in release payload: {references_path}"
        )
    if not references_path.is_dir():
        raise FileNotFoundError(f"Missing references directory: {references_path}")

    payload = [skill_path]
    for path in sorted(references_path.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlinks are not allowed in release payload: {path}")
        if not path.exists() or not stat.S_ISREG(path.lstat().st_mode):
            continue
        if not path.resolve().is_relative_to(root):
            raise ValueError(f"Release payload escapes repository root: {path}")
        payload.append(path)
    return payload


def build_release(root: Path, version: str, output_dir: Path) -> Path:
    """Build and return a deterministic Interview Master release archive."""
    root = root.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = output_dir / f"interview-master-v{version}.zip"

    with zipfile.ZipFile(
        archive_path,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as bundle:
        for source_path in _payload_files(root):
            archive_name = ARCHIVE_ROOT / source_path.relative_to(root)
            info = zipfile.ZipInfo(archive_name.as_posix(), FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            bundle.writestr(
                info,
                source_path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    return archive_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Release version without v prefix")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("dist"),
        help="Directory for the generated ZIP (default: dist)",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    archive_path = build_release(root, args.version, args.output_dir)
    print(archive_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
