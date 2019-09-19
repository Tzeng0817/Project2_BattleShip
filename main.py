from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from gui.startMenu import Ui_start_menu
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startMenu = QMainWindow()
    font = QtGui.QFont()
    font.setFamily("KaiTi")
    font.setPointSize(20)
    app.setFont(font)


    ui = Ui_start_menu(startMenu)

    startMenu.show()
    sys.exit(app.exec_())
