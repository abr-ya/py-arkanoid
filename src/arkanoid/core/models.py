from __future__ import annotations

from dataclasses import dataclass


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

    def launch(self) -> None:
        if self.attached:
            self.vx = 180
            self.vy = -360
            self.attached = False


@dataclass(slots=True)
class Brick:
    x: float
    y: float
    width: float = 64
    height: float = 22
    hp: int = 1

    @property
    def rect(self) -> Rect:
        return Rect(self.x, self.y, self.width, self.height)

    def hit(self) -> bool:
        self.hp -= 1
        return self.hp <= 0
