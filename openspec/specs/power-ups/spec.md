## Purpose

Define falling bonus items, activation behavior, active effect handling, and
effect expiration for Arkanoid power-ups.

## Requirements

### Requirement: Bonus items fall from eligible bricks
The system SHALL spawn a falling bonus item when a brick configured with a power-up is destroyed.

#### Scenario: Spawn bonus item
- **WHEN** a power-up brick is destroyed
- **THEN** a bonus item appears at the brick position and moves downward

#### Scenario: Miss bonus item
- **WHEN** a bonus item crosses the bottom boundary without touching the paddle
- **THEN** the bonus item is removed without applying an effect

### Requirement: Paddle catches bonus items
The system SHALL activate a bonus item when it collides with the paddle.

#### Scenario: Catch Wide
- **WHEN** the paddle catches a `wide` bonus
- **THEN** the paddle width increases by 50 percent for 10 seconds

#### Scenario: Catch Slow
- **WHEN** the paddle catches a `slow` bonus
- **THEN** active ball speed is reduced to 70 percent for 8 seconds

#### Scenario: Catch Multi
- **WHEN** the paddle catches a `multi` bonus
- **THEN** at least one additional active ball is added

#### Scenario: Catch Sticky
- **WHEN** the paddle catches a `sticky` bonus
- **THEN** the next caught ball attaches to the paddle until launched

### Requirement: Timed effects expire
The system SHALL track active timed effects and remove their gameplay changes after their duration expires.

#### Scenario: Wide expires
- **WHEN** 10 seconds pass after Wide activation
- **THEN** the paddle width returns to its base width

#### Scenario: Multiple effects
- **WHEN** multiple effects are active
- **THEN** each effect tracks and expires independently
