## Context

The first playable slice intentionally hard-codes a simple brick layout. This change turns that layout into data and adds richer brick behavior without adding full power-up effects yet.

## Goals / Non-Goals

**Goals:**

- Make levels editable without changing gameplay code.
- Support progression across multiple levels.
- Represent brick behavior consistently through type definitions.

**Non-Goals:**

- Full bonus item falling and timed effects.
- Level editor UI.
- Procedural generation.

## Decisions

### Config format

Prefer YAML for hand-authored readability. Keep the loader isolated so JSON support can be added later if YAML becomes unnecessary.

### Indestructible bricks

Represent indestructible bricks with a dedicated type flag instead of relying only on `hp = -1`. This resolves the original contradiction where requirements said `hp >= 1` while also using `-1` as a sentinel.

### Extra life brick

Treat `extra_life` as a brick type in this change because it affects core lives and scoring. It does not create a falling bonus item.

## Risks / Trade-offs

- [Risk] Level config can become too flexible too early. -> Mitigation: support a small schema first: metadata, ball speed multiplier, paddle width, and brick rows.
- [Risk] Stronger brick behavior may disturb first-slice collision tests. -> Mitigation: add type-specific tests at the core layer.
