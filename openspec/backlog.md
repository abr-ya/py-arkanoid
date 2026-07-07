# Arkanoid OpenSpec Backlog

This file is the navigation point for the split Arkanoid roadmap. The numbered
change directories under `openspec/changes/` are the intended implementation
order.

## Source Change

- [`open-arkanoid`](changes/open-arkanoid/proposal.md): original broad draft
  that captured the full Arkanoid vision. Keep it as reference material while
  the split changes are reviewed. Do not use it as the next implementation
  target unless the split is intentionally rolled back.

## Feature Sequence

| Order | Change | Scope | Key Artifacts |
|-------|--------|-------|---------------|
| 01 | [`01-build-first-playable-arkanoid`](changes/01-build-first-playable-arkanoid/proposal.md) | First playable local game: Pygame shell, state machine, paddle, ball, simple bricks, lives, basic scoring, and core tests. | [design](changes/01-build-first-playable-arkanoid/design.md), [tasks](changes/01-build-first-playable-arkanoid/tasks.md), [specs](changes/01-build-first-playable-arkanoid/specs/) |
| 02 | [`02-add-levels-and-brick-types`](changes/02-add-levels-and-brick-types/proposal.md) | Configured levels, level progression, and richer brick behavior. | [design](changes/02-add-levels-and-brick-types/design.md), [tasks](changes/02-add-levels-and-brick-types/tasks.md), [specs](changes/02-add-levels-and-brick-types/specs/) |
| 03 | [`03-add-power-ups`](changes/03-add-power-ups/proposal.md) | Falling bonuses, Wide/Slow/Multi/Sticky effects, and effect timers. | [design](changes/03-add-power-ups/design.md), [tasks](changes/03-add-power-ups/tasks.md), [specs](changes/03-add-power-ups/specs/) |
| 04 | [`04-add-local-leaderboard`](changes/04-add-local-leaderboard/proposal.md) | Offline score persistence, name entry, and top-10 display. | [design](changes/04-add-local-leaderboard/design.md), [tasks](changes/04-add-local-leaderboard/tasks.md), [specs](changes/04-add-local-leaderboard/specs/) |
| 05 | [`05-add-online-leaderboard-client`](changes/05-add-online-leaderboard-client/proposal.md) | Optional HTTP leaderboard integration with local-first fallback. | [design](changes/05-add-online-leaderboard-client/design.md), [tasks](changes/05-add-online-leaderboard-client/tasks.md), [specs](changes/05-add-online-leaderboard-client/specs/) |
| 06 | [`06-add-distribution-builds`](changes/06-add-distribution-builds/proposal.md) | Packaged Windows and Linux builds after gameplay and resource paths stabilize. | [design](changes/06-add-distribution-builds/design.md), [tasks](changes/06-add-distribution-builds/tasks.md), [specs](changes/06-add-distribution-builds/specs/) |
| 07 | [`07-polish-arkanoid-experience`](changes/07-polish-arkanoid-experience/proposal.md) | Presentation, feedback, readability, and tuning after core behavior is stable. | [design](changes/07-polish-arkanoid-experience/design.md), [tasks](changes/07-polish-arkanoid-experience/tasks.md), [specs](changes/07-polish-arkanoid-experience/specs/) |

## Working Rule

Before implementing a later feature, review and adjust its proposal, design,
tasks, and specs against the actual code produced by earlier changes.
