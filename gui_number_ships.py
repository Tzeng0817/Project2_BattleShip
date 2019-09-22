import arcade
from button import TextButton
from button import check_mouse_press_for_buttons
from button import check_mouse_release_for_buttons
from gui_shiplocations import ShipLocations

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 8

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 80
HEIGHT = 80

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

#
OFFSET_AXIS_LABEL = 30
OFFSET_BUTTON = 100

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + OFFSET_AXIS_LABEL #1315
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + OFFSET_AXIS_LABEL + OFFSET_BUTTON #1415


class NumberShips(arcade.View):
    def __init__(self):
        """
        Constructs a new MainMenuGUI object and sets the background color of the window.
        :return: returns none.
        """
        super().__init__()
        self.button_list = []
        self.button_1 = TextButton(110, 260, self.number_1, "1")
        self.button_2 = TextButton(250, 260, self.number_2, "2")
        self.button_3 = TextButton(390, 260, self.number_3, "3")
        self.button_4 = TextButton(530, 260, self.number_4, "4")
        self.button_5 = TextButton(670, 260, self.number_5, "5")

        self.button_list.append(self.button_1)
        self.button_list.append(self.button_2)
        self.button_list.append(self.button_3)
        self.button_list.append(self.button_4)
        self.button_list.append(self.button_5)

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("How many Ships do you want?", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=45, anchor_x="center")

        for element in self.button_list:
            element.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called whenever the mouse moves
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called whenever the released the mouse
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    def number_1(self):
        """
        return 1 to the next window
        :return: 1 (int)
        """
        print("clicked on button 1")
        dummy_view = ShipLocations()
        self.window.show_view(dummy_view)
        return 1

    def number_2(self):
        """
        return 2 to the next window
        :return: 2 (int)
        """
        print("clicked on button 2")
        dummy_view = ShipLocations()
        self.window.show_view(dummy_view)
        return 2

    def number_3(self):
        """
        return 3 to the next window
        :return: 3 (int)
        """
        print("clicked on button 3")
        dummy_view = ShipLocations()
        self.window.show_view(dummy_view)
        return 3

    def number_4(self):
        """
        return 4 to the next window
        :return: 4 (int)
        """
        print("clicked on button 4")
        dummy_view = ShipLocations()
        self.window.show_view(dummy_view)
        return 4

    def number_5(self):
        """
        return 5 to the next window
        :return: 5 (int)
        """
        print("clicked on button 5")
        dummy_view = ShipLocations()
        self.window.show_view(dummy_view)
        return 5



