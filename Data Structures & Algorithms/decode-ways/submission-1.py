from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        decision tree
        
            i
        取1位   取两位
        1         12
       / \
   取一位 取两位
   2        None
        '''
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            
            return res
        return dfs(0)

        # bottom up
        # 这里其实当前的dp[i] 会depend dp[i+1], dp[i+2]
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] == "0"
            else:
                dp[i] = dp[i+1]

                if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+1]
        return dp[0]
