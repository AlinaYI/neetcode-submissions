class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        这道题要做的就是找到最大的rectangle
        这里最大的rectangle就是要看面积
            长方形的面积就是底*高，这里的底就是长度，然后高就是要算小的那个

        这里的bruteforce就是从第一个element开始double for loop算过去
        然后找最大的值，这样的tc就是 On^2

        这里的底是随着element增加的，可以控制的高
        可以maintain一个单调递增栈
        直到遇到比当前小的，算一下stack中能最远的柱子在哪里
        然后update 面积
        这里可以给heights末尾加一个element，保证heights都算到
        '''

        heights.append(0)
        res = 0
        stack = [] # 这里的stack存idx

        for i,h in enumerate(heights):
            
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                res = max(res, width * heights[top])

            stack.append(i)
        return res