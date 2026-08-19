class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # number, idx
        res = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                preTemp, preIdx = stack.pop()
                res[preIdx] = idx - preIdx
            stack.append( (temp, idx) )
        return res
