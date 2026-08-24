class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # top down DP
        @cache
        def dfs(i):
            #如果i==n，就是有一条路线能走通，所以加1
            if i == n:
                return 1
            # 如果 当前的值大于n，走过了，就是 0
            if i > n:
                return 0            
            return dfs(i+1) + dfs(i+2)
        return dfs(0)

        # bottom up
        # On
        # On
        if n <= 2:
            return n
        
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        '''

        # On
        # O1
        if n <= 2:
            return n

        prev_prev = 1
        prev = 2

        for i in range(3, n + 1):
            curr = prev + prev_prev
            
            prev_prev = prev
            prev = curr

        return prev