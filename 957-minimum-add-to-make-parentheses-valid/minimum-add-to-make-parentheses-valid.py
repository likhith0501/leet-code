class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        min_add = 0
        
        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    min_add += 1
                    
        return min_add + open_count