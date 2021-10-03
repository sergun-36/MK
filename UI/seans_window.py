from templates.create_seanse import Ui_CreateSeans
from system_message import SystemMessage
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
from settings import root_url
import requests

class SeansWindow(Ui_CreateSeans, QtWidgets.QMainWindow, SystemMessage):

	url = f"{root_url}/create/seans/"

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.pressed.connect(self.create_seanse)
		self.date = datetime.today().strftime("%Y-%m-%d")
		self.number_player = None
		self.number_hero =None

	def set_data_seans(self):
		number_player = self.lineEdit.text()
		number_hero =self.lineEdit_2.text()
		try:
			number_player = int(number_player)
			number_hero = int(number_hero)
			if number_player > 0 and number_hero > 0:
				self.number_player = number_player
				self.number_hero = number_hero
				is_ok = True
			else:
				self.show_warning("Fields should be more than zero")
				is_ok = False
		except:
			self.show_warning("Fields should be numbers")

			self.lineEdit.setText("")
			self.lineEdit_2.setText("")
			is_ok = False

		return is_ok


	def create_seanse(self):
		if self.set_data_seans():
			data = {"date": self.date,
					"number_player": self.number_player,
					"number_hero": self.number_hero}
			try:
				response = requests.post(self.url, json={"date": self.date,
														"number_player": self.number_player,
														"number_hero": self.number_hero})
				status = response.status_code
				if status == 201:
					self.show_success(f"You create tounument with {self.number_hero} heroes for {self.number_player} players")
					self.close()
				else:
					self.show_warning(f"{status} is wrong {response.error}. Try again")
			except Exception as ex:
				message = f"{ex} has broken. Try again"
				self.show_warning(message)
			

app =QtWidgets.QApplication([])
#window = SeansWindow()
#window.show()
#app.exec()


if __name__ == '__main__':
	#app =QtWidgets.QApplication([])
	window = SeansWindow()
	window.show()
	app.exec()
