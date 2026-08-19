class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # 这里要存的就是 height，start
        heights.append(0)
        stack = []
        res = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][0]:
                preH, preIdx = stack.pop()
                res = max(res, preH*(idx-preIdx))
                start = preIdx
            stack.append( (height, start) )
        return res