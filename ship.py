from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Ship:
    def __init__(self, data, origin, direction):
        self.size = data
        self.origin = origin
        self.direction = direction

        self.List = []

    def getOrientation(self):
        if(self.direction.casefold() == "left"):
            self.List=[self.origin, (self.origin[0], self.origin[1]-1), (self.origin[0], self.origin[1]-2)]
        elif(self.direction.casefold() =="right"):
            self.List = [self.origin, (self.origin[0], self.origin[1]+1), (self.origin[0], self.origin[1]+2)]
        elif(self.direction.casefold() =="up"):
            self.List = [self.origin, (self.origin[0]-1, self.origin[1]), (self.origin[0]-2, self.origin[1])]
        elif(self.direction.casefold()=="down"):
            self.List = [self.origin, (self.origin[0]+1, self.origin[1]), (self.origin[0]+2, self.origin[1])]
        

        return self.List



battleship  = Ship(4, (4,3), "left") 

print(battleship.getOrientation())

