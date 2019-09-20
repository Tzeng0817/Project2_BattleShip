##Player
"""
Player module for containing the player class
"""
from board import Board

class Player():
    """
    Player controls moves players can make and keeps track of given plyer's ships
    """
    def __init__(self, name, num_of_ships):
        """
        Constructs a new Player object. Manages player's ships.
        :return: returns none.
        """
        self.name = name
        self.num_of_ships = num_of_ships
        self.lost = False
        self.total_ship_blocks = self.get_ship_blocks(num_of_ships)
        self.board = Board()


    def be_attacked(self):
        """
        Decreases amount of ship blocks for current player when one of their ships has been attacked
        :return: returns none.
        """
        if self.total_ship_blocks > 0:
            self.total_ship_blocks-=1

    def has_lost(self):
        """
        Lets player know when they have lost. 
        :return: returns none.
        """
        self.lost = True
        print(self.name + "has lost")

    def get_ship_blocks(self, num_of_ships):
        """
        calculates amount of ship blocks a player has.
        :return: int - amount of ship blocks available to player.
        """
        sum = 0
        for i in range(1, num_of_ships+1):
            sum+=i
        return sum
