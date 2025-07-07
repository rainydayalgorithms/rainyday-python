import unittest
import rainyday.solutions.binary_search as binarysearch

# Test Scenarios to cover
# > Best case: Search for any valid value in the array
# > Search for a value that isn't present (negative case)
# > Search for a value at the beginning and end of the array

class TestBinarySearch(unittest.TestCase):
  def test_binary_search_1(self):
    test_list = [1, 2, 3, 4, 5, 6 , 7, 8]
    target = 1
    self.assertEqual(binarysearch.search(test_list, target), 0)

  def test_binary_search_2(self):
    test_list = [1, 2, 3, 4, 5, 6 , 7, 8]
    target = 5
    self.assertEqual(binarysearch.search(test_list, target), 4)

  def test_binary_search_4(self):
    test_list = [-3, -1, 0, 3, 5, 9, 12]
    target = 0
    self.assertEqual(binarysearch.search(test_list, target), 2)

  def test_binary_search_5(self):
    test_list = [-100, -30, -27, -23, -10, -3, -1, 0, 3, 5, 9, 12]
    target = -23
    self.assertEqual(binarysearch.search(test_list, target), 3)

  def test_binary_search_6(self):
    test_list = [-100, -30, -27, -23, -10, -3, -1, 0, 3, 5, 9, 12]
    target = -25
    self.assertEqual(binarysearch.search(test_list, target), -1)

if __name__ == '__main__':
    unittest.main()
