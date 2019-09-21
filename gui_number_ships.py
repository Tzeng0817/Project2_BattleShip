import arcade
from button import Button
from button import NumberButton
from button import check_mouse_press_for_buttons
from button import check_mouse_release_for_buttons


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Click on the number of ships"


class NumberShips(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.button_list = []
        self.button_1 = NumberButton(110, 490, self.number_1, "1")
        self.button_list.append(self.button_1)
        self.button_2 = NumberButton(250, 490, self.number_2, "2")
        self.button_list.append(self.button_2)
        self.button_3 = NumberButton(390, 490, self.number_3, "3")
        self.button_list.append(self.button_3)
        self.button_4 = NumberButton(530, 490, self.number_4, "4")
        self.button_list.append(self.button_4)
        self.button_5 = NumberButton(670, 490, self.number_5, "5")
        self.button_list.append(self.button_5)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("How many Ships do you want?", 80, 530, arcade.color.BLACK, 40)

        for element in self.button_list:
            element.draw()

        # arcade.finish_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        check_mouse_press_for_buttons(x, y, self.button_list)
        # temp_view = TempView()
        # self.window.show_view(temp_view)

    def on_mouse_release(self, x, y, button, key_modifiers):
        check_mouse_release_for_buttons(x, y, self.button_list)

    def pause_program(self):
        self.pause = True

    def resume_program(self):
        self.pause = False

    def dummy_function(self):
        print("hi")

    @staticmethod
    def number_1():
        print("clicked on button 1")
        return 1

    @staticmethod
    def number_2():
        print("clicked on button 2")
        return 2

    @staticmethod
    def number_3():
        print("clicked on button 3")
        return 3

    @staticmethod
    def number_4():
        print("clicked on button 4")
        return 4

    @staticmethod
    def number_5():
        print("clicked on button 5")
        return 5

class TempView (arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)


def main():
    window = NumberShips(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    # window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # my_game = MyGame()
    # window.show_view(my_game)
    arcade.run()


if __name__ == "__main__":
    main()
