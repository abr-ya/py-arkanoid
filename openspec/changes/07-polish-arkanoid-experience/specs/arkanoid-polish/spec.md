## ADDED Requirements

### Requirement: Gameplay screens are readable
The application SHALL present menu, gameplay, pause, level-clear, and game-over screens with readable text and clear visual hierarchy.

#### Scenario: View each screen
- **WHEN** each primary game screen is shown at the default window size
- **THEN** text is readable and does not overlap primary gameplay objects

### Requirement: Important events provide feedback
The application SHALL provide visible feedback for brick hits, score changes, life loss, level clear, and game over.

#### Scenario: Brick hit feedback
- **WHEN** the ball hits a brick
- **THEN** the player receives immediate visual feedback

#### Scenario: Life loss feedback
- **WHEN** the player loses a life
- **THEN** the player receives clear feedback before the next launch

### Requirement: Tuning supports fair play
The default gameplay tuning SHALL allow a new player to reasonably keep the ball in play while still increasing challenge across levels.

#### Scenario: Start first level
- **WHEN** a new session begins
- **THEN** the initial speed and paddle width are suitable for learning the controls
