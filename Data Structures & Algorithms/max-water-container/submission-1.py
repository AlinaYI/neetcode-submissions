class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        brute force: 尝试所有的possible pair, 然后对比
        '''
        left = 0
        right = len(heights) - 1
        res = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right -left)
            res = max(res, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res        
