class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # 存 idx
        col_set = set()
        pos_diag = set()
        nag_diag = set()
        
        board = [["."]*n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(line) for line in board])
                return

            for col in range(n):
                if col in col_set or row+col in pos_diag or row-col in nag_diag:
                    continue
                
                board[row][col] = "Q"
                col_set.add(col)
                pos_diag.add(row+col)
                nag_diag.add(row-col)

                backtrack(row+1)

                board[row][col] = "."
                col_set.remove(col)
                pos_diag.remove(row+col)
                nag_diag.remove(row-col)


        res = []
        backtrack(0)
        return res