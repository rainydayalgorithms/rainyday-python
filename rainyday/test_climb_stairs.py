import unittest
import rainyday.solutions.climb_stairs as climbstairs

class TestClimbStairs(unittest.TestCase):
  def test_stairs_2(self):
    stairs = 2
    self.assertEqual(climbstairs.climb(stairs), 2)

  def test_stairs_1(self):
    stairs = 1
    self.assertEqual(climbstairs.climb(stairs), 1)

  def test_stairs_5(self):
    stairs = 5
    self.assertEqual(climbstairs.climb(stairs), 8)

  def test_stairs_7(self):
    stairs = 7
    self.assertEqual(climbstairs.climb(stairs), 21)
