class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def isPalindrom(sub):
            return sub == sub[::-1]

        def backtrack(start, comb):
            if start == len(s):
                res.append(comb[:])
                return

            for i in range(start, len(s)):
                curr = s[start:i+1]

                if not isPalindrom(curr):
                    continue
                
                comb.append(curr)
                backtrack(i+1, comb)
                comb.pop()

        res = []
        backtrack(0, [])
        return res