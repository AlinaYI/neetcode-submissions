class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # height, start
        heights.append(0)
        stack = []
        res = 0
        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][0] > h:
                preH, preI = stack.pop()
                res = max(res, preH*(idx-preI))
                start = preI
            stack.append((h, start))
        return res