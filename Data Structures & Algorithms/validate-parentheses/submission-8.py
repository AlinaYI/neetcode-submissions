class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for c in s:
            if c not in "})]":
                stack.append(c)
            else:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0