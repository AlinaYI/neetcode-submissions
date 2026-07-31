# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
            
        # preorder
        # root, left, right
        root_val = preorder[0]
        root = TreeNode(root_val)

        # inorder
        # left, root, right
        root_idx = inorder.index(root_val)
        
        preorder_left = preorder[1:root_idx+1]
        preorder_right = preorder[root_idx+1:]

        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root