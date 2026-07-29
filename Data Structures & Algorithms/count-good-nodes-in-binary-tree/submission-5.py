# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, path_maxi):
            if not node:
                return 0
            
            if node.val >= path_maxi:
                self.res += 1
            
            path_maxi = max(path_maxi, node.val)

            left = dfs(node.left, path_maxi)
            right = dfs(node.right, path_maxi)

            return max(left, right)
            
        dfs(root, root.val)
        return self.res