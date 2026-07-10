# Py Arkanoid

First playable Arkanoid slice for the OpenSpec-driven implementation.

## Run

```bash
python -m arkanoid
```

## Levels

The first level is configured in `levels/level_01.yaml`. Brick row symbols use
`1`/`N` for normal, `2`/`S` for strong, `B` for bonus-marker, `X` for
indestructible, and `L` for extra-life bricks. Missing or invalid level files
fall back to a safe default layout.

## Test

```bash
pytest
```
