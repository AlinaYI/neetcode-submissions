class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # totalLen - maxFreq > k --> False
        count = defaultdict(int)
        maxFreq = 0
        res = 0
        left = 0
        for right in range(len(s)):
            currChar = s[right]
            count[currChar] += 1
            maxFreq = max(maxFreq, count[currChar])

            while right-left+1 - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
            right += 1
        return res