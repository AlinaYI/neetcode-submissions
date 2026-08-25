from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        decision tree
                []
          /     |   \
          1     2   3 --> 根据remaining再选之后的
       /  |  \  |    |
      1   2   3 2    3
     /   / \
    1   1   2
   /   /
  1   1

        '''

        # top-down
        @cache
        def dfs(idx, remain):
            if remain == 0:
                return 1
            
            if idx == len(coins) or remain < 0:
                return 0
            
            # choose
            choose = dfs(idx, remain-coins[idx])
            # skip
            skip = dfs(idx+1, remain)
            
            return choose+skip
        return dfs(0, amount)


        # bottom-up
        '''
                        amount
                   0   1   2   3   4   5
        coin 1     1   ?   ?   ?   ?   ?
        coin 2     1   ?   ?   ?   ?   ?
        coin 5     1   ?   ?   ?   ?   ?
        no coin    1   0   0   0   0   0

        '''

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                # skip 当前 coin
                dp[i][a] = dp[i + 1][a]

                # 选当前 coin
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]


        # 压缩成1D
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]