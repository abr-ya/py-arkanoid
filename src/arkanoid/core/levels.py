from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from arkanoid import resources
from arkanoid.core.models import Brick, BrickType, PowerUpType, create_brick

DEFAULT_LEVEL_NUMBER = 1
DEFAULT_LEVEL_NAME = "Training Wall"
DEFAULT_BALL_SPEED_MULTIPLIER = 1.0
DEFAULT_PADDLE_WIDTH = 96.0
DEFAULT_BRICK_LEFT = 44.0
DEFAULT_BRICK_TOP = 72.0
DEFAULT_BRICK_WIDTH = 72.0
DEFAULT_BRICK_HEIGHT = 22.0
DEFAULT_BRICK_GAP = 8.0
DEFAULT_BRICK_ROWS = ("111111111", "111111111", "111111111", "111111111")
DEFAULT_BRICK_SYMBOLS = {
    "1": BrickType.NORMAL,
    "N": BrickType.NORMAL,
    "2": BrickType.STRONG,
    "S": BrickType.STRONG,
    "B": BrickType.BONUS_MARKER,
    "W": (BrickType.BONUS_MARKER, PowerUpType.WIDE),
    "F": (BrickType.BONUS_MARKER, PowerUpType.SLOW),
    "M": (BrickType.BONUS_MARKER, PowerUpType.MULTI),
    "T": (BrickType.BONUS_MARKER, PowerUpType.STICKY),
    "X": BrickType.INDESTRUCTIBLE,
    "L": BrickType.EXTRA_LIFE,
}


@dataclass(frozen=True, slots=True)
class BrickLayout:
    rows: tuple[str, ...]
    left: float = DEFAULT_BRICK_LEFT
    top: float = DEFAULT_BRICK_TOP
    width: float = DEFAULT_BRICK_WIDTH
    height: float = DEFAULT_BRICK_HEIGHT
    gap: float = DEFAULT_BRICK_GAP


@dataclass(frozen=True, slots=True)
class LevelConfig:
    number: int = DEFAULT_LEVEL_NUMBER
    name: str = DEFAULT_LEVEL_NAME
    ball_speed_multiplier: float = DEFAULT_BALL_SPEED_MULTIPLIER
    paddle_width: float = DEFAULT_PADDLE_WIDTH
    bricks: BrickLayout = field(default_factory=lambda: BrickLayout(rows=DEFAULT_BRICK_ROWS))


def default_level(level_number: int = DEFAULT_LEVEL_NUMBER) -> LevelConfig:
    return LevelConfig(number=level_number)


def default_levels_dir() -> Path:
    return resources.levels_dir()


def load_level(level_number: int = DEFAULT_LEVEL_NUMBER, levels_dir: Path | None = None) -> LevelConfig:
    path = (levels_dir or default_levels_dir()) / f"level_{level_number:02}.yaml"
    try:
        raw = _parse_level_yaml(path)
        return _level_from_mapping(raw)
    except (OSError, TypeError, ValueError):
        return default_level(level_number)


def create_bricks_for_level(level: LevelConfig) -> list[Brick]:
    bricks: list[Brick] = []
    for row_index, row in enumerate(level.bricks.rows):
        for column_index, cell in enumerate(row):
            if cell in {" ", ".", "0", "_"}:
                continue
            symbol = DEFAULT_BRICK_SYMBOLS.get(cell)
            if symbol is None:
                continue
            brick_type = symbol[0] if isinstance(symbol, tuple) else symbol
            bonus_marker = symbol[1].value if isinstance(symbol, tuple) else None
            bricks.append(
                create_brick(
                    x=level.bricks.left + column_index * (level.bricks.width + level.bricks.gap),
                    y=level.bricks.top + row_index * (level.bricks.height + level.bricks.gap),
                    width=level.bricks.width,
                    height=level.bricks.height,
                    type=brick_type,
                    bonus_marker=bonus_marker,
                )
            )
    return bricks


