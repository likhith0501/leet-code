class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern is exhausted, text must also be exhausted
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' wildcard in pattern
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: Ignore the 'char*' (0 occurrences)
                # Option 2: Use '*' (1 or more occurrences, if first_match is True)
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Move both pointers forward
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)