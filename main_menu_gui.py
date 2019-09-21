"""
main_menu_gui module contains the MainMenuGUI class for, shockingly, making the main menu gui.
The basic architecture for the code was taken from an example in the Arcade documentation: http://arcade.academy/examples/gui_text_button.html
"""

import arcade
import buttons
import sys

WIDTH = 800
HEIGHT = 800

class MainMenuGUI(arcade.View):
    def __init__(self):
        super().__init__()
        self.button_list = []
        play_button = buttons.PlayTextButton(WIDTH/2, HEIGHT/3, self.play_game)
        quit_button = buttons.QuitTextButton(WIDTH/2, (HEIGHT/3) - 55, self.quit_game)
        self.button_list.append(play_button)
        self.button_list.append(quit_button)

    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to KRAAG Battleship!", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        :return: returns none.
        """
        buttons.check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        :return: returns none.
        """
        buttons.check_mouse_release_for_buttons(x, y, self.button_list)

    def play_game(self):
        """
        Will one day advance the game state.
        :return: returns none.
        """
        ship_num_view = NumOfShipsGUI()
        self.window.show_view(ship_num_view)

    def quit_game(self):
        """
        Closes the game.
        :return: returns none.
        """
        arcade.close_window()
        sys.exit() #forcibly exits the python program so no futher windows open
