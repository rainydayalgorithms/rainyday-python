# REVERSE AN INTEGER
# You are given an integer. Reverse it and return the reversed value
# Examples...
# If the input is -1234, the expected output is -4321
# If the input is -130, the expected output is -31.
# Important note: Check if the output is within the valid int limits. If not, return 0

# SOLUTION 1: Loop through and use modulo to build a new integer
def reverse_floor(x: int) -> int:
  plus_minus = 1
  reversed = 0

  if x < -2147483648 or x > 2147483647:
    return 0
  if x < 0:
    x *= -1
    plus_minus = -1
  
  while x > 0:
    reversed = reversed * 10 + x % 10
    x //= 10

  if reversed < -2147483648 or reversed > 2147483647:
    return 0
  elif plus_minus == -1:
    return -reversed
  else:
    return reversed

# SOLUTION 2: Use Python slicing to reverse
def reverse_slicing(x: int) -> int:
  if x <= -2147483648 or x >= 2147483647:
    return 0
  elif x < 0:
    plus_minus = -1
    x *= -1
  else:
    plus_minus = 1

  reversed = int(str(x)[::-1]) * plus_minus
  if reversed < -2147483648 or reversed > 2147483647:
    return 0
  else:
    return reversed
