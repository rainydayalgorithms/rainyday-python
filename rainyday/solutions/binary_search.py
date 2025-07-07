from typing import List
import math

# BINARY SEARCH
# You are given a sorted list of numbers and a target number
# If the target exists in the list, return the index of the target 
# If target does not exist, return -1

def search(nums: List[int], target: int) -> int:
  first = 0
  last = len(nums) - 1

  while first <= last:
    midpoint = math.floor((first + last ) // 2)

    if nums[midpoint] > target:
      last = midpoint - 1
    elif nums[midpoint] < target:
      first = midpoint + 1
    else:
      return midpoint
  
  return -1
