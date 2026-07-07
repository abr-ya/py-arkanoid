## ADDED Requirements

### Requirement: Records save to local JSON
The system SHALL store local leaderboard records in a JSON file containing a `records` array.

#### Scenario: Save record
- **WHEN** a player submits a name and score after game over
- **THEN** the record is written to local leaderboard storage

#### Scenario: Missing records file
- **WHEN** no leaderboard file exists
- **THEN** the system treats the leaderboard as empty

#### Scenario: Corrupted records file
- **WHEN** the leaderboard file cannot be parsed
- **THEN** the system continues with an empty leaderboard without crashing

### Requirement: Top records are sorted
The system SHALL sort records by score in descending order and display at most 10 records.

#### Scenario: More than ten records
- **WHEN** more than 10 records exist
- **THEN** only the 10 highest scores are displayed

### Requirement: Player enters a short name
The system SHALL let the player enter a three-character name for a non-zero score after game over.

#### Scenario: Submit name
- **WHEN** the player confirms a three-character name
- **THEN** the score is saved with that name
