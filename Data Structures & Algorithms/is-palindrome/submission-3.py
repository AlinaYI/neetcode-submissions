class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        nums = []
        for char in s:
            if char.isalnum():
                nums.append(char.lower())
        return nums == nums[::-1]