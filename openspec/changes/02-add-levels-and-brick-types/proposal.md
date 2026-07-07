## Why

After the first playable slice works, the game needs replay value and a cleaner content boundary. This change replaces the hard-coded starter layout with configured levels and adds brick variety.

## What Changes

- Add level loading from YAML or JSON files.
- Add level progression after all destructible bricks are cleared.
- Add normal, strong, bonus-marker, indestructible, and extra-life brick definitions.
- Add transition behavior between levels.
- Keep actual falling power-up effects deferred to `add-power-ups`.

## Capabilities

### New Capabilities

- `levels`: Config-based level loading, progression, clear detection, and transition screens.
- `brick-types`: Brick health, indestructible bricks, extra-life bricks, and type-based scoring hooks.

### Modified Capabilities

None.

## Impact

- Adds level config files under `levels/`.
- Adds a level loader dependency if YAML is selected.
- Extends core brick and session models from the first playable slice.
