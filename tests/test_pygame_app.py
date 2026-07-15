import pygame

from arkanoid.pygame_app import FOREGROUND, _render_fit


def test_render_fit_handles_tiny_width_without_hanging() -> None:
    pygame.font.init()
    font = pygame.font.Font(None, 30)

    rendered = _render_fit(font, "X" * 200, FOREGROUND, 20)

    assert rendered.get_width() > 0
