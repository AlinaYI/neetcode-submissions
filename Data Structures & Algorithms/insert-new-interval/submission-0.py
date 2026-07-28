class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        给了一个sorted intervals，然后需要merge进一个新的

        edge case：
            empty intervals
            new interval在最前面/最后面， 在中间没有overlap
            new interval只跟一个 interval重叠/多个/所有重叠
            new interval包含所有的old interval
            new interval被所有的interval包含
        
        三种情况：
        1. 不merge
        2. 
        '''

        n = len(intervals)
        idx = 0
        res = []
        new_start, new_end = newInterval

        # [[1,3],[4,6]] , [4, 6]
        while idx < n and intervals[idx][1] < new_start:
            res.append(intervals[idx])
            idx += 1
        # [[1,3],[4,6]] ,, [2,5]
        while idx < n and intervals[idx][0] <= new_end:
            new_start = min(intervals[idx][0], new_start)
            new_end = max(intervals[idx][1], new_end)
            idx += 1

        res.append([new_start, new_end])
        while idx < n:
            res.append(intervals[idx])
            idx += 1
        return res
