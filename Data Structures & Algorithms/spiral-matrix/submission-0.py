class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        # 四个方向
        # top - left -> right
        # bot - right-> left
        # left - top -> bot
        # right - bot -> top
        if not matrix:
            return matrix

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bot = len(matrix) - 1
        res = []

        while left < right and top < bot:

            # top
            for i in range(left, right):
                res.append(matrix[top][i])
            
            # right
            for i in range(top, bot):
                res.append(matrix[i][right])
            
            # bot
            for i in range(right, left, -1):
                res.append(matrix[bot][i])
            
            # left
            for i in range(bot, top, -1):
                res.append(matrix[i][left])
            
            top += 1
            right -= 1
            bot -= 1
            left += 1

        if left == right and top == bot:
            res.append(matrix[top][left])
        
        # 剩下同一行
        elif top == bot:
            for i in range(left, right+1):
                res.append(matrix[top][i])
        # 同一列
        elif left == right:
            for i in range(top, bot+1):
                res.append(matrix[i][left])
        return res
