class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i,j):
            if board[i][j] != "O":
                return
                
            seen.add((i,j))
            board[i][j] = "D"
            for di, dj in directions:
                ni,nj = i+di, j+dj
                if 0<=ni<len(board) and 0<=nj <len(board[0]) and board[ni][nj]=="O" and (ni,nj) not in seen:
                    dfs(ni,nj)
        
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(board)):
            dfs(i,0)
            dfs(i, len(board[0])-1)
        
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                