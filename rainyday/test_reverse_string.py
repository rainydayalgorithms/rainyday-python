import unittest
import rainyday.solutions.reverse_string as reverse

class TestReverseString(unittest.TestCase):
  def test_golden(self):
    test_stringlist = ["g","o","l","d","e","n"]
    self.assertEqual(reverse.reverseString(test_stringlist), ["n","e","d","l","o","g"])

  def test_oddball(self):
    test_stringlist = ["o","d","d","b","a","l","l"]
    self.assertEqual(reverse.reverseString(test_stringlist), ["l","l","a","b","d","d","o"])

  def test_a(self):
    test_stringlist = ["a"]
    self.assertEqual(reverse.reverseString(test_stringlist), ["a"])

  def test_capital(self):
    test_stringlist = ["C","a","P","i","T","a","L"]
    self.assertEqual(reverse.reverseString(test_stringlist), ["L","a","T","i","P","a","C"])

if __name__ == '__main__':
    unittest.main()
