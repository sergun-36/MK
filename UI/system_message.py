from PyQt6.QtWidgets import QMessageBox

class SystemMessage():

	warning = None
	success = None

	def show_warning(self, text):
		self.warning = QMessageBox()
		self.warning.setStyleSheet("QMenu {color: red;}" )
		self.warning.setWindowTitle("Warning. Be carefull")
		self.warning.setText(text)
		self.warning.exec()

	def show_success(self, text):
		self.success = QMessageBox()
		self.success.setStyleSheet("background-color: green;")
		self.success.setWindowTitle("Success. Congratulate")
		self.success.setText(text)
		self.success.exec()