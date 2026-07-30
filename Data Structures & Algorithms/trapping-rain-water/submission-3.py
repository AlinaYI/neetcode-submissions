class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        height = [0,2,0,3,1,0,1,3,2,1]
                        |
                left_max    right_max
        min(left_max, right_max) - height[i]
        every postion -> [left_max, right_max]

        '''

        if not height:
            return 0
        
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        lmax, rmax, res = 0, 0, 0

        for i in range(len(height)):
            lmax = max(lmax, height[i])
            left_max[i] = lmax
        
        for i in range(len(height)-1, -1, -1):
            rmax = max(rmax, height[i])
            right_max[i] = rmax
        
        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]

        return res