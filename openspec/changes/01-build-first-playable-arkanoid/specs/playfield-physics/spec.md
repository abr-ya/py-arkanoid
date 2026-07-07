## ADDED Requirements

### Requirement: Ball moves with seconds-based delta time
The core gameplay system SHALL update ball position using seconds-based `dt`.

#### Scenario: Advance ball position
- **WHEN** a ball has velocity `(vx, vy)` and the core update receives `dt` seconds
- **THEN** the ball position changes by `(vx * dt, vy * dt)`

### Requirement: Ball reflects from playfield walls
The ball SHALL reflect from the top, left, and right playfield boundaries.

#### Scenario: Reflect from top wall
- **WHEN** the ball touches the top boundary while moving upward
- **THEN** its vertical velocity becomes downward

#### Scenario: Reflect from side wall
- **WHEN** the ball touches a side boundary while moving toward that side
- **THEN** its horizontal velocity reverses away from the boundary

### Requirement: Paddle reflection depends on hit offset
The ball SHALL reflect upward from the paddle, with horizontal direction influenced by the hit position relative to the paddle center.

#### Scenario: Center paddle hit
- **WHEN** the ball hits near the center of the paddle
- **THEN** the reflected ball travels mostly upward

#### Scenario: Edge paddle hit
- **WHEN** the ball hits near a paddle edge
- **THEN** the reflected ball gains horizontal velocity toward that edge

### Requirement: Brick collision reflects the ball
The ball SHALL reflect after colliding with a brick and SHALL process only one brick collision per frame.

#### Scenario: Hit one brick
- **WHEN** the ball collides with a brick
- **THEN** the ball velocity reflects away from the collision side

#### Scenario: Touch multiple bricks
- **WHEN** the ball overlaps multiple bricks during one update
- **THEN** only one brick collision is applied for that update
