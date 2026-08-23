class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i,j):
            if board[i][j] != 'O':
                return

            board[i][j] = 'D'
            for di, dj in directions:
                ni,nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and board[ni][nj] == 'O':
                    dfs(ni,nj)

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row, col = len(board), len(board[0])
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)

        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        # mark connected to D
        # go throught the map, 
        # change all D to O, left O to X
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return 