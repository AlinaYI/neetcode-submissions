class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n

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