class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = []
        for c in s:
            if c.isalnum():
                nums.append(c.lower())
        return nums == nums[::-1]