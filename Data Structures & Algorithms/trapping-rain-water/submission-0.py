class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        recode the bindary, then calculate the water
        '''

        max_left = [0]*len(height)
        max_right = [0]*len(height)
        lmax = rmax = res = 0

        for i in range(len(height)):
            lmax = max(lmax, height[i])
            max_left[i] = lmax
        
        for i in range(len(height)-1, -1, -1):
            rmax = max(rmax, height[i])
            max_right[i] = rmax

        for i in range(len(height)):
            res += min(max_left[i], max_right[i]) - height[i]
        
        return res