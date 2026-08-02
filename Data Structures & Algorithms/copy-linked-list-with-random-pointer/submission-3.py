"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # 接node
        if not head:
            return None
        
        # 记录node : node_copy
        node_map = {}
        curr= head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        # connect all and random
        curr = head
        while curr:
            node_map[curr].next = node_map.get(curr.next)
            node_map[curr].random = node_map.get(curr.random)
            curr = curr.next
        
        return node_map[head]
