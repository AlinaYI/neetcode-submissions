class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        windows = defaultdict(int)
        res = 0
        while right < len(s):
            currChar = s[right]
            if currChar in windows:
                # abba
                left = max(left, windows[currChar]+1)
            windows[currChar] = right
            res = max(res, right-left+1)
            right += 1
        return res
