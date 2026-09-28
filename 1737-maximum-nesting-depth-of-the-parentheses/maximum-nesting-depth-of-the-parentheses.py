class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_d = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_d = max(max_d, current_depth)
            elif char == ')':
                current_depth -= 1
                
        return max_d