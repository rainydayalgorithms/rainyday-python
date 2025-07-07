import unittest
import rainyday.solutions.integer_to_roman as introman

class TestIntegerToRomanMethods(unittest.TestCase):
  def test_1(self):
    self.assertEqual(introman.intToRoman(1), "I")

  def test_99(self):
    self.assertEqual(introman.intToRoman(99), "XCIX")

  def test_48(self):
    self.assertEqual(introman.intToRoman(48), "XLVIII")

  def test_501(self):
    self.assertEqual(introman.intToRoman(501), "DI")

  def test_432(self):
    self.assertEqual(introman.intToRoman(432), "CDXXXII")

  def test_1647(self):
    self.assertEqual(introman.intToRoman(1647), "MDCXLVII")

  def test_3999(self):
    self.assertEqual(introman.intToRoman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()
