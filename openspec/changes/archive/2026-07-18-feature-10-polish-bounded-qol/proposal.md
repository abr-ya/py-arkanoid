## Why

After event feedback is handled, the game needs a calm follow-up space for small comfort fixes discovered during play. Splitting this out keeps feedback polish focused while giving quality-of-life work a clear observation-driven boundary.

## What Changes

- Review play observations after the readability and feedback polish slices.
- Add only small quality-of-life adjustments tied to observed clarity, pacing, or frustration issues.
- Preserve accepted gameplay, level progression, sound, leaderboard, and distribution behavior.
- Defer larger controls, balance, content, online, packaging, or settings work to later changes.

## Capabilities

### New Capabilities

- `arkanoid-bounded-qol`: Observation-driven quality-of-life polish that preserves accepted gameplay behavior.

### Modified Capabilities

None.

## Impact

- May tune small presentation or interaction constants.
- May add narrow UI hints or state handling when backed by an observation.
- Should not add new mechanics, new level content, sound-system work, server work, online leaderboard work, or packaging work.
