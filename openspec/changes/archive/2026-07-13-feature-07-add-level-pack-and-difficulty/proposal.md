## Why

The game already supports configured levels, but it needs more content and a clearer difficulty curve before polish. A small level pack gives players more replay value and creates better playtest data for later tuning.

## What Changes

- Expand the shipped level set to at least 3 levels, with a target of 5 if the layouts remain focused.
- Define an intentional difficulty curve across level layouts, brick types, ball speed, and optional paddle settings.
- Keep level files editable and validated through the existing loader.
- Add tests or checks that the shipped level sequence can load and progress.

## Capabilities

### New Capabilities

- `level-pack`: Curated built-in level pack and difficulty progression.

### Modified Capabilities

None.

## Impact

- Adds or updates files under `levels/`.
- May tune level metadata such as speed multiplier or paddle width.
- May add tests for all shipped levels and progression order.
