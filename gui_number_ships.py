import arcade
from button import NumberButton
from button import check_mouse_press_for_buttons
from button import check_mouse_release_for_buttons

WIDTH = 800
HEIGHT = 600


class MainMenu(arcade.View):
    def __init__(self):
        """
        Constructs a new MainMenuGUI object and sets the background color of the window.
        :return: returns none.
        """
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to KRAAG Battleship", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=48, anchor_x="center")
        arcade.draw_text("Click to play", WIDTH/2, HEIGHT/2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        number_ships = NumberShips()
        self.window.show_view(number_ships)


class NumberShips(arcade.View):
    def __init__(self):
        """
        Constructs a new MainMenuGUI object and sets the background color of the window.
        :return: returns none.
        """
        super().__init__()
        self.button_list = []
        self.button_1 = NumberButton(110, 260, self.number_1, "1")
        self.button_2 = NumberButton(250, 260, self.number_2, "2")
        self.button_3 = NumberButton(390, 260, self.number_3, "3")
        self.button_4 = NumberButton(530, 260, self.number_4, "4")
        self.button_5 = NumberButton(670, 260, self.number_5, "5")

        self.button_list.append(self.button_1)
        self.button_list.append(self.button_2)
        self.button_list.append(self.button_3)
        self.button_list.append(self.button_4)
        self.button_list.append(self.button_5)

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("How many Ships do you want?", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        # self.button_1.draw()
        # self.button_2.draw()
        # self.button_3.draw()
        # self.button_4.draw()
        # self.button_5.draw()
        for element in self.button_list:
            element.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called whenever the mouse moves
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called whenever the released the mouse
        :param: x (int): the x position of the mouse
        :param: y (int): the y position of the mouse
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    def number_1(self):
        """
        return 1 to the next window
        :return: 1 (int)
        """
        print("clicked on button 1")
        dummy_view = DummyView()
        self.window.show_view(dummy_view)
        return 1

    def number_2(self):
        """
        return 2 to the next window
        :return: 2 (int)
        """
        print("clicked on button 2")
        dummy_view = DummyView()
        self.window.show_view(dummy_view)
        return 2

    def number_3(self):
        """
        return 3 to the next window
        :return: 3 (int)
        """
        print("clicked on button 3")
        dummy_view = DummyView()
        self.window.show_view(dummy_view)
        return 3

    def number_4(self):
        """
        return 4 to the next window
        :return: 4 (int)
        """
        print("clicked on button 4")
        dummy_view = DummyView()
        self.window.show_view(dummy_view)
        return 4

    def number_5(self):
        """
        return 5 to the next window
        :return: 5 (int)
        """
        print("clicked on button 5")
        dummy_view = DummyView()
        self.window.show_view(dummy_view)
        return 5


class DummyView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Dummy Screen", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")


def main():
    window = arcade.Window(WIDTH, HEIGHT, "KRAAG BATTLESHIP")
    window.total_score = 0
    main_menu = MainMenu()
    window.show_view(main_menu)
    arcade.run()


if __name__ == "__main__":
    main()
