# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 先对半，然后reverse， 再merge

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None

        # reverse
        curr = part2
        prev = None
        while curr:
            next_node = curr.next

            curr.next = prev
            prev = curr
            curr = next_node
        
        # merge
        part1 = head
        part2 = prev
        while part1 and part2:
            temp1 = part1.next
            temp2 = part2.next

            part1.next = part2
            part2.next = temp1

            part1 = temp1
            part2 = temp2

        