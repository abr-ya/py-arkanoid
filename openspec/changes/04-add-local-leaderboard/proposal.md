## Why

Once a player can complete sessions, local records give the game a persistent goal without requiring any server. This change keeps persistence local and offline-first.

## What Changes

- Add local `leaderboard.json` persistence.
- Add name entry after game over.
- Add top-10 sorting and display.
- Handle missing or corrupted leaderboard files gracefully.

## Capabilities

### New Capabilities

- `local-leaderboard`: Offline score persistence, top-10 ranking, name entry, and game-over display.

### Modified Capabilities

None.

## Impact

- Adds local file I/O near the application data path.
- Extends game-over flow and UI.
