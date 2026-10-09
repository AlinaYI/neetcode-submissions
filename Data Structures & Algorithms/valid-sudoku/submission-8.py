class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                currNum = board[i][j]
                
                if currNum == ".":
                    continue

                if currNum in rowSet[i]:
                    return False
                rowSet[i].add(currNum)

                if currNum in colSet[j]:
                    return False
                colSet[j].add(currNum)

                boxIdx = 3*(i//3) + (j//3)
                if currNum in boxSet[boxIdx]:
                    return False
                boxSet[boxIdx].add(currNum)
        return True
                