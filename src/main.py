from init import init
from pygame_utils import start_pygame_clock, clear_screen
from Game import Game
from drawScreen import drawPausedScreen, drawEndingScreens
from handleEvents import handleEvents
from objects import board, snake
from Cell import Cell
from Direction import Direction
from CellType import CellType
from constants import screen
from update import update
from draw import drawPointsCounter

if __name__ == "__main__":
    init()
    clock = start_pygame_clock()

    while 1:
        if Game.is_it_the_end():
            drawEndingScreens()
            break

        elif Game.is_game_paused():
            drawPausedScreen()

        elif Game.is_game_playing():
            handleEvents()

            snake_head: Cell = snake.head
            x: int = snake_head.x
            y: int = snake_head.y

            cell: Cell = board.cells[y][x]
            if snake.direction == Direction.LEFT and x - 1 >= 0:
                cell: Cell = board.cells[y][x - 1]
            elif snake.direction == Direction.RIGHT and x + 1 <= board.width - 1:
                cell: Cell = board.cells[y][x + 1]
            elif snake.direction == Direction.UP and y - 1 >= 0:
                cell: Cell = board.cells[y - 1][x]
            elif snake.direction == Direction.DOWN and y + 1 <= board.height - 1:
                cell: Cell = board.cells[y + 1][x]

            if cell.get_type() == CellType.FOOD:
                snake.eat()
                Game.add_point()
                board.generate_food()

            b: bool = False
            for y in range(board.height):
                for x in range(board.width):
                    if board.cells[y][x].get_type() == CellType.FOOD:
                        b = True
                        break
            if b is False:
                board.generate_food()

            if snake.is_cell_was_lethal(cell):
                Game.end_game()

            snake.move(cell)

            update(screen.get_rect())
            clear_screen()
            board.draw()
            snake.draw()

        clock.tick(8)
        drawPointsCounter()
