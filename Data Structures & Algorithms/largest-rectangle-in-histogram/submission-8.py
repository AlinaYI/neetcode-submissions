class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        # h, startIdx
        stack = []
        res = 0
        for idx, height in enumerate(heights):
            start = idx

            while stack and stack[-1][0] > height:
                h, i = stack.pop()
                res = max(res, h*(idx-i))
                start = i
            stack.append( (height, start) )
        return res