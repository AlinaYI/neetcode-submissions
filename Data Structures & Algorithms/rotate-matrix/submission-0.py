class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # 先对角换，然后再reverse row
        def reverse(row):
            return row[::-1]
        
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix

        matrix = transpose(matrix)
        for i in range(len(matrix)):
            matrix[i] = reverse(matrix[i])
