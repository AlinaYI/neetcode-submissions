class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, comb):
            if start == len(s):
                res.append(comb[:])
                return
            
            for i in range(start, len(s)):
                curr = s[start:i+1]

                if not isPalindrome(curr):
                    continue
                
                backtrack(i+1, comb+[curr])


        res = []
        backtrack(0, [])
        return res