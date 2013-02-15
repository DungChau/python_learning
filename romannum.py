import unittest

def int_to_roman(i):
	roman_map = zip(("M", "D", "C", "L", "X", "IX", "V", "IV", "I")
		,(1000, 500, 100, 50, 10, 9, 5, 4, 1))
	result = []
	for roman, num in roman_map:
		quo = int(i / num)
		if quo == 0:
			continue
		else:
			result.append(roman)
			quo -= 1
			while quo > 0:
				quo -= 1
				result.append("I")
			break
	return "".join(result)

class Test_roman(unittest.TestCase):
	"""docstring for Test_roman"""
	def test_one(self):
		self.assertTrue(int_to_roman(1) == "I")
	def test_three(self):
		self.assertTrue(int_to_roman(3) == "III")
	def test_four(self):
		self.assertTrue(int_to_roman(4) == "IV")
	def test_five(self):
		self.assertTrue(int_to_roman(5) == "V")
	def test_six(self):
		self.assertTrue(int_to_roman(6) == "VI")
	# def test_eight(self):
	# 	self.assertTrue(int_to_roman(8) == "VIII")
	# def test_nine(self):
	# 	self.assertTrue(int_to_roman(9) == "IX")
	# def test_thirteen(self):
	# 	self.assertTrue(int_to_roman(13) == "XIII")

if __name__ == '__main__':
	unittest.main()
		