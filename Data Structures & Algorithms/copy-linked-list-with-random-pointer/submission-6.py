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

        # inplace copy
        # A -> B
        # A -> A' -> B -> B'
        curr = head
        while curr:
            nextNode = curr.next
            copyNode = Node(curr.val)

            curr.next = copyNode
            copyNode.next = nextNode

            curr = curr.next.next
        
        # connect random
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # split node
        curr = head
        copyHead = head.next
        currCopy = copyHead
        while curr:
            curr.next = curr.next.next
            currCopy.next = currCopy.next.next if currCopy.next else None

            curr = curr.next
            currCopy = currCopy.next
        return copyHead
