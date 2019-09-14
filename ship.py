from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Ship:
    # constructor - creates a ship of size(size), an origin and a given direction
    # assumes that edge cases are checked for (no negative indices)
    def __init__(self, size, origin, direction):
        self.size = size
        self.origin = origin
        self.direction = Direction(direction)

        self.List = []

    #returns indexes that the ship has occupied  
    def get_cells(self):
        self.list=[self.origin]

        for i in range(1, self.size):
            if(self.direction == self.direction.LEFT):
                self.list.append((self.origin[0], self.origin[1]-i))
            elif(self.direction ==self.direction.RIGHT):
                self.list.append((self.origin[0], self.origin[1]+i))
            elif(self.direction ==self.direction.UP):
                self.list.append((self.origin[0]-i, self.origin[1]))
            elif(self.direction ==self.direction.DOWN):
                self.list.append((self.origin[0]+i, self.origin[1]))
        
        

        return self.list

