## Context

Polish is intentionally delayed until the game mechanics have stopped moving. This keeps visual and feedback work from hiding core bugs.

## Goals / Non-Goals

**Goals:**

- Make the game feel clear, readable, and responsive.
- Improve feedback for important events.
- Tune difficulty using real play observations.

**Non-Goals:**

- New major mechanics.
- Rewriting physics.
- Server or packaging work.

## Decisions

### Preserve core contracts

Polish may adjust presentation and constants, but it must not silently change core requirements from earlier changes. Any meaningful gameplay rule change should become its own OpenSpec change.

### Asset approach

Start with simple generated or hand-authored bitmap/font assets only when they improve readability. Avoid making asset production a blocker for gameplay fixes.

## Risks / Trade-offs

- [Risk] Polish can expand endlessly. -> Mitigation: keep tasks tied to observable feedback and stop when the game is clear and shareable.
- [Risk] Tuning can invalidate tests that assume exact constants. -> Mitigation: tests should cover behavior and bounds, not decorative values.
