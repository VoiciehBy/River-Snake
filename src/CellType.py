from enum import Enum


class CellType(Enum):
    NONE = 1,
    SNAKE = 2,
    SNAKE_HEAD = 4,
    FOOD = 3
