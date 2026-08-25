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