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
	start_x = 10

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
		line.setObjectName(f"lineEdit_{number}_{self.order}")
		line.setPlaceholderText(f"Hero {number+1}")
		line.show()
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


	def draw_result(self, hero):
		player = QtWidgets.QLabel(self.frame_2)
		player.setGeometry(QtCore.QRect(self.start_x, self.start_y_frame, 105, 25))
		player.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
		player.setObjectName("label_frame")
		name_player = [player["name_player"] for player in self.players if player["id_player"] == hero["id_player"]]
		player.setText(f"{name_player[0]}")

		hero_line = QtWidgets.QLabel(self.frame_2)
		hero_line.setGeometry(QtCore.QRect(self.start_x+105+11, self.start_y_frame, 105, 25))
		hero_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
		hero_line.setObjectName("label_frame")
		hero_line.setText(f"{hero['name_hero']}")


	def show_results(self):
		self.label.setText("Your choices")
		#creation frame with results
		self.frame_2 = QtWidgets.QFrame(self.centralwidget)
		self.frame_2.setGeometry(QtCore.QRect(30, 50, 241, 120))
		self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_2.setObjectName("frame_2")

		#adding row for each hero
		for hero in self.data_heroes:
			self.draw_result(hero)
			self.start_y_frame += 40
		self.frame_2.resize(241, self.start_y_frame+35)
		self.resize(299, self.start_y_frame+95+20)

		# creation push button
		self.pushButton_Db = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_Db.setGeometry(QtCore.QRect(140, self.start_y_frame, 89, 25))
		self.pushButton_Db.setAutoDefault(False)
		self.pushButton_Db.setObjectName("push_db")
		self.pushButton_Db.setText("Push Heroes")
		self.pushButton_Db.pressed.connect(self.push_heroes)

		self.frame_2.show()


	def push_heroes(self):
		print(f"Your results are sent {self.data_heroes}")
		


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

			#remove old objects
			if self.order != len(self.players):
				self.start_y_frame = 40
				self.create_fields()
			else:
				self.frame.hide()
				self.start_y_frame = 10
				self.show_results()

		# self.order += 1
		# self.create_fields()
		return is_ok
		

			


app =QtWidgets.QApplication([])
window = HeroWindow()
# window.draw_window()
window.show()
print(window.number_heroes)
app.exec()
