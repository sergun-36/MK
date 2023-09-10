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


	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.pressed.connect(self.push_names)


	def create_fields(self):

		for player in range(0, self.number_players):
			self.draw_lines(player, f"enter name of player {player+1}")
			self.start_y += 60
		

	def draw_lines(self, order, text="enter name player"):
		self.lineEdits[f'lineEdit_{order}'] = QtWidgets.QLineEdit(self.centralwidget)
		line = self.lineEdits[f'lineEdit_{order}']
		line.setGeometry(QtCore.QRect(30, self.start_y+31, 471, 30))
		line.setObjectName(f"lineEdit_{order}")
		line.setPlaceholderText(text)


	def draw_window(self):
		self.create_fields()
		self.resize(532, self.start_y+90)# icreazed window size
		self.pushButton.setGeometry(QtCore.QRect(410, self.start_y+30, 89, 25))# put buton on window from enter player



	def set_players_names(self):
		self.players_names = []
		for line in self.lineEdits.values():
			if line.text():
				if line.text() not in self.players_names:
					self.players_names.append(line.text())
					is_ok = True
				else:
					self.show_warning(f"Player with '{line.text()}' name already exist. The name should be unique")	
					is_ok = False
			else:
				self.show_warning("Can not be empty")	
				is_ok = False
				break
		return is_ok


	def push_names(self):
		if self.set_players_names():
			print(self.players_names)




app =QtWidgets.QApplication([])
window = PlayerWindow()
window.draw_window()
window.show()
app.exec()



