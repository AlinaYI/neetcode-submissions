from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        这里虽然能reuse word in s，但是要所有word in wordDict要组成完整的s

        这里make decision就是按照 word in wordDict去选择
              []
            /     \
         neet    code
          |         |
         code       neet

        就是看remainning能不能用剩下的word组成
        '''

        # top-down
        # 这里的status就是要看的是 s的idx
        @cache
        def dfs(idx):
            if idx == len(s):
                return True
            
            for right in range(idx, len(s)):
                if s[idx:right+1] in wordDict:
                    if dfs(right+1):
                        return True
            return False
        return dfs(0)
