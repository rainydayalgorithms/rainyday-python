def romanToInt(s: str) -> int:
  roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  answer = 0

  for i in range (0, len(s) - 1):
    currentValue = s[i]
    nextValue = s[i + 1]

    if (roman[currentValue] >= roman[nextValue]):
      answer = answer + roman[currentValue]
    else:
      answer = answer - roman[currentValue]
  
  answer = answer + roman[s[len(s) - 1]]

  return answer