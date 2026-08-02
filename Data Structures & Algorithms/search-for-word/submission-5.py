class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i,j,idx):
            if idx == len(word)-1:
                return True
            
            seen.add((i,j))
            for di,dj in directions:
                ni, nj  = i+di, j+dj
                if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj] ==word[idx+1] and (ni,nj) not in seen:
                    if backtrack(ni,nj,idx+1):
                        return True
                
            seen.remove((i,j))
            return False

        seen = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(i,j,0):
                    return True
        return False