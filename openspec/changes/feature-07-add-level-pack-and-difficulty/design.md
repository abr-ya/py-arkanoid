## Context

Feature 02 added configurable levels and progression. This change uses that foundation to create a small built-in campaign instead of changing the loader architecture.

## Goals / Non-Goals

**Goals:**

- Ship 3-5 built-in levels.
- Make level 1 approachable and later levels progressively harder.
- Use existing brick types and power-up configuration before adding new mechanics.
- Verify every shipped level loads successfully.

**Non-Goals:**

- A level editor.
- New brick types or power-up types.
- Procedural generation.
- Broad physics rewrites.

## Decisions

### Level count

Target 5 levels, but accept 3 if the extra layouts would be filler. Each shipped level should have a distinct purpose: intro, brick variety, durability, hazards, and higher-pressure play.

### Difficulty curve

Increase difficulty through layout density, durable bricks, indestructible obstacles, speed multiplier, and power-up availability. Keep jumps moderate enough that a new player can learn from each level.

### Validation

Extend tests or add a small validation path that loads every shipped level and confirms progression can find the next one.

## Risks / Trade-offs

- [Risk] More levels can make balance feel uneven. -> Mitigation: keep metadata explicit and leave final tuning to the polish slice.
- [Risk] Layout files can drift from loader rules. -> Mitigation: validate every shipped level in tests.
- [Risk] New content can accidentally introduce new mechanics. -> Mitigation: limit this slice to existing brick and power-up behavior.
