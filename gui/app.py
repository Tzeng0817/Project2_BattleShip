from PyQt5.QtWidgets import QDialog, QApplication
from gui.startMenu import Ui_start_menu

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_start_menu()
        self.ui.setupUi(self)
        self.show()
