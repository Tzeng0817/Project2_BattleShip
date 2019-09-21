"""
buttons module contains the TextButton class for creating buttons with text in them. It also contains 
the funtions check_mouse_press_for_buttons and check_mouse_release_for_buttons which check if a button was pressed.
It also contains several classes of specific buttons used throughout the program.
The code for the TextButton class and the functions check_mouse_press_for_buttons and check_mouse_release_for_buttons
was taken from an example in the Arcade documentation: http://arcade.academy/examples/gui_text_button.html
"""

import arcade

class TextButton:
    """
    Textbutton manages drawing and clicking on the buttons.
    """
    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        """
        Constructs a new TextButton.
        :return: returns none.
        """
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """
        Draws the button.
        :return: returns none.
        """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False


def check_mouse_press_for_buttons(x, y, button_list):
    """
    Given an x, y, see if we need to register any button clicks.
    :return: returns none.
    """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(x, y, button_list):
    """
    If a mouse button has been released, see if we need to process
    any release events. 
    :return: returns none.
    """
    for button in button_list:
        if button.pressed:
            button.on_release()


class PlayTextButton(TextButton):
    """
    PlayTextButton is the button on the main menu that a user clicks on if they want to play.
    """
    def __init__(self, center_x, center_y, action_function):
        """
        Constructs a new PlayTextButton.
        :return: returns none.
        """
        super().__init__(center_x, center_y, 100, 40, "Start", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        """
        Checks if the PlayTextButton was pressed and executes the appropriate function.
        :return: returns none.
        """
        super().on_release()
        self.action_function()


class QuitTextButton(TextButton):
    """
    QuitTextButton is the button on the main menu that a user clicks on if they want to quit.
    """
    def __init__(self, center_x, center_y, action_function):
        """
        Constructs a new QuitTextButton.
        :param: center_x (int): x position of where the center of the button is so the textbutton class can draw it.
        :param: center_y (int): y position of where the center of the button is so the textbutton class can draw it.
        :param: action_function: The function that is executed when the button is pressed.
        :return: returns none.
        """
        super().__init__(center_x, center_y, 100, 40, "Stop", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        """
        Checks if the QuitTextButton was pressed and executes the appropriate function.
        :param: center_x (int): x position of where the center of the button is so the textbutton class can draw it.
        :param: center_y (int): y position of where the center of the button is so the textbutton class can draw it.
        :param: action_function: The function that is executed when the button is pressed.
        :return: returns none.
        """
        super().on_release()
        self.action_function()

