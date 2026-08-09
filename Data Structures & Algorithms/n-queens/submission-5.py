class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtrack
        # backtrack(row) -> start row 0 -> row == n
        # queen in col_set
        # [0,1,2,-3]
        # [1,2,-1,4]
        # [2,.,4,.]
        # pos_diag -> row + col
        # nag_diag -> row - col
        # n x n
        # On!
        # Omn

        '''
        [[Q, ., ., .],
         [., ., ., .],
         [., ., ., .],
         [., ., ., .]]
        '''

        board= [["."] * n for _ in range(n)]
        colSet = set()
        posDiag = set()
        nagDiag = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(line) for line in board])
                return
            
            for col in range(n):
                
                if col in colSet or row+col in posDiag or row-col in nagDiag:
                    continue
        
                board[row][col] = "Q"
                colSet.add(col)
                posDiag.add(row+col)
                nagDiag.add(row-col)

                backtrack(row+1)
                board[row][col] = "."
                colSet.remove(col)
                posDiag.remove(row+col)
                nagDiag.remove(row-col)

        res = []
        backtrack(0)
        return res