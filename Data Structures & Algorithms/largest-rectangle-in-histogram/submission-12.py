class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(height, start)
        heights.append(0)
        res = 0
        for idx, h in enumerate(heights):
            start = idx
            while stack and h < stack[-1][0]:
                prevH, prevS = stack.pop()
                res = max(res, prevH*(idx-prevS))
                start = prevS
            stack.append( (h, start) )
        return res