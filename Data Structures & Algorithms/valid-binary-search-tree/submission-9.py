# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        valid 就是符合 left < node < right
        '''

        q = deque([ (float("-inf"), root, float("inf")) ])

        while q:
            low, node, high = q.popleft()

            if not (low < node.val < high):
                return False
            
            if node.left:
                q.append((low, node.left, node.val))
            
            if node.right:
                q.append((node.val, node.right, high))
        
        return True