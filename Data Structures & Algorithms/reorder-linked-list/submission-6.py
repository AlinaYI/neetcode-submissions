# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # split half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        part2 = slow.next
        slow.next = None

        # reverse part2
        curr = part2
        prev = None
        while curr:
            nextNode = curr.next

            curr.next = prev
            prev = curr
            curr = nextNode
        part2 = prev

        # connect part1 & part2
        part1Curr = head
        part2Curr = part2
        while part2Curr:
            # part1Curr -> temp1
            # part2Curr -> temp2
            temp1 = part1Curr.next
            temp2 = part2Curr.next

            # part1Curr  temp1
            #    |      /
            # part2Curr   temp2
            part1Curr.next = part2Curr
            part2Curr.next = temp1

            part1Curr = temp1
            part2Curr = temp2
        return
