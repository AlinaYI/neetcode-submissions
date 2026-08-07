class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = height[0]
        rightMax = height[-1]
        left, right = 0, len(height)
        res = 0

        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        return res