class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        maintain windows
        if repeated, keep moving left, until no same char
        '''

        seen = set()
        left = res = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res