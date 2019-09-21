"""
Game module containing the Game class and
the SetUp class which gets the information needed for
Game to initialize 
"""

import arcade
from player import Player

class Game:
    """
    Game manages the flow of the game
    """

    def __init__(self, num_of_ships):
        """
        Constructs a new Game object. Creates two internal player objects.
        :return: returns none.
        """
        self.num_of_ships = 0
        self.make_main_menu()
        #some class that handles getting the num_of_ships from the user from Karen
        self.player1 = Player(num_of_ships)
        self.player2 = Player(num_of_ships)

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
        if self.player1.has_lost() == True:
            print("Player 1 has won!")
        elif self.player2.has_lost() == False:
            print("Player 2 has won!")

    def run(self):
        """
        Handles the flow of the game and detects if a player has lost
        :return: returns none.
        """
        while (self.player1.has_lost == False) and (self.player2.has_lost == False):
            self.player1_turn()
            self.player2_turn()
        self.end_game()