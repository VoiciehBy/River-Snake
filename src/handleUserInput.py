import pygame
from objects import snake
from Game import Game

from Direction import Direction


def on_return_pressed():
    Game.start_game()


def on_p_key_pressed():
    Game.pause_game()


def on_escape_pressed():
    exit()


def on_left_pressed():
    snake.direction = Direction.LEFT


def on_right_pressed():
    snake.direction = Direction.RIGHT


def on_up_pressed():
    snake.direction = Direction.UP


def on_down_pressed():
    snake.direction = Direction.DOWN


def on_user_input_via_keyboard(event: pygame.event):
    event_key_id: int = event.key
    if event_key_id == pygame.K_RETURN:
        on_return_pressed()
    elif event_key_id == pygame.K_p:
        on_p_key_pressed()
    elif event_key_id == pygame.K_ESCAPE:
        on_escape_pressed()
    elif event_key_id == pygame.K_LEFT:
        on_left_pressed()
    elif event_key_id == pygame.K_RIGHT:
        on_right_pressed()
    elif event_key_id == pygame.K_UP:
        on_up_pressed()
    elif event_key_id == pygame.K_DOWN:
        on_down_pressed()
