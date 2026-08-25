from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        这道题就是戳气球
        再一个区间里，找到最后要戳哪个balloon
        '''
        nums = [1] + nums + [1]

        @cache
        def dfs(left, right):
            if left > right:
                return 0

            res = 0

            for k in range(left, right + 1):
                coins = (
                    nums[left - 1] * nums[k] * nums[right + 1]
                    + dfs(left, k - 1)
                    + dfs(k + 1, right)
                )

                res = max(res, coins)

            return res

        return dfs(1, len(nums) - 2)


        # bottom up
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # length = 当前区间长度
        for length in range(1, n - 1):
            for left in range(1, n - length):
                right = left + length - 1

                for k in range(left, right + 1):
                    coins = (
                        dp[left][k - 1]
                        + nums[left - 1] * nums[k] * nums[right + 1]
                        + dp[k + 1][right]
                    )

                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][n - 2]