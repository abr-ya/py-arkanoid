from arkanoid.core.game import BRICK_SCORE, create_session
from arkanoid.core.levels import (
    DEFAULT_BRICK_ROWS,
    DEFAULT_LEVEL_NAME,
    create_bricks_for_level,
    load_level,
)
from arkanoid.core.models import Brick, BrickType, create_brick
from arkanoid.core.state import GameState, toggle_pause


def test_state_transitions_start_pause_and_restart() -> None:
    session = create_session()

    assert session.state is GameState.MENU
    session.start()
    assert session.state is GameState.PLAYING
    session.toggle_pause()
    assert session.state is GameState.PAUSED
    session.toggle_pause()
    assert session.state is GameState.PLAYING

    session.state = GameState.GAME_OVER
    session.score = 500
    session.start()
    assert session.state is GameState.PLAYING
    assert session.score == 0


def test_toggle_pause_ignores_menu_and_game_over() -> None:
    assert toggle_pause(GameState.MENU) is GameState.MENU
    assert toggle_pause(GameState.GAME_OVER) is GameState.GAME_OVER


def test_wall_reflection() -> None:
    session = create_session()
    session.start()
    session.ball.attached = False
    session.ball.x = session.ball.radius - 1
    session.ball.y = 100
    session.ball.vx = -120
    session.ball.vy = -100

    session.update(0)

    assert session.ball.vx > 0

    session.ball.x = 100
    session.ball.y = session.ball.radius - 1
    session.ball.vx = 0
    session.ball.vy = -100
    session.update(0)

    assert session.ball.vy > 0


def test_paddle_reflection_uses_hit_offset() -> None:
    session = create_session()
    session.start()
    session.ball.attached = False
    session.ball.x = session.paddle.x + session.paddle.width - 4
    session.ball.y = session.paddle.y - 1
    session.ball.vx = 0
    session.ball.vy = 250

    session.update(0)

    assert session.ball.vy < 0
    assert session.ball.vx > 0


def test_brick_destroyed_once_and_score_increases() -> None:
    session = create_session()
    session.start()
    brick = Brick(x=100, y=100)
    second_brick = Brick(x=100, y=100)
    session.bricks = [brick, second_brick]
    session.ball.attached = False
    session.ball.x = 110
    session.ball.y = 110
    session.ball.vx = 0
    session.ball.vy = -200

    session.update(0)

    assert brick not in session.bricks
    assert second_brick in session.bricks
    assert session.score == BRICK_SCORE


def test_life_loss_resets_ball_and_final_life_sets_game_over() -> None:
    session = create_session()
    session.start()
    session.ball.attached = False
    session.ball.y = session.playfield.height + session.ball.radius + 1

    session.update(0)

    assert session.lives == 2
    assert session.state is GameState.PLAYING
    assert session.ball.attached

    session.lives = 1
    session.ball.attached = False
    session.ball.y = session.playfield.height + session.ball.radius + 1
    session.update(0)

    assert session.lives == 0
    assert session.state is GameState.GAME_OVER


def test_valid_level_config_loads_layout_and_settings(tmp_path) -> None:
    levels_dir = tmp_path / "levels"
    levels_dir.mkdir()
    (levels_dir / "level_01.yaml").write_text(
        "\n".join(
            [
                "number: 1",
                'name: "Tiny Test"',
                "ball_speed_multiplier: 1.25",
                "paddle_width: 120",
                "bricks:",
                "  left: 10",
                "  top: 20",
                "  width: 30",
                "  height: 12",
                "  gap: 2",
                "  rows:",
                '    - "101"',
                '    - "010"',
            ]
        ),
        encoding="utf-8",
    )

    level = load_level(levels_dir=levels_dir)
    bricks = create_bricks_for_level(level)

    assert level.name == "Tiny Test"
    assert level.ball_speed_multiplier == 1.25
    assert level.paddle_width == 120
    assert len(bricks) == 3
    assert bricks[0].x == 10
    assert bricks[0].y == 20
    assert bricks[1].x == 74
    assert bricks[2].x == 42
    assert bricks[2].y == 34


def test_invalid_or_missing_level_config_falls_back(tmp_path) -> None:
    missing = load_level(levels_dir=tmp_path)
    assert missing.name == DEFAULT_LEVEL_NAME
    assert missing.bricks.rows == DEFAULT_BRICK_ROWS

    levels_dir = tmp_path / "levels"
    levels_dir.mkdir()
    (levels_dir / "level_01.yaml").write_text(
        "\n".join(
            [
                "number: 1",
                'name: "Broken"',
                "bricks:",
                "  rows:",
            ]
        ),
        encoding="utf-8",
    )

    invalid = load_level(levels_dir=levels_dir)
    assert invalid.name == DEFAULT_LEVEL_NAME


def test_session_uses_loaded_level_layout() -> None:
    session = create_session()

    assert session.level.name == DEFAULT_LEVEL_NAME
    assert session.paddle.width == session.level.paddle_width
    assert len(session.bricks) == len(DEFAULT_BRICK_ROWS) * len(DEFAULT_BRICK_ROWS[0])


def test_strong_brick_requires_two_hits() -> None:
    brick = create_brick(x=0, y=0, type=BrickType.STRONG)

    assert not brick.hit()
    assert brick.hp == 1
    assert brick.visual_state == "strong-damaged"
    assert brick.hit()


def test_indestructible_brick_survives_hits_and_does_not_block_clear() -> None:
    session = create_session()
    session.start()
    brick = create_brick(x=100, y=100, type=BrickType.INDESTRUCTIBLE)
    session.bricks = [brick]
    session.ball.attached = False
    session.ball.x = 110
    session.ball.y = 110
    session.ball.vx = 0
    session.ball.vy = -200

    session.update(0)

    assert brick in session.bricks
    assert session.score == 0
    assert session.is_level_cleared()


def test_extra_life_brick_grants_life_when_destroyed() -> None:
    session = create_session()
    session.start()
    brick = create_brick(x=100, y=100, type=BrickType.EXTRA_LIFE)
    session.bricks = [brick]
    session.ball.attached = False
    session.ball.x = 110
    session.ball.y = 110
    session.ball.vx = 0
    session.ball.vy = -200

    session.update(0)

    assert brick not in session.bricks
    assert session.lives == 4


def test_bonus_marker_brick_scores_without_spawning_power_up() -> None:
    brick = create_brick(x=0, y=0, type=BrickType.BONUS_MARKER)

    assert brick.bonus_marker == "future-power-up"
    assert brick.hit()


def test_level_clear_starts_transition_and_next_level_preserves_score() -> None:
    session = create_session()
    session.start()
    brick = create_brick(x=100, y=100)
    session.bricks = [brick]
    session.ball.attached = False
    session.ball.x = 110
    session.ball.y = 110
    session.ball.vx = 0
    session.ball.vy = -200

    session.update(0)

    assert session.state is GameState.LEVEL_CLEAR
    assert session.score == BRICK_SCORE

    session.update(1)

    assert session.state is GameState.PLAYING
    assert session.level.number == 2
    assert session.score == BRICK_SCORE
    assert session.lives == 3
    assert session.bricks
