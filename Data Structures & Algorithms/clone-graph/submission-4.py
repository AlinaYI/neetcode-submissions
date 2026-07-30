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

        seen = {node:Node(node.val)}
        q = deque([node])
        while q:
            curr= q.popleft()
        
            for nei in curr.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val)
                    q.append(nei)
                
                seen[curr].neighbors.append(seen[nei])
        return seen[node]