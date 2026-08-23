class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        colSet = set()
        posSet = set()
        nagSet = set()
        grid = [ ["."]*n for _ in range(n)]
        res = []
        def backtrack(row):
            if row == n:
                res.append(["".join(line) for line in grid] )
            
            for col in range(n):

                if col in colSet or row+col in posSet or row-col in nagSet:
                    continue
                
                colSet.add(col)
                posSet.add(row+col)
                nagSet.add(row-col)
                grid[row][col] = "Q"

                backtrack(row+1)
                colSet.remove(col)
                posSet.remove(row+col)
                nagSet.remove(row-col)
                grid[row][col] = "."

        
        backtrack(0)
        return res
