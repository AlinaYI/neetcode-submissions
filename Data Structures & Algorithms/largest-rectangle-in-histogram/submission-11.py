class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] #startIdx, height
        res = 0
        heights.append(0)
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                prevIdx, prevHeight = stack.pop()
                res = max(res, prevHeight * (idx - prevIdx))
                start = prevIdx
            stack.append((start, height))
        return res