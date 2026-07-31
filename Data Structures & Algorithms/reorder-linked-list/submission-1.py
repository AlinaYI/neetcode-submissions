# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def dfs(left, right):
            # right 已经在linked list 底部了
            if not right:
                return left
            
            left = dfs(left, right.next)

            # 就是没有left需要排了
            if not left:
                return None

            # odd number: left 和 right相遇
            # even number: left.next == right
            if left == right or left.next == right:
                right.next = None
                return None
            
            next_left = left.next

            left.next = right
            right.next = next_left

            return next_left
        
        if not head:
            return

        head = dfs(head, head.next) 