class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        stack = [] # height, startIdx
        res = 0 
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][0] > height:
                h, startIdx = stack.pop()
                res = max(res, (idx-startIdx)*h)
                start = startIdx
            stack.append( (height, start) )
        return res
            