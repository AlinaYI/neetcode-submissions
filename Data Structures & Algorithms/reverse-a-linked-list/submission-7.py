# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        # prev curr --> curr.next
        while curr:
            currNext = curr.next

            # prev <-- curr  curr.next
            curr.next = prev

            prev = curr
            curr = currNext
        return prev
