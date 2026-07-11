from __future__ import annotations

from typing import Iterable

import pygame

from arkanoid.core.game import GameSession, create_session
from arkanoid.core.models import PowerUpType
from arkanoid.core.state import GameState

WIDTH = 800
HEIGHT = 600
FPS = 60

BACKGROUND = (18, 20, 28)
FOREGROUND = (234, 238, 246)
MUTED = (144, 153, 166)
PADDLE = (76, 201, 240)
BALL = (255, 209, 102)
BONUS_COLORS = {
    PowerUpType.WIDE: (76, 201, 240),
    PowerUpType.SLOW: (118, 120, 237),
    PowerUpType.MULTI: (255, 209, 102),
    PowerUpType.STICKY: (6, 214, 160),
}
BRICK_COLORS = [(239, 71, 111), (255, 159, 67), (6, 214, 160), (118, 120, 237)]
BRICK_STATE_COLORS = {
    "normal": (239, 71, 111),
    "strong": (255, 159, 67),
    "strong-damaged": (255, 209, 102),
    "bonus": (118, 120, 237),
    "indestructible": (144, 153, 166),
    "extra-life": (6, 214, 160),
}


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Py Arkanoid")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    title_font = pygame.font.Font(None, 56)
    session = create_session()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                _handle_keydown(event.key, session)

        keys = pygame.key.get_pressed()
        direction = float(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - float(
            keys[pygame.K_LEFT] or keys[pygame.K_a]
        )
        session.update(dt, direction)

        if session.wants_quit:
            running = False

        _draw(screen, session, font, title_font)
        pygame.display.flip()

    pygame.quit()


def _handle_keydown(key: int, session: GameSession) -> None:
    if key in {pygame.K_q}:
        session.request_quit()
    elif key == pygame.K_ESCAPE:
        session.toggle_pause()
    elif key in {pygame.K_RETURN, pygame.K_SPACE} and session.state in {
        GameState.MENU,
        GameState.GAME_OVER,
    }:
        session.start()
    elif key == pygame.K_r and session.state is GameState.GAME_OVER:
        session.restart()
    elif key == pygame.K_SPACE and session.state is GameState.PLAYING:
        session.launch_ball()


def _draw(
    screen: pygame.Surface,
    session: GameSession,
    font: pygame.font.Font,
    title_font: pygame.font.Font,
) -> None:
    screen.fill(BACKGROUND)

    if session.state is GameState.MENU:
        _draw_centered(screen, title_font, "PY ARKANOID", HEIGHT / 2 - 40, FOREGROUND)
        _draw_centered(screen, font, "Press Enter or Space", HEIGHT / 2 + 18, MUTED)
        return

    _draw_hud(screen, session, font)
    _draw_entities(screen, session)

    if session.state is GameState.PAUSED:
        _draw_centered(screen, title_font, "PAUSED", HEIGHT / 2 - 16, FOREGROUND)
    elif session.state is GameState.LEVEL_CLEAR:
        _draw_centered(screen, title_font, "LEVEL CLEAR", HEIGHT / 2 - 16, FOREGROUND)
    elif session.state is GameState.GAME_OVER:
        _draw_centered(screen, title_font, "GAME OVER", HEIGHT / 2 - 42, FOREGROUND)
        _draw_centered(screen, font, f"Final score: {session.score}", HEIGHT / 2 + 12, MUTED)
        _draw_centered(screen, font, "Press Enter or Space", HEIGHT / 2 + 48, MUTED)


def _draw_hud(screen: pygame.Surface, session: GameSession, font: pygame.font.Font) -> None:
    label = font.render(f"Score: {session.score}    Lives: {session.lives}", True, FOREGROUND)
    screen.blit(label, (18, 16))
    effect_labels = [
        f"{effect.type.value.upper()} {max(0, effect.remaining):.0f}s"
        for effect in session.active_effects.values()
    ]
    if session.sticky_charges:
        effect_labels.append(f"STICKY x{session.sticky_charges}")
    if effect_labels:
        effects = font.render("  ".join(effect_labels), True, MUTED)
        screen.blit(effects, (18, 42))


def _draw_entities(screen: pygame.Surface, session: GameSession) -> None:
    pygame.draw.rect(screen, PADDLE, _to_pygame_rect(session.paddle.rect), border_radius=4)
    for ball in session.balls:
        pygame.draw.circle(
            screen,
            BALL,
            (round(ball.x), round(ball.y)),
            round(ball.radius),
        )
    for item in session.bonus_items:
        pygame.draw.rect(
            screen,
            BONUS_COLORS[item.type],
            _to_pygame_rect(item.rect),
            border_radius=6,
        )
    for index, brick in enumerate(session.bricks):
        pygame.draw.rect(
            screen,
            BRICK_STATE_COLORS.get(
                brick.visual_state,
                BRICK_COLORS[index // 9 % len(BRICK_COLORS)],
            ),
            _to_pygame_rect(brick.rect),
            border_radius=3,
        )


def _draw_centered(
    screen: pygame.Surface,
    font: pygame.font.Font,
    text: str,
    y: float,
    color: tuple[int, int, int],
) -> None:
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH / 2, y))
    screen.blit(rendered, rect)


def _to_pygame_rect(rect: object) -> pygame.Rect:
    return pygame.Rect(
        round(getattr(rect, "x")),
        round(getattr(rect, "y")),
        round(getattr(rect, "width")),
        round(getattr(rect, "height")),
    )
