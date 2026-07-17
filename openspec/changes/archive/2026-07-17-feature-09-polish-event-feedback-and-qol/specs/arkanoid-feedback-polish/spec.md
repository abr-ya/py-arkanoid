## ADDED Requirements

### Requirement: Important events provide feedback
The application SHALL provide visible feedback for brick hits, score changes, life loss, level clear, and game over.

#### Scenario: Brick hit feedback
- **WHEN** the ball hits a brick
- **THEN** the player receives immediate visual feedback

#### Scenario: Life loss feedback
- **WHEN** the player loses a life
- **THEN** the player receives clear feedback before the next launch

#### Scenario: Score change feedback
- **WHEN** the score changes because of gameplay
- **THEN** the player can identify that the score changed without losing track of the ball

### Requirement: Feedback polish preserves gameplay contracts
Feedback polish SHALL preserve accepted gameplay, level progression, sound, leaderboard, and distribution behavior unless a separate change updates those contracts.

#### Scenario: Apply feedback adjustment
- **WHEN** a visual feedback adjustment is made
- **THEN** the established difficulty curve and local leaderboard flow remain valid
