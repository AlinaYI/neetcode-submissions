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
        
        # O1 space
        # A -> A' -> B -> B' 
        if not head:
            return None
        
        curr = head
        while curr:
            copy_node = Node(curr.val)

            copy_node.next = curr.next
            curr.next = copy_node

            curr = copy_node.next
        
        '''
        A -> A' -> B -> B' -> C -> C' -> D -> D'
        |    |    |     |     |    |
        V    V    V     V     V    V
        C    C'    D     D'    B    B'
        '''
        # copy random_node
        curr = head
        while curr:
            if curr.random:
                # A -> C, 那么A' -> C'
                curr.next.random = curr.random.next
            curr = curr.next.next


        # split
        curr = head
        
        copyHead = head.next # A'
        copyCurr = copyHead

        while curr:
            '''
            A' \    
            A ->  B -> B' -> C -> C' -> D -> D'
            |     |     |     |    |
            V     V     V     V    V
            C     D     D'    B    B'


            '''
            curr.next = curr.next.next
            '''
            A' --------
            |          |  
            V          |
            C'         |
                       V
            A ->  B -> B' -> C -> C' -> D -> D'
            |     |     |     |    |
            V     V     V     V    V
            C     D     D'    B    B'
            '''
            copyCurr.next = copyCurr.next.next if copyCurr.next else None

            curr = curr.next
            copyCurr = copyCurr.next
        
        return copyHead




