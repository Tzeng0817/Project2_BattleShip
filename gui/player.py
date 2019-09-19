import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.oneBoard import Ui_oneBoard

class Ui_player(object):
    def open_board(self):
        self.window = QtWidgets.QMainWindow()
        #second file name
        self.main_window.close()
        self.ui = Ui_oneBoard()
        self.ui.setupUi(self.window)
        self.window.show()

    def store_data(self):
        print("hi")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 486)

        self.main_window = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 341, 411))
        font = QtGui.QFont()
        font.setFamily("KaiTi")
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.player_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.player_container.setContentsMargins(0, 0, 0, 0)
        self.player_container.setObjectName("player_container")
        self.label_kraag = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_kraag.setMinimumSize(QtCore.QSize(30, 132))

        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(20)
        self.label_kraag.setFont(font)
        self.label_kraag.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_kraag.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kraag.setObjectName("label_kraag")
        self.player_container.addWidget(self.label_kraag)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_player1 = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(22)
        self.label_player1.setFont(font)
        self.label_player1.setObjectName("label_player1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_player1)
        self.label_name1 = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(16)
        self.label_name1.setFont(font)
        self.label_name1.setObjectName("label_name1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_name1)

        self.line_name1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KaiTi")
        self.line_name1.setFont(font)
        self.line_name1.setObjectName("line_name1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_name1)

        self.line_name2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KaiTi")
        self.line_name2.setFont(font)
        self.line_name2.setObjectName("line_name1_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_name2)
        self.line_name2.textChanged.connect(self.store_data)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_player2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(22)
        self.label_player2.setFont(font)
        self.label_player2.setObjectName("label_player2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_player2)
        self.label_name2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(16)
        self.label_name2.setFont(font)
        self.label_name2.setObjectName("label_name2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_name2)

        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox_1to5 = QtWidgets.QSpinBox(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("KaiTi")
        self.spinBox_1to5.setFont(font)
        self.spinBox_1to5.setMinimum(1)
        self.spinBox_1to5.setMaximum(5)
        self.spinBox_1to5.setObjectName("spinBox_1to5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinBox_1to5)
        self.button_continue = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_continue.clicked.connect(self.open_board)

        self.button_continue.setObjectName("button_continue")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.button_continue)
        self.player_container.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
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
        self.label_player1.setText(_translate("MainWindow", "PLAYER1"))
        self.label_name1.setText(_translate("MainWindow", "NAME:"))
        self.label_player2.setText(_translate("MainWindow", "PLAYER2"))
        self.label_name2.setText(_translate("MainWindow", "NAME:"))
        self.label.setText(_translate("MainWindow", "HOW MANY SHIPS "))
        self.button_continue.setText(_translate("MainWindow", "Continue"))

