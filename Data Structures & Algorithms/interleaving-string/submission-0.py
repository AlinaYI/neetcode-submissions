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
