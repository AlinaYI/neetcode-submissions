class Solution:
    def trap(self, height: List[int]) -> int:
        # min(maxL, maxR) - height[i]

        maxLeft = [0]*len(height)
        maxL = height[0]

        maxRight = [0]*len(height)
        maxR = height[-1]

        for i in range(len(height)):
            maxL = max(maxL, height[i])
            maxLeft[i] = maxL
        
        for i in range(len(height)-1, -1, -1):
            maxR = max(maxR, height[i])
            maxRight[i] = maxR
        
        res = 0
        for i in range(len(height)):
            res += (min(maxLeft[i], maxRight[i]) - height[i])
        return res 