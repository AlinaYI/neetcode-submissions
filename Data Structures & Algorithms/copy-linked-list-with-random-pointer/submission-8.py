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
        
        if not head:
            return None

        # A ->A' -> B
        curr = head
        while curr:
            nextNode = curr.next
            copyNode = Node(curr.val)

            curr.next = copyNode
            copyNode.next = nextNode
            curr = copyNode.next
        
        # connect random
        # A -> A' -> B
        # |          |
        # C          D
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            
            curr = curr.next.next
        
        # split node
        # A -> A' -> B
        # |    |     |
        # C    C'    D
        curr = head
        copyHead = head.next
        copyCurr = copyHead
        while curr:
            #      ------------
            # -----|-----|    |
            # A    A'    B -> B'
            # |    |     |
            # C    C'    D
            
            curr.next = curr.next.next
            copyCurr.next = copyCurr.next.next if copyCurr.next else None

            curr = curr.next
            copyCurr = copyCurr.next
        return copyHead


                