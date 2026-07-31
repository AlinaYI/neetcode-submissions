# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, listHead in enumerate(lists):
            if listHead:
                heapq.heappush(heap, (listHead.val, idx, listHead))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            nodeVal, idx, node = heapq.heappop(heap)
            
            curr.next = node
            curr = node

            # list still have node 
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next) )
        return dummy.next