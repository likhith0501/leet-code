class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in matching_bracket:
                # Check if the stack is non-empty and the top matches the required opening bracket
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # Valid only if all opened brackets have been closed (stack is empty)
        return len(stack) == 0