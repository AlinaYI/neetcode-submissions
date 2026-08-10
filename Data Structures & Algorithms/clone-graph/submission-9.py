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
        
        q = deque([node])
        hashmap = {node: Node(node.val)} # node:copyNode
        while q:
            curr = q.popleft()
            
            for nei in curr.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                    q.append(nei)
                hashmap[curr].neighbors.append(hashmap[nei])
        return hashmap[node]
