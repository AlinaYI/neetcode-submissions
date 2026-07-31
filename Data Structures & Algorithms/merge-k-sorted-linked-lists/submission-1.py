# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
         --- merge list --- 
        把这道题break成两两linked List

        如果一个一个的merge比较费时间，
        所以可以把整个part分为两部分，
        然后把其他一部分再分为两部分，
        这样一直分下去，直到变成是merge 2 list

        用recursion合并，最终可以合并所有的链表
        合并两个有序链表的time 是On
        tc: O nlogk
        sc: O 1  --- worst case: （递归 O(log k)）
        '''


        # 第一步先确定是一个有效的能被分解的list
        if not lists or len(lists) == 0:
            return None
        
        # 用一个helper function，merge two list
        def mergeList(l1, l2):
            dummy = ListNode()
            tail = dummy
            
            # 这里merge two lists，一定要注意的两种情况：
            # 两个list一样长，两个list不一样长
            while l1 and l2:
                # 这里要注意加value
                # 哪个小就在tail后面加那个
                if l1.val < l2.val:
                    tail.next = l1 
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            # 可能linked list还会有剩下的，就直接加入到tail 后面
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2
            return dummy.next

        # 接下来就是把无数的list分成两部分
        # 只要是整个list里包含大于一个的list，就可以被拆分
        while len(lists) > 1:
            # 新拆分的list，就存在这里
            newlists = []

            # 就是每次隔两个
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # 这里的限制条件因为可能拆分到最后只剩下一个
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # 就是再次调用自己.这里是先merge分出来的list，然后在调用原来的函数
                newlists.append(mergeList(l1, l2))
        
            lists = newlists
        
        return lists[0]