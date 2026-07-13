## Why

The game is playable, but important moments still feel quiet. Baseline sounds will make launches, collisions, brick breaks, power-up pickups, and level completion easier to perceive without turning audio production into a blocker.

## What Changes

- Add a small sound service or adapter around Pygame mixer.
- Add baseline sound effects for launch/start, wall or paddle collision, brick break, power-up pickup, and level completion.
- Keep sound assets replaceable so better effects can be added later.
- Provide a way to run without audio hardware or with sound disabled.

## Capabilities

### New Capabilities

- `basic-sounds`: Lightweight sound effects for key gameplay events with safe fallback when audio is unavailable.

### Modified Capabilities

None.

## Impact

- Adds audio assets under the project resources.
- Touches the Pygame presentation layer and event wiring.
- May add tests around sound dispatch without requiring real audio playback.
