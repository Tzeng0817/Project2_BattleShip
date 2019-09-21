import arcade
from ship import Ship, Direction

battle = Ship(3, 4, (2,1))
def rotate(ship, direction):
    positions = ship.get_cells()
    shift = ship.size - 1
    ship.positions = [ship.origin]

    for i in range(1, ship.size):
        if(direction==ship.direction.down):
            positions.append((ship.orign[0]+i, ship.origin[1])) 

    

