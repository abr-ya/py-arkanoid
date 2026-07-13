# Py Arkanoid

First playable Arkanoid slice for the OpenSpec-driven implementation.

## Run

```bash
python -m arkanoid
```

To verify resource loading without opening the game window:

```bash
python -m arkanoid --smoke
```

## Levels

The first level is configured in `levels/level_01.yaml`. Brick row symbols use
`1`/`N` for normal, `2`/`S` for strong, `B` for bonus-marker, `X` for
indestructible, and `L` for extra-life bricks. Missing or invalid level files
fall back to a safe default layout.

## Leaderboard

During development, local scores are stored in `leaderboard.json` next to the
game process. In packaged builds, local scores are stored in the user's app data
directory so the game does not need to write next to the executable. Set
`ARKANOID_DATA_DIR` to override the writable data directory.

## Sound

Short gameplay sound effects are loaded from packaged resources. Set
`ARKANOID_SOUND=0` to run silently for quiet play, tests, or systems without
working audio output.

## Packaged Builds

Install build dependencies:

```bash
python -m pip install -e ".[build]"
```

Build a Linux artifact on Linux:

```bash
scripts/build_linux.sh
```

The Linux script creates `dist/arkanoid-linux.tar.gz`, a portable artifact for
Ubuntu and Linux Mint. For this slice, `.deb` and AppImage packaging are
documented as follow-up options in `docs/distribution/linux-packaging-decision.md`.

Build a Windows `.exe` on Windows:

```powershell
.\scripts\build_windows.ps1
```

Windows builds are also available from the GitHub Actions workflow
`Build Windows executable`, which uploads an `arkanoid-windows` artifact. See
`docs/distribution/manual-smoke-checklist.md` before sharing packaged builds.

## Test

```bash
pytest
```
