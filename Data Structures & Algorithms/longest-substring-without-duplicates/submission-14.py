class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # hashmap = {char:idx}
        left = 0
        hashmap = {}
        res = 0
        for right in range(len(s)):
            currChar = s[right]
            if currChar in hashmap:
                left = max(left, hashmap[currChar]+1)
            hashmap[currChar] = right
            res = max(res, right-left+1)
        return res