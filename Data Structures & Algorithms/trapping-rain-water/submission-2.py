class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1

        left_max = height[0]
        right_max = height[-1]
        res = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max ,height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1
        return res