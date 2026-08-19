class Solution:
    def trap(self, height: List[int]) -> int:
        # min(maxLeft, maxRight) - height[i]
        maxL = height[0]
        maxR = height[-1]
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                res += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR,height[right])
                res += maxR - height[right]
            
        return res

        