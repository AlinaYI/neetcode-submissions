class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 这里就是从边缘的O traverse
        # 把与边缘连接的变成 H
        # 再traverse一遍，如果是O-> X, H->O
        def dfs(i, j):
            board[i][j] = "H"
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj] == "O":
                    dfs(ni,nj)

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        q = deque([])
        for i in range(len(board)):
            if board[i][0] == "O":
               dfs(i, 0)
            if board[i][len(board[0])-1] == "O":
                dfs(i, len(board[0])-1)
        
        for j in range(len(board[0])):
            if board[0][j] == "O":
                dfs(0, j)
            if board[len(board)-1][j] == "O":
                dfs(len(board)-1, j )

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "H":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return 
