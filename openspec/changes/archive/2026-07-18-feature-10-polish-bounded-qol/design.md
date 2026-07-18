## Context

Feature 08 handled readability and primary screens. Feature 09 handles immediate event and completion feedback. This change is reserved for quality-of-life polish that emerges from actually playing those slices together.

## Goals / Non-Goals

**Goals:**

- Capture play observations before making QoL changes.
- Make small, focused comfort improvements that reduce confusion or frustration.
- Keep accepted gameplay contracts intact unless a later change explicitly updates them.

**Non-Goals:**

- New major mechanics.
- Rewriting physics or collision behavior.
- Difficulty-curve redesign or new level content.
- Sound-system, server, online leaderboard, settings, or packaging work.

## Decisions

### Observation first

Each QoL task should name the observed issue it addresses. If the issue cannot be described from manual play or a focused reproduction, defer it instead of guessing.

### Small changes only

Prefer tiny hints, timing adjustments, or local presentation changes over new systems. Anything that touches balance, controls, persistence, or configuration broadly should become its own change.

### Preserve surrounding contracts

QoL changes may make the game feel clearer or less frustrating, but they should not change score rules, level progression, local leaderboard flow, sound behavior, build behavior, or online leaderboard boundaries.

## Risks / Trade-offs

- [Risk] QoL can become a grab bag. -> Mitigation: require an observation for each change and defer unrelated ideas.
- [Risk] A small comfort fix can accidentally affect difficulty. -> Mitigation: verify level progression and local leaderboard behavior after changes.
