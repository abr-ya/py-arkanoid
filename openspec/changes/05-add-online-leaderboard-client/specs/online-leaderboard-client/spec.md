## ADDED Requirements

### Requirement: Remote leaderboard is optional
The system SHALL support an optional remote leaderboard URL and SHALL continue using local records when no URL is configured.

#### Scenario: No remote URL
- **WHEN** no remote leaderboard URL is configured
- **THEN** the game uses local leaderboard behavior only

### Requirement: Client submits scores best-effort
The system SHALL attempt to submit scores to the configured remote server without blocking or crashing gameplay on failure.

#### Scenario: Submit succeeds
- **WHEN** the remote server accepts a score submission
- **THEN** the client records the success for diagnostics

#### Scenario: Submit fails
- **WHEN** the remote server times out or refuses the connection
- **THEN** the score remains saved locally
- **AND** gameplay continues without an unhandled exception

### Requirement: Client fetches top scores best-effort
The system SHALL fetch remote top scores when available and fall back to local top scores when the remote request fails.

#### Scenario: Fetch succeeds
- **WHEN** the remote server returns valid top-score data
- **THEN** the game can display the remote top-score list

#### Scenario: Fetch fails
- **WHEN** the remote server request fails or returns invalid data
- **THEN** the game displays local top scores
