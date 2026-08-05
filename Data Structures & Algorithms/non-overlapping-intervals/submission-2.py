class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0

        intervals.sort()
        prevEnd = intervals[0][1]
        remove = 0
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start < prevEnd:
                remove += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return remove