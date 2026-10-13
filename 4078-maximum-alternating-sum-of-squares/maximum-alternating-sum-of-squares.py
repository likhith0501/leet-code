class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums], reverse=True)
        total = 0
        
        # We want to add the largest elements at even indices (0, 2, 4...)
        # and subtract the remaining elements at odd indices (1, 3, 5...).
        # Sorting descending means squares is [3^2, 2^2, 1^2] for nums = [1, 2, 3].
        # If we iterate through the sorted list, the largest elements come first,
        # but the alternating sign pattern adds index 0, subtracts index 1, adds index 2...
        # So we actually want the largest elements at indices 0, 2, 4... and smaller ones at 1, 3...
        # If squares is sorted descending: squares[0] is largest, squares[1] next, etc.
        # To maximize: add squares[0], subtract squares[1], add squares[2] works if we arrange them properly,
        # Wait! For [1, 2, 3], squares are [9, 4, 1].
        # If we place them as [3, 1, 2], the squares are [9, 1, 4].
        # Score = 9 - 1 + 4 = 12.
        # Here, index 0 gets 9 (largest), index 2 gets 4 (second largest), index 1 gets 1 (smallest).
        # So the sorted squares should be interleaved or placed such that the largest values are added and smallest values subtracted.
        # Specifically, the largest (n + 1)//2 elements are added, and the remaining are subtracted.
        
        n = len(squares)
        evens = squares[: (n + 1) // 2]
        odds = squares[(n + 1) // 2 :]
        
        return sum(evens) - sum(odds)