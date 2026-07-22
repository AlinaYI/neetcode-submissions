class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 这道题也是一样的，就是从边上的o开始search，如果跟边上的O连上了，那就肯定不能被surround

        def dfs(i, j):
            if (
                i < 0 or i >= len(board)
                or j < 0 or j >= len(board[0])
                or board[i][j] != "O"
            ):
                return

            board[i][j] = "T"
            for di, dj in directions:
                ni, nj = di + i, dj + j
                dfs(ni, nj)
            return

        directions = [(0,1), (0,-1), (1,0), (-1, 0)]        
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"