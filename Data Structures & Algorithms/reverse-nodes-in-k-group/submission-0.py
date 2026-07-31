class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Step 1: 找当前组的第 k 个节点
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Step 2: 保存下一组的起点
            group_next = kth.next

            # 当前组原来的头，反转后会成为尾巴
            old_group_head = group_prev.next

            # Step 3: 反转当前组
            prev = group_next
            curr = old_group_head

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Step 4: 接回前一组
            group_prev.next = kth

            # 移动到下一组之前
            group_prev = old_group_head