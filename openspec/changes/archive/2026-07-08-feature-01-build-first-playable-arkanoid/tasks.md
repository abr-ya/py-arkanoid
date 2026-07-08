## 1. Project Foundation

- [x] 1.1 Create package structure for core logic, Pygame adapter, assets placeholder, and tests.
- [x] 1.2 Add project dependency metadata for runtime and test dependencies.
- [x] 1.3 Add a launch entry point that opens an 800x600 Pygame window and exits cleanly.

## 2. Core Game Model

- [x] 2.1 Implement game state enum and transition helpers for menu, playing, paused, and game over.
- [x] 2.2 Implement pure Python data models for paddle, ball, brick, playfield, and game session.
- [x] 2.3 Implement lives, ball reset, restart, and quit intent handling.

## 3. Physics And Gameplay

- [x] 3.1 Implement ball movement using seconds-based `dt`.
- [x] 3.2 Implement wall collision for top, left, and right boundaries.
- [x] 3.3 Implement paddle collision with offset-based reflection.
- [x] 3.4 Implement simple brick collision, damage, removal, and single-collision-per-frame behavior.
- [x] 3.5 Implement bottom-boundary life loss and game-over transition.

## 4. Rendering And Input

- [x] 4.1 Map keyboard input to start, launch, pause, resume, restart, paddle movement, and quit actions.
- [x] 4.2 Draw menu, playing HUD, pause overlay, and game-over screen.
- [x] 4.3 Draw paddle, ball, and simple bricks with stable positions and sizes.

## 5. Scoring And Tests

- [x] 5.1 Add score increments for destroyed simple bricks.
- [x] 5.2 Display score and lives in the HUD.
- [x] 5.3 Add unit tests for state transitions, wall reflection, paddle reflection, brick destruction, life loss, and score updates.
- [x] 5.4 Run the focused test suite and perform a manual launch smoke test.
