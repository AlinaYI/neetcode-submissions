class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        intervals 是sortedd + non-overlapping
        可以用把整个intervals 分成三部分，
        左边不重叠，中间重叠，右边不重叠
        '''
        n = len(intervals)
        new_start, new_end = newInterval
        idx = 0
        res = []
        # 左边不重叠
        while idx < n and intervals[idx][1] < new_start:
            res.append(intervals[idx]) 
            idx += 1

        while idx < n and intervals[idx][0] <= new_end:
            new_start = min(new_start,intervals[idx][0] )
            new_end = max(new_end, intervals[idx][1])
            idx += 1
        res.append([new_start, new_end])
        
        while idx < n:
            res.append(intervals[idx])
            idx += 1

        return res