from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        dfs(i, j)

        p[j+1] == '*' ?
            /                 \
            yes                  no
            |                    |
        skip x* / use x*      当前必须 match
            /        \              |
        j+2       i+1,j          i+1,j+1
        '''

        @cache
        def dfs(i, j):
            # pattern 用完
            if j == len(p):
                return i == len(s)

            first_match = ( i < len(s) and (p[j] == s[i] or p[j] == ".") )

            # p[j+1] 是 *
            if j + 1 < len(p) and p[j + 1] == "*":
                # 1. 不使用这个 x*
                skip = dfs(i, j + 2)
                # 2. 使用一个字符，但 pattern 不动
                use = first_match and dfs(i + 1, j)
                return skip or use

            # 普通字符 / .
            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)



        '''
        bottom up
        '''
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                first_match = (i < m and (s[i] == p[j] or p[j] == "."))

                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = ( dp[i][j + 2] or (first_match and dp[i + 1][j]))
                else:
                    if i < m:
                        dp[i][j] = (first_match and dp[i + 1][j + 1])

        return dp[0][0]