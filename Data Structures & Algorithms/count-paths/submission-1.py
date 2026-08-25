from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        '''
        这道题要找到unique path 从左上到右下
        就是要维护两个status，一个是i，一个是j
        每次就是由大概两个选择，一个是往右边，一个是往下走
        '''

        # top down
        @cache
        def dfs(i, j):
            # 出界
            if i >= m or j >= n:
                return 0

            # 到target
            if i == m-1 and j == n-1:
                return 1

            return dfs(i+1, j) + dfs(i, j+1)

        return dfs(0, 0)


        # bottom up
        dp = [ [0]*n for _ in range(m) ]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

