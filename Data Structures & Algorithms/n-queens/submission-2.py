class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [["."]*n for _ in range(n)]
        cols = set()
        positive_diag = set()
        negative_diag = set()

        def backtarck(row):
            
            # base case
            if row == n:
                res.append(["".join(line) for line in board])
                return
            
            for col in range(n):
                # 如果这个在set里面，continue
                if col in cols or row+col in positive_diag or row-col in negative_diag:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                positive_diag.add(row+col)
                negative_diag.add(row-col)

                backtarck(row+1)

                board[row][col] = "."
                cols.remove(col)
                positive_diag.remove(row+col)
                negative_diag.remove(row-col)

        backtarck(0)
        return res