class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        [0]
        [4, 1] -->
        [1]
        '''
        res = 0
        farest = 0
        level_end = 0

        for i in range(len(nums)-1):
            farest = max(farest, i + nums[i])

            if i == level_end:
                res += 1
                level_end = farest
        return res
            
