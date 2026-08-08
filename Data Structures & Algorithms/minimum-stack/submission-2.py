class MinStack:

    def __init__(self):
        self.stack = []
        # 只记录“历史上出现过的新最小值”，包括相同的最小值。
        self.minStack = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        
        # if minStack为空 or val <= 当前最小值
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
