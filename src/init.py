import pygame
from constants import window_name


def init():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(window_name)
    pygame.event.set_allowed(
        [pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
