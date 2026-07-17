## 1. Event Feedback

- [x] 1.1 Add immediate visual feedback for brick hits.
- [x] 1.2 Add clear score-change feedback where it helps the player notice scoring.
- [x] 1.3 Add clear life-loss feedback before the next launch.

## 2. Completion And Failure States

- [x] 2.1 Improve level-clear feedback without changing level progression rules.
- [x] 2.2 Improve game-over feedback without changing local leaderboard flow.
- [x] 2.3 Verify feedback does not obscure the ball, paddle, bricks, or HUD.

## 3. Scope Guard

- [x] 3.1 Confirm broader QoL observations are deferred to `feature-10-polish-bounded-qol`.
- [x] 3.2 Keep sound, level-content, server, online leaderboard, controls, balance, and packaging follow-ups out of this slice unless they are feedback regressions.

## Verification

- Manual visual check confirmed life-loss, level-clear, and game-over feedback remain readable and do not obscure the ball, paddle, bricks, HUD, or leaderboard flow.
- Scope guard confirmed: broader QoL stays in `feature-10-polish-bounded-qol`; sound, level-content, server, online leaderboard, controls, balance, and packaging work stay out of Feature 09.
