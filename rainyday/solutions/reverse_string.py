from typing import List

# REVERSE A STRING
# You are giving a string. Return the versed version of it. 
# Notes: 
# Assume there isn't any extra whitespace around the beginning and end of string
# Leave all caps as they are as well as whitespace in between words

def reverseString(s: List[str]) -> List[str]:
    """
      For testing, return the string list so we can test it properly
    """
    front = 0
    back = len(s) - 1

    while front < back:
      temp = s[front]
      s[front] = s[back]
      s[back] = temp

      front += 1
      back -= 1

    return s
