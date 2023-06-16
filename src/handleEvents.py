import pygame
from handleUserInput import on_user_input_via_keyboard


def handleEvents():
    g_object = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            on_user_input_via_keyboard(event)
    return g_object
