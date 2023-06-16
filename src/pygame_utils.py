from pygame import Surface, Rect, mouse, transform, time
from constants import screen, clearColor


def clear_screen():
    screen.fill(clearColor)


def move_pygame_rect(rect: Rect, x: int, y: int) -> Rect:
    return rect.move(x, y)


def is_mouse_over_rect(g_object) -> bool:
    mouse_position = mouse.get_pos()
    rect_to_check = g_object.sprite_rect()
    result = rect_to_check.collidepoint(mouse_position)
    return result


def is_two_pygame_rect_intersects(a: Rect, b: Rect):
    return a.colliderect(b)


def flip_surface(surface: Surface, horizontally: bool, vertically: bool) -> Surface:
    return transform.flip(surface, horizontally, vertically)


def flip_surface_horizontally(surface: Surface) -> Surface:
    return flip_surface(surface, True, False)


def flip_surface_vertically(surface: Surface) -> Surface:
    return flip_surface(surface, False, True)


def wait(milliseconds: int):
    time.wait(milliseconds)


def start_pygame_clock():
    return time.Clock()
