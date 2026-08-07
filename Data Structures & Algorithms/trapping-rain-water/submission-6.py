class Solution:
    def trap(self, height: List[int]) -> int:
        
        # min(leftMax, rightMax) - height[i]
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        leftM = 0
        rightM = 0
        res = 0

        for i in range(len(height)):
            leftM = max(leftM, height[i])
            leftMax[i] = leftM
        
        for j in range(len(height)-1, -1, -1):
            rightM = max(rightM, height[j])
            rightMax[j] = rightM
        
        for i in range(len(height)):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res