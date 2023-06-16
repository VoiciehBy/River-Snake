from pygame import Surface, Rect
from constants import font_size, screen
from draw import drawText
from update import update
from handleEvents import handleEvents
from pygame_utils import clear_screen, wait
from Game import Game


def drawScreen(surface: Surface, lines):
    surface_rect = Rect(surface.get_rect())

    rect = Rect(10, 10, surface_rect.width - 20, surface_rect.height - 20)

    left = int(rect.width / 4)
    top = int(rect.height / 8)
    width = int(rect.width / 4)
    height = int(rect.height / 8)

    rect = Rect(left, top, width, height)
    n = len(lines)
    for i in range(n):
        r_rect = Rect(rect.left, rect.top + 2 * i *
                      font_size * 2, rect.width, rect.height)
        drawText(surface, lines[i], r_rect, font_size * 2)


def drawPausedScreen():
    drawScreen(screen, ["PAUSED"])
    update(screen.get_rect())

    handleEvents()
    clear_screen()


def drawEndScreen():
    clear_screen()
    drawScreen(screen, ["THE END"])
    update(screen.get_rect())


def drawResultScreen():
    points = str(Game.points) + ' ' + "POINTS"
    txt = ["YOU GAINED: ", points]

    clear_screen()
    drawScreen(screen, txt)
    update(screen.get_rect())


def drawEndingScreens():
    drawEndScreen()
    wait(2000)
    drawResultScreen()
    wait(2000)
