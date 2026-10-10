class Solution:
    def trap(self, height: List[int]) -> int:
        
        # min(LeftMax, RightMax) - height[i]
        LeftMax = [1]*len(height)
        LMax = height[0]
        RightMax = [1]*len(height)
        RMax = height[-1]
        res = 0
        for i in range(len(height)):
            LMax = max(LMax, height[i])
            LeftMax[i] = LMax
        
        for i in range(len(height)-1,-1,-1):
            RMax = max(RMax, height[i])
            RightMax[i] = RMax
        
        for i in range(len(height)):
            res += min(LeftMax[i], RightMax[i]) - height[i]
        return res