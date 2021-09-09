import pytest
import sys
#print(sys.path)
sys.path.append("../")
from seans_window import SeansWindow


class TestSeansWindow():
	
	def test_assert(self):
		assert 2 == 3 
	

	def test_positive_number(self):
		
		test_window = SeansWindow()
		t_positive_player = 2
		t_positive_hero = 4
		test_window.lineEdit.setText(str(t_positive_player))
		test_window.lineEdit_2.setText(str(t_positive_hero))
		t_result = test_window.set_data_seans()
		
		assert t_positive_player == test_window.number_player
		assert t_positive_hero == test_window.number_hero
		assert isinstance(t_result, bool)
		assert t_result == True

	def test_negative_number(self):
		test_window = SeansWindow()
		t_negative_player = -2
		t_negative_hero = -4
		test_window.lineEdit.setText(str(t_negative_player))
		test_window.lineEdit_2.setText(str(t_negative_hero))
		t_result = test_window.set_data_seans()
		test_window.warning.close()
		
		assert t_negative_player != test_window.number_player
		assert t_negative_hero != test_window.number_hero
		assert isinstance(t_result, bool)
		assert t_result == False
		assert test_window.number_player == None
		assert test_window.number_hero == None

	def test_zero_number(self):
		test_window = SeansWindow()
		t_negative_player = 0
		t_negative_hero = 0
		test_window.lineEdit.setText(str(t_negative_player))
		test_window.lineEdit_2.setText(str(t_negative_hero))
		t_result = test_window.set_data_seans()
		test_window.warning.close()
		
		assert t_negative_player != test_window.number_player
		assert t_negative_hero != test_window.number_hero
		assert isinstance(t_result, bool)
		assert t_result == False
		assert test_window.number_player == None
		assert test_window.number_hero == None