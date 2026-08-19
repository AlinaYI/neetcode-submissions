class Solution:
    def isPalindrome(self, s: str) -> bool:
        # On On
        res = []
        for c in s:
            if c.isalnum():
                res.append(c.lower())
        return res == res[::-1]