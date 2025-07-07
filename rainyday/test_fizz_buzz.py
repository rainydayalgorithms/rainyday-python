import unittest
import rainyday.solutions.fizz_buzz as fizzbuzz

class TestFizzBuzzBasic(unittest.TestCase):

# Test Scenarios
# > Ensure something divisible by 3 returns Fizz
# > Ensure something divisible by 5 returns Buzz
# > Ensure something divisible by 3 and 5 returns FizzBuzz
# > Ensure something not divisble by 3 or 5 returns the string value of the number

  def test_stairs_2(self):
    num = 2
    self.assertEqual(fizzbuzz.fizzBuzz(num), "2")
  
  def test_stairs_3(self):
    num = 3
    self.assertEqual(fizzbuzz.fizzBuzz(num), "Fizz")

  def test_stairs_5(self):
    num = 5
    self.assertEqual(fizzbuzz.fizzBuzz(num), "Buzz")

  def test_stairs_15(self):
    num = 15
    self.assertEqual(fizzbuzz.fizzBuzz(num), "FizzBuzz")

class TestFizzBuzzList(unittest.TestCase):

# Test Scenarios
# > At a minimum, need to test 15, because that includes all 4 scenarios: Fizz, Buzz, FizzBuzz and string value of number

  def test_stairs_2(self):
    num = 2
    self.assertEqual(fizzbuzz.fizzBuzzList(num), ['1', '2'])
  
  def test_stairs_3(self):
    num = 3
    self.assertEqual(fizzbuzz.fizzBuzzList(num), ['1', '2', 'Fizz'])

  def test_stairs_5(self):
    num = 5
    self.assertEqual(fizzbuzz.fizzBuzzList(num), ['1', '2', 'Fizz', '4', 'Buzz'])

  def test_stairs_15(self):
    num = 15
    self.assertEqual(fizzbuzz.fizzBuzzList(num), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])
