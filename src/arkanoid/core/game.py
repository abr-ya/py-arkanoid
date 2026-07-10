from __future__ import annotations

from dataclasses import dataclass, field

from arkanoid.core.levels import LevelConfig, create_bricks_for_level, load_level
from arkanoid.core.models import Ball, Brick, Paddle, Playfield, Rect
from arkanoid.core.state import GameState, toggle_pause

BRICK_SCORE = 100
LEVEL_CLEAR_SECONDS = 0.8


def create_starter_bricks() -> list[Brick]:
    return create_bricks_for_level(load_level())


@dataclass(slots=True)
class GameSession:
    playfield: Playfield = field(default_factory=Playfield)
    state: GameState = GameState.MENU
    level: LevelConfig = field(default_factory=load_level)
    paddle: Paddle = field(init=False)
    ball: Ball = field(init=False)
    bricks: list[Brick] = field(init=False)
    lives: int = 3
    score: int = 0
    level_clear_timer: float = 0
    wants_quit: bool = False

    def __post_init__(self) -> None:
        self.paddle = Paddle(
            x=(self.playfield.width - self.level.paddle_width) / 2,
            y=self.playfield.height - 56,
            width=self.level.paddle_width,
        )
        self.ball = Ball(x=0, y=0)
        self.bricks = create_bricks_for_level(self.level)
        self.reset_ball()

    def start(self) -> None:
        if self.state in {GameState.MENU, GameState.GAME_OVER}:
            fresh = create_session()
            self.playfield = fresh.playfield
            self.state = GameState.PLAYING
            self.level = fresh.level
            self.paddle = fresh.paddle
            self.ball = fresh.ball
            self.bricks = fresh.bricks
            self.lives = fresh.lives
            self.score = fresh.score
            self.level_clear_timer = 0
            self.wants_quit = False

    def restart(self) -> None:
        self.state = GameState.GAME_OVER
        self.start()

    def toggle_pause(self) -> None:
        self.state = toggle_pause(self.state)

    def request_quit(self) -> None:
        self.wants_quit = True

    def reset_ball(self) -> None:
        self.ball.attach_to(self.paddle)

    def launch_ball(self) -> None:
        if self.state is GameState.PLAYING:
            self.ball.launch(self.level.ball_speed_multiplier)

    def update(self, dt: float, paddle_direction: float = 0) -> None:
        if self.state is GameState.LEVEL_CLEAR:
            self._update_level_clear(dt)
            return

        if self.state is not GameState.PLAYING:
            return

        self.paddle.move(paddle_direction, dt, self.playfield)
        if self.ball.attached:
            self.ball.attach_to(self.paddle)
            return

        self.ball.x += self.ball.vx * dt
        self.ball.y += self.ball.vy * dt

        self._handle_wall_collisions()
        self._handle_paddle_collision()
        self._handle_brick_collision()
        self._handle_bottom_boundary()

    def _handle_wall_collisions(self) -> None:
        if self.ball.x - self.ball.radius <= 0 and self.ball.vx < 0:
            self.ball.x = self.ball.radius
            self.ball.vx = abs(self.ball.vx)
        elif self.ball.x + self.ball.radius >= self.playfield.width and self.ball.vx > 0:
            self.ball.x = self.playfield.width - self.ball.radius
            self.ball.vx = -abs(self.ball.vx)

        if self.ball.y - self.ball.radius <= 0 and self.ball.vy < 0:
            self.ball.y = self.ball.radius
            self.ball.vy = abs(self.ball.vy)

    def _handle_paddle_collision(self) -> None:
        if self.ball.vy <= 0 or not self.ball.rect.overlaps(self.paddle.rect):
            return

        offset = (self.ball.x - self.paddle.center_x) / (self.paddle.width / 2)
        offset = max(-1, min(1, offset))
        self.ball.y = self.paddle.y - self.ball.radius
        self.ball.vx = offset * 300 * self.level.ball_speed_multiplier
        self.ball.vy = -360 * self.level.ball_speed_multiplier

    def _handle_brick_collision(self) -> None:
        ball_rect = self.ball.rect
        for brick in list(self.bricks):
            if not ball_rect.overlaps(brick.rect):
                continue

            self._reflect_from_rect(brick.rect)
            if brick.hit():
                self.bricks.remove(brick)
                self.score += brick.score
                if brick.grants_extra_life:
                    self.lives += 1
                if self.is_level_cleared():
                    self._start_level_clear()
            break

    def is_level_cleared(self) -> bool:
        return all(not brick.destructible for brick in self.bricks)

    def _start_level_clear(self) -> None:
        self.state = GameState.LEVEL_CLEAR
        self.level_clear_timer = LEVEL_CLEAR_SECONDS
        self.ball.attached = True

    def _update_level_clear(self, dt: float) -> None:
        self.level_clear_timer -= dt
        if self.level_clear_timer > 0:
            return
        self._load_next_level()

    def _load_next_level(self) -> None:
        next_level_number = self.level.number + 1
        self.level = load_level(next_level_number)
        self.paddle = Paddle(
            x=(self.playfield.width - self.level.paddle_width) / 2,
            y=self.playfield.height - 56,
            width=self.level.paddle_width,
        )
        self.bricks = create_bricks_for_level(self.level)
        self.reset_ball()
        self.level_clear_timer = 0
        self.state = GameState.PLAYING

    def _reflect_from_rect(self, rect: Rect) -> None:
        dx_left = abs(self.ball.rect.right - rect.left)
        dx_right = abs(rect.right - self.ball.rect.left)
        dy_top = abs(self.ball.rect.bottom - rect.top)
        dy_bottom = abs(rect.bottom - self.ball.rect.top)
        smallest = min(dx_left, dx_right, dy_top, dy_bottom)

        if smallest in {dx_left, dx_right}:
            self.ball.vx *= -1
        else:
            self.ball.vy *= -1

    def _handle_bottom_boundary(self) -> None:
        if self.ball.y - self.ball.radius <= self.playfield.height:
            return

        self.lives -= 1
        if self.lives <= 0:
            self.state = GameState.GAME_OVER
            self.ball.attached = True
        else:
            self.reset_ball()


def create_session() -> GameSession:
    return GameSession()
