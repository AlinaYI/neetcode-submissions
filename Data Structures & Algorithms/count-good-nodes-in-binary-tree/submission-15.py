# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0
        def dfs(node, maxiVal):
            if not node:
                return 0
            
            if node.val >= maxiVal:
                self.res += 1
            
            maxiVal = max(maxiVal, node.val)
            left = dfs(node.left, maxiVal)
            right = dfs(node.right, maxiVal)

        dfs(root, root.val)
        return self.res