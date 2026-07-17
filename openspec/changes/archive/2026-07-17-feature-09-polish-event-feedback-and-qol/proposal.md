## Why

After readability and primary screen polish are handled, the game should provide clearer moment-to-moment feedback without changing its core rules. This change keeps event and completion feedback separate from both the first readability pass and the later quality-of-life tuning slice.

## What Changes

- Add visible feedback for brick hits, score changes, life loss, level clear, and game over.
- Verify the feedback remains lightweight and does not obscure core play.
- Defer broader quality-of-life tuning to `feature-10-polish-bounded-qol`.

## Capabilities

### New Capabilities

- `arkanoid-feedback-polish`: Event and completion feedback that preserves accepted gameplay behavior.

### Modified Capabilities

None.

## Impact

- May add short-lived visual effects or state markers.
- May tune feedback presentation constants while preserving gameplay contracts.
- Should not add new mechanics, new level content, sound-system work, server work, or packaging work.
