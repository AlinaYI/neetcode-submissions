from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        这里就是根据给的list然后算target
        这里只有加减

                2
             /    \
            +      -
            /       \
          2+2        2-2
          /  \      /   \       
         +    -    +     -
      2+2+2 2+2-2  2-2+2 2-2-2
        '''

        @cache
        def dfs(idx, currRes):
            if idx == len(nums):
                return 1 if currRes == target else 0
            
            return dfs(idx+1, currRes+nums[idx]) + dfs(idx+1, currRes-nums[idx])

        return dfs(0, 0)

        # bottom up
        '''
                        currRes
                -6 -4 -2  0  2  4  6
        idx 0             1
        idx 1
        idx 2
        idx 3
        '''
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total+nums[i]] += count
                dp[i+1][total-nums[i]] += count
        return dp[i][target]


        # space optimize
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]