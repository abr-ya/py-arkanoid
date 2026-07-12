## Context

Local records are the source of truth for offline play. This later change adds optional online synchronization without owning or implementing the server, after the standalone game is stronger.

## Goals / Non-Goals

**Goals:**

- Submit scores to a configured server when available.
- Fetch top records from a configured server when available.
- Fall back to local records on timeout, connection error, or invalid response.

**Non-Goals:**

- Implementing the FastAPI server.
- Authentication, accounts, or score verification.
- Blocking gameplay on network activity.

## Decisions

### Configuration

Read `LEADERBOARD_URL` from the environment first, then optional config, then default to no remote submission unless explicitly enabled. This avoids surprising localhost calls in normal play.

### Failure policy

All network operations are best-effort. Exceptions are caught, logged, and converted to local-only behavior.

## Risks / Trade-offs

- [Risk] Server API may change because it is not in this repo. -> Mitigation: keep the client boundary small and easy to adapt.
- [Risk] Synchronous HTTP could stall the UI. -> Mitigation: use short timeouts first; consider background submission only if needed.
