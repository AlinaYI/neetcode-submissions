from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        这道题的意思就是robber
        不能rob 两个相邻的房子，要想rob 最多的money

        top-down
        那就是rob了当前的话，只能rob i + 2
        要不然直接就是下一家
        想要max就是， max(nums[i]+nums[i+2], nums[i+1])
        '''
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0
            
            return max(nums[i]+dfs(i+2), dfs(i+1))
        return dfs(0)

        '''
        bottom up
        就是 当前的money得是前前一个房子的钱
        '''
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]

        #最优还是用两个常数
        prev_prev = nums[0]
        prev =  max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(nums[i] + prev_prev, prev)

            prev_prev = prev
            prev = curr
        return prev
