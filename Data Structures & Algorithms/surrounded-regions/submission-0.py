class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        这道题就是要看中间是不是包围着的， 从外围往内部search
        '''

        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
                return
            
            board[i][j] = "T"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # each cols, first and last
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
