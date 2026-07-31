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

        
        # 接node
        # A -> A' -> B -> B'
        curr = head
        while curr:
            # A -> B 
            # A'
            copyNode = Node(curr.val)

            # A -> B
            # A' --|
            copyNode.next = curr.next

            # A -> A' -> B
            curr.next = copyNode

            # move pointer
            curr = copyNode.next
        

        # connect random
        '''
         ---------------------
        |                     | 
        A -> A' -> B -> B' -> C -> C' -> D -> D'
                   |                     |
                    ---------------------
      curr
        '''
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        '''
             ----------------------   
         ----|-----------------    |
        |    |                |    |
        A -> A' -> B -> B' -> C -> C' -> D -> D'
                   |    |                 |   |
                    ----|-----------------    |
                        -----------------------
       cur  Copycur
        '''
        curr = head

        copyHead = head.next # A'
        copyCurr = copyHead

        while curr:
            # A -> B -> B'
            # A'---|
            curr.next = curr.next.next

            # A -> B -> B'-> C
            # A'--------|
            copyCurr.next = copyCurr.next.next if copyCurr.next else None

            curr = curr.next
            copyCurr = copyCurr.next
        return copyHead



