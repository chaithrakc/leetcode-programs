class SolutionValidParentheses:
    PARENTHESES_MAP = {')': '(', '}': '{', ']': '['}

    def isValid(self, s: str) -> bool:
        stack = list()
        for char in s:
            if char in self.PARENTHESES_MAP:
                if stack and self.PARENTHESES_MAP[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False

