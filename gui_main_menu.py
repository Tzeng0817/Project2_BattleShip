"""
main_menu_gui module contains the MainMenuGUI class for, shockingly, making the main menu gui.
The basic architecture for the code was taken from an example in the Arcade documentation: http://arcade.academy/examples/gui_text_html
"""

import arcade
from button import TextButton
from button import check_mouse_press_for_buttons
from button import check_mouse_release_for_buttons
import sys
from gui_number_ships import NumberShips

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class MainMenu(arcade.View):
    def __init__(self):
        super().__init__()
        self.button_list = []
        play_button = TextButton(SCREEN_WIDTH/2, SCREEN_HEIGHT/3, self.play_game, "Start")
        quit_button = TextButton(SCREEN_WIDTH/2, (SCREEN_HEIGHT/3) - 55, self.quit_game, "Quit")
        self.button_list.append(play_button)
        self.button_list.append(quit_button)

    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to KRAAG Battleship!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        for element in self.button_list:
            element.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse 
        :return: returns none.
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse 
        :return: returns none.
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    def play_game(self):
        """
        Will one day advance the game state.
        :return: returns none.
        """
        ship_num_view = NumberShips()
        self.window.show_view(ship_num_view)

    @staticmethod
    def quit_game():
        """
        Closes the game.
        :return: returns none.
        """
        arcade.close_window()
        sys.exit() #forcibly exits the python program so no futher windows open


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "KRAAG BATTLESHIP")
    window.total_score = 0
    main_menu = MainMenu()
    window.show_view(main_menu)
    arcade.run()


if __name__ == "__main__":
    main()
