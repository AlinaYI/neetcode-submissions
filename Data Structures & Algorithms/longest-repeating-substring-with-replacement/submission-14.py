class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # keep maxFreq， 如果totalLen - maxFreq < k, valid
        count = defaultdict(int)
        maxFreq = 0
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])

            # shrink windows
            while right-left+1 - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res
