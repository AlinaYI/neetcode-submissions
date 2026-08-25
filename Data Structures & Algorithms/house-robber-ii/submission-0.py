class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        这道题也是housr robber
        然后不能rob 两个相近的房子
        max(nums[i-1], nums[i-2]+nums[i])
        '''
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):
            prev_prev = 0
            prev = 0

            for money in arr:
                curr = max(
                    prev,
                    prev_prev + money
                )

                prev_prev = prev
                prev = curr

            return prev

        return max(
            rob_line(nums[:-1]),  # 不抢最后一家
            rob_line(nums[1:])    # 不抢第一家
        )