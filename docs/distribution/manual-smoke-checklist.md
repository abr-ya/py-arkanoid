# Packaged Artifact Smoke Checklist

Use this checklist after downloading or building a packaged artifact.

## Automatic Smoke

- Run `arkanoid --smoke` from the extracted artifact location.
- Confirm it prints `arkanoid smoke ok`.
- Confirm the printed `levels_dir` points to bundled runtime resources.
- Confirm the printed `sounds_dir` points to bundled runtime resources.
- Confirm the printed `leaderboard` path points to writable local user data or the expected development directory.

## Manual Game Smoke

- Launch the packaged game normally.
- Start a game with Enter or Space.
- Confirm launch, collision, brick-break, power-up, and level-clear moments play short sounds when audio is available.
- Relaunch with `ARKANOID_SOUND=0` and confirm gameplay continues silently.
- Confirm level 1 loads with bricks visible and a forgiving paddle width.
- Break at least one brick and confirm score changes.
- Clear at least one level when practical and confirm the next built-in level loads.
- Lose all lives or enter game-over flow and confirm the app does not crash when reading or writing local scores.
- Close the game from the window close button or with `q`.

## Platform Notes

- Windows artifacts are built on a Windows runner through GitHub Actions.
- Linux artifacts should be checked on Ubuntu or Linux Mint when possible.
- If a windowed build fails silently, rebuild with `python scripts/build_pyinstaller.py --console` for diagnostics.
