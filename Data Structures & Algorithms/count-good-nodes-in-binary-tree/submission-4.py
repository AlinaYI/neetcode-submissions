# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # root 永远都是good node，比node大的就是good nodes

        def dfs(node, path_max):
            if not node:
                return 0
            
            count = 0
            if node.val >= path_max:
                count = 1
            
            maxi = max(node.val, path_max)

            return count + dfs(node.right, maxi) + dfs(node.left, maxi)
        
        return dfs(root, root.val)