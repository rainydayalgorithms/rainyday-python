from typing import List

# FIZZ BUZZ: Basic
# This solution returns a single value for fizz buzz

def fizzBuzz(num: int) -> str:
  mod3 = num % 3
  mod5 = num % 5

  if mod3 == 0 and mod5 == 0:
    return "FizzBuzz"
  elif mod3 == 0:
    return "Fizz"
  elif mod5 == 0:
    return "Buzz"
  else:
    return str(num)
  
# FIZZ BUZZ: Basic
# This solution returns a list of every fizz buzz answer from 1 to n
  
def fizzBuzzList(n: int) -> List[str]:
  answer_list = []
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
      answer_list.append("FizzBuzz") 
    elif i % 3 == 0:
      answer_list.append("Fizz")
    elif i % 5 == 0:
      answer_list.append("Buzz")
    else:
      answer_list.append(str(i))

  return answer_list
