## Purpose

Defines typed brick behavior, durability, and brick-specific rewards.

## Requirements

### Requirement: Bricks have typed durability
The system SHALL support brick types with explicit durability and destruction behavior.

#### Scenario: Normal brick
- **WHEN** a normal brick is hit once
- **THEN** it is destroyed

#### Scenario: Strong brick
- **WHEN** a strong brick is hit
- **THEN** its remaining durability decreases
- **AND** it is destroyed only after its durability reaches zero

#### Scenario: Indestructible brick
- **WHEN** an indestructible brick is hit
- **THEN** it remains in play
- **AND** it does not block level clear after all destructible bricks are gone

### Requirement: Extra-life bricks grant lives immediately
The system SHALL grant one life when an extra-life brick is destroyed.

#### Scenario: Destroy extra-life brick
- **WHEN** an extra-life brick is destroyed
- **THEN** the player's lives increase by one

### Requirement: Bonus-marker bricks expose future bonus hooks
The system SHALL allow a brick to be marked with a future power-up type without applying the power-up in this change.

#### Scenario: Destroy bonus-marker brick before power-ups exist
- **WHEN** a bonus-marker brick is destroyed
- **THEN** it is removed and scored like a bonus brick
- **AND** no falling power-up is spawned until the power-up feature is implemented
