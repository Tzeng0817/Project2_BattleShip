'''
Contains BoardWindow class and required additional Constants defining the cell sizes
'''

from functools import reduce
import arcade
from board import CellStatus
from player import Player


# This sets the WIDTH and HEIGHT of each grid location
CELL_WIDTH = 80
CELL_HEIGHT = 80

# This sets the margin between each cell
MARGIN = 5

OFFSET = 30

class BoardWindow(arcade.Window):
    '''
    Window for the main game phase (displaying boards and shooting shots)
    '''

    def __init__(self, width: int, height: int, title: str, player: Player, on_end, is_own_board: bool):
        '''
        Initialize Board Window

        :param: width (int): Width of window
        :param: height (int): Height of window
        :param: title (str): Title for Window
        :param: player (Player): Player data this board shows
        :param: on_end (Function): Function to call when a turn ends
        :param: is_own_board (Bool): Is this board owned by the player it refers to
        :return: None
        '''

        super().__init__(width, height, title)
        self.shape_list = None
        self.player = player
        self.on_end = on_end
        self.is_own_board = is_own_board
        self.width = width
        self.height = height

        arcade.set_background_color(arcade.color.BLACK)
        self.recreate_grid()

    def recreate_grid(self):
        '''
        Rebuild grid based on updated player data

        :returns: None
        '''

        self.shape_list = arcade.ShapeElementList()
        grid = self.player.board.get_board_view()[0]
        for row in range(8):
            for column in range(8):
                if grid[row][column] == CellStatus.EMPTY:
                    color = arcade.color.WHITE
                elif grid[row][column] == CellStatus.MISS:
                    color = arcade.color.GRAY
                elif grid[row][column] == CellStatus.HIT:
                    color = arcade.color.RED
                x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                current_rect = arcade.create_rectangle_filled(x + OFFSET, y, CELL_WIDTH, CELL_HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        """
        Renders the class to the screen
        """

        arcade.start_render()
        self.shape_list.draw()
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        numbers.reverse()
        for i in range(8):
            arcade.draw_text(letters[i], (i * 80) + 70, self.width - 20, arcade.color.WHITE)
            arcade.draw_text(numbers[i], 15, (i * 80) + 70, arcade.color.WHITE)
        if self.is_own_board:
            for row in range(8):
                for column in range(8):
                    # Flatmap the list of ship positions, since we don't care which ship has which cell
                    if (row, column) in reduce(list.__add__, self.player.board.get_board_view()[1]):
                        x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                        y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                        arcade.draw_text("X", x + (OFFSET / 2), y - (OFFSET / 2), arcade.color.BLACK, 32)


    def on_mouse_press(self, x, y, button, modifiers):
        """
        Handles user clicking on a grid cell
        """

        if self.is_own_board:
            return

        # Change the x/y screen coordinates to grid coordinates
        column = (x - OFFSET) // (CELL_WIDTH + MARGIN)
        row = (y) // (CELL_HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < 8 and column < 8:
            self.player.be_attacked(row, column)
        self.recreate_grid()
        self.on_end()
