class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if not board:
            return False

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]

                if curr == ".":
                    continue
                
                if curr in row_set[i]:
                    return False
                row_set[i].add(curr)
            
                if curr in col_set[j]:
                    return False
                col_set[j].add(curr)

                box_idx = (i//3)*3 + j//3
                if curr in box_set[box_idx]:
                    return False
                box_set[box_idx].add(curr)
        return True