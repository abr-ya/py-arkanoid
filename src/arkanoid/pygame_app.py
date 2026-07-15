from __future__ import annotations

from typing import Iterable

import pygame

from arkanoid.core.game import GameSession, create_session
from arkanoid.core.events import SoundEvent
from arkanoid.core.models import PowerUpType
from arkanoid.core.state import GameState
from arkanoid.sound import PygameSoundService, SoundService

WIDTH = 800
HEIGHT = 600
FPS = 60

BACKGROUND = (12, 15, 24)
SURFACE = (26, 32, 45)
SURFACE_LIGHT = (40, 48, 65)
FOREGROUND = (244, 247, 252)
MUTED = (177, 187, 202)
ACCENT = (116, 214, 146)
WARNING = (255, 216, 102)
PADDLE = (84, 190, 255)
BALL = (255, 231, 135)
BONUS_COLORS = {
    PowerUpType.WIDE: (84, 190, 255),
    PowerUpType.SLOW: (178, 132, 255),
    PowerUpType.MULTI: (255, 216, 102),
    PowerUpType.STICKY: (116, 214, 146),
}
BRICK_COLORS = [(248, 88, 108), (255, 174, 82), (84, 190, 255), (178, 132, 255)]
BRICK_STATE_COLORS = {
    "normal": (248, 88, 108),
    "strong": (255, 174, 82),
    "strong-damaged": (255, 216, 102),
    "bonus": (178, 132, 255),
    "indestructible": (132, 145, 162),
    "extra-life": (116, 214, 146),
}
HUD_HEIGHT = 76
TEXT_MARGIN = 36


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Py Arkanoid")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    title_font = pygame.font.Font(None, 56)
    session = create_session()
    sound_service = PygameSoundService.create()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                _handle_keydown(event, session)
                _dispatch_sound_events(session, sound_service)

        keys = pygame.key.get_pressed()
        direction = float(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - float(
            keys[pygame.K_LEFT] or keys[pygame.K_a]
        )
        session.update(dt, direction)
        _dispatch_sound_events(session, sound_service)

        if session.wants_quit:
            running = False

        _draw(screen, session, font, title_font)
        pygame.display.flip()

    pygame.quit()


def _handle_keydown(event: pygame.event.Event, session: GameSession) -> None:
    key = event.key
    if session.state is GameState.NAME_ENTRY:
        if key == pygame.K_BACKSPACE:
            session.delete_score_name_char()
        elif key == pygame.K_RETURN:
            session.submit_score_name()
        elif key == pygame.K_ESCAPE:
            session.request_quit()
        else:
            session.enter_score_name_char(getattr(event, "unicode", ""))
    elif key in {pygame.K_q}:
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


def _dispatch_sound_events(session: GameSession, sound_service: SoundService) -> None:
    for sound_event in session.pull_sound_events():
        sound_service.play(sound_event)


def _draw(
    screen: pygame.Surface,
    session: GameSession,
    font: pygame.font.Font,
    title_font: pygame.font.Font,
) -> None:
    screen.fill(BACKGROUND)

    if session.state is GameState.MENU:
        _draw_overlay_panel(screen, HEIGHT / 2 - 118, 236)
        _draw_centered_fit(screen, title_font, "PY ARKANOID", HEIGHT / 2 - 66, FOREGROUND)
        _draw_centered_fit(screen, font, "Break every brick. Keep the ball alive.", HEIGHT / 2 - 8, MUTED)
        _draw_centered_fit(screen, font, "Enter or Space to start", HEIGHT / 2 + 36, ACCENT)
        _draw_centered_fit(screen, font, "Move: A/D or arrows    Launch: Space", HEIGHT / 2 + 76, MUTED)
        return

    _draw_hud(screen, session, font)
    _draw_entities(screen, session)

    if session.state is GameState.PAUSED:
        _draw_overlay_panel(screen, HEIGHT / 2 - 84, 168)
        _draw_centered_fit(screen, title_font, "PAUSED", HEIGHT / 2 - 34, FOREGROUND)
        _draw_centered_fit(screen, font, "Esc to resume", HEIGHT / 2 + 18, ACCENT)
        _draw_centered_fit(screen, font, "Q to quit", HEIGHT / 2 + 54, MUTED)
    elif session.state is GameState.LEVEL_CLEAR:
        _draw_overlay_panel(screen, HEIGHT / 2 - 76, 152)
        _draw_centered_fit(screen, title_font, "LEVEL CLEAR", HEIGHT / 2 - 24, ACCENT)
        _draw_centered_fit(screen, font, "Next level loading", HEIGHT / 2 + 30, MUTED)
    elif session.state is GameState.NAME_ENTRY:
        _draw_overlay_panel(screen, HEIGHT / 2 - 132, 242)
        _draw_centered_fit(screen, title_font, "NEW SCORE", HEIGHT / 2 - 90, FOREGROUND)
        _draw_centered_fit(screen, font, f"Final score: {session.score}", HEIGHT / 2 - 38, MUTED)
        _draw_centered_fit(screen, font, f"Name: {session.score_name:<3}", HEIGHT / 2 + 6, ACCENT)
        _draw_centered_fit(screen, font, "Type 3 letters, then press Enter", HEIGHT / 2 + 48, MUTED)
    elif session.state is GameState.GAME_OVER:
        _draw_overlay_panel(screen, HEIGHT / 2 - 152, 286)
        _draw_centered_fit(screen, title_font, "GAME OVER", HEIGHT / 2 - 104, FOREGROUND)
        _draw_centered_fit(screen, font, f"Final score: {session.score}", HEIGHT / 2 - 50, MUTED)
        _draw_leaderboard(screen, session, font, HEIGHT / 2 - 12)
        _draw_centered_fit(screen, font, "Enter or Space to play again", HEIGHT - 72, ACCENT)
        _draw_centered_fit(screen, font, "Q to quit", HEIGHT - 42, MUTED)


def _draw_hud(screen: pygame.Surface, session: GameSession, font: pygame.font.Font) -> None:
    pygame.draw.rect(screen, SURFACE, pygame.Rect(0, 0, WIDTH, HUD_HEIGHT))
    pygame.draw.line(screen, SURFACE_LIGHT, (0, HUD_HEIGHT), (WIDTH, HUD_HEIGHT), 2)

    label = _render_fit(
        font,
        f"Score {session.score}    Lives {session.lives}    Level {_level_progress_label(session)}",
        FOREGROUND,
        WIDTH // 2 - TEXT_MARGIN,
    )
    screen.blit(label, (18, 16))

    hint = _render_fit(font, "A/D or arrows move    Space launch    Esc pause", MUTED, WIDTH // 2 - TEXT_MARGIN)
    screen.blit(hint, (WIDTH - hint.get_width() - 18, 16))

    effect_labels = [
        f"{effect.type.value.upper()} {max(0, effect.remaining):.0f}s"
        for effect in session.active_effects.values()
    ]
    if session.sticky_charges:
        effect_labels.append(f"STICKY x{session.sticky_charges}")
    if effect_labels:
        effects = _render_fit(font, "  ".join(effect_labels), WARNING, WIDTH - TEXT_MARGIN * 2)
        screen.blit(effects, (18, 42))
    else:
        level_label = _render_fit(
            font,
            f"Level {_level_progress_label(session)}: {session.level.name}",
            MUTED,
            WIDTH // 2 - TEXT_MARGIN,
        )
        screen.blit(level_label, (18, 42))

    if any(ball.attached for ball in session.balls):
        launch_hint = _render_fit(font, "Space to launch", ACCENT, WIDTH // 2 - TEXT_MARGIN)
        screen.blit(launch_hint, (WIDTH - launch_hint.get_width() - 18, 42))


def _draw_entities(screen: pygame.Surface, session: GameSession) -> None:
    pygame.draw.rect(screen, PADDLE, _to_pygame_rect(session.paddle.rect), border_radius=4)
    for ball in session.balls:
        pygame.draw.circle(
            screen,
            BALL,
            (round(ball.x), round(ball.y)),
            round(ball.radius),
        )
        pygame.draw.circle(
            screen,
            FOREGROUND,
            (round(ball.x), round(ball.y)),
            round(ball.radius),
            width=1,
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
        pygame.draw.rect(
            screen,
            BACKGROUND,
            _to_pygame_rect(brick.rect),
            width=1,
            border_radius=3,
        )


def _level_progress_label(session: GameSession) -> str:
    if session.total_levels <= 0:
        return str(session.level.number)
    return f"{session.level.number}/{session.total_levels}"


def _draw_leaderboard(
    screen: pygame.Surface,
    session: GameSession,
    font: pygame.font.Font,
    start_y: float,
) -> None:
    _draw_centered_fit(screen, font, "TOP SCORES", start_y, FOREGROUND)
    if not session.leaderboard_records:
        _draw_centered_fit(screen, font, "No records yet", start_y + 28, MUTED)
        return
    for index, record in enumerate(session.leaderboard_records[:5], start=1):
        label = f"{index}. {record.name} {record.score}"
        _draw_centered_fit(screen, font, label, start_y + index * 28, MUTED)


def _draw_overlay_panel(screen: pygame.Surface, y: float, height: float) -> None:
    panel = pygame.Rect(96, round(y), WIDTH - 192, round(height))
    pygame.draw.rect(screen, SURFACE, panel, border_radius=10)
    pygame.draw.rect(screen, SURFACE_LIGHT, panel, width=2, border_radius=10)


def _draw_centered_fit(
    screen: pygame.Surface,
    font: pygame.font.Font,
    text: str,
    y: float,
    color: tuple[int, int, int],
    max_width: int = WIDTH - TEXT_MARGIN * 2,
) -> None:
    rendered = _render_fit(font, text, color, max_width)
    rect = rendered.get_rect(center=(WIDTH / 2, y))
    screen.blit(rendered, rect)


def _render_fit(
    font: pygame.font.Font,
    text: str,
    color: tuple[int, int, int],
    max_width: int,
) -> pygame.Surface:
    rendered = font.render(text, True, color)
    if rendered.get_width() <= max_width:
        return rendered

    for end in range(len(text) - 1, 0, -1):
        shortened = text[:end].rstrip() + "..."
        rendered = font.render(shortened, True, color)
        if rendered.get_width() <= max_width:
            return rendered
    return font.render("...", True, color)


def _to_pygame_rect(rect: object) -> pygame.Rect:
    return pygame.Rect(
        round(getattr(rect, "x")),
        round(getattr(rect, "y")),
        round(getattr(rect, "width")),
        round(getattr(rect, "height")),
    )
