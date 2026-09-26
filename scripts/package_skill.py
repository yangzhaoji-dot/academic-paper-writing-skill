#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import tempfile
import zipfile

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / ".agents" / "skills" / "academic-paper-writing"
DIST = REPO_ROOT / "dist"
OUTPUT = DIST / "academic-paper-writing.zip"
TOP_LEVEL = "academic-paper-writing"


def main() -> None:
    if not (SOURCE / "SKILL.md").exists():
        raise SystemExit(f"Missing {SOURCE / 'SKILL.md'}")

    DIST.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()

    with tempfile.TemporaryDirectory() as td:
        staging = Path(td) / TOP_LEVEL
        shutil.copytree(SOURCE, staging)

        with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(staging.rglob("*")):
                if path.is_file():
                    arcname = Path(TOP_LEVEL) / path.relative_to(staging)
                    zf.write(path, arcname.as_posix())

    print(OUTPUT)


if __name__ == "__main__":
    main()
