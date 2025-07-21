import unittest
import rainyday.solutions.reverse_integer as reverseint

class TestReverseIntFloor(unittest.TestCase):
  def test_floor_21(self):
    self.assertEqual(reverseint.reverse_floor(21), 12)

  def test_floor_200(self):
    self.assertEqual(reverseint.reverse_floor(200), int('002'))

  def test_floor_202(self):
    self.assertEqual(reverseint.reverse_floor(202), 202)

  def test_floor_negative_203(self):
    self.assertEqual(reverseint.reverse_floor(-203), -302)

  def test_floor_negative_130(self):
    self.assertEqual(reverseint.reverse_floor(-130), -31)
  
  def test_floor_negative_1734235429(self):
    self.assertEqual(reverseint.reverse_floor(-1734235429), 0)
  
  def test_floor_9245324371(self):
    self.assertEqual(reverseint.reverse_floor(9245324371), 0)

class TestReverseIntSlice(unittest.TestCase):
  def test_slice_21(self):
    self.assertEqual(reverseint.reverse_slicing(21), 12)

  def tes_slice_200(self):
    self.assertEqual(reverseint.reverse_slicing(200), int('002'))

  def test_floor_negative_130(self):
    self.assertEqual(reverseint.reverse_slicing(-130), -31)

  def test_slice_202(self):
    self.assertEqual(reverseint.reverse_slicing(202), 202)

  def test_slice_negative_203(self):
    self.assertEqual(reverseint.reverse_slicing(-203), -302)
  
  def test_slice_negative_1734235429(self):
    self.assertEqual(reverseint.reverse_slicing(-1734235429), 0)
  
  def test_slice_9245324371(self):
    self.assertEqual(reverseint.reverse_slicing(9245324371), 0)