# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxiVal):
            if not node:
                return 0
            
            good = 1 if node.val >= maxiVal else 0
            maxiVal = max(maxiVal, node.val)
            return (good + dfs(node.left, maxiVal) + dfs(node.right, maxiVal) )

        return dfs(root, root.val)