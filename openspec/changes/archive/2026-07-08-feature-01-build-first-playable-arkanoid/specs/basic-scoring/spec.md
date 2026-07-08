## ADDED Requirements

### Requirement: Score increases when simple bricks are destroyed
The system SHALL add 100 points to the current score when a simple brick is destroyed.

#### Scenario: Destroy brick
- **WHEN** a simple brick is removed because of a ball hit
- **THEN** the current score increases by 100

### Requirement: HUD displays score and lives
The application SHALL display the current score and remaining lives during gameplay.

#### Scenario: Update HUD after scoring
- **WHEN** the score changes
- **THEN** the HUD reflects the new score on the next rendered frame

#### Scenario: Update HUD after life loss
- **WHEN** lives decrease
- **THEN** the HUD reflects the new lives count on the next rendered frame

### Requirement: Game over displays final score
The game-over screen SHALL show the final score for the ended session.

#### Scenario: Show final score
- **WHEN** the state becomes `GAME_OVER`
- **THEN** the game-over screen displays the final score
