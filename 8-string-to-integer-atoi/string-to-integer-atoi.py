class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        # Check sign
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
            
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Parse digits
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            res = res * 10 + digit
            index += 1
            
        # Apply sign
        res *= sign
        
        # Clamp within 32-bit signed integer range
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res