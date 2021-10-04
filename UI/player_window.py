from templates.enter_players import Ui_Enter_players
from system_message import SystemMessage
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
from settings import root_url
import requests

class PlayerWindow(Ui_Enter_players, QtWidgets.QMainWindow, SystemMessage):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


app =QtWidgets.QApplication([])
window = PlayerWindow()
window.show()
app.exec()


