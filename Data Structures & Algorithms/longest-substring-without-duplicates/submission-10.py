class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        hashmap = {} # char:idx
        res = 0
        for right in range(len(s)):
            currChar = s[right]
            # abba
            if currChar in hashmap and hashmap[currChar] >= left:
                left = hashmap[currChar] + 1
            
            hashmap[currChar] = right
            res = max(res, right-left+ 1)
        return res