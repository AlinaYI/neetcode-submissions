"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # clone 要查duplicate
        # seen = {node : cloned}
        if not node:
            return None

        seen = {}

        def dfs(node):
            if node in seen:
                return seen[node]
            
            cloned = Node(node.val)
            seen[node] = cloned
            for nei in node.neighbors:
                cloned.neighbors.append(dfs(nei))
            return cloned
        
        return dfs(node)
