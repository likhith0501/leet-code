class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
            
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
            
        ans = [0] * n
        L = 0
        for i in range(n):
            # A component boundary (cut) exists at index i if all elements to the left
            # are <= all elements to the right.
            if i == n - 1 or prefix_max[i] <= suffix_min[i + 1]:
                max_val = prefix_max[i]
                for j in range(L, i + 1):
                    ans[j] = max_val
                L = i + 1
                
        return ans