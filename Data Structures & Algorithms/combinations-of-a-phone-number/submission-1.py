class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dig_lett = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }

        def backtrack(start, comb):
            if len(comb) == len(digits):
                res.append(comb[:])
                return
            
            for char in dig_lett[digits[start]]:
                backtrack(start+1, comb + char)
        
        res = []
        if digits:
            backtrack(0, "")
        return res