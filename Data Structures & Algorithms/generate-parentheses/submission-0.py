class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(open_count, close_count, comb):
            if len(comb) == n*2:
                res.append(comb)
                return
            
            if open_count < n:
                backtrack(open_count+1, close_count, comb+"(")
            
            if close_count < open_count:
                backtrack(open_count, close_count+1, comb+")")

        res = []
        backtrack(0, 0, "")
        return res