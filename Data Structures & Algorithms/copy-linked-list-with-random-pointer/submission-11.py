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
            return

        # inplace
        # A -> A' -> B
        curr = head
        while curr:
            nextNode = curr.next
            newNode = Node(curr.val)

            curr.next = newNode
            newNode.next = nextNode

            curr = newNode.next
        
        # connect random
        # A -> A' -> B
        # |          |
        # C          D
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # split curr and currCopy
        #      -----------
        # -----|-----     |
        # |    |     |    |
        # A    A'    B -> B'
        # |    |     |    |
        # C    C'    D    D'
        copyHead = head.next
        curr = head
        copyCurr = copyHead
        while curr:

            curr.next = curr.next.next
            copyCurr.next = copyCurr.next.next if copyCurr.next else None

            curr = curr.next
            copyCurr = copyCurr.next
        return copyHead