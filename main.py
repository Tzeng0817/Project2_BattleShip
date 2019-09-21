from game import Game
import arcade

if __name__ == "__main__":
    GAME = Game(2)
    arcade.schedule(GAME.run, 0.25)
    arcade.run()
