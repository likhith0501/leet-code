class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0  # 0 jumps to reach the starting index
        
        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1 and -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
                    
        return dp[n - 1]