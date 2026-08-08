# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None

        # reverse part2
        prev = None
        curr = part2
        while curr:
            nextNode = curr.next

            curr.next = prev

            prev = curr
            curr = nextNode
        
        # connect part1 + part2
        part2 = prev
        curr1 = head
        curr2 = part2
        while curr2:
            # curr1    temp1
            #    |   /
            # curr2    temp2
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2
