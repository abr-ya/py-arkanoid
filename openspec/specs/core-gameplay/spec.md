# core-gameplay Specification

## Purpose
TBD - created by archiving change feature-01-build-first-playable-arkanoid. Update Purpose after archive.
## Requirements
### Requirement: Player controls a paddle
The system SHALL provide a horizontal paddle controlled by keyboard input and constrained to the playfield bounds.

#### Scenario: Move paddle left
- **WHEN** the player holds the left movement key
- **THEN** the paddle moves left without crossing the left playfield boundary

#### Scenario: Move paddle right
- **WHEN** the player holds the right movement key
- **THEN** the paddle moves right without crossing the right playfield boundary

### Requirement: Ball launches from the paddle
The system SHALL start each life with the ball attached to the paddle until the player launches it.

#### Scenario: Ball follows paddle before launch
- **WHEN** the ball is attached
- **THEN** the ball remains above the paddle and follows the paddle horizontally

#### Scenario: Launch ball
- **WHEN** the player presses Space during `PLAYING` while the ball is attached
- **THEN** the ball receives an upward velocity and begins moving independently

### Requirement: Simple bricks can be destroyed
The first playable slice SHALL include simple destructible bricks that are removed after one hit.

#### Scenario: Destroy simple brick
- **WHEN** the ball collides with a simple brick
- **THEN** the brick is removed from the playfield

### Requirement: Lives control game over
The system SHALL decrement lives when the ball crosses the bottom boundary and enter `GAME_OVER` when no lives remain.

#### Scenario: Lose one life
- **WHEN** the ball crosses the bottom boundary and at least one life remains afterwards
- **THEN** the ball resets to the paddle
- **AND** the game remains in `PLAYING`

#### Scenario: Lose final life
- **WHEN** the ball crosses the bottom boundary and no lives remain
- **THEN** the state becomes `GAME_OVER`

