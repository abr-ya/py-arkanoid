## ADDED Requirements

### Requirement: Application launches a Pygame window
The system SHALL provide a launch entry point that opens an 800x600 Pygame window, runs a frame loop capped at 60 FPS, and exits cleanly when the player closes the window.

#### Scenario: Start application
- **WHEN** the player starts the application
- **THEN** an 800x600 game window is created
- **AND** the initial screen is the main menu

#### Scenario: Close application
- **WHEN** the player closes the window
- **THEN** the application exits without an unhandled exception

### Requirement: Application exposes first-slice game states
The system SHALL support `MENU`, `PLAYING`, `PAUSED`, and `GAME_OVER` states for the first playable slice.

#### Scenario: Start from menu
- **WHEN** the player presses Enter or Space in `MENU`
- **THEN** the game starts in `PLAYING`

#### Scenario: Toggle pause
- **WHEN** the player presses Escape during `PLAYING`
- **THEN** the state becomes `PAUSED`
- **WHEN** the player presses Escape during `PAUSED`
- **THEN** the state becomes `PLAYING`

#### Scenario: Restart after game over
- **WHEN** the player presses Enter or Space in `GAME_OVER`
- **THEN** a fresh session starts in `PLAYING`
