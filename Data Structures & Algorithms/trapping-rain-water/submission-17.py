class Solution:
    def trap(self, height: List[int]) -> int:
        
        # min(maxL, maxR) - height[i]
        LeftMax = height[0]
        Lmax = [1]*len(height)
        RightMax = height[-1]
        Rmax = [1]*len(height)
        res = 0
        
        for i in range(len(height)):
            LeftMax = max(LeftMax, height[i])
            Lmax[i] = LeftMax
        for i in range(len(height)-1, -1, -1):
            RightMax = max(RightMax, height[i])
            Rmax[i] = RightMax
        
        for i in range(len(height)):
            res += min(Lmax[i], Rmax[i]) - height[i]
        return res