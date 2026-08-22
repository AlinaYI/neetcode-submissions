# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        '''     
        # return里面每次都要创建新list
        # TC O(n^2)
        # SC O(N)
        if not root:
            return []
            
        def inorder(node):
            if not node:
                return []
            
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        return inorder(root)[k-1]
        '''

        res = []
        def inorder(node):
            if not node:
                return 

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res[k-1]        