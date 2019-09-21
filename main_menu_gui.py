"""
main_menu_gui module contains the MainMenuGUI class for, shockingly, making the main menu gui.
The basic architecture for the code was taken from an example in the Arcade documentation: http://arcade.academy/examples/gui_text_button.html
"""

import arcade
import buttons

class MainMenuGUI(arcade.Window):
    """
    MainMenuGUI manages the main menu GUI.
    """

    def __init__(self, width, height, title):
        """
        Constructs a new MainMenuGUI object and sets the background color of the window.
        :return: returns none.
        """
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.button_list = None

    def setup_main_menu(self):
        """
        Creates the on-screen GUI buttons
        :return: returns none.
        """
        self.button_list = []

        play_button = buttons.PlayTextButton(400, 455, self.play_game)
        self.button_list.append(play_button)

        quit_button = buttons.QuitTextButton(400, 400, self.quit_game)
        self.button_list.append(quit_button)

    def on_draw(self):
        """
        Renders the screen.
        :return: returns none.
        """

        arcade.start_render()

        # Draw the buttons
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
        return

    def quit_game(self):
        """
        Closes the game.
        :return: returns none.
        """
        arcade.close_window()
