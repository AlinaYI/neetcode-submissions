class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]

                if curr == ".":
                    continue
                
                if curr in rowSet[i]:
                    return False
                rowSet[i].add(curr)

                if curr in colSet[j]:
                    return False
                colSet[j].add(curr)

                box = 3*(i//3) + j//3
                if curr in boxSet[box]:
                    return False
                boxSet[box].add(curr)
        return True