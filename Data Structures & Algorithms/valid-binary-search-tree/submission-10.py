# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # node.left < node < node.right

        def dfs(left, node, right):

            if not node:
                return True

            if not(left < node.val < right):
                return False
            
            # left, node.left, node
            left = dfs(left, node.left, node.val)
            # node, node.right, right
            right = dfs(node.val, node.right, right)

            return left and right
        
        return dfs(float("-inf"), root, float("inf"))