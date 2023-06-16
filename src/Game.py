from enum import Enum


class State(Enum):
    PLAYING = "Playing",
    PAUSED = "Paused",

    END = "End"


class Game:
    currentState = State.PAUSED
    result = False
    points = 0

    @staticmethod
    def start_game():
        if Game.currentState == State.PAUSED:
            Game.currentState = State.PLAYING

    @staticmethod
    def pause_game():
        if Game.currentState == State.PLAYING:
            Game.currentState = State.PAUSED

    @staticmethod
    def add_point():
        Game.points += 1

    @staticmethod
    def end_game(was_ai_victorious=False):
        if Game.currentState in [State.PLAYING]:
            Game.currentState = State.END
            Game.result = was_ai_victorious

    @staticmethod
    def is_game_paused() -> bool:
        return Game.currentState == State.PAUSED

    @staticmethod
    def is_game_not_paused() -> bool:
        return Game.currentState != State.PAUSED

    @staticmethod
    def is_game_playing() -> bool:
        return Game.currentState == State.PLAYING

    @staticmethod
    def is_it_the_end() -> bool:
        return Game.currentState == State.END

    @staticmethod
    def get_current_state() -> str:
        if Game.currentState == State.PLAYING:
            return "Playing"
        elif Game.currentState == State.PAUSED:
            return "Paused"
        elif Game.currentState == State.END:
            return "End"
        else:
            return "NoState"
