# VALID BRACKETS
# You are given a string of brackets () {} [].
# Valid brackets can be nested, but must have a corresponding closing bracket in the correct place
# Return if the input brackets are valid

def isValid(s: str) -> bool:
  open_brackets = ["(", "{", "["]
  close_brackets = [")", "}", "]"]
  bracket_stack = []

  for i in s:
    if i in open_brackets:
      bracket_stack.append(i)
    else:
      which_bracket = close_brackets.index(i)
      if (len(bracket_stack) > 0) and (open_brackets[which_bracket] == bracket_stack[-1]):
        bracket_stack.pop(-1)
      else:
        return False
  
  return len(bracket_stack) == 0
