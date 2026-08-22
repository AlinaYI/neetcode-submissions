# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p,q):
            if not q and not p:
                return True
            
            if not q or not p:
                return False
            
            if q.val != p.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        if not root:
            return False
        
        if not subRoot:
            return True
        
        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)