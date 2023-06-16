from Cell import Cell
from numpy import zeros
from pygame import Rect, Color
from constants import clearColor, screen
from draw import drawPygameRect

from CellType import CellType
from update import update
from utils import generate_random_integer


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = zeros((self.height, self.width), dtype=Cell)

        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x] = Cell(x, y, CellType.NONE)

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                cell_width, cell_height = self.cells[y][x].get_width(), self.cells[y][x].get_height()
                rect = Rect(x * cell_width, y * cell_height, cell_width, cell_height)
                color: Color = clearColor
                if self.cells[y][x].get_type() == CellType.SNAKE:
                    color = Color("green")
                elif self.cells[y][x].get_type() == CellType.FOOD:
                    color = Color("red")
                drawPygameRect(screen, color, rect)

    def generate_food(self):
        y: int = generate_random_integer(0, self.height - 1)
        x: int = generate_random_integer(0, self.width - 1)
        while self.cells[y][x].get_type() == CellType.SNAKE:
            y: int = generate_random_integer(0, self.height - 1)
            x: int = generate_random_integer(0, self.width - 1)
        self.cells[y][x].set_type(CellType.FOOD)
        update(self.cells[y][x].rect)
