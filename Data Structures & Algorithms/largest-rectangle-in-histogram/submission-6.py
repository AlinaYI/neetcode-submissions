class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # stack 里面存height，start
        # 遇到小的就开始算，因为没有可能更大了
        # 要记录start points，是因为还能利用 height较小的高度
        heights.append(0)
        stack = []
        res = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][0]:
                h, i = stack.pop()
                area = h*(idx-i)
                res = max(area, res)
                start = i
            stack.append( (height, start) )
        return res 