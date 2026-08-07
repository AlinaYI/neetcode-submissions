class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # total - maxFreq < k

        count = defaultdict(int)
        maxFreq = 0
        res = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])
            
            while right-left+1 - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res
