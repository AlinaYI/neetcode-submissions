# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left < node < right

        q = deque([(float("-inf"), root, float("inf"))])
        while q:
            left, curr, right = q.popleft()

            if not(left < curr.val < right):
                return False
            
            # -inf < left < node
            if curr.left:
                q.append((left, curr.left, curr.val))
            
            # node < right < inf
            if curr.right:
                q.append((curr.val, curr.right, right))

        return True