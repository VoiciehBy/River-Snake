from CellType import CellType
from constants import side, screen, clearColor
from pygame import Rect, Color
from VSprite import VSprite

from constants import snake_cell_image, food_image


class Cell:
    def __init__(self, x: int, y: int, cell_type: CellType):
        self.width = side
        self.height = side
        self.x = x
        self.y = y
        self.cell_type = cell_type
        self.rect = Rect(side * self.x, side * self.y, side, side)
        self.cell_sprite = VSprite(clearColor, self.rect, screen)

        if self.cell_type == CellType.SNAKE:
            self.cell_sprite.set_texture(snake_cell_image)
        elif self.cell_type == CellType.SNAKE_HEAD:
            self.cell_sprite.set_texture(snake_cell_image)
        elif self.cell_type == CellType.FOOD:
            self.cell_sprite.set_texture(food_image)

    def draw(self):
        self.cell_sprite = VSprite(clearColor, self.rect, screen)

        if self.cell_type == CellType.NONE:
            self.cell_sprite.set_color(clearColor)
        elif self.cell_type == CellType.SNAKE:
            self.cell_sprite.set_texture(snake_cell_image)
        elif self.cell_type == CellType.SNAKE_HEAD:
            self.cell_sprite.set_texture(snake_cell_image)
        elif self.cell_type == CellType.FOOD:
            self.cell_sprite.set_texture(food_image)

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
