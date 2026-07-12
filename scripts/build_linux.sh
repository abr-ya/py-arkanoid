#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -x ".venv/bin/python" ]]; then
  PYTHON=".venv/bin/python"
else
  PYTHON="python3"
fi

if ! "$PYTHON" -c "import PyInstaller" >/dev/null 2>&1; then
  "$PYTHON" -m pip install -e ".[build]"
fi
"$PYTHON" scripts/build_pyinstaller.py --clean

ARTIFACT_DIR="dist/linux/arkanoid-linux"
rm -rf "$ARTIFACT_DIR"
mkdir -p "$ARTIFACT_DIR"
cp dist/arkanoid "$ARTIFACT_DIR/arkanoid"
chmod +x "$ARTIFACT_DIR/arkanoid"

tar -C dist/linux -czf dist/arkanoid-linux.tar.gz arkanoid-linux

echo "Linux artifact: dist/arkanoid-linux.tar.gz"
