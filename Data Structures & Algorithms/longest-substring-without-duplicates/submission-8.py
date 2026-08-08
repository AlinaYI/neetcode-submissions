class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = {} # char:idx <- updated idx
        res = 0
        left = 0
        for idx, char in enumerate(s):
            # abba
            if char in hashmap and hashmap[char] >= left:
                left = hashmap[char] + 1
            
            hashmap[char] = idx
            res = max(res, idx-left+1)
        return res