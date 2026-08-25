from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        按照长度较小的text去做选择吧
        text1 = "cat", text2 = "crabt" 

        decision tree
        当前的text2的字母是不是符合text1
        /       \
       选       skip
        '''

        #top-down
        @cache
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            # 相等
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            
            # 不相等
            return max( dfs(i+1, j), dfs(i, j+1) )
        return dfs(0,0)
        
        # bottom up
        '''
           text1
        t       c   a  t
        e    c  1   0  0
        x    r  1   1  1
        t    a  1   2  2
        2    b  1   2  2
             t  1   2  3

        相等：左上 + 1
        不等：上/左取 max
        '''
        dp = [ [0]*(len(text2)+1) for _ in range(len(text1)+1) ]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[len(text1)][len(text2)]