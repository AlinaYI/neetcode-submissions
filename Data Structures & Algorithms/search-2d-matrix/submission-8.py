class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # O(m+n)
        # O1
        row = 0
        col = len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            curr = matrix[row][col]
            if curr == target:
                return True
            elif curr > target:
                col -= 1
            else:
                row += 1
        return False