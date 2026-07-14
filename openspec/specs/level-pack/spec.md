## Purpose

Define the curated built-in Arkanoid level pack and its difficulty progression.

## Requirements

### Requirement: Game ships with a multi-level pack
The application SHALL include at least 3 built-in playable levels and SHOULD include 5 levels when the added layouts are meaningfully distinct.

#### Scenario: Start built-in level sequence
- **WHEN** a new game starts with default content
- **THEN** the first built-in level loads successfully

#### Scenario: Load shipped levels
- **WHEN** each shipped level file is loaded
- **THEN** the loader accepts the level without falling back to the default level

### Requirement: Built-in levels define a difficulty curve
The shipped level sequence SHALL progress from approachable early play toward more challenging layouts.

#### Scenario: Compare early and later levels
- **WHEN** the built-in level sequence is reviewed
- **THEN** later levels use layout density, brick durability, obstacles, speed, or paddle settings to increase challenge

#### Scenario: First level remains approachable
- **WHEN** a new player starts level 1
- **THEN** the level uses forgiving settings suitable for learning the controls

### Requirement: Progression covers shipped levels
The game SHALL advance through the shipped level sequence without missing configured levels.

#### Scenario: Clear a shipped level
- **WHEN** a player clears a built-in level that has a following level
- **THEN** the game loads the next shipped level
