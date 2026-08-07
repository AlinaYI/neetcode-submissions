class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix[0]) - 1

        while left < len(matrix) and right >= 0:
            
            curr = matrix[left][right]

            if curr == target:
                return True
            elif curr > target:
                right -= 1
            elif curr < target:
                left  += 1
        return False