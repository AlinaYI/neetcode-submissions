class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 要找到没有repeat char的
        
        hashmap = {} # char: idx
        
        left= 0
        res = 0
        for right in range(len(s)):

            if s[right] in hashmap:
                # 防止一个已经过期的旧 index 把 left 拉回去
                # abba
                left = max(left, hashmap[s[right]] + 1 )
            res = max(res, right-left+1)
            hashmap[s[right]] = right
        return res