## Context

The first polish slice focuses on readability and primary screens. This follow-up slice covers the responsive feel of play: whether hits, score changes, life loss, and completion states are obvious without adding new mechanics.

## Goals / Non-Goals

**Goals:**

- Make important gameplay events visibly clear.
- Add small, bounded QoL adjustments from play observations.
- Keep changes compatible with accepted gameplay, level-pack, sound, leaderboard, and distribution behavior.

**Non-Goals:**

- New major mechanics.
- Rewriting physics.
- New level content or difficulty-curve expansion.
- Sound-system, server, online leaderboard, or packaging work.

## Decisions

### Feedback stays lightweight

Prefer short-lived visual state, simple effects, or HUD changes over asset-heavy animation. The goal is clarity, not a new visual system.

### QoL requires an observation

QoL changes should be tied to an observed problem from playtesting or manual review. Avoid speculative tweaks that would broaden the slice.

## Risks / Trade-offs

- [Risk] Feedback effects can obscure gameplay. -> Mitigation: keep effects short and verify they do not hide the ball, paddle, or bricks.
- [Risk] QoL can become a catch-all. -> Mitigation: keep each QoL item tied to a specific observation and defer unrelated ideas to a later change.
