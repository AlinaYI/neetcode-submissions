class Solution:
    def trap(self, height: List[int]) -> int:
        
        # min(LeftMax, RightMax) - height[i]
        Lmax = height[0]
        Rmax = height[-1]
        res = 0
        
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                left += 1
                Lmax = max(Lmax, height[left])
                res += Lmax - height[left]
            else:
                right -= 1
                Rmax = max(Rmax, height[right])
                res += Rmax - height[right]
        return res