class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(startIdx, comb):
            if startIdx == len(s):
                res.append(comb[:])
            
            for i in range(startIdx, len(s)):
                curr = s[startIdx:i+1]
                if isPalindrome(curr):
                    backtrack(i+1, comb + [curr])
        res = []
        backtrack(0, [])
        return res