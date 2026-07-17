## Context

The first polish slice focuses on readability and primary screens. This follow-up slice covers the responsive feel of play: whether hits, score changes, life loss, and completion states are obvious without adding new mechanics. Broader quality-of-life changes are split into the next change so they can be reviewed calmly from play observations.

## Goals / Non-Goals

**Goals:**

- Make important gameplay events visibly clear.
- Keep changes compatible with accepted gameplay, level-pack, sound, leaderboard, and distribution behavior.

**Non-Goals:**

- New major mechanics.
- Rewriting physics.
- New level content or difficulty-curve expansion.
- Sound-system, server, online leaderboard, or packaging work.
- Quality-of-life tuning beyond event and completion feedback.

## Decisions

### Feedback stays lightweight

Prefer short-lived visual state, simple effects, or HUD changes over asset-heavy animation. The goal is clarity, not a new visual system.

### QoL moves to the next slice

Quality-of-life tuning now belongs to `feature-10-polish-bounded-qol`. This change can still fix issues created by feedback itself, but it should not become a catch-all for controls, pacing, balance, or broader comfort work.

## Risks / Trade-offs

- [Risk] Feedback effects can obscure gameplay. -> Mitigation: keep effects short and verify they do not hide the ball, paddle, or bricks.
- [Risk] Feedback polish can become a catch-all. -> Mitigation: keep this change limited to visible feedback for already accepted gameplay events.
