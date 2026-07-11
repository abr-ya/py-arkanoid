## Context

The brick-types change introduces bonus-marker bricks but intentionally does not spawn or apply bonus effects. This change completes that gameplay loop.

## Goals / Non-Goals

**Goals:**

- Add catchable falling bonuses.
- Keep effect timing deterministic and testable in core logic.
- Support multiple simultaneous effects where reasonable.

**Non-Goals:**

- Randomized rare special effects beyond the defined list.
- Networked or persistent bonus state.

## Decisions

### Effect registry

Use a small registry mapping power-up identifiers to effect handlers. This keeps level config values stable and avoids hard-coded conditionals spreading through the game loop.

### Multi-ball lifecycle

Multiple balls remain active until lost. The life is lost only when the last active ball crosses the bottom boundary.

### Sticky behavior

Sticky is consumed on the next paddle catch and launch cycle, rather than running as a long timer.

## Risks / Trade-offs

- [Risk] Multiple balls can complicate collision and life-loss behavior. -> Mitigation: add tests for losing one ball versus losing the final ball.
- [Risk] Stacking rules may feel unclear. -> Mitigation: document effect refresh/stack behavior in specs and show active effects in UI.
