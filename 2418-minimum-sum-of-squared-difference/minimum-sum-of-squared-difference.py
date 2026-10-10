class Solution:

    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_k = k1 + k2

        if sum(diffs) <= total_k:
            return 0

        # Count frequencies of differences
        max_diff = max(diffs)
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1

        # Greedily reduce the largest differences
        rem_k = total_k
        for d in range(max_diff, 0, -1):
            if count[d] > 0:
                if rem_k >= count[d]:
                    rem_k -= count[d]
                    count[d - 1] += count[d]
                    count[d] = 0
                else:
                    count[d] -= rem_k
                    count[d - 1] += rem_k
                    break

        # Calculate the final minimum sum of squared difference
        ans = 0
        for d in range(max_diff + 1):
            if count[d] > 0:
                ans += count[d] * (d**2)

        return ans