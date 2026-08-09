class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = deque()
        row, col = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for i in range(row):
            if board[i][0] == "O":
                q.append((i,0))
            
            if board[i][col-1] == "O":
                q.append((i,col-1))
        
        for j in range(col):
            if board[0][j] == "O":
                q.append((0,j))
            
            if board[row-1][j] == "O":
                q.append((row-1, j))
        
        while q:
            i,j = q.popleft()
            board[i][j] = "D"
            for di, dj in directions:
                ni,nj=i+di, j+dj
                if 0<=ni<row and 0<=nj<col and board[ni][nj] == "O":
                    q.append((ni,nj))
            


        for i in range(row):
            for j in range(col):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return