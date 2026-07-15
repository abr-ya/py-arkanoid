## Context

Polish is intentionally delayed until distribution, baseline sounds, and the expanded level pack have landed. This first polish slice is limited to readability and primary game screens so it stays small and easy to verify.

## Goals / Non-Goals

**Goals:**

- Make the game feel clear, readable, and responsive.
- Make menu, pause, level-clear, game-over, HUD, and controls hints easier to scan.
- Keep visual changes bounded to presentation and readability.

**Non-Goals:**

- New major mechanics.
- Rewriting physics.
- Event-effect feedback, score/life feedback, and broader QoL tuning.
- Sound-system work, level-pack expansion, server work, or packaging work.

## Decisions

### Preserve core contracts

Readability polish may adjust presentation and text layout, but it must not silently change core requirements from earlier changes. Any meaningful gameplay rule change should become its own OpenSpec change.

### Asset approach

Start with built-in rendering and simple constants. Add font or UI assets only when they directly improve readability.

## Risks / Trade-offs

- [Risk] Polish can expand endlessly. -> Mitigation: keep this change tied to readability and screen presentation; move event feedback and QoL tuning to Feature 09.
- [Risk] Tuning can invalidate tests that assume exact constants. -> Mitigation: tests should cover behavior and bounds, not decorative values.
