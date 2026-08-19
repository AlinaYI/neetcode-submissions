class Solution:
    def trap(self, height: List[int]) -> int:
        # min(maxLeft, maxRight) - height[i]
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)
        maxL = height[0]
        maxR = height[-1]
        res = 0

        for i in range(len(height)):
            maxL = max(maxL, height[i])
            maxLeft[i] = maxL
        
        for i in range(len(height)-1, -1, -1):
            maxR = max(maxR, height[i])
            maxRight[i] = maxR

        for i in range(len(height)):
            res += (min(maxLeft[i], maxRight[i]) - height[i])
        return res