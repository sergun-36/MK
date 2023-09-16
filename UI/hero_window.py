from templates.enter_hero import Ui_Enter_Hero
# from templates.heros import Ui_MainWindow
from system_message import SystemMessage
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from settings import root_url
import requests
# Ui_Enter_Hero

class HeroWindow(Ui_Enter_Hero, QtWidgets.QMainWindow, SystemMessage):

	url = f'{root_url}/create/hero'
	url_seans = f'{root_url}/seans/'
	order = 0
	start_y_frame = 40
	lineEdits = {}
	data_heroes = []

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.players = [{'id_player': 3, 'id_seans': 45, 'name_player': 'sergei1'},
						 {'id_player': 4, 'id_seans': 45, 'name_player': 'valery1'}]
		# self.fetch_number_hero()
		self.number_heroes = 2 # get using get request
		self.pushButton.pressed.connect(self.set_heroes_player)
		self.create_fields()
		# self.draw_window()

	def fetch_number_hero(self):
		id_seans = self.players[0]['id_seans']
		response = requests.get(f'{self.url_seans}{id_seans}')
		if response.status_code == 200:
			self.number_heroes = response.json()['number_hero']
		else:
			print(f"{response} something wrong")

	def draw_line(self, number):
		# self.lineEdits[self.players[self.order]['id_player']] = {number: QtWidgets.QLineEdit(self.frame)
		line = QtWidgets.QLineEdit(self.frame)
		# lines = self.lineEdits[self.players[self.order]['id_player']]
		line.setGeometry(QtCore.QRect(10, self.start_y_frame, 221, 30))
		line.setObjectName(f"lineEdit_{number}")
		line.setPlaceholderText(f"Hero {number+1}")
		print(line)
		self.start_y_frame += 40
		return line
		
			
	def create_fields(self):
		player = self.players[self.order]
		player_lineEdits = []
		self.label_frame.setText(f"{player['name_player']}")
		for row in range(0, self.number_heroes):
			player_lineEdits.append(self.draw_line(row))
		self.pushButton.move(140, self.start_y_frame)
		self.frame.resize(241, self.start_y_frame+35)
		self.resize(299, self.start_y_frame+120)
		self.lineEdits[player["id_player"]] = player_lineEdits
		


	def set_heroes_player(self):
		player_id = self.players[self.order]["id_player"]

		for line in self.lineEdits[player_id]:
			if line.text():
				if line.text() not in [x["name_hero"] for x in self.data_heroes if x["id_player"] == player_id]:
					self.data_heroes.append({'name_hero':line.text(), 'id_player': player_id})
					is_ok = True


				else:
					self.show_warning(f" The '{line.text()}'hero is chosen several time. Please select different heroes")	
					is_ok = False
					#remove all data heroes with  player ID
					break
			else:
				self.show_warning("Can not be empty")	
				is_ok = False
				#remove all data heroes with  player ID
				break
		else:

			self.order += 1
			self.start_y_frame = 40
			#remove old objects
			self.create_fields()
		print(self.data_heroes)
		return is_ok
		

			


app =QtWidgets.QApplication([])
window = HeroWindow()
# window.draw_window()
window.show()
print(window.number_heroes)
app.exec()
