from templates.enter_hero import Ui_Enter_Hero
from system_message import SystemMessage
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from settings import root_url
import requests


class HeroWindow(Ui_Enter_Hero, QtWidgets.QMainWindow, SystemMessage):

	url = f'{root_url}/create/hero'
	url_seans = f'{root_url}/seans/'

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.players = [{'id_player': 3, 'id_seans': 45, 'name_player': 'sergei1'},
						 {'id_player': 4, 'id_seans': 45, 'name_player': 'valery1'}]
		self.fetch_number_hero()
		#self.number_heroes = 2 # get using get request
		# self.draw_window()

	def fetch_number_hero(self):
		id_seans = self.players[0]['id_seans']
		response = requests.get(f'{self.url_seans}{id_seans}')
		if response.status_code == 200:
			self.number_heroes = response.json()['number_hero']
		else:
			print(f"{response} something wrong")



app =QtWidgets.QApplication([])
window = HeroWindow()
# window.draw_window()
window.show()
print(window.number_heroes)
app.exec()
