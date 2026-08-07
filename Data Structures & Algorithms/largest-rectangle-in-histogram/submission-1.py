class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # 这里可以给heights末尾加一个element，保证heights都算到
        heights.append(0)
        stack = [] # h, idx
        res = 0

        for idx, h in enumerate(heights):
            start = idx
            while stack and h < stack[-1][0]:
                height, i = stack.pop()
                res = max(res, height*(idx-i))
                start = i
            stack.append((h, start))
        return res