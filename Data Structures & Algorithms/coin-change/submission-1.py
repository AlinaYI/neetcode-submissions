from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        这里就是换钱，
        然后需要的就是最少需要几个

        decision tree
            []
          /  |  \
         1   5  10
         ...

        '''
        @cache
        def dfs(remain):
            if remain == 0:
                return 0 
            
            if remain < 0:
                return float("inf")
            
            res = float("inf")
            for coin in coins:
                res = min(res, 1 + dfs(remain-coin))
            return res
        ans = dfs(amount)
        return ans if ans != float("inf") else -1