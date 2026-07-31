# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # prev -> head - > next
        curr = head
        prev = None

        while curr:
            next_node = curr.next

            # 0  <-   1     2
            # prev  head head.next
            curr.next = prev

            # 0  <-   1     2
            #       prev  head  head.next
            prev = curr
            curr = next_node
        return prev