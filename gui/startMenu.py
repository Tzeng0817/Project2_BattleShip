from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.player import Ui_player

class Ui_start_menu(object):
    def open_player(self):
        self.window = QtWidgets.QMainWindow()
        self.main_window.close()
        #second file name
        self.ui = Ui_player()
        # to hide the other windeow
        self.ui.setupUi(self.window)
        self.window.show()
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 486)

        self.main_window = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 341, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.startMenu_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.startMenu_container.setContentsMargins(0, 0, 0, 0)
        self.startMenu_container.setObjectName("startMenu_container")

        self.label_kraag = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_kraag.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_kraag.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kraag.setObjectName("label_kraag")
        self.startMenu_container.addWidget(self.label_kraag)
        
        self.button_play = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_play.sizePolicy().hasHeightForWidth())
        
        self.button_play.setSizePolicy(sizePolicy)
        self.button_play.setMinimumSize(QtCore.QSize(10, 10))
        # font
        self.button_play.setObjectName("button_play")
        self.button_play.clicked.connect(self.open_player)
        self.startMenu_container.addWidget(self.button_play)

        self.button_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy)
        # font
        # self.button_exit.setFont(font)
        self.button_exit.setObjectName("button_exit")
        self.button_exit.clicked.connect(MainWindow.close)
        self.startMenu_container.addWidget(self.button_exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_kraag.setText(_translate("MainWindow", "KRAAG BATTLESHIP"))
        self.button_play.setText(_translate("MainWindow", "PLAY"))
        self.button_exit.setText(_translate("MainWindow", "EXIT"))


