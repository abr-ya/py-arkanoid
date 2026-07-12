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

### Requirement: Polish preserves fair play
The polish pass SHALL preserve the accepted difficulty curve and SHALL keep early play approachable.

#### Scenario: Start first level
- **WHEN** a new session begins
- **THEN** the initial presentation and controls remain suitable for learning the game
