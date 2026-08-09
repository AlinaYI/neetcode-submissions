class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 一直加入stack
        # 直到遇到比当前大的数字，就开始算具体是比之前大几天
        
        stack= [] #  store, (temp, idx)
        res = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                preTemp, preIdx = stack.pop()
                res[preIdx] = (idx-preIdx)
            stack.append( (temp, idx) )
        return res