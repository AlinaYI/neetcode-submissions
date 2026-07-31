# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        valid 就是符合 left < node < right
        '''

        def dfs(low, node, high):

            if not node:
                return True
            
            if not (low < node.val < high):
                return False

            # low, node.left, node
            left = dfs(low, node.left, node.val)

            # node, node.right, high
            right = dfs(node.val, node.right, high)

            return left and right
        
        return dfs(float("-inf"), root, float("inf"))
