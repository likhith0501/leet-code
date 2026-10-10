class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_k = k1 + k2
        
        if sum(diff) <= total_k:
            return 0
            
        count = [0] * (max(diff) + 1)
        for d in diff:
            count[d] += 1
            
        curr = len(count) - 1
        rem = total_k
        
        while rem > 0 and curr > 0:
            if count[curr] == 0:
                curr -= 1
                continue
            
            take = min(rem, count[curr])
            count[curr] -= take
            count[curr - 1] += take
            rem -= take
            
            if take == rem and count[curr] > 0:
                break
            if rem > 0 and count[curr] == 0:
                curr -= 1
                
        return sum(i * i * count[i] for i in range(len(count)))