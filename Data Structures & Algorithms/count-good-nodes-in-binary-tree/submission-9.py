# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0 

        def dfs(node, pathMax):
            if not node:
                return
            
            if node.val >= pathMax:
                self.res += 1
            
            currMax = max(pathMax, node.val)
            left = dfs(node.left, currMax)
            right = dfs(node.right, currMax)
        
        dfs(root, root.val)
        return self.res