from create_seanse import Ui_CreateSeans
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from datetime import datetime

class SeansWindow(Ui_CreateSeans, QtWidgets.QMainWindow):
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
				warning = QMessageBox()
				warning.setWindowTitle("Warning. Be carefull")
				warning.setText("Fields should be more than zero")
				warning.exec()
				is_ok = False
		except:
			warning = QMessageBox()
			warning.setWindowTitle("Warning. Be carefull")
			warning.setText("Fields should be numbers")
			warning.exec()
			self.lineEdit.setText("")
			self.lineEdit_2.setText("")
			is_ok = False

		return is_ok


	def create_seanse(self):
		if self.set_data_seans():
			pass
			self.close()


app =QtWidgets.QApplication([])
window = SeansWindow()
window.show()
app.exec()
#seans_window = SeansWindow()