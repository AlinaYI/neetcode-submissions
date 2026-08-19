class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {} # char:idx
        left, right = 0, 0
        res = 0
        while right < len(s):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)
            hashmap[s[right]] = right
            res = max(res, right-left + 1)

            right += 1
        return res
