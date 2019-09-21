"""
Window with buttons and Text(How many ships)
"""
import arcade
from button import Button
from button import NumberButton
from button import check_mouse_press_for_buttons
from button import check_mouse_release_for_buttons


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Click on the number of ships"


class NumberShips(arcade.Window):
    """
    NumberShips class is the window for gui_number_ships
    """
    def __init__(self, width, height, title):
        """
        Constructs a new NumberShips window.
        :return: returns none.
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """
        Adding button to the button_list
        """
        self.button_list = []
        self.button_1 = NumberButton(110, 490, self.number_1, "1")
        self.button_list.append(self.button_1)
        self.button_2 = NumberButton(250, 490, self.number_2, "2")
        self.button_list.append(self.button_2)
        self.button_3 = NumberButton(390, 490, self.number_3, "3")
        self.button_list.append(self.button_3)
        self.button_4 = NumberButton(530, 490, self.number_4, "4")
        self.button_list.append(self.button_4)
        self.button_5 = NumberButton(670, 490, self.number_5, "5")
        self.button_list.append(self.button_5)

    def on_draw(self):
        """
        draw the text and the buttons in the list_button
        """
        arcade.start_render()
        arcade.draw_text("How many Ships do you want?", 80, 530, arcade.color.BLACK, 40)

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

    def pause_program(self):
        """
        pause the program
        """
        self.pause = True

    def resume_program(self):
        """
        resume the program
        """
        self.pause = False

    @staticmethod
    def number_1():
        """
        return 1 to the next window
        :return: 1 (int)
        """
        print("clicked on button 1")
        return 1

    @staticmethod
    def number_2():
        """
        return 2 to the next window
        :return: 2 (int)
        """
        print("clicked on button 2")
        return 2

    @staticmethod
    def number_3():
        """
        return 3 to the next window
        :return: 3 (int)
        """
        print("clicked on button 3")
        return 3

    @staticmethod
    def number_4():
        """
        return 4 to the next window
        :return: 4 (int)
        """
        print("clicked on button 4")
        return 4

    @staticmethod
    def number_5():
        """
        return 5 to the next window
        :return: 5 (int)
        """
        print("clicked on button 5")
        return 5


def main():
    window = NumberShips(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
