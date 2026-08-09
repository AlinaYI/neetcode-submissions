class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # if stack[-1] > curr: 
        # check the ares
        stack = [] # heigh, idx
        heights.append(0)
        res = 0
        for idx, heigh in enumerate(heights):
            start = idx
            while stack and stack[-1][0] > heigh:
                h, i = stack.pop()
                area = (idx-i)*h
                res = max(res, area)
                start = i
            stack.append( (heigh, start) )

        return res