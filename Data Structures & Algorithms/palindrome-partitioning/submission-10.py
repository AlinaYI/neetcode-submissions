class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def palindrom(sub):
            return sub == sub[::-1]
        
        def backtrack(idx, comb):
            if idx == len(s):
                res.append(comb[:])
            
            for i in range(idx, len(s)):
                curr = s[idx:i+1]
                if palindrom(curr):
                    backtrack(i+1, comb + [curr])

        res = []
        backtrack(0, [])
        return res