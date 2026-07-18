## Feature 10 Play Review

Review date: 2026-07-18

## Method

- Checked the Feature 10 proposal, design, specs, and task list.
- Reviewed the current post-Feature 09 gameplay/UI paths in `src/arkanoid/core/game.py`
  and `src/arkanoid/pygame_app.py`.
- Ran `.venv/bin/python -m arkanoid --smoke` to verify the current game resources
  load successfully.

Note: this pass is code-grounded and smoke-verified. A short interactive play
check should still be performed after selecting the QoL fixes.

## Observations Worth Addressing

1. Level-clear feedback may be too brief to comfortably read.
   - Evidence: `LEVEL_CLEAR_SECONDS` is `0.8`, while the overlay now includes
     level progress, score, and a progress bar.
   - QoL applied: lengthen the level-clear pause to `1.2` seconds without
     changing level progression rules.

2. Name entry gives no feedback when Enter is pressed before all 3 letters are
   entered.
   - Evidence: `submit_score_name()` ignores incomplete names, while the screen
     only shows the static "Type 3 letters, then press Enter" hint.
   - Candidate QoL: add a narrow presentation cue for incomplete name entry.

3. After life loss, relaunch depends on noticing the attached ball and HUD hint.
   - Evidence: losing the final active ball records "-1 LIFE", immediately resets
     the ball onto the paddle, and relies on the existing "Space to launch" hint.
   - Candidate QoL: make the relaunch-ready state more obvious only after a life
     loss, without changing lives, scoring, speed, or launch controls.

## Deferred Ideas

- Do not change paddle controls, key bindings, physics, or collision behavior in
  this slice.
- Do not adjust level layouts, brick types, ball speed curve, paddle widths, or
  other balance/content settings.
- Do not add settings, online leaderboard behavior, packaging changes, or sound
  system work.
