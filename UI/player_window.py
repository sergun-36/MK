from templates.enter_players import Ui_Enter_players
from system_message import SystemMessage
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
from settings import root_url
from hero_window import HeroWindow
import requests

class PlayerWindow(Ui_Enter_players, QtWidgets.QMainWindow, SystemMessage):
	
	url = f'{root_url}/create/player'
	number_players = None
	start_y = 60
	lineEdits = {}


	def __init__(self, number_players=1, id=None):
		super().__init__()
		self.setupUi(self)
		self.pushButton.pressed.connect(self.push_names)
		self.number_players = number_players
		self.seans_id = id
		self.draw_window()


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
				if line.text() not in [x["name"] for x in self.players_names]:
					self.players_names.append({'name':line.text(), 'id_seans':self.seans_id})
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
			try:
				response = requests.post(self.url, json = self.players_names)
				status = response.status_code
				print(response.json())
				
				if status == 201:
					self.show_success("You've added players")
					self.close()
					#open hero_window
					self.hero_window = HeroWindow(response.json())
					self.hero_window.show()
				else:
					self.show_warning(f"Status {status} is wrong '{response.json()['error']}'. Try again")
			except Exception as ex:
				message = f"{ex} has broken. Try again"
				self.show_warning(message)




# app =QtWidgets.QApplication([])
# window = PlayerWindow()
# window.draw_window()
# window.show()
# app.exec()



