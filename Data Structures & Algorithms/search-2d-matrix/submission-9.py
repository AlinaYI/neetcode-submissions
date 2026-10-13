class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # # O(m+n)
        # # O1
        # row = 0
        # col = len(matrix[0])-1
        # while row < len(matrix) and col >= 0:
        #     curr = matrix[row][col]
        #     if curr == target:
        #         return True
        #     elif curr > target:
        #         col -= 1
        #     else:
        #         row += 1
        # return False


        # TC: O(log(m*n))
        # SC: O(1)
        left = 0
        right = len(matrix)*len(matrix[0]) - 1

        while left <= right:

            idx = left + (right-left)//2

            row = idx//len(matrix[0])
            col = idx%len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] >target:
                right = idx - 1
            else:
                left =  idx + 1
        return False