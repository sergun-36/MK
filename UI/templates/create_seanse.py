# Form implementation generated from reading ui file 'create_seanse.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateSeans(object):
    def setupUi(self, CreateSeans):
        CreateSeans.setObjectName("CreateSeans")
        CreateSeans.setEnabled(True)
        CreateSeans.resize(239, 159)
        CreateSeans.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(CreateSeans)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 101, 20))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setMaxLength(2)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 20, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(15, 50, 101, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 101, 20))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 101, 23))
        self.pushButton.setObjectName("pushButton")
        CreateSeans.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateSeans)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 239, 21))
        self.menubar.setObjectName("menubar")
        CreateSeans.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateSeans)
        self.statusbar.setObjectName("statusbar")
        CreateSeans.setStatusBar(self.statusbar)

        self.retranslateUi(CreateSeans)
        QtCore.QMetaObject.connectSlotsByName(CreateSeans)

    def retranslateUi(self, CreateSeans):
        _translate = QtCore.QCoreApplication.translate
        CreateSeans.setWindowTitle(_translate("CreateSeans", "Create Seans"))
        self.label.setText(_translate("CreateSeans", "Number of players"))
        self.label_2.setText(_translate("CreateSeans", "Number of heroes"))
        self.pushButton.setText(_translate("CreateSeans", "Create Seans"))