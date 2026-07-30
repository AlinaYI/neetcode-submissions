# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(node, path_max):
            if not node:
                return
            
            if node.val >= path_max:
                self.res += 1

            maxi = max(node.val, path_max)

            dfs(node.left, maxi)
            dfs(node.right, maxi)


        dfs(root, root.val)
        return self.res