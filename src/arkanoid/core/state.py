from enum import Enum, auto


class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    LEVEL_CLEAR = auto()
    PAUSED = auto()
    NAME_ENTRY = auto()
    GAME_OVER = auto()


def start_from_menu(state: GameState) -> GameState:
    if state in {GameState.MENU, GameState.GAME_OVER}:
        return GameState.PLAYING
    return state


def toggle_pause(state: GameState) -> GameState:
    if state is GameState.PLAYING:
        return GameState.PAUSED
    if state is GameState.PAUSED:
        return GameState.PLAYING
    return state
