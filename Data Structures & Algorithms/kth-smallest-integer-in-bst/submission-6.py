# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # inorder tree: root, left, right
        # [left.val, root.val, right.val]
        # [left.left.val, left.val, left.right.val, root.val, right.left.val, right.val, right.right.val]
        def compact(node):
            if not node:
                return []
            
            return compact(node.left) + [node.val] + compact(node.right)

        return compact(root)[k-1]