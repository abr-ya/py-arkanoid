from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass(slots=True)
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def left(self) -> float:
        return self.x

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def top(self) -> float:
        return self.y

    @property
    def bottom(self) -> float:
        return self.y + self.height

    @property
    def center_x(self) -> float:
        return self.x + self.width / 2

    @property
    def center_y(self) -> float:
        return self.y + self.height / 2

    def overlaps(self, other: Rect) -> bool:
        return (
            self.left < other.right
            and self.right > other.left
            and self.top < other.bottom
            and self.bottom > other.top
        )


@dataclass(slots=True)
class Playfield:
    width: int = 800
    height: int = 600


@dataclass(slots=True)
class Paddle:
    x: float
    y: float
    width: float = 96
    height: float = 16
    speed: float = 420

    @property
    def rect(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)

    @property
    def center_x(self) -> float:
        return self.x + self.width / 2

    def move(self, direction: float, dt: float, playfield: Playfield) -> None:
        self.x += direction * self.speed * dt
        self.x = max(0, min(self.x, playfield.width - self.width))


@dataclass(slots=True)
class Ball:
    x: float
    y: float
    radius: float = 8
    vx: float = 0
    vy: float = 0
    attached: bool = True

    @property
    def rect(self) -> Rect:
        diameter = self.radius * 2
        return Rect(self.x - self.radius, self.y - self.radius, diameter, diameter)

    def attach_to(self, paddle: Paddle) -> None:
        self.x = paddle.center_x
        self.y = paddle.y - self.radius - 2
        self.vx = 0
        self.vy = 0
        self.attached = True

    def launch(self, speed_multiplier: float = 1.0) -> None:
        if self.attached:
            self.vx = 180 * speed_multiplier
            self.vy = -360 * speed_multiplier
            self.attached = False


class PowerUpType(Enum):
    WIDE = "wide"
    SLOW = "slow"
    MULTI = "multi"
    STICKY = "sticky"


@dataclass(slots=True)
class BonusItem:
    x: float
    y: float
    type: PowerUpType
    size: float = 18
    speed: float = 140

    @property
    def rect(self) -> Rect:
        return Rect(self.x, self.y, self.size, self.size)

    def move(self, dt: float) -> None:
        self.y += self.speed * dt


@dataclass(slots=True)
class ActiveEffect:
    type: PowerUpType
    remaining: float


@dataclass(slots=True)
class VisualFeedback:
    kind: str
    x: float
    y: float
    width: float
    height: float
    remaining: float
    duration: float
    label: str = ""

    @property
    def rect(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)

    @property
    def progress(self) -> float:
        if self.duration <= 0:
            return 1
        return max(0, min(1, self.remaining / self.duration))


class BrickType(Enum):
    NORMAL = "normal"
    STRONG = "strong"
    BONUS_MARKER = "bonus-marker"
    INDESTRUCTIBLE = "indestructible"
    EXTRA_LIFE = "extra-life"


@dataclass(frozen=True, slots=True)
class BrickTypeDefinition:
    type: BrickType
    hp: int
    score: int = 100
    destructible: bool = True
    grants_extra_life: bool = False
    bonus_marker: str | None = None
    visual_state: str = "normal"


BRICK_TYPES: dict[BrickType, BrickTypeDefinition] = {
    BrickType.NORMAL: BrickTypeDefinition(
        type=BrickType.NORMAL,
        hp=1,
        visual_state="normal",
    ),
    BrickType.STRONG: BrickTypeDefinition(
        type=BrickType.STRONG,
        hp=2,
        score=150,
        visual_state="strong",
    ),
    BrickType.BONUS_MARKER: BrickTypeDefinition(
        type=BrickType.BONUS_MARKER,
        hp=1,
        score=125,
        bonus_marker=PowerUpType.WIDE.value,
        visual_state="bonus",
    ),
    BrickType.INDESTRUCTIBLE: BrickTypeDefinition(
        type=BrickType.INDESTRUCTIBLE,
        hp=1,
        score=0,
        destructible=False,
        visual_state="indestructible",
    ),
    BrickType.EXTRA_LIFE: BrickTypeDefinition(
        type=BrickType.EXTRA_LIFE,
        hp=1,
        score=100,
        grants_extra_life=True,
        visual_state="extra-life",
    ),
}


@dataclass(slots=True)
class Brick:
    x: float
    y: float
    width: float = 64
    height: float = 22
    hp: int = 1
    type: BrickType = BrickType.NORMAL
    score: int = 100
    destructible: bool = True
    grants_extra_life: bool = False
    bonus_marker: str | None = None

    @property
    def rect(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)

    @property
    def visual_state(self) -> str:
        if self.type is BrickType.STRONG and self.hp == 1:
            return "strong-damaged"
        return BRICK_TYPES[self.type].visual_state

    def hit(self) -> bool:
        if not self.destructible:
            return False
        self.hp -= 1
        return self.hp <= 0


def create_brick(
    *,
    x: float,
    y: float,
    width: float = 64,
    height: float = 22,
    type: BrickType = BrickType.NORMAL,
    bonus_marker: str | None = None,
) -> Brick:
    definition = BRICK_TYPES[type]
    return Brick(
        x=x,
        y=y,
        width=width,
        height=height,
        hp=definition.hp,
        type=definition.type,
        score=definition.score,
        destructible=definition.destructible,
        grants_extra_life=definition.grants_extra_life,
        bonus_marker=bonus_marker or definition.bonus_marker,
    )
