import unittest

roman_map = zip(("M", "D", "C", "L", "X", "V", "I")
	,(1000, 500, 100, 50, 10, 5, 1))

def int_to_roman(i):
	pass

class Test_roman(unittest.TestCase):
	"""docstring for Test_roman"""
	def test_one(self):
		self assertTrue(int_to_roman(1) == "I")
	def test_three(self):
		self assertTrue(int_to_roman(3) == "III")
	def test_four(self):
		self assertTrue(int_to_roman(4) == "IV")
	def test_five(self):
		self assertTrue(int_to_roman(5) == "V")
	def test_six(self):
		self assertTrue(int_to_roman(6) == "VI")
	def test_eight(self):
		self assertTrue(int_to_roman(8) == "VIII")
	def test_nine(self):
		self assertTrue(int_to_roman(9) == "IX")
	def test_thirteen(self):
		self assertTrue(int_to_roman(13) == "XIII")
		