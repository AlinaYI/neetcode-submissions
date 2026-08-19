class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left = 0
        right = col-1

        while left < row and right >= 0:
            curr = matrix[left][right]
            if curr == target:
                return True
            elif curr < target:
                left += 1
            else:
                right -= 1
        return False
