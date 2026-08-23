class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(openCount, closeCount, comb):
            
            if len(comb) == n*2:
                res.append(comb)
            
            if openCount < n:
                backtrack(openCount+1, closeCount, comb+"(")
            if closeCount < openCount:
                backtrack(openCount, closeCount+1, comb+")")
        
        res = []
        backtrack(0,0, "")
        return res