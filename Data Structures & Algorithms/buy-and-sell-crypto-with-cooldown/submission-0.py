from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            这道题就是要卖stock with cooldown time

                    decision tree
            遇到一个coin       如果你手上已经持有一个
            /       \              /        \
            买       不买        skip        卖掉，下次买要有一个cooldown

        '''

        @cache
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            
            if holding:
                # 可以卖/skip
                sell = prices[i] + dfs(i+2, False)
                skip = dfs(i+1, True)

                return max(sell, skip)
            else:
                # 可以买/skip
                buy = -prices[i] + dfs(i+1, True)
                skip = dfs(i+1, False)

                return max(buy, skip)

        return dfs(0, False)

        # bottom up
        '''
            priecs
                0/False没有股票     1/True有股票
            1       
            3
            4
            0
            4
        '''

        dp = [[0]*2 for _ in range(len(prices)+2)]

        for i in range(len(prices)-1, -1, -1):
            # 没有股票的时候，就是买/skip
            dp[i][0] = max( -prices[i] + dp[i+1][1], dp[i+1][0])

            # 有股票的时候，就是卖/skip
            dp[i][1] = max( prices[i] + dp[i+2][0], dp[i+1][1])
        return dp[0][0]