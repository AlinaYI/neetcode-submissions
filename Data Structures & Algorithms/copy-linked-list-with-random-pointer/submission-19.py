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
        
        # # 用hashmap On On
        # if not head:
        #     return
        # hashmap = {}

        # curr = head
        # while curr:
        #     hashmap[curr] = Node(curr.val)
        #     curr = curr.next
        
        # curr = head
        # while curr:
        #     hashmap[curr].next = hashmap.get(curr.next)
        #     hashmap[curr].random = hashmap.get(curr.random)
        #     curr = curr.next
        # return hashmap[head]


        # in place change
        if not head:
            return None
        
        # # A -> A' -> B -> B'
        curr = head
        while curr:
            nextNode = curr.next
            newNode = Node(curr.val)

            curr.next = newNode
            newNode.next = nextNode
            curr = curr.next.next
        
        # connect random On O1
        # A -> A' -> B -> B'
        # |          |
        # C          D
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # split node & nodeCopy
        # connect random
        # A -> A' -> B -> B'
        # |    |     |    |
        # C    C'    D    D'
        copyHead = head.next
        curr = head
        currCopy = copyHead
        while curr:

            curr.next = curr.next.next
            currCopy.next = currCopy.next.next if currCopy.next else None

            curr = curr.next
            currCopy = currCopy.next
        return copyHead




