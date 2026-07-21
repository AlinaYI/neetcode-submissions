class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def backtrack(i, j, idx):
            if idx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or seen[i][j] == True:
                return False
            
            seen[i][j] = True
            for di, dj in directions:
                ni, nj = di + i, dj + j
                if backtrack(ni, nj, idx+1):
                    return True
            
            seen[i][j] = False
            return False

        seen = [[False]*len(board[0]) for _ in range(len(board))]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False