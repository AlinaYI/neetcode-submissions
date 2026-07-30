class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = deque([])
        for i in range(len(board)):
            if board[i][0] == "O":
                q.append((i,0))
            
            if board[i][len(board[0])-1] == "O":
                q.append((i, len(board[0])-1))

        for j in range(len(board[0])):
            if board[0][j] == "O":
                q.append((0,j))
            if board[len(board)-1][j] == "O":
                q.append((len(board)-1, j))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            i, j = q.popleft()
            board[i][j] = "D"
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < len(board) and 0<=nj<len(board[0]) and board[ni][nj] == "O":
                    board[ni][nj] = "D"
                    q.append((ni,nj))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return
        
