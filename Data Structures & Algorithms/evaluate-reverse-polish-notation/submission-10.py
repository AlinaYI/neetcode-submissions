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
                    stack.append(num1+num2)
                elif c == "-":
                    stack.append(num1-num2)
                elif c == "*":
                    stack.append(num1*num2)
                else:
                    stack.append(num1/num2)
        return int(stack[-1])