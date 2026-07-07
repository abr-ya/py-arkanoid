## Why

The current Arkanoid plan is broad enough to delay the first playable result. This change creates the smallest complete vertical slice: a local Pygame game that can be launched, played, lost, restarted, and tested at the core-logic level.

## What Changes

- Add the initial Python project structure for a Pygame Arkanoid app.
- Add a Pygame window and event loop with menu, playing, paused, and game-over states.
- Add paddle, ball, simple destructible bricks, lives, restart flow, and quit flow.
- Add core collision behavior for walls, paddle, and bricks.
- Add a minimal score counter for destroyed bricks.
- Add focused unit tests for pure Python game logic.
- Defer advanced levels, power-ups, persistence, online leaderboard, packaging, and visual polish to later changes.

## Capabilities

### New Capabilities

- `arkanoid-app`: Launchable local Pygame application shell and state transitions.
- `core-gameplay`: Paddle, ball, simple bricks, lives, restart, and game-over gameplay.
- `playfield-physics`: Basic deterministic collision and reflection behavior for the first playable slice.
- `basic-scoring`: Minimal score accumulation and HUD display.

### Modified Capabilities

None.

## Impact

- Adds Python package/module layout under `src/`, a launch entry point, and tests.
- Introduces `pygame` as the runtime dependency and `pytest` for tests.
- Establishes a pure core module boundary: core gameplay logic must not import `pygame`.
