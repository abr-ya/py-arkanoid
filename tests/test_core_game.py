from pathlib import Path

from arkanoid.core.game import BRICK_SCORE, SLOW_BALL_MULTIPLIER, create_session
from arkanoid.core.events import SoundEvent
from arkanoid.core.leaderboard import LeaderboardStore
from arkanoid.core.levels import (
    DEFAULT_BRICK_ROWS,
    DEFAULT_LEVEL_NAME,
    create_bricks_for_level,
    load_level,
)
from arkanoid.core.models import BonusItem, Brick, BrickType, PowerUpType, create_brick
from arkanoid.core.state import GameState, toggle_pause

SHIPPED_LEVEL_NUMBERS = (1, 2, 3, 4, 5)


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
    assert session.pull_sound_events() == [SoundEvent.COLLISION]

    session.ball.x = 100
    session.ball.y = session.ball.radius - 1
    session.ball.vx = 0
    session.ball.vy = -100
    session.update(0)

    assert session.ball.vy > 0
    assert session.pull_sound_events() == [SoundEvent.COLLISION]


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


def test_game_over_score_entry_saves_record_and_allows_restart(tmp_path) -> None:
    session = create_session(LeaderboardStore(tmp_path / "leaderboard.json"))
    session.start()
    session.score = 500
    session.lives = 1
    session.ball.attached = False
    session.ball.y = session.playfield.height + session.ball.radius + 1

    session.update(0)

    assert session.state is GameState.NAME_ENTRY
    session.enter_score_name_char("a")
    session.enter_score_name_char("b")
    session.enter_score_name_char("c")
    session.submit_score_name()

    assert session.state is GameState.GAME_OVER
    assert [(record.name, record.score) for record in session.leaderboard_records] == [("ABC", 500)]

    session.start()

    assert session.state is GameState.PLAYING
    assert session.score == 0
    assert [(record.name, record.score) for record in session.leaderboard_records] == [("ABC", 500)]


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


def test_level_symbols_can_configure_specific_power_up_bricks(tmp_path) -> None:
    levels_dir = tmp_path / "levels"
    levels_dir.mkdir()
    (levels_dir / "level_01.yaml").write_text(
        "\n".join(
            [
                "number: 1",
                'name: "Power Test"',
                "bricks:",
                "  rows:",
                '    - "WFMT"',
            ]
        ),
        encoding="utf-8",
    )

    level = load_level(levels_dir=levels_dir)
    bricks = create_bricks_for_level(level)

    assert [brick.bonus_marker for brick in bricks] == [
        PowerUpType.WIDE.value,
        PowerUpType.SLOW.value,
        PowerUpType.MULTI.value,
        PowerUpType.STICKY.value,
    ]


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
    assert len(session.bricks) == len(create_bricks_for_level(session.level))


def test_shipped_level_pack_loads_all_builtin_levels() -> None:
    levels_dir = Path("levels")
    level_files = sorted(levels_dir.glob("level_*.yaml"))

    assert len(level_files) == len(SHIPPED_LEVEL_NUMBERS)

    names: list[str] = []
    speed_multipliers: list[float] = []
    paddle_widths: list[float] = []

    for number in SHIPPED_LEVEL_NUMBERS:
        level = load_level(number, levels_dir=levels_dir)
        bricks = create_bricks_for_level(level)

        assert level.number == number
        assert level.bricks.rows != DEFAULT_BRICK_ROWS
        assert bricks
        assert any(brick.destructible for brick in bricks)
        names.append(level.name)
        speed_multipliers.append(level.ball_speed_multiplier)
        paddle_widths.append(level.paddle_width)

    assert len(set(names)) == len(SHIPPED_LEVEL_NUMBERS)
    assert speed_multipliers == sorted(speed_multipliers)
    assert paddle_widths[0] > paddle_widths[-1]


def test_shipped_level_progression_loads_next_level_sequence() -> None:
    session = create_session()

    for number, next_number in zip(SHIPPED_LEVEL_NUMBERS, SHIPPED_LEVEL_NUMBERS[1:]):
        session.level = load_level(number)
        session.state = GameState.LEVEL_CLEAR
        session.level_clear_timer = 0

        session.update(0)

        expected_next = load_level(next_number)
        assert session.state is GameState.PLAYING
        assert session.level.number == expected_next.number
        assert session.level.name == expected_next.name
        assert session.paddle.width == expected_next.paddle_width
        assert session.bricks


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

    assert brick.bonus_marker == PowerUpType.WIDE.value
    assert brick.hit()


