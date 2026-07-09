from arkanoid.core.game import BRICK_SCORE, create_session
from arkanoid.core.models import Brick
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
