class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # 一直往stack里面push比当前小的
        # 如果遇到了比当前大的，那就pop，process number
        stack = [] # store, temp:idx
        res = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
        # 如果curr > stack[-1]
            while stack and temp > stack[-1][0]:
                pretemp, preIdx = stack.pop()
                res[preIdx] = idx - preIdx
            stack.append( (temp, idx) )
        return res