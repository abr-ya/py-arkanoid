## ADDED Requirements

### Requirement: Gameplay screens are readable
The application SHALL present menu, gameplay, pause, level-clear, and game-over screens with readable text and clear visual hierarchy.

#### Scenario: View each screen
- **WHEN** each primary game screen is shown at the default window size
- **THEN** text is readable and does not overlap primary gameplay objects

### Requirement: Controls are discoverable
The application SHALL show concise controls guidance where it helps a new player start or resume play.

#### Scenario: Start from menu
- **WHEN** the main menu is shown
- **THEN** the player can see the primary controls needed to begin play

### Requirement: Polish preserves fair play
The polish pass SHALL preserve the accepted difficulty curve and SHALL keep early play approachable.

#### Scenario: Start first level
- **WHEN** a new session begins
- **THEN** the initial presentation and controls remain suitable for learning the game
