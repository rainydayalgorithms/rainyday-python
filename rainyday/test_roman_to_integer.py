import unittest
import rainyday.solutions.roman_to_integer as romanint

class TestRomantoIntegerMethods(unittest.TestCase):
  def test_1(self):
    self.assertEqual(romanint.romanToInt('I'), 1)

  def test_99(self):
    self.assertEqual(romanint.romanToInt('XCIX'), 99)

  def test_48(self):
    self.assertEqual(romanint.romanToInt('XLVIII'), 48)

  def test_501(self):
    self.assertEqual(romanint.romanToInt('DI'), 501)

  def test_432(self):
    self.assertEqual(romanint.romanToInt('CDXXXII'), 432)

  def test_1647(self):
    self.assertEqual(romanint.romanToInt('MDCXLVII'), 1647)

  def test_3999(self):
    self.assertEqual(romanint.romanToInt('MMMCMXCIX'), 3999)

if __name__ == '__main__':
    unittest.main()
