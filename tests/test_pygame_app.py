import pygame

from arkanoid.core.game import create_session
from arkanoid.pygame_app import (
    FOREGROUND,
    _level_clear_summary,
    _level_progress_label,
    _render_fit,
)


def test_render_fit_handles_tiny_width_without_hanging() -> None:
    pygame.font.init()
    font = pygame.font.Font(None, 30)

    rendered = _render_fit(font, "X" * 200, FOREGROUND, 20)

    assert rendered.get_width() > 0


def test_level_progress_label_includes_total_level_count() -> None:
    session = create_session()
    session.level = session.level.__class__(number=3, name=session.level.name)
    session.total_levels = 5

    assert _level_progress_label(session) == "3/5"


def test_level_clear_summary_names_completed_level() -> None:
    session = create_session()
    session.level = session.level.__class__(number=2, name=session.level.name)
    session.total_levels = 5

    assert _level_clear_summary(session) == "Level 2/5 complete"
