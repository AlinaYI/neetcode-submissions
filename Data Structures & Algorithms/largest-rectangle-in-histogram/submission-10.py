class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        # height, start
        stack = []
        res = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][0] >= height:
                prevH ,prevI = stack.pop()
                res = max(res, (idx-prevI)*prevH)
                start = prevI
            stack.append((height, start))
        return res
            