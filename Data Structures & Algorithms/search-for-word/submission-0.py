class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, index):

            if board[i][j] != word[index]:
                return False

            if index == len(word)-1:
                return True
            
            visited.add((i, j))
            for di, dr in direction:
                ni, nr = di + i, dr + j

                if 0 <= ni < len(board) and 0 <= nr < len(board[0]) and (ni, nr) not in visited:
                    if backtrack(ni, nr, index + 1):
                        return True
            
            visited.remove((i, j))
            return False


        
        direction = [(1,0),(-1, 0), (0,1), (0,-1)]
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        
        return False