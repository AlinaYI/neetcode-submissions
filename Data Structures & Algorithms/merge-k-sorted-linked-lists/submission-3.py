# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(Nlogk)
        # Ok
        minHeap = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(minHeap, (l.val, idx, l) )
        
        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = node

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        return dummy.next