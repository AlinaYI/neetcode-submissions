# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        curr = head
        while fast and fast.next:
            curr = curr.next
            fast = fast.next
        
        curr.next = curr.next.next
        return head