"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # 这里就是要检查dfs
        # hashmap = {node:clonedNode}
        if not node:
            return None
        
        q = deque([node])
        seen = {node:Node(node.val)}
        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val)
                    q.append(nei)
                
                seen[curr].neighbors.append(seen[nei])
        return seen[node]