## ADDED Requirements

### Requirement: QoL changes are observation-driven
The application SHALL apply quality-of-life polish only when it is tied to an observed clarity, pacing, or frustration issue from play review.

#### Scenario: Review play observations
- **WHEN** quality-of-life work begins
- **THEN** the observed issue being addressed is identified before implementation

#### Scenario: Defer unobserved idea
- **WHEN** a proposed quality-of-life idea is not tied to an observed issue
- **THEN** it is deferred instead of being implemented in this slice

### Requirement: QoL changes preserve gameplay contracts
Quality-of-life polish SHALL preserve accepted gameplay, level progression, sound, leaderboard, and distribution behavior unless a separate change updates those contracts.

#### Scenario: Apply QoL adjustment
- **WHEN** a small quality-of-life adjustment is made
- **THEN** the established difficulty curve and local leaderboard flow remain valid

#### Scenario: Exclude larger work
- **WHEN** an observation suggests new mechanics, level content, online behavior, settings, packaging, or broad balance changes
- **THEN** that work is deferred to a separate change
