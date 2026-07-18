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
| 01 | [`feature-01-build-first-playable-arkanoid`](changes/archive/2026-07-08-feature-01-build-first-playable-arkanoid/proposal.md) | First playable local game: Pygame shell, state machine, paddle, ball, simple bricks, lives, basic scoring, and core tests. | [design](changes/archive/2026-07-08-feature-01-build-first-playable-arkanoid/design.md), [tasks](changes/archive/2026-07-08-feature-01-build-first-playable-arkanoid/tasks.md), [specs](changes/archive/2026-07-08-feature-01-build-first-playable-arkanoid/specs/) |
| 02 | [`feature-02-add-levels-and-brick-types`](changes/archive/2026-07-09-feature-02-add-levels-and-brick-types/proposal.md) | Configured levels, level progression, and richer brick behavior. | [design](changes/archive/2026-07-09-feature-02-add-levels-and-brick-types/design.md), [tasks](changes/archive/2026-07-09-feature-02-add-levels-and-brick-types/tasks.md), [specs](changes/archive/2026-07-09-feature-02-add-levels-and-brick-types/specs/) |
| 03 | [`feature-03-add-power-ups`](changes/archive/2026-07-10-feature-03-add-power-ups/proposal.md) | Falling bonuses, Wide/Slow/Multi/Sticky effects, and effect timers. | [design](changes/archive/2026-07-10-feature-03-add-power-ups/design.md), [tasks](changes/archive/2026-07-10-feature-03-add-power-ups/tasks.md), [specs](changes/archive/2026-07-10-feature-03-add-power-ups/specs/) |
| 04 | [`feature-04-add-local-leaderboard`](changes/archive/2026-07-11-feature-04-add-local-leaderboard/proposal.md) | Offline score persistence, name entry, and top-10 display. | [design](changes/archive/2026-07-11-feature-04-add-local-leaderboard/design.md), [tasks](changes/archive/2026-07-11-feature-04-add-local-leaderboard/tasks.md), [specs](changes/archive/2026-07-11-feature-04-add-local-leaderboard/specs/) |
| 05 | [`feature-05-add-distribution-builds`](changes/archive/2026-07-12-feature-05-add-distribution-builds/proposal.md) | Shareable Windows `.exe` and Linux artifacts, with GitHub Actions support and Linux installer options documented. | [design](changes/archive/2026-07-12-feature-05-add-distribution-builds/design.md), [tasks](changes/archive/2026-07-12-feature-05-add-distribution-builds/tasks.md), [specs](changes/archive/2026-07-12-feature-05-add-distribution-builds/specs/) |
| 06 | [`feature-06-add-basic-sounds`](changes/archive/2026-07-13-feature-06-add-basic-sounds/proposal.md) | Baseline sound effects for launch, collisions, brick breaks, power-up pickup, and level completion, with a path for later asset upgrades. | [design](changes/archive/2026-07-13-feature-06-add-basic-sounds/design.md), [tasks](changes/archive/2026-07-13-feature-06-add-basic-sounds/tasks.md), [specs](changes/archive/2026-07-13-feature-06-add-basic-sounds/specs/) |
| 07 | [`feature-07-add-level-pack-and-difficulty`](changes/archive/2026-07-13-feature-07-add-level-pack-and-difficulty/proposal.md) | Expand the level set to 3-5 levels and define a clearer difficulty curve. | [design](changes/archive/2026-07-13-feature-07-add-level-pack-and-difficulty/design.md), [tasks](changes/archive/2026-07-13-feature-07-add-level-pack-and-difficulty/tasks.md), [specs](changes/archive/2026-07-13-feature-07-add-level-pack-and-difficulty/specs/) |
| 08 | [`feature-08-polish-readability-and-screens`](changes/archive/2026-07-15-feature-08-polish-readability-and-screens/proposal.md) | Readability, colors, HUD, primary screens, control hints, and text fit after builds, sounds, and level content are in place. | [design](changes/archive/2026-07-15-feature-08-polish-readability-and-screens/design.md), [tasks](changes/archive/2026-07-15-feature-08-polish-readability-and-screens/tasks.md), [specs](changes/archive/2026-07-15-feature-08-polish-readability-and-screens/specs/) |
| 09 | [`feature-09-polish-event-feedback-and-qol`](changes/archive/2026-07-17-feature-09-polish-event-feedback-and-qol/proposal.md) | Visible feedback for important gameplay events and completion/failure states. | [design](changes/archive/2026-07-17-feature-09-polish-event-feedback-and-qol/design.md), [tasks](changes/archive/2026-07-17-feature-09-polish-event-feedback-and-qol/tasks.md), [specs](changes/archive/2026-07-17-feature-09-polish-event-feedback-and-qol/specs/) |
| 10 | [`feature-10-polish-bounded-qol`](changes/archive/2026-07-18-feature-10-polish-bounded-qol/proposal.md) | Observation-driven quality-of-life polish that preserves accepted gameplay behavior. | [design](changes/archive/2026-07-18-feature-10-polish-bounded-qol/design.md), [tasks](changes/archive/2026-07-18-feature-10-polish-bounded-qol/tasks.md), [specs](changes/archive/2026-07-18-feature-10-polish-bounded-qol/specs/) |
| 11 | [`feature-11-add-online-leaderboard-client`](changes/feature-11-add-online-leaderboard-client/proposal.md) | Optional HTTP leaderboard client integration with local-first fallback; server-side score persistence remains separate. | [design](changes/feature-11-add-online-leaderboard-client/design.md), [tasks](changes/feature-11-add-online-leaderboard-client/tasks.md), [specs](changes/feature-11-add-online-leaderboard-client/specs/) |

## Future Candidates

- Allow local leaderboard name entry between 2 and 12 characters, replacing the
  current fixed 3-character initials constraint. This should be a dedicated
  leaderboard/input change because it updates score-entry validation, display
  layout, and saved-record expectations.

## Working Rule

Before implementing a later feature, review and adjust its proposal, design,
tasks, and specs against the actual code produced by earlier changes.
