class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        intervals.sort(key=lambda x: x[0])
        remove = 0
        preEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < preEnd:
                remove += 1
                preEnd = min(intervals[i][1], preEnd)
            else:
                preEnd = intervals[i][1]
        return remove