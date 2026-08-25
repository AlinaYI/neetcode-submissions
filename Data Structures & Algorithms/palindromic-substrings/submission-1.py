class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand(left, right):
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        res = 0

        for i in range(len(s)):
            # odd
            res += expand(i, i)

            # even
            res += expand(i, i + 1)

        return res