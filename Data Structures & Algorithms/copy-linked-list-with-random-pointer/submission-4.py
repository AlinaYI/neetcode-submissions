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
        
        # inplace copy node
        # A -> A' -> B -> B'
        curr = head
        while curr:
            next_node = curr.next
            copyNode= Node(curr.val)

            curr.next = copyNode
            copyNode.next = next_node

            curr = curr.next.next

        # add random
        '''
         ---------------------
        |                     | 
        A -> A' -> B -> B' -> C -> C' -> D -> D'
                   |                     |
                    ---------------------
      curr
        '''
        curr= head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        

        # split original and copy
        curr = head
        copyHead = head.next
        currCopy = copyHead

        while curr:

            curr.next = curr.next.next
            currCopy.next = currCopy.next.next if currCopy.next else None

            curr = curr.next
            currCopy = currCopy.next
        
        return copyHead



