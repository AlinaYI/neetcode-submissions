from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        这道题就是看s1和s2 interleve能不能组成s3

        decision tree
        就是 哪个能匹配s3选哪个
        如果两个都匹配s3，那就是都可以选
        '''

        # top-down
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(idx1, idx2):
            if idx1 == len(s1) and idx2 == len(s2):
                return True
            # idx3
            k = idx1 + idx2
            if idx1 < len(s1) and s1[idx1] == s3[k]:
                if dfs(idx1+1, idx2):
                    return True
            
            if idx2 < len(s2) and s2[idx2] == s3[k]:
                if dfs(idx1, idx2+1):
                    return True
            
            return False
        
        return dfs(0,0)

        # bottom up
        '''
         s1    
    s2-- |   b   b   b   b
         a
         a
         a
         a

        上面 dp[i-1][j] = 最后一个字符从 s1 来
        左边 dp[i][j-1] = 最后一个字符从 s2 来
            上
            ↓
            X ← 左
        '''
        # edge case
        if len(s3) != len(s2) + len(s1):
            return False
        
        m, n = len(s1), len(s2)
        dp = [[[False] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                if i == 0 and j == 0:
                    continue

                k = i + j - 1

                from_s1 = (i > 0 and dp[i - 1][j] and s1[i - 1] == s3[k])
                from_s2 = (j > 0 and dp[i][j - 1] and s2[j - 1] == s3[k])

                dp[i][j] = from_s1 or from_s2

        return dp[m][n]

        '''
        因为 dp[i][j] 只依赖：

        dp[i - 1][j]   # 上
        dp[i][j - 1]   # 左
        '''
        if len(s1) + len(s2) != len(s3):
            return False

        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m, n = len(s1), len(s2)
        dp = [False] * (n + 1)
        dp[0] = True

        # 第一行：只用 s2
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # 第一列：只用 s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                k = i + j - 1

                from_s1 = dp[j] and s1[i - 1] == s3[k]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[k]

                dp[j] = from_s1 or from_s2

        return dp[n]