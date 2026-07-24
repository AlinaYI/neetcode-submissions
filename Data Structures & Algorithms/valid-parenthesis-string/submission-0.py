class Solution:
    def checkValidString(self, s: str) -> bool:
        open_low = 0
        open_high = 0

        for char in s:
            if char == "(":
                open_low += 1
                open_high += 1
            elif char == ")":
                open_low -= 1
                open_high -= 1
            else:
                open_low -= 1
                open_high += 1
            if open_high < 0:
                return False
            open_low = max(open_low, 0)
        return open_low == 0