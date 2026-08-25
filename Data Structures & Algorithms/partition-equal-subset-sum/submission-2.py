from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        这里是要找到两个一样的subset
        那就是target找到一个subset是 totalSum//2

        那也就是遇到一个nums[i] -> 选/不选

        '''
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total//2

        @cache
        def dfs(i, remain):
            if remain == 0:
                return True
            
            if i == len(nums) or remain < 0:
                return False
            
            return dfs(i+1, remain-nums[i]) or dfs(i+1, remain)
        return dfs(0, target)

        # bottom up
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total//2

        dp = [False]* (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num-1, -1):
                dp[s] = dp[s] or dp[s-num]

        return dp[target]