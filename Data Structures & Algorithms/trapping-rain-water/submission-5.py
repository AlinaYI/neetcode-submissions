class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        # min(maxleft - maxright)- height[i]
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)
        maxL = maxR = res = 0 

        for i in range(len(height)):
            maxL = max(maxL, height[i])
            maxLeft[i] = maxL
        
        for j in range(len(height)-1,-1,-1):
            maxR = max(maxR, height[j])
            maxRight[j] = maxR
        
        for i in range(len(height)):
            res += (min(maxLeft[i], maxRight[i]) - height[i])
        
        return res