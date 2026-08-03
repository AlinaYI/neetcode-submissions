class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {} # hashmap record {char: idx}
        left = 0
        right = 0

        res = 0
        while right < len(s):
            if s[right] in seen:
                # prev : seen[s[right]]
                left = max(left, seen[s[right]] + 1)
            res = max(res, right-left+1)
            seen[ s[right] ] = right
            right += 1
        return res
            
            