import unittest

def int_to_roman(i):
    roman_map = zip(
        ("M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV", "I")
        ,(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1))
    result = []
    for roman, num in roman_map:
        while num <= i:
            i -= num
            result.append(roman)
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
    def test_eight(self):
        self.assertTrue(int_to_roman(8) == "VIII")
    def test_nine(self):
        self.assertTrue(int_to_roman(9) == "IX")
    def test_thirteen(self):
        self.assertTrue(int_to_roman(13) == "XIII")
    def test_sixteen(self):
        self.assertTrue(int_to_roman(16) == "XVI")
    def test_twenty(self):
        self.assertTrue(int_to_roman(20) == "XX")
    def test_nineteen(self):
        self.assertTrue(int_to_roman(19) == "XIX")
    def test_2013(self):
        self.assertTrue(int_to_roman(2013) == "MMXIII")
if __name__ == '__main__':
    unittest.main()
        