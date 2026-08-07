class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # 用total - maxFreq < k 就符合条件
        count = defaultdict(int)
        maxFreq = 0
        left = 0
        res = 0

        for right, c in enumerate(s):
            count[c] += 1
            maxFreq = max(maxFreq, count[c])

            while right-left + 1  - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res
            