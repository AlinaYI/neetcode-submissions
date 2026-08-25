class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # decision tree
        # 就是选 i+1, 还是 i+2
        
        '''
        # top down
        @cache
        def dfs(i):
            if i >= len(cost):
                return 0

            return cost[i] + min(dfs(i + 1), dfs(i + 2))
        return min(dfs(0), dfs(1))
        '''

        # bottom up
        n = len(cost)
        dp = [0]*n

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])

        # 最优
        # 算dp[i]的时候，只需要dp[i-1]和dp[i-2]
        prev_prev = cost[0]
        prev = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev, prev_prev)

            prev_prev = prev
            prev = curr
        return min(prev, prev_prev)