def test_bonus_marker_brick_spawns_falling_bonus_item() -> None:
    session = create_session()
    session.start()
    bonus_brick = create_brick(x=100, y=100, type=BrickType.BONUS_MARKER)
    spare_brick = create_brick(x=300, y=100)
    session.bricks = [bonus_brick, spare_brick]
    session.ball.attached = False
    session.ball.x = 110
    session.ball.y = 110
    session.ball.vx = 0
    session.ball.vy = -200

    session.update(0)

    assert bonus_brick not in session.bricks
    assert len(session.bonus_items) == 1
    assert session.bonus_items[0].type is PowerUpType.WIDE


def test_missed_bonus_item_is_removed_without_effect() -> None:
    session = create_session()
    session.start()
    session.bonus_items = [
        BonusItem(
            x=session.paddle.x,
            y=session.playfield.height + 1,
            type=PowerUpType.WIDE,
        )
    ]

    session.update(0)

    assert session.bonus_items == []
    assert PowerUpType.WIDE not in session.active_effects


def test_catching_wide_bonus_increases_paddle_width_and_expires() -> None:
    session = create_session()
    session.start()
    base_width = session.paddle.width
    session.bonus_items = [BonusItem(x=session.paddle.x, y=session.paddle.y, type=PowerUpType.WIDE)]

    session.update(0)

    assert session.bonus_items == []
    assert session.paddle.width == base_width * 1.5

    session.update(10.1)

    assert session.paddle.width == base_width
    assert PowerUpType.WIDE not in session.active_effects


def test_slow_bonus_scales_active_ball_and_expires_independently() -> None:
    session = create_session()
    session.start()
    session.launch_ball()
    original_vx = session.ball.vx
    original_vy = session.ball.vy
    session._activate_power_up(PowerUpType.SLOW)
    session._activate_power_up(PowerUpType.WIDE)

    assert session.ball.vx == original_vx * SLOW_BALL_MULTIPLIER
    assert session.ball.vy == original_vy * SLOW_BALL_MULTIPLIER
    assert PowerUpType.SLOW in session.active_effects
    assert PowerUpType.WIDE in session.active_effects

    session._update_active_effects(8.1)

    assert round(session.ball.vx, 6) == original_vx
    assert round(session.ball.vy, 6) == original_vy
    assert PowerUpType.SLOW not in session.active_effects
    assert PowerUpType.WIDE in session.active_effects


def test_recatching_timed_effect_refreshes_without_compounding() -> None:
    session = create_session()
    session.start()
    base_width = session.paddle.width

    session._activate_power_up(PowerUpType.WIDE)
    session.update(4)
    session._activate_power_up(PowerUpType.WIDE)

    assert session.paddle.width == base_width * 1.5
    assert session.active_effects[PowerUpType.WIDE].remaining == 10


def test_multi_bonus_adds_ball_and_only_final_ball_loses_life() -> None:
    session = create_session()
    session.start()
    session.launch_ball()
    session._activate_power_up(PowerUpType.MULTI)

    assert len(session.balls) == 2

    first_ball = session.balls[0]
    first_ball.y = session.playfield.height + first_ball.radius + 1
    session.update(0)

    assert len(session.balls) == 1
    assert session.lives == 3
    assert session.state is GameState.PLAYING

    final_ball = session.balls[0]
    final_ball.y = session.playfield.height + final_ball.radius + 1
    session.update(0)

    assert session.lives == 2
    assert len(session.balls) == 1
    assert session.ball.attached


def test_sticky_bonus_catches_next_ball_until_launch() -> None:
    session = create_session()
    session.start()
    session._activate_power_up(PowerUpType.STICKY)
    session.ball.attached = False
    session.ball.x = session.paddle.center_x
    session.ball.y = session.paddle.y - 1
    session.ball.vx = 0
    session.ball.vy = 250

    session.update(0)

    assert session.ball.attached
    assert session.sticky_charges == 0

    session.launch_ball()

    assert not session.ball.attached


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
    assert session.pull_sound_events() == [
        SoundEvent.BRICK_BREAK,
        SoundEvent.LEVEL_COMPLETE,
    ]

    session.update(1)

    assert session.state is GameState.PLAYING
    assert session.level.number == 2
    assert session.score == BRICK_SCORE
    assert session.lives == 3
    assert session.bricks


def test_launch_ball_records_launch_sound_once() -> None:
    session = create_session()
    session.start()

    session.launch_ball()
    session.launch_ball()

    assert session.pull_sound_events() == [SoundEvent.LAUNCH]


def test_catching_bonus_records_power_up_pickup_sound() -> None:
    session = create_session()
    session.start()
    session.bonus_items = [BonusItem(x=session.paddle.x, y=session.paddle.y, type=PowerUpType.WIDE)]

    session.update(0)

    assert session.pull_sound_events() == [SoundEvent.POWER_UP_PICKUP]
