"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # curr -》 clone,  看重复

        def dfs(curr_node):
            if curr_node in seen:
                return seen[curr_node]

            cloned = Node(curr_node.val)
            seen[curr_node] = cloned
            for nei in curr_node.neighbors:
                cloned.neighbors.append(dfs(nei))
            return cloned
        seen = {}
        return dfs(node) if node else None