class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays
        S2 = [0] * (4 * n)  # sum of squares
        S1 = [0] * (4 * n)  # sum of values
        lazy = [0] * (4 * n) # lazy propagation values
        length = [0] * (4 * n) # segment lengths
        
        def build(node, l, r):
            length[node] = r - l + 1
            if l == r:
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            
        build(1, 0, n - 1)
        
        def apply(node, val):
            # When adding val to all elements in the range:
            # sum((x + val)^2) = sum(x^2 + 2*val*x + val^2) = S2 + 2*val*S1 + val^2 * length
            S2[node] = (S2[node] + 2 * val * S1[node] + val * val * length[node]) % MOD
            # sum(x + val) = S1 + val * length
            S1[node] = (S1[node] + val * length[node]) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node):
            if lazy[node] != 0:
                apply(2 * node, lazy[node])
                apply(2 * node + 1, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, val)
                return
            push(node)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            S1[node] = (S1[2 * node] + S1[2 * node + 1]) % MOD
            S2[node] = (S2[2 * node] + S2[2 * node + 1]) % MOD

        last_occurrence = {}
        total_sum = 0
        
        for j in range(n):
            x = nums[j]
            prev = last_occurrence.get(x, -1)
            last_occurrence[x] = j
            
            # Increment the distinct count of all subarrays starting from prev + 1 to j
            update(1, 0, n - 1, prev + 1, j, 1)
            
            # S2[1] contains the sum of squares of distinct counts for all subarrays ending at index j
            total_sum = (total_sum + S2[1]) % MOD
            
        return total_sum