## Context

Sound should improve feedback while preserving the testable core game. The implementation should keep audio optional and avoid letting mixer errors break gameplay.

## Goals / Non-Goals

**Goals:**

- Play short sounds for the main gameplay events.
- Allow later replacement of the baseline sound files.
- Keep tests independent from real audio hardware.
- Let the game continue silently when sound initialization fails.

**Non-Goals:**

- Music, advanced mixing, or volume UI.
- Final-quality sound design.
- Changing gameplay rules to fit audio timing.

## Decisions

### Sound boundary

Introduce a small sound boundary used by the Pygame app layer. Core gameplay can expose events or state transitions, but it should not import or depend on Pygame mixer directly.

### Baseline assets

Use short, lightweight placeholder effects that are easy to replace. Prefer repository-owned files over runtime synthesis once the final packaging path is known, because packaged builds need deterministic resources.

### Audio fallback

If mixer initialization or a specific sound file fails, log or record diagnostics and continue with a no-op sound implementation.

## Risks / Trade-offs

- [Risk] Audio can fail in CI or headless environments. -> Mitigation: make sound optional and test dispatch with fakes.
- [Risk] Placeholder sounds may feel rough. -> Mitigation: keep filenames and event mapping stable so assets can be upgraded later.
- [Risk] Sound event wiring can leak into core logic. -> Mitigation: keep mixer calls in the presentation layer or a dedicated adapter.
