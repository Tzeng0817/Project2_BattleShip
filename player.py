##Player
from board import Board

class Player():
    #Player contructor called from game class
<<<<<<< HEAD
    def __init__(self, name, num_of_ships):
        """
        Constructs a player object

        :param: name (string): gets us the name of the player (Player 1/2)
        :param: num_of_ships (int): gives us the player's shape
        :return: returns none
        """
        self.name = name
=======
    def __init__(self, num_of_ships):
>>>>>>> 8b8cb2d28665fd5557df6754793eae031e0bba44
        self.num_of_ships = num_of_ships
        self.lost = False
        self.total_ship_blocks = self.get_ship_blocks(num_of_ships)
        self.board = Board()

    #used by game class to determine if player has lost
    def has_lost(self):
<<<<<<< HEAD
        """
        Lets board know when player has lost
        :return: returns bool - loss status
        
        """
        if self.total_ship_blocks == 0:
            self.lost = True
            print(self.name + "has lost")
            return True
        else:
            return False
=======
            if self.total_ship_blocks == 0:
                self.lost = True
                print("You have lost")
                return True
            else:
                return False
>>>>>>> 8b8cb2d28665fd5557df6754793eae031e0bba44

    #calls board class to determine if ship is hit and returns information to game
    def be_attacked(self, x_pos: int, y_pos: int) -> bool:
        """
        Decrements amount of ship blocks available when player is attacked
        :return: bool - true if hit, false if not
        """
        if self.board.attacked(x_pos, y_pos) == True and self.total_ship_blocks > 0:
            self.total_ship_blocks-=1
            print("You have hit the other player's ship!")
            return True
        else:
            print("Miss... Next player please")
            return False

    #calculates number of total ship blocks from number of ships choosen from user
    def get_ship_blocks(self, num_of_ships):
        """
        Calculates amount of ship blocks available to player
        :return: int - amount of ship blocks player has
        """
        sum = 0
        for i in range(1, num_of_ships+1):
            sum+=i
        return sum
