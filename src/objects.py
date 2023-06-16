from Snake import Snake
from Board import Board
from constants import board_width, board_height

board: Board = Board(board_width, board_height)
snake: Snake = Snake(board.cells[0][0])
board.generate_food()
