class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        hashmap = {} # char:idx-updated
        res = 0
        
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]]+ 1)

            hashmap[ s[right] ] = right
            res = max(right-left + 1, res)
        return res

            