class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        count = [0] * 32
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    count[i] += 1
        
        res = 0
        MOD = 10**9 + 7
        for _ in range(k):
            current = 0
            for i in range(32):
                if count[i] > 0:
                    current |= (1 << i)
                    count[i] -= 1
            res = (res + current * current) % MOD
        return res