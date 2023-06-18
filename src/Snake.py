from Cell import Cell
from CellType import CellType
from Direction import Direction


class Snake:
    def __init__(self, head: Cell):
        self.head = head
        self.head.cell_type = CellType.SNAKE
        self.segments = list([])
        self.segments.append(head)
        self.direction = Direction.RIGHT

    def update(self):
        for cell in self.segments:
            cell.set_type(CellType.SNAKE)

    def move(self, cell: Cell):
        self.update()
        tail: Cell = self.segments.pop()
        tail.cell_type = CellType.NONE
        self.head = cell
        self.head.set_type(CellType.SNAKE_HEAD)
        self.segments.insert(0, self.head)

    def eat(self):
        self.segments.append(self.head)

    def is_cell_was_lethal(self, cell: Cell) -> bool:
        for i in self.segments:
            if i == cell:
                return True
        return False
