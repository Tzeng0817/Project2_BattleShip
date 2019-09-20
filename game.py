"""
Game module containing the Game class and
the SetUp class which gets the information needed for
Game to initialize 
"""
from Player import Player, be_attacked, has_lost

class SetUp:
    """
    SetUp creates the main menu and collects information
    from the players
    """

    def __init__(self):
        """
        Constructs a new SetUp object with all game information
        set to default values
        :return: returns none.
        """
        self.player1_name = ""
        self.player2_name = ""
        self.num_of_ships = 0

    def setup(self):
        """
        Handles main menu graphics and creating and running Game
        object
        :return: returns none.
        @TODO: Implement this through PyQT5
        """
        #make main menu in PYQT
        #Get user input of name and num of ships from PYQT
        print("Welcome to Battleship!")
        self.player1_name = input("Enter player one's name: ")
        self.player2_name = input("Enter player two's name: ")
        while (self.num_of_ships <= 0) or (self.num_of_ships > 5):
            self.num_of_ships = int(input("Enter how many ships you are playing with: " ))
            if self.num_of_ships <= 0:
                print("The number of ships must be more than 0.")
            elif self.num_of_ships > 5:
                print("The number of ships cannot be greater than 5.")
        #creates game object and runs it
        my_game = Game(self.player1_name, self.player2_name, self.num_of_ships)
        my_game.run()

class Game:
    """
    Game manages the flow of the game
    """

    def __init__(self, player1_name, player2_name, num_of_ships):
        """
        Constructs a new Game object. Creates two internal player objects.
        :return: returns none.
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1 = Player(player1_name, num_of_ships)
        self.player2 = Player(player2_name, num_of_ships)

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
        self.player2.be_attacked()

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
        self.player1.be_attacked()

    def end_game(self):
        """
        Shows the endgame screen and announces the winner
        :return: returns none.
        @TODO: Implement the endgame screen through PyQT5
        """
        #Show end game screen (PYQT)
        if self.player1.has_lost() == True:
            print(self.player1_name + " has won!")
        elif self.player2.has_lost() == False:
            print(self.player2_name + " has won!")

    def run(self):
        """
        Handles the flow of the game and detects if a player has lost
        :return: returns none.
        """
        while (self.player1.has_lost == False) and (self.player2.has_lost == False):
            player1_turn()
            player2_turn()
        end_game()