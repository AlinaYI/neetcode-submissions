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
        # On^2
        # On
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

        # bottom up
        # 这里的dp 就代表能不能组成的状态
        # On^2
        # On
        dp = [False]*len(s)+1
        dp[0] = True # 代表空的，是可以组成的
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp(len(s))

        # 优化
        # 这里dp直接从reachable state 往后跳
        # O(n × m × L)
        # On
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            for word in wordDict:
                end = i + len(word)

                if end <= n and s[i:end] == word:
                    dp[end] = True

        return dp[n]

