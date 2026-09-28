class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_count = 0
        
        # Digits that make a number invalid: 3, 4, 7
        # Digits that rotate to a different digit: 2, 5, 6, 9
        # Digits that rotate to themselves: 0, 1, 8
        
        for i in range(1, n + 1):
            s = str(i)
            # Must not contain invalid digits (3, 4, 7)
            if any(d in s for d in '347'):
                continue
            # Must contain at least one digit that changes upon rotation (2, 5, 6, 9)
            if any(d in s for d in '2569'):
                good_count += 1
                
        return good_count