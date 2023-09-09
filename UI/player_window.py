from templates.enter_players import Ui_Enter_players
from system_message import SystemMessage
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
from settings import root_url
import requests

class PlayerWindow(Ui_Enter_players, QtWidgets.QMainWindow, SystemMessage):
	

	number_players = 3
	start_y = 60
	lineEdits = {}


	def create_fields(self):

		for player in range(0, self.number_players):
			self.draw_lines(player, f"enter name of player {player+1}")
			self.start_y += 60
		


	def __init__(self):
		super().__init__()

		self.setupUi(self)


	def draw_lines(self, order, text="enter name player"):
		self.lineEdits[f'lineEdit_{order}'] = QtWidgets.QLineEdit(self.centralwidget)
		line = self.lineEdits[f'lineEdit_{order}']
		line.setGeometry(QtCore.QRect(30, self.start_y+31, 471, 30))
		line.setObjectName(f"lineEdit_{order}")
		line.setText(text)

	def draw_window(self):
		self.create_fields()
		self.resize(532, self.start_y+90)# icreazed window size
		self.pushButton.setGeometry(QtCore.QRect(410, self.start_y+30, 89, 25))# put buton on window from enter player



app =QtWidgets.QApplication([])
window = PlayerWindow()
window.draw_window()
window.show()
app.exec()



