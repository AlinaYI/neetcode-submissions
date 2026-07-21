# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder
        # node, left, right

        # inorder
        # left, node, right

        if not preorder and not inorder:
            return
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # split point: node.idx, len(left)
        root_val = preorder[0]
        # root.idx in inorder --> length of left
        left_length = inorder.index(root_val)
        root = TreeNode(root_val)

        # split inorder
        inorder_left = inorder[:left_length]
        inorder_right = inorder[(left_length+1):]

        # split preorder
        preorder_left = preorder[1:left_length+1]
        preorder_right = preorder[left_length+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

