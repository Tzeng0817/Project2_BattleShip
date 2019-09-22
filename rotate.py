"""""
Rotate a ship function
"""""

from ship import Ship, Direction

battle = Ship(3, 4, (2, 1))


def rotate(ship, direction):
    """
    Rotate when you press SPACE

    :param: ship : ships size 1x5 or 1x4 or 1x3 or 1x2 or 1x1
    :param: direction : left, right, down, up
    """
    positions = ship.get_cells()
    shift = ship.size - 1
    ship.positions = [ship.origin]

    for i in range(1, ship.size):
        if direction == ship.direction.down :
            positions.append((ship.orign[0]+i, ship.origin[1])) 

    

