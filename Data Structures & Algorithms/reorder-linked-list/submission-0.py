# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 这里先break mid
        # 然后reverse part2
        # 然后merge part1 and part2

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow = part2.head
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node
        
        # merge two linked list
        part1 = head
        part2 = prev

        while part1 and part2:
            temp1 = part1.next
            temp2 = part2.next

            part1.next = part2
            part2.next = temp1

            part1 = temp1
            part2 = temp2
