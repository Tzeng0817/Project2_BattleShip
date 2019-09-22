"""""
Need a player passed to me with number of player
"""""
import arcade
from board import Board
from ship import Ship, Direction
# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 8
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 80
HEIGHT = 80
# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5
# handles offset of screen to allow for space for text and axis
OFFSET_AXIS_LABEL = 30
OFFSET_BUTTON = 100
# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + OFFSET_AXIS_LABEL
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + OFFSET_AXIS_LABEL + OFFSET_BUTTON
SCREEN_TITLE = "BATTLESHIP"

class SHIP_LOCATION_SETUP(arcade.view):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Application constructor.
        """
        super().__init__(width, height, title)
        #initialized global variables
        self.board = Board()
        self.shape_list = None
        self.length_of_ship = 5
        self.selected = False
        self.row = 0
        self.column = 0
        self.direction = Direction.RIGHT
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell
        self.recreate_grid()

    def on_show(self):
        #set background color to black
        arcade.set_background_color(arcade.color.BLACK)

    def recreate_grid(self):
        """
        Redraws grid after event.
        """
        self.shape_list = arcade.ShapeElementList()
        #draws each grid box and assigns color based on 2Darray value
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                #if grid box is white 2Darray value will be 0
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE
                #if grid box is red 2Darray value will be 1
                else:
                    color = arcade.color.RED
                #calculates value of x and y coordinates from screen inputs
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                #updates current list values holding grid
                current_rect = arcade.create_rectangle_filled(x + OFFSET_AXIS_LABEL, y, WIDTH, HEIGHT, color)
                self.shape_list.append(current_rect)

    def on_draw(self):
        """
        Initial screen view.
        """
        arcade.start_render()
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        numbers.reverse()
        for i in range(8):
            arcade.draw_text(letters[i], (i * WIDTH) + 70, SCREEN_WIDTH - 20, arcade.color.WHITE)
            arcade.draw_text(numbers[i], OFFSET_AXIS_LABEL / 2, (i * HEIGHT) + 70, arcade.color.WHITE)
        self.shape_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Change the x/y screen coordinates to grid coordinates
        self.column = (x - OFFSET_AXIS_LABEL) // (WIDTH + MARGIN)
        self.row = y // (HEIGHT + MARGIN)
        row = self.row
        column = self.column
        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        # Make sure initial mouse press is on grid
        if row < ROW_COUNT and column < COLUMN_COUNT:
            i = 0
            #allows selection of location of ship to be horizontal
            if self.direction == Direction.RIGHT:
                #if grid cell is white with no ship currently placed, change grid cells to selected based on
                #ship length, origin, and direction and then change setting to ship is successfully selected
                if self.grid[row][column] == 0 and not self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (column + self.length_of_ship - 1) < COLUMN_COUNT:
                            self.grid[row][column + i] = 1
                            self.selected = True
                        else:
                            print(f"invalid placement")
                            self.selected = False
                            break
                #if grid cell is red and ship is selected make current selection ship cells white again and
                #changed selection back to not selection
                elif self.grid[row][column] == 1 and self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (column + self.length_of_ship - 1) < COLUMN_COUNT:
                            self.grid[row][column + i] = 0
                            self.selected = False
                        else:
                            print(f"offscreen redo")
                            self.selected = False
                            break
                #if grid cell selected is white and a ship location has already been selected
                #then do not select another ship
                elif self.grid[row][column] == 0 and self.selected:
                    print(f"ship already selected")
                #if grid cell selected is red and a ship location has not been selected then a
                #ship already occupies that location and another grid cell must be selected
                elif self.grid[row][column] == 1 and not self.selected:
                    print(f"there is already a ship in this space")
            #allows selection of location of ship to be vertical
            elif self.direction == Direction.DOWN:
                #if grid cell is white with no ship currently placed, change grid cells to selected based on
                #ship length, origin, and direction and then change setting to ship is successfully selected
                if self.grid[row][column] == 0 and not self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (row - self.length_of_ship + 1) > -1:
                            self.grid[row - i][column] = 1
                            self.selected = True
                        else:
                            print(f"invalid placement")
                            self.selected = False
                            break
                #if grid cell is red and ship is selected make current selection ship cells white again and
                #changed selection back to not selection
                elif self.grid[row][column] == 1 and self.selected:
                    for i in range(self.length_of_ship):
                        if row < ROW_COUNT and column < COLUMN_COUNT and (row - self.length_of_ship + 1) > -1:
                            self.grid[row - i][column] = 0
                            self.selected = False
                        else:
                            print(f"invalid placement")
                            self.selected = False
                            break
                #if grid cell selected is white and a ship location has already been selected
                #then do not select another ship
                elif self.grid[row][column] == 0 and self.selected:
                    print(f"ship already selected")
                #if grid cell selected is red and a ship location has not been selected then a
                #ship already occupies that location and another grid cell must be selected
                elif self.grid[row][column] == 1 and not self.selected:
                    print(f"there is already a ship in this space")
        #redraw grid
        self.recreate_grid()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        #sets the location of first ship in board class when enter key is pressed and then remaining
        #ships as they are looped through
        if key == arcade.key.ENTER:
            if self.selected:
                self.selected = False
                print(self.row, self.column)
                self.board.place_ships(self.length_of_ship, (self.row, self.column), self.direction)
                #loops through the remaining ships in decreasing length
                if self.length_of_ship > 0:
                    self.length_of_ship = self.length_of_ship - 1
                    self.row = 0
                    self.column = 0
                    print(self.board.get_board_view()[1])
            else:
                print(f"please place ship")
        #allows the orientation of the ship placement to change between horizontal and vertical
        #when space bar is pushed and a ship is not currently selected
        if key == arcade.key.SPACE and not self.selected:
            print(f"space")
            if self.direction == Direction.RIGHT:
                self.direction = Direction.DOWN
                print(self.direction)
            elif self.direction == Direction.DOWN:
                self.direction = Direction.RIGHT
                print(self.direction)
        #is space bar is pushed while ship is selected, then orientation is not
        elif key == arcade.key.SPACE and self.selected:
            print(f"cannot change direction while ship is selected")

# def main():
#     SHIP_LOCATION_SETUP(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     arcade.run()
#
# if __name__ == "__main__":
#     main()