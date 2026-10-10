class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(c)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if c == "+":
                    curr = num1+num2
                elif c == "-":
                    curr = num1-num2
                elif c == "*":
                    curr = num1*num2
                else:
                    curr = num1/num2
                stack.append(curr)
        return int(stack[-1])