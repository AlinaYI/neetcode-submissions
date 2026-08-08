class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # temp, idx
        res = [0]*len(temperatures)

        for idx, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                prevTemp, prevIdx = stack.pop()
                res[prevIdx] = idx - prevIdx
            
            stack.append( (temp, idx) )
        return res