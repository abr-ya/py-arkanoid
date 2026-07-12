## Context

Polish is intentionally delayed until distribution, baseline sounds, and the expanded level pack have landed. This keeps visual and usability work focused on the version players are likely to try.

## Goals / Non-Goals

**Goals:**

- Make the game feel clear, readable, and responsive.
- Improve feedback for important events.
- Add small quality-of-life improvements from play observations.

**Non-Goals:**

- New major mechanics.
- Rewriting physics.
- Sound-system work, level-pack expansion, server work, or packaging work.

## Decisions

### Preserve core contracts

Polish may adjust presentation and small usability constants, but it must not silently change core requirements from earlier changes. Any meaningful gameplay rule change should become its own OpenSpec change.

### Asset approach

Start with simple generated or hand-authored bitmap/font assets only when they improve readability. Avoid making asset production a blocker for gameplay fixes.

## Risks / Trade-offs

- [Risk] Polish can expand endlessly. -> Mitigation: keep tasks tied to observable feedback and stop when the game is clear and shareable.
- [Risk] Tuning can invalidate tests that assume exact constants. -> Mitigation: tests should cover behavior and bounds, not decorative values.
