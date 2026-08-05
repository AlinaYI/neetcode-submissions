# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. split
        # 2. reverse part2
        # 3. merge two list

        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # break list1 and list2
        list2 = slow.next
        slow.next = None

        # reverse
        prev = None
        curr = list2
        while curr:
            nextNode = curr.next

            curr.next = prev

            prev = curr
            curr = nextNode
        
        list2 = prev
        list1 = head
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2
        return 

        