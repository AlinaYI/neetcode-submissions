# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        1. dfs 应该返回的left path
        2. 空节点 返回0
        3. 拿到left/right, 加起来
        4. 返回的是 max(left,right) + 1
        '''

        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.diameter