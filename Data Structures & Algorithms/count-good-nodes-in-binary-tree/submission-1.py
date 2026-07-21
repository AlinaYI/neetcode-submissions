# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root always be good node
        res = 0
        q = deque([(root, root.val)])

        while q:
            node, path_max = q.popleft()
            if node.val >= path_max:
                res += 1
            
            maxi = max(path_max, node.val)
            if node.left:
                q.append((node.left, maxi))
            if node.right:
                q.append((node.right, maxi))
        return res