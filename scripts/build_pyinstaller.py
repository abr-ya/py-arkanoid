from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Py Arkanoid with PyInstaller.")
    parser.add_argument(
        "--console",
        action="store_true",
        help="keep a console window for debugging packaged startup failures",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="remove previous PyInstaller build directories before building",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    dist_dir = root / "dist"
    build_dir = root / "build"

    if args.clean:
        shutil.rmtree(build_dir, ignore_errors=True)
        shutil.rmtree(dist_dir, ignore_errors=True)

    try:
        import PyInstaller.__main__
    except ImportError:
        print("PyInstaller is not installed. Run: python -m pip install -e .[build]", file=sys.stderr)
        return 2

    add_data = f"{root / 'levels'}{os.pathsep}levels"
    command = [
        "--name",
        "arkanoid",
        "--onefile",
        "--noconfirm",
        "--clean",
        "--distpath",
        str(dist_dir),
        "--workpath",
        str(build_dir),
        "--specpath",
        str(build_dir),
        "--add-data",
        add_data,
    ]
    if not args.console:
        command.append("--windowed")
    command.append(str(root / "src" / "arkanoid" / "__main__.py"))

    PyInstaller.__main__.run(command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
