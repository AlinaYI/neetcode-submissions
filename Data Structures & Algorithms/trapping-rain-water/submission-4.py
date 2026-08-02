class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        min(lmax, rmax) - height[i]
        '''

        lmax = [0]*len(height)
        rmax = [0]*len(height)
        left = height[0]
        right = height[-1]
        res = 0

        for i in range(len(height)):
            left = max(left, height[i])
            lmax[i] = left
        
        for j in range(len(height)-1, -1, -1):
            right = max(right, height[j])
            rmax[j] = right
        
        for i in range(len(height)):
            res += min(lmax[i], rmax[i]) - height[i]
        
        return res