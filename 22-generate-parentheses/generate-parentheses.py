class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count: int, close_count: int, current_str: str):
            # Base case: valid combination formed
            if len(current_str) == 2 * n:
                res.append(current_str)
                return

            # Add an opening bracket if we haven't reached n yet
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")

            # Add a closing bracket if it wouldn't exceed open brackets
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")

        backtrack(0, 0, "")
        return res