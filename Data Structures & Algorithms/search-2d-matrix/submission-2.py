class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])-1

        while left <= len(matrix) - 1 and right >= 0:

            curr = matrix[left][right]
            print(f"curr: {curr}")
            if curr == target:
                return True
            elif curr > target:
                right -= 1
            else:
                left += 1

        return False