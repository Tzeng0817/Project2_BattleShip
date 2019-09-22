"""
Game module containing the Game class and
the SetUp class which gets the information needed for
Game to initialize
"""

import sys
import arcade
from board_window import BoardWindow
from popup_modal import PopupModal
from player import Player

WINDOW_HEIGHT = 715
WINDOW_WIDTH = 715

class Game:
    """
    Game manages the flow of the game and the GUI.
    """

    def __init__(self, player1: Player, player2: Player):
        """
        Constructs a new Game object. creates and instance of the main menu window.
        :return: returns none.
        """

        self.player1 = player1
        self.player2 = player2
        self.turn_over = True
        self.game_over = False

        self.player2_own_board = BoardWindow(
            WINDOW_WIDTH, WINDOW_HEIGHT, "Your Board", self.player2, self.on_turn_end, True)
        self.player2_own_board.set_visible(False)
        self.player2_other_board = BoardWindow(
            WINDOW_WIDTH, WINDOW_HEIGHT, "Their Board", self.player1, self.on_turn_end, False)
        self.player2_other_board.set_visible(False)

        self.player1_own_board = BoardWindow(
            WINDOW_WIDTH, WINDOW_HEIGHT, "Your Board", self.player1, self.on_turn_end, True)
        self.player1_own_board.set_visible(False)
        self.player1_other_board = BoardWindow(
            WINDOW_WIDTH, WINDOW_HEIGHT, "Their Board", self.player2, self.on_turn_end, False)
        self.player1_other_board.set_visible(False)

        self.current_player = self.player1

    def end_game(self):
        """
        Shows the endgame screen and announces the winner
        :return: returns none.
        """

        self.game_over = True

        self.player1_other_board.set_visible(False)
        self.player1_own_board.set_visible(False)
        self.player2_other_board.set_visible(False)
        self.player2_own_board.set_visible(False)

        if not self.player1.has_lost():
            PopupModal("Player 1 wins!")
            print("Player 1 has won!")
        elif not self.player2.has_lost():
            print("Player 2 has won!")
            PopupModal("Player 2 wins!")

        arcade.schedule(sys.exit, 5)

    def on_turn_end(self):
        '''
        Handles switching player states at the end of a turn

        :return: None
        '''
        if self.current_player == self.player1:
            self.player1_own_board.set_visible(False)
            self.player1_other_board.set_visible(False)
            self.current_player = self.player2
        else:
            self.player2_own_board.set_visible(False)
            self.player2_other_board.set_visible(False)
            self.current_player = self.player1

        self.turn_over = True

    def run(self, _):
        """
        Handles the flow of the game and deciding when to switch turns
        :return: returns none
        """
        
        if ((not self.player1.has_lost()) or (not self.player2.has_lost())) and self.turn_over:
            if self.current_player == self.player1:
                self.player1_own_board.recreate_grid()
                self.player1_own_board.set_visible(True)
                self.player1_other_board.set_visible(True)
            else:
                self.player2_own_board.recreate_grid()
                self.player2_own_board.set_visible(True)
                self.player2_other_board.set_visible(True)
            self.turn_over = False
        elif self.player1.has_lost() or self.player2.has_lost():
            self.end_game()
