class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False
            
        counts = [0] * (n + 1)
        for x in nums:
            if x > n:
                return False
            counts[x] += 1
            
        for i in range(1, n):
            if counts[i] != 1:
                return False
                
        return counts[n] == 2