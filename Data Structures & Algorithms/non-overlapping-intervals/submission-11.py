class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        prevStart, prevEnd = intervals[0]
        removed = 0
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]

            if currStart < prevEnd:
                removed += 1
                prevEnd = min(prevEnd, currEnd)
            else:
                prevEnd = currEnd
        return removed
