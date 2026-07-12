## Why

The eventual leaderboard server is outside this project, but the game should be able to submit and read scores when a server exists. This change is deferred until the local, shareable game has builds, baseline sounds, more levels, and polish.

## What Changes

- Add configurable leaderboard server URL.
- Add HTTP submit and fetch operations.
- Keep local leaderboard behavior as the required fallback.
- Ensure network failures never interrupt gameplay.

## Capabilities

### New Capabilities

- `online-leaderboard-client`: Optional HTTP leaderboard integration with offline fallback.

### Modified Capabilities

None.

## Impact

- Adds an HTTP dependency such as `requests`.
- Extends leaderboard service boundaries and configuration.
