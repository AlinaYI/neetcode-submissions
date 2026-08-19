class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Olog(m*n)
        # O1
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            r = mid // cols
            c = mid % cols

            curr = matrix[r][c]

            if curr == target:
                return True
            elif curr < target:
                left = mid + 1
            else:
                right = mid - 1

        return False