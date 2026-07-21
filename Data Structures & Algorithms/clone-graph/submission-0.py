"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        seen = {}
        def dfs(curr_node):
            if curr_node in seen:
                return seen[curr_node]
            
            new_node = Node(curr_node.val)
            seen[curr_node] = new_node

            for n in curr_node.neighbors:
                new_node.neighbors.append(dfs(n))
            return new_node

        return dfs(node)