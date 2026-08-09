class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # total - maxFrea < k --> valid
        maxFreq = 0
        count = defaultdict(int) # char:freq
        res = 0
        left = 0
        for right, char in enumerate(s):
            count[char] += 1
            maxFreq = max(maxFreq, count[char])

            if right-left+1 - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res