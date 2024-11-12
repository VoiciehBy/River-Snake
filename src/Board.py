from Cell import Cell
from numpy import zeros

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
                self.cells[y][x].draw()

    def generate_food(self):
        y: int = generate_random_integer(1, self.height - 1)
        x: int = generate_random_integer(1, self.width - 1)
        while self.cells[y][x].get_type() == CellType.SNAKE:
            y: int = generate_random_integer(1, self.height - 1)
            x: int = generate_random_integer(1, self.width - 1)
        self.cells[y][x].set_type(CellType.FOOD)

    def reset(self, width, height):
        self.__init__(width, height)
