from board_window import BoardWindow
from board import Board
import arcade

WIDTH = 80
HEIGHT = 80
MARGIN = 5
SCREEN_WIDTH = (WIDTH + MARGIN) * 8 + MARGIN + 30
SCREEN_HEIGHT = (HEIGHT + MARGIN) * 8 + MARGIN + 30

if __name__ == "__main__":
    your_board = Board()
    their_board = Board()
    your_board.attacked(0, 0)
    your_board.attacked(3, 3)
    BoardWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Your Board", your_board)
    BoardWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Their Board", their_board)
    arcade.run()

