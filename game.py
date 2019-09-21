"""
Game module containing the Game class and
the SetUp class which gets the information needed for
Game to initialize 
"""
import arcade
from player import Player
from board_window import BoardWindow

class Game:
    """
    Game manages the flow of the game
    """

    def __init__(self, num_of_ships):
        """
        Constructs a new Game object. Creates two internal player objects.
        :return: returns none.
        """
        self.player1 = Player(num_of_ships)
        self.player2 = Player(num_of_ships)
        self.turn_over = True

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
        if self.player1.has_lost() == True:
            print("Player 1 has won!")
        elif self.player2.has_lost() == False:
            print("Player 2 has won!")
    
    def on_turn_end(self):
        self.turn_over = True
        if self.current_player == self.player1:
            self.player1_own_board.set_visible(False)
            self.player1_other_board.set_visible(False)
            self.current_player = self.player2
        else:
            self.player2_own_board.set_visible(False)
            self.player2_other_board.set_visible(False)
            self.current_player = self.player1

    def run(self, _):
        """
        Handles the flow of the game and detects if a player has lost
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
        elif not self.turn_over:
            pass
        else:
            self.end_game()
