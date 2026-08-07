class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]

                if curr == ".":
                    continue
                
                if curr in rowSet[i]:
                    return False
                rowSet[i].add(curr)

                if curr in colSet[j]:
                    return False
                colSet[j].add(curr)

                boxIdx = 3*(i//3) + j//3
                if curr in boxSet[boxIdx]:
                    return False
                boxSet[boxIdx].add(curr)
        return True