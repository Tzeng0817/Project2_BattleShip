"""
game module containing the Game class which creates the main menu GUI.
"""

import arcade
from main_menu_gui import MainMenuGUI
from player import Player

GAME_TITLE = "KRAAG Battleship!"
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

class Game:
    """
    Game manages the flow of the game and the GUI.
    """

    def __init__(self, num_of_ships):
        """
        Constructs a new Game object. creates and instance of the main menu window.
        :return: returns none.
        """
        self.num_of_ships = 0
        self.main_menu = MainMenuGUI(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

    def run(self):
        """
        Will eventually handle the flow of the game. Currently only creates the main menu window.
        :return: returns none.
        """
        self.main_menu.setup_main_menu()