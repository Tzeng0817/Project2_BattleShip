from game import Game
from player import Player
from ship import Direction
import arcade

if __name__ == "__main__":
    player1 = Player(1)
    player2 = Player(1)
    player1.board.place_ships(1, (0, 0), Direction.RIGHT)
    player2.board.place_ships(1, (1, 1), Direction.RIGHT)
    GAME = Game(player1, player2)
    arcade.schedule(GAME.run, 0.25)
    arcade.run()
