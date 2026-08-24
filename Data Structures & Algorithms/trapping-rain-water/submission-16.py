class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxL = height[0]
        maxR = height[-1]
        res = 0
        left, right = 0, len(height)-1

        while left < right:
            if height[left] < height[right]:
                left += 1
                maxL = max(height[left], maxL)
                res += maxL - height[left]
            else:
                right -= 1
                maxR = max(height[right], maxR)
                res += maxR - height[right]

        return res