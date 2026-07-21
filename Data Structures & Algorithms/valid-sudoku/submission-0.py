class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                
                val = board[r][c]
                
                if val == ".":
                    continue

                if val in row_set[r]:
                    return False
                row_set[r].add(val)

                if val in col_set[c]:
                    return False
                col_set[c].add(val)

                idx = (r//3)*3 + c//3
                if val in box_set[idx]:
                    return False
                box_set[idx].add(val)
        return True