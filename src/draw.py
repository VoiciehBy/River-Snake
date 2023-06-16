from constants import screen, points_counter_rect, default_rect_border_radius, font_size, d_font_size
from Game import Game
from pygame import Surface, Color, Rect, draw, font


def drawText(surface: Surface, text: str, rect: Rect, text_font_size=font_size):
    txt = font.Font(None, text_font_size)
    txt_surface = txt.render(text, False, (0, 0, 0))
    surface.blit(txt_surface, rect)


def drawFPSCounter(clock):
    drawText(screen, str(int(clock.get_fps())), screen.get_rect())


def drawPointsCounter():
    turn_str = "Points" + ": " + str(Game.points)
    drawText(screen, turn_str, points_counter_rect, d_font_size)


def drawPygameRect(surface: Surface, color: Color, rect: Rect, border_radius=default_rect_border_radius):
    draw.rect(surface, color, rect, border_radius=border_radius)


def drawImageOverRect(surface: Surface, image: Surface, rect: Rect):
    surface.blit(image, rect)
