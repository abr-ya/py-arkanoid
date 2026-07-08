## 1. Level Config

- [ ] 1.1 Define the initial level config schema and sample `levels/level_01.yaml`.
- [ ] 1.2 Implement a pure Python level loader with validation and default fallback.
- [ ] 1.3 Replace the hard-coded starter layout with loaded level data.

## 2. Brick Types

- [ ] 2.1 Add brick type definitions for normal, strong, bonus-marker, indestructible, and extra-life bricks.
- [ ] 2.2 Implement HP reduction, destruction rules, and visual state values.
- [ ] 2.3 Implement extra-life brick behavior.

## 3. Progression

- [ ] 3.1 Detect level clear when all destructible bricks are gone.
- [ ] 3.2 Add a `LEVEL_CLEAR` transition or equivalent timed transition state.
- [ ] 3.3 Load the next level while preserving score and lives.

## 4. Tests

- [ ] 4.1 Add tests for valid and invalid level configs.
- [ ] 4.2 Add tests for each brick type.
- [ ] 4.3 Add tests for level clear and next-level progression.
