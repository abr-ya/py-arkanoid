## Context

The first playable slice shows a final score but does not persist it. This change adds local persistence before any online leaderboard integration.

## Goals / Non-Goals

**Goals:**

- Save and load local records reliably.
- Never break gameplay because a records file is missing or corrupted.
- Keep the local storage API reusable by the later online client.

**Non-Goals:**

- Remote submission.
- User accounts.
- Anti-cheat validation.

## Decisions

### Storage format

Use a small JSON document with a `records` array. Each record stores `name`, `score`, and ISO timestamp.

### Corruption handling

If the file is unreadable or invalid, treat it as empty records for the current run. Do not overwrite the corrupted file until a new score is saved.

### Name entry

Use a simple three-character name entry screen after game over when score is greater than zero.

## Risks / Trade-offs

- [Risk] Writing beside an executable can be platform-sensitive after packaging. -> Mitigation: isolate the leaderboard path behind a resolver that can change in the distribution feature.
