from pygame import DOUBLEBUF, SRCALPHA, Color, Rect
from pygame.display import set_mode

window_name = "River River Snake by VoiciehBy"

board_width = 10 * 2
board_height = 6 * 2
side = 64

window_width = side * board_width
window_height = side * board_height

windowShape = (window_width, window_height)
screen = set_mode(windowShape, flags=DOUBLEBUF | SRCALPHA)

clearColor = Color("yellow")

font_size = 16
d_font_size = font_size * 2
default_rect_border_radius = int(font_size/2)

points_counter_rect = Rect(window_width - 4 * d_font_size,
                           window_height - 2 * d_font_size, d_font_size, d_font_size)