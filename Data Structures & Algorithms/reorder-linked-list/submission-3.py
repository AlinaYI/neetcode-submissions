# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        '''
        split -> revers -> merge
        '''

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None

        curr = part2
        prev = None
        while curr:
            next_node = curr.next

            curr.next = prev
            prev = curr
            curr = next_node
        part2 = prev

        part1 = head
        while part1 and part2:
            '''
            part1 -> part1.1
                        temp1
            part2 -> part2.1
                        temp2
            '''

            temp1 = part1.next      # 保存第一条链表剩下的部分
            temp2 = part2.next      # 保存第二条链表剩下的部分

            part1.next = part2      # 插入第二条链表的一个节点
            part2.next = temp1      # 再接回第一条链表

            part1 = temp1           # 第一条链表继续往后
            part2 = temp2           # 第二条链表继续往后
        return
        
        
