from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        @cache
        def dfs(r: int, c: int, k: int) -> bool:
            k += 1 if grid[r][c] == '(' else -1
            if k < 0 or k > (m + n - 1) // 2:
                return False
            if r == m - 1 and c == n - 1:
                return k == 0
            
            return (r + 1 < m and dfs(r + 1, c, k)) or (c + 1 < n and dfs(r, c + 1, k))

        return dfs(0, 0, 0)