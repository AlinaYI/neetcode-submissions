# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderMap = {val: idx for idx, val in enumerate(inorder)}
        
        preorderIdx = 0
        def dfs(left, right):
            nonlocal preorderIdx

            if left > right:
                return None
            
            rootVal = preorder[preorderIdx]
            preorderIdx += 1

            root = TreeNode(rootVal)
            rootIdx = inorderMap[rootVal]

            root.left = dfs(left, rootIdx-1)
            root.right = dfs(rootIdx + 1, right)

            return root
        
        return dfs(0, len(inorder)-1)