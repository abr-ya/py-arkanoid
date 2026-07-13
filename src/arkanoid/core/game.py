from __future__ import annotations

from dataclasses import dataclass, field

from arkanoid.core.events import SoundEvent
from arkanoid.core.leaderboard import LeaderboardRecord, LeaderboardStore
from arkanoid.core.levels import LevelConfig, create_bricks_for_level, load_level
from arkanoid.core.models import (
    ActiveEffect,
    Ball,
    BonusItem,
    Brick,
    Paddle,
    Playfield,
    PowerUpType,
    Rect,
)
from arkanoid.core.state import GameState, toggle_pause

BRICK_SCORE = 100
LEVEL_CLEAR_SECONDS = 0.8
WIDE_DURATION_SECONDS = 10.0
SLOW_DURATION_SECONDS = 8.0
WIDE_PADDLE_MULTIPLIER = 1.5
SLOW_BALL_MULTIPLIER = 0.7


def create_starter_bricks() -> list[Brick]:
    return create_bricks_for_level(load_level())


@dataclass(slots=True)
class GameSession:
    playfield: Playfield = field(default_factory=Playfield)
    state: GameState = GameState.MENU
    level: LevelConfig = field(default_factory=load_level)
    paddle: Paddle = field(init=False)
    balls: list[Ball] = field(init=False)
    bricks: list[Brick] = field(init=False)
    leaderboard_store: LeaderboardStore = field(default_factory=LeaderboardStore)
    leaderboard_records: list[LeaderboardRecord] = field(default_factory=list)
    bonus_items: list[BonusItem] = field(default_factory=list)
    active_effects: dict[PowerUpType, ActiveEffect] = field(default_factory=dict)
    sticky_charges: int = 0
    lives: int = 3
    score: int = 0
    score_name: str = ""
    level_clear_timer: float = 0
    wants_quit: bool = False
    sound_events: list[SoundEvent] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.leaderboard_records:
            self.leaderboard_records = self.leaderboard_store.load_records()
        self.paddle = Paddle(
            x=(self.playfield.width - self.level.paddle_width) / 2,
            y=self.playfield.height - 56,
            width=self.level.paddle_width,
        )
        self.balls = [Ball(x=0, y=0)]
        self.bricks = create_bricks_for_level(self.level)
        self.reset_ball()

    @property
    def ball(self) -> Ball:
        return self.balls[0]

    @ball.setter
    def ball(self, value: Ball) -> None:
        self.balls = [value]

    def start(self) -> None:
        if self.state in {GameState.MENU, GameState.GAME_OVER}:
            fresh = create_session(leaderboard_store=self.leaderboard_store)
            self.playfield = fresh.playfield
            self.state = GameState.PLAYING
            self.level = fresh.level
            self.paddle = fresh.paddle
            self.balls = fresh.balls
            self.bricks = fresh.bricks
            self.leaderboard_records = fresh.leaderboard_records
            self.bonus_items = fresh.bonus_items
            self.active_effects = fresh.active_effects
            self.sticky_charges = fresh.sticky_charges
            self.lives = fresh.lives
            self.score = fresh.score
            self.score_name = ""
            self.level_clear_timer = 0
            self.wants_quit = False
            self.sound_events = []

    def restart(self) -> None:
        self.state = GameState.GAME_OVER
        self.start()

    def toggle_pause(self) -> None:
        self.state = toggle_pause(self.state)

    def request_quit(self) -> None:
        self.wants_quit = True

    def reset_ball(self) -> None:
        self.balls = [Ball(x=0, y=0)]
        self.ball.attach_to(self.paddle)

    def launch_ball(self) -> None:
        if self.state is GameState.PLAYING:
            launched = False
            for ball in self.balls:
                was_attached = ball.attached
                ball.launch(self._ball_speed_multiplier())
                launched = launched or (was_attached and not ball.attached)
            if launched:
                self._record_sound_event(SoundEvent.LAUNCH)

    def pull_sound_events(self) -> list[SoundEvent]:
        events = self.sound_events.copy()
        self.sound_events.clear()
        return events

    def enter_score_name_char(self, value: str) -> None:
        if self.state is not GameState.NAME_ENTRY or len(self.score_name) >= 3:
            return
        if len(value) != 1 or not value.isalnum():
            return
        self.score_name += value.upper()

    def delete_score_name_char(self) -> None:
        if self.state is GameState.NAME_ENTRY:
            self.score_name = self.score_name[:-1]

    def submit_score_name(self) -> None:
        if self.state is not GameState.NAME_ENTRY or len(self.score_name) != 3:
            return
        record = LeaderboardRecord.create(self.score_name, self.score)
        self.leaderboard_records = self.leaderboard_store.add_record(record)
        self.state = GameState.GAME_OVER

    def update(self, dt: float, paddle_direction: float = 0) -> None:
        if self.state is GameState.LEVEL_CLEAR:
            self._update_level_clear(dt)
            return

        if self.state is not GameState.PLAYING:
            return

        self._update_active_effects(dt)
        self.paddle.move(paddle_direction, dt, self.playfield)
        for ball in self.balls:
            if ball.attached:
                ball.attach_to(self.paddle)

        self._update_bonus_items(dt)

        moving_balls = [ball for ball in self.balls if not ball.attached]
        if not moving_balls:
            return

        for ball in list(moving_balls):
            ball.x += ball.vx * dt
            ball.y += ball.vy * dt

            self._handle_wall_collisions(ball)
            self._handle_paddle_collision(ball)
            self._handle_brick_collision(ball)
            self._handle_bottom_boundary(ball)

    def _handle_wall_collisions(self, ball: Ball) -> None:
        if ball.x - ball.radius <= 0 and ball.vx < 0:
            ball.x = ball.radius
            ball.vx = abs(ball.vx)
            self._record_sound_event(SoundEvent.COLLISION)
        elif ball.x + ball.radius >= self.playfield.width and ball.vx > 0:
            ball.x = self.playfield.width - ball.radius
            ball.vx = -abs(ball.vx)
            self._record_sound_event(SoundEvent.COLLISION)

        if ball.y - ball.radius <= 0 and ball.vy < 0:
            ball.y = ball.radius
            ball.vy = abs(ball.vy)
            self._record_sound_event(SoundEvent.COLLISION)

    def _handle_paddle_collision(self, ball: Ball) -> None:
        if ball.vy <= 0 or not ball.rect.overlaps(self.paddle.rect):
            return

        if self.sticky_charges > 0:
            self.sticky_charges -= 1
            ball.attach_to(self.paddle)
            self._record_sound_event(SoundEvent.COLLISION)
            return

        offset = (ball.x - self.paddle.center_x) / (self.paddle.width / 2)
        offset = max(-1, min(1, offset))
        speed_multiplier = self._ball_speed_multiplier()
        ball.y = self.paddle.y - ball.radius
        ball.vx = offset * 300 * speed_multiplier
        ball.vy = -360 * speed_multiplier
        self._record_sound_event(SoundEvent.COLLISION)

    def _handle_brick_collision(self, ball: Ball) -> None:
        ball_rect = ball.rect
        for brick in list(self.bricks):
            if not ball_rect.overlaps(brick.rect):
                continue

            self._reflect_from_rect(ball, brick.rect)
            if brick.hit():
                self.bricks.remove(brick)
                self.score += brick.score
                self._record_sound_event(SoundEvent.BRICK_BREAK)
                if brick.grants_extra_life:
                    self.lives += 1
                self._spawn_bonus_from_brick(brick)
                if self.is_level_cleared():
                    self._start_level_clear()
            else:
                self._record_sound_event(SoundEvent.COLLISION)
            break

    def is_level_cleared(self) -> bool:
        return all(not brick.destructible for brick in self.bricks)

    def _start_level_clear(self) -> None:
        self.state = GameState.LEVEL_CLEAR
        self.level_clear_timer = LEVEL_CLEAR_SECONDS
        self.balls = [self.ball]
        self.ball.attached = True
        self.bonus_items.clear()
        self._record_sound_event(SoundEvent.LEVEL_COMPLETE)

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
        self.bonus_items.clear()
        self.active_effects.clear()
        self.sticky_charges = 0
        self.reset_ball()
        self.level_clear_timer = 0
        self.state = GameState.PLAYING

    def _reflect_from_rect(self, ball: Ball, rect: Rect) -> None:
        dx_left = abs(ball.rect.right - rect.left)
        dx_right = abs(rect.right - ball.rect.left)
        dy_top = abs(ball.rect.bottom - rect.top)
        dy_bottom = abs(rect.bottom - ball.rect.top)
        smallest = min(dx_left, dx_right, dy_top, dy_bottom)

        if smallest in {dx_left, dx_right}:
            ball.vx *= -1
        else:
            ball.vy *= -1

    def _handle_bottom_boundary(self, ball: Ball) -> None:
        if ball.y - ball.radius <= self.playfield.height:
            return

        if len(self.balls) > 1:
            self.balls.remove(ball)
            return

        self.lives -= 1
        if self.lives <= 0:
            self.state = GameState.NAME_ENTRY if self.score > 0 else GameState.GAME_OVER
            self.score_name = ""
            ball.attached = True
        else:
            self.reset_ball()

    def _spawn_bonus_from_brick(self, brick: Brick) -> None:
        if brick.bonus_marker is None:
            return
        try:
            power_up_type = PowerUpType(brick.bonus_marker)
        except ValueError:
            return
        self.bonus_items.append(
            BonusItem(
                x=brick.rect.center_x - 9,
                y=brick.rect.center_y - 9,
                type=power_up_type,
            )
        )

    def _update_bonus_items(self, dt: float) -> None:
        for item in list(self.bonus_items):
            item.move(dt)
            if item.rect.overlaps(self.paddle.rect):
                self.bonus_items.remove(item)
                self._activate_power_up(item.type)
                self._record_sound_event(SoundEvent.POWER_UP_PICKUP)
            elif item.y > self.playfield.height:
                self.bonus_items.remove(item)

    def _activate_power_up(self, power_up_type: PowerUpType) -> None:
        if power_up_type is PowerUpType.WIDE:
            self.active_effects[power_up_type] = ActiveEffect(power_up_type, WIDE_DURATION_SECONDS)
            self._apply_paddle_width()
        elif power_up_type is PowerUpType.SLOW:
            if power_up_type not in self.active_effects:
                self._scale_active_ball_velocities(SLOW_BALL_MULTIPLIER)
            self.active_effects[power_up_type] = ActiveEffect(power_up_type, SLOW_DURATION_SECONDS)
        elif power_up_type is PowerUpType.MULTI:
            self._add_extra_ball()
        elif power_up_type is PowerUpType.STICKY:
            self.sticky_charges += 1

    def _update_active_effects(self, dt: float) -> None:
        expired: list[PowerUpType] = []
        for effect in self.active_effects.values():
            effect.remaining -= dt
            if effect.remaining <= 0:
                expired.append(effect.type)
        for effect_type in expired:
            del self.active_effects[effect_type]
        if PowerUpType.WIDE in expired:
            self._apply_paddle_width()
        if PowerUpType.SLOW in expired:
            self._scale_active_ball_velocities(1 / SLOW_BALL_MULTIPLIER)

    def _apply_paddle_width(self) -> None:
        center_x = self.paddle.center_x
        width = self.level.paddle_width
        if PowerUpType.WIDE in self.active_effects:
            width *= WIDE_PADDLE_MULTIPLIER
        self.paddle.width = width
        self.paddle.x = max(0, min(center_x - width / 2, self.playfield.width - width))

    def _ball_speed_multiplier(self) -> float:
        multiplier = self.level.ball_speed_multiplier
        if PowerUpType.SLOW in self.active_effects:
            multiplier *= SLOW_BALL_MULTIPLIER
        return multiplier

    def _scale_active_ball_velocities(self, multiplier: float) -> None:
        for ball in self.balls:
            if not ball.attached:
                ball.vx *= multiplier
                ball.vy *= multiplier

    def _add_extra_ball(self) -> None:
        source = next((ball for ball in self.balls if not ball.attached), self.ball)
        if source.attached:
            source.launch(self._ball_speed_multiplier())
        self.balls.append(
            Ball(
                x=source.x,
                y=source.y,
                radius=source.radius,
                vx=-source.vx or -180 * self._ball_speed_multiplier(),
                vy=source.vy or -360 * self._ball_speed_multiplier(),
                attached=False,
            )
        )

    def _record_sound_event(self, event: SoundEvent) -> None:
        self.sound_events.append(event)


def create_session(leaderboard_store: LeaderboardStore | None = None) -> GameSession:
    if leaderboard_store is None:
        return GameSession()
    return GameSession(leaderboard_store=leaderboard_store)
