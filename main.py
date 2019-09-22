import arcade
import gui_main_menu

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "KRAAG BATTLESHIP")
    main_menu = gui_main_menu.MainMenu()
    window.show_view(main_menu)
    arcade.run()
