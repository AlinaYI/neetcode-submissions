class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # totalCount - maxFreq <= k
        maxFreq = 0
        windows = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            currChar = s[right]
            windows[currChar] += 1
            maxFreq = max(maxFreq, windows[currChar])

            while right-left+1 - maxFreq > k:
                leftChar = s[left]
                windows[leftChar] -= 1
                left += 1
            res = max(res, right-left+1)
        return res