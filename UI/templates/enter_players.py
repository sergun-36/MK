# Form implementation generated from reading ui file 'enter_players.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Enter_players(object):
    def setupUi(self, Enter_players):
        Enter_players.setObjectName("Enter_players")
        Enter_players.resize(532, 197)
        self.centralwidget = QtWidgets.QWidget(Enter_players)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")

        # moved to player_window
        # self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit.setGeometry(QtCore.QRect(30, 60, 471, 31))
        # self.lineEdit.setObjectName("lineEdit_0")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(410, 150, 89, 25))# moved to player window
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(36, 20, 461, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        Enter_players.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Enter_players)
        self.statusbar.setObjectName("statusbar")
        Enter_players.setStatusBar(self.statusbar)

        self.retranslateUi(Enter_players)
        QtCore.QMetaObject.connectSlotsByName(Enter_players)

    def retranslateUi(self, Enter_players):
        _translate = QtCore.QCoreApplication.translate
        Enter_players.setWindowTitle(_translate("Enter_players", "Enter players"))
        self.pushButton.setText(_translate("Enter_players", "Ok"))
        self.label.setText(_translate("Enter_players", "Enter name of players"))
