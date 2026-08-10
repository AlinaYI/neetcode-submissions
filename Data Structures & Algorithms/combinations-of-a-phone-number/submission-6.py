class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digNum = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtrack(idx, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return

            chars = digNum[digits[idx]]
            for c in chars:
                backtrack(idx+1, comb + c)
        res = []
        backtrack(0, "")
        return res if digits else []