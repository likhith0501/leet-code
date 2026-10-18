import math
from typing import List


class Solution:

  def numOfWays(self, nums: List[int]) -> int:
    MOD = 10**9 + 7

    def helper(arr):
      if len(arr) <= 2:
        return 1

      root = arr[0]
      left = [x for x in arr if x < root]
      right = [x for x in arr if x > root]

      # Combinations: choose len(left) positions out of len(left) + len(right)
      ways_comb = math.comb(len(left) + len(right), len(left)) % MOD
      ways_left = helper(left)
      ways_right = helper(right)

      return (ways_comb * ways_left % MOD * ways_right) % MOD

    # Subtract 1 because the original array itself shouldn't be counted as a "reordering"
    return (helper(nums) - 1) % MOD