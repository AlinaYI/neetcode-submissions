class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            "]":"[",
            "}" : "{",
            ")" : "("
        }

        for char in s:
            if char in "[({":
                stack.append(char)
            else:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0