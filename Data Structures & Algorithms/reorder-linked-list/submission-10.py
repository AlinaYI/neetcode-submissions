# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # split half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None

        # reverse part2
        prev = None
        curr = part2
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        part2Head = prev

        # merge two linked list
        part1Head = head
        curr1 = part1Head
        curr2 = part2Head 
        while curr1 and curr2:
            curr1Next = curr1.next
            curr2Next = curr2.next
            # part1Head   part1HeadNext
            #     |
            # part2Head -> part2HeadNext

            curr1.next = curr2
            curr2.next = curr1Next

            curr1 = curr1Next
            curr2 = curr2Next

