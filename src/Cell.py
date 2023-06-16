from CellType import CellType
from constants import side, screen
from pygame import Rect, Color
from VSprite import VSprite


class Cell:
    def __init__(self, x: int, y: int, cell_type: CellType):
        self.width = side
        self.height = side
        self.x = x
        self.y = y
        self.cell_type = cell_type
        self.rect = Rect(side * self.x, side * self.y, side, side)
        self.cell_sprite = VSprite(Color("green"), self.rect, screen)

    def draw(self):
        self.rect = Rect(side * self.x, side * self.y, side, side)
        self.cell_sprite = VSprite(Color("green"), self.rect, screen)
        self.cell_sprite.draw()

    def set_type(self, cell_type: CellType):
        self.cell_type = cell_type

    def get_type(self) -> CellType:
        return self.cell_type

    def get_width(self) -> int:
        return int(self.width)

    def get_height(self) -> int:
        return int(self.height)

    def __str__(self) -> str:
        return str(self.cell_type)
