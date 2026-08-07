class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res