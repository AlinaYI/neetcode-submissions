class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(start, comb):
            if start == len(s):
                res.append(comb[:])
                return

            for i in range(start, len(s)):
                curr = s[start:i+1]
                if isPalindrome(curr):
                    backtrack(i+1, comb+[curr])
        res = []
        backtrack(0, [])
        return res