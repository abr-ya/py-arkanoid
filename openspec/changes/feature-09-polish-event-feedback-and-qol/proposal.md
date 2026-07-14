## Why

After readability and primary screen polish are handled, the game should provide clearer moment-to-moment feedback without changing its core rules. This change keeps event feedback and small quality-of-life tuning separate from the first readability pass.

## What Changes

- Add visible feedback for brick hits, score changes, life loss, level clear, and game over.
- Review play observations after the readability pass and level-pack work.
- Add small quality-of-life improvements only when they make play clearer or less frustrating.

## Capabilities

### New Capabilities

- `arkanoid-feedback-polish`: Event feedback and bounded QoL polish that preserves accepted gameplay behavior.

### Modified Capabilities

None.

## Impact

- May add short-lived visual effects or state markers.
- May tune presentation constants while preserving gameplay contracts.
- Should not add new mechanics, new level content, sound-system work, server work, or packaging work.
