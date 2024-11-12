from pygame import Surface, Rect
from constants import font_size, screen
from draw import drawText
from update import update
from handleEvents import handleEvents
from pygame_utils import clear_screen, wait
from Game import Game


def drawScreen(surface: Surface, lines):
    clear_screen()

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
    update(screen.get_rect())
    clear_screen()


def drawPausedScreen():
    drawScreen(screen, ["PAUSED"])


def drawEndScreen():
    drawScreen(screen, ["THE END"])


def drawResultScreen():
    points = str(Game.points) + ' ' + "POINTS"
    txt = ["YOU GAINED: ", points]
    drawScreen(screen, txt)


def drawContinueScreen():
    drawScreen(screen, ["START NEW GAME?", "YES - ENTER", "NO - ESC"])


def drawEndingScreens():
    drawEndScreen()
    wait(2000)
    drawResultScreen()
    wait(2000)


def drawNewGameScreen():
    drawContinueScreen()
