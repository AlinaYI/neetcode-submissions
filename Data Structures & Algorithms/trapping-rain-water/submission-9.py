class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftM = height[0]
        leftMax = [0]*len(height)

        rightM = height[-1]
        rightMax = [0]*len(height)

        res = 0

        for i in range(len(height)):
            leftM = max(leftM, height[i])
            leftMax[i] = leftM
        
        for i in range(len(height)-1, -1,-1):
            rightM = max(rightM, height[i])
            rightMax[i] = rightM
        
        for i in range(len(height)):
            res += min(rightMax[i], leftMax[i]) - height[i]
        return res