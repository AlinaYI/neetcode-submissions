class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0

        curr_end = 0
        farest = 0

        for i in range(len(nums)-1):
            farest = max(farest, nums[i] + i)

            if i == curr_end:
                res += 1
                curr_end = farest
        return res