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
| 01 | [`feature-01-build-first-playable-arkanoid`](changes/feature-01-build-first-playable-arkanoid/proposal.md) | First playable local game: Pygame shell, state machine, paddle, ball, simple bricks, lives, basic scoring, and core tests. | [design](changes/feature-01-build-first-playable-arkanoid/design.md), [tasks](changes/feature-01-build-first-playable-arkanoid/tasks.md), [specs](changes/feature-01-build-first-playable-arkanoid/specs/) |
| 02 | [`feature-02-add-levels-and-brick-types`](changes/feature-02-add-levels-and-brick-types/proposal.md) | Configured levels, level progression, and richer brick behavior. | [design](changes/feature-02-add-levels-and-brick-types/design.md), [tasks](changes/feature-02-add-levels-and-brick-types/tasks.md), [specs](changes/feature-02-add-levels-and-brick-types/specs/) |
| 03 | [`feature-03-add-power-ups`](changes/feature-03-add-power-ups/proposal.md) | Falling bonuses, Wide/Slow/Multi/Sticky effects, and effect timers. | [design](changes/feature-03-add-power-ups/design.md), [tasks](changes/feature-03-add-power-ups/tasks.md), [specs](changes/feature-03-add-power-ups/specs/) |
| 04 | [`feature-04-add-local-leaderboard`](changes/feature-04-add-local-leaderboard/proposal.md) | Offline score persistence, name entry, and top-10 display. | [design](changes/feature-04-add-local-leaderboard/design.md), [tasks](changes/feature-04-add-local-leaderboard/tasks.md), [specs](changes/feature-04-add-local-leaderboard/specs/) |
| 05 | [`feature-05-add-online-leaderboard-client`](changes/feature-05-add-online-leaderboard-client/proposal.md) | Optional HTTP leaderboard integration with local-first fallback. | [design](changes/feature-05-add-online-leaderboard-client/design.md), [tasks](changes/feature-05-add-online-leaderboard-client/tasks.md), [specs](changes/feature-05-add-online-leaderboard-client/specs/) |
| 06 | [`feature-06-add-distribution-builds`](changes/feature-06-add-distribution-builds/proposal.md) | Packaged Windows and Linux builds after gameplay and resource paths stabilize. | [design](changes/feature-06-add-distribution-builds/design.md), [tasks](changes/feature-06-add-distribution-builds/tasks.md), [specs](changes/feature-06-add-distribution-builds/specs/) |
| 07 | [`feature-07-polish-arkanoid-experience`](changes/feature-07-polish-arkanoid-experience/proposal.md) | Presentation, feedback, readability, and tuning after core behavior is stable. | [design](changes/feature-07-polish-arkanoid-experience/design.md), [tasks](changes/feature-07-polish-arkanoid-experience/tasks.md), [specs](changes/feature-07-polish-arkanoid-experience/specs/) |

## Working Rule

Before implementing a later feature, review and adjust its proposal, design,
tasks, and specs against the actual code produced by earlier changes.
