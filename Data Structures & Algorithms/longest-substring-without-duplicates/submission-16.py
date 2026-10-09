class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        windows = set()
        res = 0
        for right in range(len(s)):
            currChar = s[right]
            while currChar in windows:
                windows.remove(s[left])
                left += 1
            windows.add(currChar)
            res = max(res, right-left+1)
        return res