def _level_from_mapping(raw: dict[str, Any]) -> LevelConfig:
    bricks = raw.get("bricks")
    if not isinstance(bricks, dict):
        raise ValueError("level config requires bricks")

    rows = bricks.get("rows")
    if (
        not isinstance(rows, list)
        or not rows
        or not all(isinstance(row, str) and row for row in rows)
    ):
        raise ValueError("level config requires non-empty brick rows")

    layout = BrickLayout(
        rows=tuple(rows),
        left=_read_float(bricks, "left", DEFAULT_BRICK_LEFT),
        top=_read_float(bricks, "top", DEFAULT_BRICK_TOP),
        width=_read_positive_float(bricks, "width", DEFAULT_BRICK_WIDTH),
        height=_read_positive_float(bricks, "height", DEFAULT_BRICK_HEIGHT),
        gap=_read_float(bricks, "gap", DEFAULT_BRICK_GAP),
    )
    return LevelConfig(
        number=_read_int(raw, "number", DEFAULT_LEVEL_NUMBER),
        name=_read_str(raw, "name", DEFAULT_LEVEL_NAME),
        ball_speed_multiplier=_read_positive_float(
            raw,
            "ball_speed_multiplier",
            DEFAULT_BALL_SPEED_MULTIPLIER,
        ),
        paddle_width=_read_positive_float(raw, "paddle_width", DEFAULT_PADDLE_WIDTH),
        bricks=layout,
    )


def _parse_level_yaml(path: Path) -> dict[str, Any]:
    raw: dict[str, Any] = {}
    bricks: dict[str, Any] | None = None
    in_rows = False

    for line in path.read_text(encoding="utf-8").splitlines():
        content = line.split("#", 1)[0].rstrip()
        if not content.strip():
            continue

        stripped = content.strip()
        indent = len(content) - len(content.lstrip(" "))

        if indent == 0:
            in_rows = False
            if stripped == "bricks:":
                bricks = {}
                raw["bricks"] = bricks
                continue
            key, value = _split_scalar(stripped)
            raw[key] = _parse_scalar(value)
            continue

        if bricks is None or indent != 2:
            if not (in_rows and indent == 4 and stripped.startswith("- ")):
                raise ValueError("unsupported level config shape")

        if in_rows and indent == 4 and stripped.startswith("- "):
            rows = bricks.setdefault("rows", [])
            if not isinstance(rows, list):
                raise ValueError("brick rows must be a list")
            rows.append(_parse_scalar(stripped[2:]))
            continue

        key, value = _split_scalar(stripped)
        if key == "rows":
            if value:
                raise ValueError("brick rows must use list items")
            bricks[key] = []
            in_rows = True
            continue
        bricks[key] = _parse_scalar(value)

    return raw


def _split_scalar(line: str) -> tuple[str, str]:
    if ":" not in line:
        raise ValueError("expected key-value pair")
    key, value = line.split(":", 1)
    key = key.strip()
    if not key:
        raise ValueError("missing key")
    return key, value.strip()


def _parse_scalar(value: str) -> str | int | float:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def _read_str(raw: dict[str, Any], key: str, default: str) -> str:
    value = raw.get(key, default)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{key} must be a non-empty string")
    return value


def _read_int(raw: dict[str, Any], key: str, default: int) -> int:
    value = raw.get(key, default)
    if not isinstance(value, int):
        raise ValueError(f"{key} must be an integer")
    return value


def _read_float(raw: dict[str, Any], key: str, default: float) -> float:
    value = raw.get(key, default)
    if not isinstance(value, int | float):
        raise ValueError(f"{key} must be numeric")
    return float(value)


def _read_positive_float(raw: dict[str, Any], key: str, default: float) -> float:
    value = _read_float(raw, key, default)
    if value <= 0:
        raise ValueError(f"{key} must be positive")
    return value
