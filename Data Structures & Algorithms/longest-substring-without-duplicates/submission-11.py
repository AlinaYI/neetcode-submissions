class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            # 1. add
            count[s[right]] += 1

            # 2. shrink
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1

            # 3. update answer
            res = max(res, right - left + 1)

        return res