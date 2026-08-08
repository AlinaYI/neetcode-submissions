class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # rule: windowSize - maxFreq < k
        maxFreq = 0
        count = defaultdict(int)
        left = 0
        res = 0
        for idx, char in enumerate(s):

            count[char] += 1
            maxFreq = max(maxFreq, count[char])

            while idx-left+1 - maxFreq > k: 
                count[s[left]] -= 1
                left += 1
            
            res = max(idx-left+1, res)
        return res