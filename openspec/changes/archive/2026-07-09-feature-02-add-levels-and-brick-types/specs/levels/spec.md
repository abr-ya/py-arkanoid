## ADDED Requirements

### Requirement: Levels load from config files
The system SHALL load levels from files under `levels/`, with each level defining metadata, brick layout, ball speed multiplier, and optional paddle width.

#### Scenario: Load valid level
- **WHEN** a valid level config is requested
- **THEN** the game creates the matching brick layout and level settings

#### Scenario: Load invalid level
- **WHEN** a level config is missing or invalid
- **THEN** the game falls back to a valid default level without crashing

### Requirement: Levels progress after clear
The system SHALL treat a level as cleared when all destructible bricks are destroyed.

#### Scenario: Clear level
- **WHEN** the last destructible brick is destroyed
- **THEN** the game starts a level-clear transition

#### Scenario: Indestructible bricks remain
- **WHEN** only indestructible bricks remain
- **THEN** the level is considered cleared

### Requirement: Score persists across levels
The system SHALL preserve the current score when advancing to the next level.

#### Scenario: Advance level
- **WHEN** the next level loads after a clear
- **THEN** the player's score is not reset
