class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in matching_bracket:
                # Check if stack is non-empty and top element matches the required opening bracket
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Open bracket, push onto stack
                stack.append(char)

        # Valid if all open brackets were properly closed
        return len(stack) == 0