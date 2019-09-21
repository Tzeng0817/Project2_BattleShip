"""
Game module containing the Game class and
the SetUp class which gets the information needed for
Game to initialize
"""
import arcade
from board_window import BoardWindow
from popup_modal import PopupModal
from player import Player
import sys
import time

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
        self.player1 = Player(num_of_ships)
        self.player2 = Player(num_of_ships)
        self.turn_over = True
        self.game_over = False

        # self.transition_window = TurnTransitionView()
        # self.transition_window.set_visible(False)

        self.player2_own_board = BoardWindow(715, 715, "Your Board", self.player2, self.on_turn_end, True)
        self.player2_own_board.set_visible(False)
        self.player2_other_board = BoardWindow(715, 715, "Their Board", self.player1, self.on_turn_end, False)
        self.player2_other_board.set_visible(False)

        self.player1_own_board = BoardWindow(715, 715, "Your Board", self.player1, self.on_turn_end, True)
        self.player1_own_board.set_visible(False)
        self.player1_other_board = BoardWindow(715, 715, "Their Board", self.player2, self.on_turn_end, False)
        self.player1_other_board.set_visible(False)

        self.current_player = self.player1

    def player1_turn(self):
        """
        Handles all the actions player 1 can 
        do on their turn
        :return: returns none.
        @TODO: Implement the board through PyQT5
        """
        #Show player one's board with ships shown (PYQT)
        #Show player two's board with ships hidden (PYQT)
        #Let player one attack (PYQT)
        #self.player2.be_attacked()

    def player2_turn(self):
        """
        Handles all the actions player 2 can 
        do on their turn
        :return: returns none.
        @TODO: Implement the board through PyQT5
        """
        #Show player one's board with ships shown (PYQT)
        #Show player two's board with ships hidden (PYQT)
        #Let player two attack (PYQT)
        #self.player1.be_attacked()

    def end_game(self):
        """
        Shows the endgame screen and announces the winner
        :return: returns none.
        @TODO: Implement the endgame screen through PyQT5
        """
        #Show end game screen (PYQT)

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

        # arcade.pause(5)
        arcade.schedule(sys.exit, 5)

    def on_turn_end(self):
        if self.current_player == self.player1:
            self.player1_own_board.set_visible(False)
            self.player1_other_board.set_visible(False)
            self.current_player = self.player2
        else:
            self.player2_own_board.set_visible(False)
            self.player2_other_board.set_visible(False)
            self.current_player = self.player1
        # switch = PopupModal("Switch Sides!")
        arcade.pause(3)
        # switch.set_visible(False)
        self.turn_over = True

    def run(self, _):
        """
        Will eventually handle the flow of the game. Currently only creates the main menu window.
        :return: returns none.
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
