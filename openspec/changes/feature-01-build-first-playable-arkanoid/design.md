## Context

The existing `open-arkanoid` change describes a full game, including bonuses, level progression, leaderboards, and builds. This first change narrows the implementation to a playable local game and keeps the core logic testable without Pygame.

## Goals / Non-Goals

**Goals:**

- Produce a playable Arkanoid loop quickly.
- Keep game rules in pure Python where practical.
- Use Pygame only for windowing, input, timing, and drawing.
- Make the first implementation easy to extend with later OpenSpec changes.

**Non-Goals:**

- YAML/JSON level progression.
- Multiple brick types beyond simple destructible bricks.
- Power-ups, local records, online records, packaged binaries, sound, or custom assets.

## Decisions

### Core and adapter split

Use a small core package for state, entities, collision helpers, and scoring. The Pygame adapter owns event translation, drawing, clock timing, and process exit. This keeps unit tests fast and avoids headless Pygame setup for core behavior.

### Time units

Use seconds for `dt` inside core update functions. Pygame returns milliseconds from `Clock.tick(60)`, so the adapter converts to seconds once at the boundary. This avoids the ambiguity in the original broad plan.

### First playable level

Hard-code a simple starter brick layout in code for this change. A later levels change will replace this with config loading and progression.

### Ball launch and life loss

The ball starts attached to the paddle. Pressing Space launches it. Crossing the bottom boundary loses one life; if lives remain, the ball resets to the paddle; if no lives remain, state becomes `GAME_OVER`.

## Risks / Trade-offs

- [Risk] A minimal hard-coded layout may need refactoring when config levels land. -> Mitigation: keep layout creation isolated behind a small factory function.
- [Risk] Collision behavior may be imperfect at high speed. -> Mitigation: cap first-slice speeds and add tests for common collision cases.
- [Risk] Pygame rendering can tempt core imports. -> Mitigation: place rendering code in a separate module and test that core modules import without Pygame initialization.
